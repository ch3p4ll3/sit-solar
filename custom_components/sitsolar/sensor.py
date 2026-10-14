"""Sensor platform for Sit Solar."""
from __future__ import annotations

from typing import Any

from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntity,
    SensorStateClass,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    PERCENTAGE,
    UnitOfElectricCurrent,
    UnitOfElectricPotential,
    UnitOfEnergy,
    UnitOfPower,
    UnitOfTemperature,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN
from .coordinator import SitSolarCoordinator

# (key, path, name, unit, device_class, state_class, is_energy)
MONITOR_SENSORS = [
    ("active_power", ["monitorInformation", "active_power"], "Active power", UnitOfPower.KILO_WATT, SensorDeviceClass.POWER, SensorStateClass.MEASUREMENT),
    ("pv_power", ["monitorInformation", "pv_total_power"], "PV power", UnitOfPower.KILO_WATT, SensorDeviceClass.POWER, SensorStateClass.MEASUREMENT),
    ("reactive_power", ["monitorInformation", "reactive_power"], "Reactive power", "kVAR", None, SensorStateClass.MEASUREMENT),
    ("temperature", ["monitorInformation", "temperature"], "Inverter temperature", UnitOfTemperature.CELSIUS, SensorDeviceClass.TEMPERATURE, SensorStateClass.MEASUREMENT),
    ("heatsink_temp", ["monitorInformation", "uwINVSink_Temp"], "Heatsink temperature", UnitOfTemperature.CELSIUS, SensorDeviceClass.TEMPERATURE, SensorStateClass.MEASUREMENT),
    ("battery_temp", ["monitorInformation", "uwBatSink1_Temp"], "Battery temperature", UnitOfTemperature.CELSIUS, SensorDeviceClass.TEMPERATURE, SensorStateClass.MEASUREMENT),
    ("frequency", ["generationPowerInfo", "uwFreq_R"], "Grid frequency", "Hz", None, SensorStateClass.MEASUREMENT),
    ("voltage_a", ["generationPowerInfo", "a_u"], "Voltage A", UnitOfElectricPotential.VOLT, SensorDeviceClass.VOLTAGE, SensorStateClass.MEASUREMENT),
    ("voltage_b", ["generationPowerInfo", "b_u"], "Voltage B", UnitOfElectricPotential.VOLT, SensorDeviceClass.VOLTAGE, SensorStateClass.MEASUREMENT),
    ("voltage_c", ["generationPowerInfo", "c_u"], "Voltage C", UnitOfElectricPotential.VOLT, SensorDeviceClass.VOLTAGE, SensorStateClass.MEASUREMENT),
    ("current_a", ["generationPowerInfo", "a_i"], "Current A", UnitOfElectricCurrent.AMPERE, SensorDeviceClass.CURRENT, SensorStateClass.MEASUREMENT),
    ("current_b", ["generationPowerInfo", "b_i"], "Current B", UnitOfElectricCurrent.AMPERE, SensorDeviceClass.CURRENT, SensorStateClass.MEASUREMENT),
    ("current_c", ["generationPowerInfo", "c_i"], "Current C", UnitOfElectricCurrent.AMPERE, SensorDeviceClass.CURRENT, SensorStateClass.MEASUREMENT),
]

BATTERY_SENSORS = [
    ("battery_soc", ["batteryInformation", "uwBatSoc"], "Battery SOC", PERCENTAGE, SensorDeviceClass.BATTERY, SensorStateClass.MEASUREMENT),
    ("battery_soh", ["batteryInformation", "battery_SOH"], "Battery SOH", PERCENTAGE, None, SensorStateClass.MEASUREMENT),
    ("battery_voltage", ["batteryInformation", "uwBatVolt_BMS"], "Battery voltage", UnitOfElectricPotential.VOLT, SensorDeviceClass.VOLTAGE, SensorStateClass.MEASUREMENT),
    ("battery_current", ["batteryInformation", "uwBatCurr_BMS"], "Battery current", UnitOfElectricCurrent.AMPERE, SensorDeviceClass.CURRENT, SensorStateClass.MEASUREMENT),
    ("battery_power", ["batteryInformation", "uwBatPower_BMS"], "Battery power", UnitOfPower.KILO_WATT, SensorDeviceClass.POWER, SensorStateClass.MEASUREMENT),
    ("battery_cycles", ["batteryInformation", "uw_bat_cycle_times"], "Battery cycles", None, None, SensorStateClass.TOTAL_INCREASING),
]

ELECTRIC_SENSORS = [
    ("daily_pv_grid", ["electricInformation", "day_pv_to_grid_capacity"], "Daily PV to grid", UnitOfEnergy.KILO_WATT_HOUR, SensorDeviceClass.ENERGY, SensorStateClass.TOTAL_INCREASING),
    ("total_pv_grid", ["electricInformation", "all_pv_to_grid_capacity"], "Total PV to grid", UnitOfEnergy.KILO_WATT_HOUR, SensorDeviceClass.ENERGY, SensorStateClass.TOTAL_INCREASING),
    ("daily_charge", ["electricInformation", "day_charge"], "Daily battery charge", UnitOfEnergy.KILO_WATT_HOUR, SensorDeviceClass.ENERGY, SensorStateClass.TOTAL_INCREASING),
    ("daily_discharge", ["electricInformation", "day_battery_to_grid_capacity"], "Daily battery discharge", UnitOfEnergy.KILO_WATT_HOUR, SensorDeviceClass.ENERGY, SensorStateClass.TOTAL_INCREASING),
    ("daily_consumption", ["electricInformation", "day_electricity_consumption"], "Daily consumption", UnitOfEnergy.KILO_WATT_HOUR, SensorDeviceClass.ENERGY, SensorStateClass.TOTAL_INCREASING),
]

STATION_ENERGY_SENSORS = [
    ("total_solar_production", ["totalGfProductPower"], "Solar production total", UnitOfEnergy.KILO_WATT_HOUR, SensorDeviceClass.ENERGY, SensorStateClass.TOTAL_INCREASING),
    ("total_product_power", ["totalProductPower"], "Product power total", UnitOfEnergy.KILO_WATT_HOUR, SensorDeviceClass.ENERGY, SensorStateClass.TOTAL_INCREASING),
    ("total_grid_import", ["totalBuyGridPower"], "Grid import total", UnitOfEnergy.KILO_WATT_HOUR, SensorDeviceClass.ENERGY, SensorStateClass.TOTAL_INCREASING),
    ("total_grid_export", ["totalOngridPower"], "Grid export total", UnitOfEnergy.KILO_WATT_HOUR, SensorDeviceClass.ENERGY, SensorStateClass.TOTAL_INCREASING),
    ("total_battery_charge", ["totalCellCharge"], "Battery charge total", UnitOfEnergy.KILO_WATT_HOUR, SensorDeviceClass.ENERGY, SensorStateClass.TOTAL_INCREASING),
    ("total_battery_discharge", ["totalCellDischarge"], "Battery discharge total", UnitOfEnergy.KILO_WATT_HOUR, SensorDeviceClass.ENERGY, SensorStateClass.TOTAL_INCREASING),
    ("total_house_load", ["totalLoadUsePower"], "House load total", UnitOfEnergy.KILO_WATT_HOUR, SensorDeviceClass.ENERGY, SensorStateClass.TOTAL_INCREASING),
    ("total_load_use_pv", ["totalLoadUsePvPower"], "Load from PV total", UnitOfEnergy.KILO_WATT_HOUR, SensorDeviceClass.ENERGY, SensorStateClass.TOTAL_INCREASING),
    ("total_load_use_battery", ["totalLoadUseBatteryPower"], "Load from battery total", UnitOfEnergy.KILO_WATT_HOUR, SensorDeviceClass.ENERGY, SensorStateClass.TOTAL_INCREASING),
    ("total_load_use_grid", ["totalLoadUseGridPower"], "Load from grid total", UnitOfEnergy.KILO_WATT_HOUR, SensorDeviceClass.ENERGY, SensorStateClass.TOTAL_INCREASING),
    ("total_pv_to_grid", ["totalPvToGridProductPower"], "PV to grid total", UnitOfEnergy.KILO_WATT_HOUR, SensorDeviceClass.ENERGY, SensorStateClass.TOTAL_INCREASING),
    ("total_pv_to_battery", ["totalPvToBatteryProductPower"], "PV to battery total", UnitOfEnergy.KILO_WATT_HOUR, SensorDeviceClass.ENERGY, SensorStateClass.TOTAL_INCREASING),
]

STATION_POWER_SENSORS = [
    ("station_active_power", ["activePower"], "Station active power", UnitOfPower.KILO_WATT, SensorDeviceClass.POWER, SensorStateClass.MEASUREMENT),
    ("station_ongrid_power", ["ongridPower"], "Grid export power", UnitOfPower.KILO_WATT, SensorDeviceClass.POWER, SensorStateClass.MEASUREMENT),
    ("station_buy_power", ["buyPower"], "Grid import power", UnitOfPower.KILO_WATT, SensorDeviceClass.POWER, SensorStateClass.MEASUREMENT),
    ("station_load_power", ["loadPower"], "House load power", UnitOfPower.KILO_WATT, SensorDeviceClass.POWER, SensorStateClass.MEASUREMENT),
    ("station_mppt_power", ["mpptPower"], "PV power", UnitOfPower.KILO_WATT, SensorDeviceClass.POWER, SensorStateClass.MEASUREMENT),
    ("station_battery_power", ["batteryPower"], "Battery power", UnitOfPower.KILO_WATT, SensorDeviceClass.POWER, SensorStateClass.MEASUREMENT),
    ("station_battery_soc_avg", ["batterySocAver"], "Battery SOC average", PERCENTAGE, SensorDeviceClass.BATTERY, SensorStateClass.MEASUREMENT),
]


def _get_nested(obj: dict, path: list[str]) -> Any:
    cur = obj
    for p in path:
        if not isinstance(cur, dict):
            return None
        cur = cur.get(p)
    return cur


class SitSolarSensor(CoordinatorEntity, SensorEntity):
    def __init__(
        self,
        coordinator: SitSolarCoordinator,
        dev_id: str,
        key: str,
        name_suffix: str,
        path: list[str],
        unit: str | None,
        device_class,
        state_class,
        source: str,
        value_fn=None,
    ) -> None:
        super().__init__(coordinator)
        self._dev_id = dev_id
        self._key = key
        self._path = path
        self._source = source
        self._value_fn = value_fn
        device = coordinator.data[dev_id]["device"]
        dev_name = device.get("devName") or device.get("snCode") or dev_id
        self._attr_name = f"{dev_name} {name_suffix}"
        self._attr_unique_id = f"sitsolar_{dev_id}_{key}"
        self._attr_native_unit_of_measurement = unit
        self._attr_device_class = device_class
        self._attr_state_class = state_class

    @property
    def _current(self) -> dict:
        return self.coordinator.data.get(self._dev_id, {})

    @property
    def native_value(self):
        data = self._current
        if self._value_fn is not None:
            try:
                return self._value_fn(data)
            except (TypeError, ValueError, KeyError):
                return None
        src = data.get(self._source, {}) or {}
        val = _get_nested(src, self._path)
        if isinstance(val, (int, float, str)):
            try:
                if isinstance(val, str):
                    return float(val) if "." in val else int(val) if val.isdigit() else val
            except (ValueError, AttributeError):
                return val
        return val

    @property
    def device_info(self) -> DeviceInfo:
        device = self._current.get("device", {})
        return DeviceInfo(
            identifiers={(DOMAIN, self._dev_id)},
            name=device.get("devName") or device.get("snCode") or self._dev_id,
            manufacturer="SiNeng",
            model=device.get("devModel"),
            sw_version=device.get("neVersion"),
        )

    def _handle_coordinator_update(self) -> None:
        self.async_write_ha_state()


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    coordinator: SitSolarCoordinator = hass.data[DOMAIN][entry.entry_id]
    entities: list[SensorEntity] = []

    for dev_id, data in (coordinator.data or {}).items():
        device = data.get("device", {})
        dev_type = device.get("devTypeId")
        monitor = data.get("monitor", {}) or {}
        battery = data.get("battery", {}) or {}
        electric = monitor.get("electricInformation", {}) if isinstance(monitor, dict) else {}

        # Station-level home screen data (totals + power flow)
        if str(dev_id).startswith("station:"):
            overview = data.get("overview", {}) or {}
            flow = data.get("station_flow", {}) or {}
            for key, path, suffix, unit, dclass, sc in STATION_ENERGY_SENSORS:
                if _get_nested(overview, path) is not None:
                    entities.append(
                        SitSolarSensor(
                            coordinator, dev_id, key, suffix, path, unit, dclass, sc, "overview"
                        )
                    )
            for key, path, suffix, unit, dclass, sc in STATION_POWER_SENSORS:
                if _get_nested(flow, path) is not None:
                    entities.append(
                        SitSolarSensor(
                            coordinator, dev_id, key, suffix, path, unit, dclass, sc, "station_flow"
                        )
                    )
            # App home shows solar power as mpptPower + acCouple when AC-coupling is enabled
            def _combined_solar(state):
                flow = (state or {}).get("station_flow", {}) or {}
                def _num(key):
                    v = flow.get(key)
                    try:
                        return float(v) if v is not None else 0.0
                    except (TypeError, ValueError):
                        return 0.0
                mppt = flow.get("mpptPower")
                ac = flow.get("acCoupleGfActivePower")
                if mppt is None and ac is None:
                    return None
                return _num("mpptPower") + _num("acCoupleGfActivePower")
            entities.append(
                SitSolarSensor(
                    coordinator,
                    dev_id,
                    "solar_power",
                    "Solar power",
                    [],
                    UnitOfPower.KILO_WATT,
                    SensorDeviceClass.POWER,
                    SensorStateClass.MEASUREMENT,
                    "station_flow",
                    value_fn=_combined_solar,
                )
            )
            continue

        # monitor sensors (if monitor data present)
        for key, path, suffix, unit, dclass, sc in MONITOR_SENSORS:
            if _get_nested(monitor, path) is not None:
                entities.append(
                    SitSolarSensor(
                        coordinator, dev_id, key, suffix, path, unit, dclass, sc, "monitor"
                    )
                )

        if dev_type == 51:
            for key, path, suffix, unit, dclass, sc in BATTERY_SENSORS:
                if _get_nested(battery, path) is not None:
                    entities.append(
                        SitSolarSensor(
                            coordinator, dev_id, key, suffix, path, unit, dclass, sc, "battery"
                        )
                    )
            # electric sensors from monitor response (storage inverter)
            for key, path, suffix, unit, dclass, sc in ELECTRIC_SENSORS:
                if _get_nested(monitor, path) is not None:
                    entities.append(
                        SitSolarSensor(
                            coordinator, dev_id, key, suffix, path, unit, dclass, sc, "monitor"
                        )
                    )

        # For non-storage devices, electric sensors might not exist; skip.

    async_add_entities(entities)