"""Data update coordinator for Sit Solar."""
from __future__ import annotations

import logging
from datetime import timedelta

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .api import SitSolarApi, SitSolarApiError, SitSolarAuthError
from .const import DEFAULT_SCAN_INTERVAL

_LOGGER = logging.getLogger(__name__)


class SitSolarCoordinator(DataUpdateCoordinator[dict]):
    def __init__(
        self,
        hass: HomeAssistant,
        api: SitSolarApi,
        scan_interval: int,
    ) -> None:
        super().__init__(
            hass,
            _LOGGER,
            name="Sit Solar",
            update_interval=timedelta(seconds=scan_interval),
        )
        self.api = api

    async def _async_update_data(self) -> dict:
        from homeassistant.helpers.aiohttp_client import async_get_clientsession
        session = async_get_clientsession(self.hass)
        # Login if needed
        try:
            await self.api.async_login(session)
        except SitSolarAuthError as err:
            raise UpdateFailed(f"Authentication failed: {err}") from err
        except SitSolarApiError as err:
            raise UpdateFailed(str(err)) from err

        try:
            devices = await self.api.async_get_devices(session)
        except SitSolarAuthError as err:
            # retry once
            try:
                await self.api.async_login(session)
                devices = await self.api.async_get_devices(session)
            except (SitSolarApiError, Exception) as err2:  # noqa: BLE001
                raise UpdateFailed(str(err2)) from err2
        except SitSolarApiError as err:
            raise UpdateFailed(str(err)) from err

        result: dict = {}
        for dev in devices:
            dev_id = dev.get("devId")
            if dev_id is None:
                continue
            entry: dict = {"device": dev}
            try:
                monitor = await self.api.async_get_monitor(session, dev_id, dev.get("devTypeId", 0))
                entry["monitor"] = monitor
            except SitSolarApiError as err:
                _LOGGER.warning("Failed to fetch monitor for %s: %s", dev_id, err)
                entry["monitor"] = {}
            dev_type = dev.get("devTypeId")
            if dev_type == 51:
                try:
                    battery = await self.api.async_get_battery(session, dev_id)
                    entry["battery"] = battery or {}
                except SitSolarApiError as err:
                    _LOGGER.warning("Failed to fetch battery for %s: %s", dev_id, err)
                    entry["battery"] = {}
            else:
                entry["battery"] = {}
            result[str(dev_id)] = entry

        # Station-level overview / energy flow (home screen data, monotonic totals)
        stations: dict[str, str] = {}
        for dev in devices:
            code = dev.get("stationCode")
            if code:
                stations[code] = dev.get("stationName") or code

        for code, name in stations.items():
            try:
                overview = await self.api.async_get_station_overview(session, code)
            except SitSolarApiError:
                overview = None
            try:
                flow = await self.api.async_get_station_flow(session, code)
            except SitSolarApiError:
                flow = None
            entry = {
                "kind": "station",
                "station_code": code,
                "device": {
                    "devId": f"station:{code}",
                    "devName": name,
                    "devModel": "Station",
                    "stationCode": code,
                    "neVersion": None,
                    "devTypeId": None,
                },
                "overview": overview or {},
                "station_flow": flow or {},
            }
            result[f"station:{code}"] = entry

        return result