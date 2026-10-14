"""API client for Sit Solar (SiNeng enjoysolar)."""
from __future__ import annotations

from typing import Any

import aiohttp

from .const import DEFAULT_HOST


class SitSolarApiError(Exception):
    """Base error."""


class SitSolarAuthError(SitSolarApiError):
    """Authentication error."""


class SitSolarApi:
    def __init__(self, host: str, username: str, password: str) -> None:
        self.host = host.rstrip("/")
        self.username = username
        self.password = password
        self._token: str | None = None

    @property
    def base_url(self) -> str:
        return f"{self.host}/prod-api"

    async def _request(
        self,
        session: aiohttp.ClientSession,
        method: str,
        path: str,
        *,
        json: Any = None,
        params: Any = None,
        _retry: bool = True,
    ) -> dict:
        url = f"{self.base_url}{path}"
        headers = {}
        if self._token:
            headers["Authorization"] = f"Bearer {self._token}"
        try:
            async with session.request(
                method, url, json=json, params=params, headers=headers, ssl=False
            ) as resp:
                data = await resp.json(content_type=None)
        except (aiohttp.ClientError, TimeoutError, ValueError) as err:
            raise SitSolarApiError(str(err)) from err

        if not isinstance(data, dict):
            raise SitSolarApiError("Unexpected response")
        code = data.get("code")
        if code in (50008, 50012, 50014, 50016):
            # token invalid/expired
            if _retry:
                await self.async_login(session)
                return await self._request(
                    session, method, path, json=json, params=params, _retry=False
                )
            raise SitSolarAuthError(data.get("msg", "auth error"))
        if code not in (20000, 200):
            msg = data.get("msg") or data.get("message")
            if code in (10008,):
                raise SitSolarAuthError(msg or "auth error")
            raise SitSolarApiError(msg or f"API error {code}")
        return data

    async def async_login(self, session: aiohttp.ClientSession) -> str:
        payload = {
            "username": self.username,
            "password": self.password,
            "loginType": 2,
            "app": True,
        }
        data = await self._request(
            session, "POST", "/auth/login", json=payload, _retry=False
        )
        token = data.get("data")
        if not isinstance(token, str) or not token:
            raise SitSolarAuthError("login did not return token")
        self._token = token
        return token

    async def async_get_devices(self, session: aiohttp.ClientSession) -> list[dict]:
        data = await self._request(
            session, "POST", "/dev/info/app/v1/devmonitor/appPageInverterMoniterList",
            json={"page": 1, "size": 100},
        )
        body = data.get("data") or {}
        records = body.get("records") if isinstance(body, dict) else None
        return records or []

    async def async_get_monitor(
        self, session: aiohttp.ClientSession, dev_id: int, dev_type: int
    ) -> dict:
        if dev_type == 51:
            path = f"/dev/info/devmonitor/getStoredInverterDevMonitorDetailMonitor/{dev_id}"
        else:
            path = f"/dev/info/app/v1/devmonitor/getAppInverterDevMonitorDetailMonitor/{dev_id}"
        data = await self._request(session, "GET", path)
        return data.get("data") or {}

    async def async_get_battery(
        self, session: aiohttp.ClientSession, dev_id: int
    ) -> dict | None:
        try:
            data = await self._request(
                session, "GET",
                f"/dev/info/devmonitor/getStoredInverterBatteryMonitor/{dev_id}",
            )
        except SitSolarApiError:
            return None
        return data.get("data") or None