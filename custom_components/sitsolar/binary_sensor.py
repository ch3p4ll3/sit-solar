"""Binary sensor platform for Sit Solar."""
from __future__ import annotations

from homeassistant.components.binary_sensor import BinarySensorDeviceClass, BinarySensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import SitSolarCoordinator


class SitSolarOnlineSensor(CoordinatorEntity, BinarySensorEntity):
    def __init__(self, coordinator: SitSolarCoordinator, dev_id: str) -> None:
        super().__init__(coordinator)
        self._dev_id = dev_id
        device = coordinator.data[dev_id]["device"]
        dev_name = device.get("devName") or device.get("snCode") or dev_id
        self._attr_name = f"{dev_name} Online"
        self._attr_unique_id = f"sitsolar_{dev_id}_online"
        self._attr_device_class = BinarySensorDeviceClass.CONNECTIVITY

    @property
    def is_on(self) -> bool:
        try:
            dev = self.coordinator.data[self._dev_id]["device"]
            monitor = self.coordinator.data[self._dev_id].get("monitor", {})
            dev_status = monitor.get("monitorInformation", {}).get("devStatus")
            if dev_status is None:
                dev_status = dev.get("devStatus")
            return str(dev_status) == "1"
        except (KeyError, TypeError):
            return False

    @property
    def device_info(self) -> DeviceInfo:
        data = self.coordinator.data.get(self._dev_id, {})
        device = data.get("device", {})
        return DeviceInfo(
            identifiers={(DOMAIN, self._dev_id)},
            name=device.get("devName") or device.get("snCode") or self._dev_id,
            manufacturer="SiNeng",
            model=device.get("devModel"),
        )

    def _handle_coordinator_update(self) -> None:
        self.async_write_ha_state()


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    coordinator: SitSolarCoordinator = hass.data[DOMAIN][entry.entry_id]
    entities = [SitSolarOnlineSensor(coordinator, dev_id) for dev_id in coordinator.data]
    async_add_entities(entities)