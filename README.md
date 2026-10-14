# Sit Solar (SiNeng EnjoySolar) for Home Assistant

A Home Assistant custom integration for **Sit Solar / SiNeng enjoysolar** solar inverters and EMS stations.

This integration was built by reverse-engineering the official Android app (`Sit Solar.apk`). The app is a **UniApp (Vue)** frontend talking to a SiNeng cloud backend. The integration replicates the same cloud API calls, including the app's AES password encryption.

---

## Features

- UI-based config flow (host, username, password)
- Demo login support (leave password blank)
- AES-128-ECB password encryption exactly as the app does it
- Polling coordinator with configurable scan interval
- Per-device sensors:
  - `active_power`, `pv_total_power`
  - Temperatures: inverter, heatsink, battery
  - Grid frequency, phase voltages/currents (A/B/C)
  - Battery SOC, SOH, voltage, current, power, cycles (storage inverters)
  - Daily energy counters (PV to grid, battery charge/discharge, consumption)
- Station / home-screen sensors (cumulative, monotonically increasing energies):
  - Solar production total (`totalGfProductPower`)
  - Product power total (`totalProductPower`)
  - Grid import / export total
  - Battery charge / discharge total
  - House load total and load-from-PV/battery/grid
  - PV-to-grid / PV-to-battery totals
- Real-time power flow sensors (home screen):
  - Station active power
  - PV / mppt power
  - Grid import / export power
  - House load power
  - Battery power
  - Battery SOC average
  - **Solar power** = `mpptPower + acCoupleGfActivePower` (matches the app home card)
- Device connectivity binary sensor (online/offline)
- Multiple inverters / gateways / meters / EMS / data collectors discovered automatically
- HACS compatible

---

## Repository layout

```
custom_components/sitsolar/
  __init__.py        # entry setup/unload
  api.py             # Sit Solar REST client
  config_flow.py     # UI configuration + options flow
  coordinator.py     # polling coordinator
  sensor.py          # sensor entities
  binary_sensor.py   # online/connectivity
  const.py
  manifest.json
  strings.json
  translations/en.json
docs/ENDPOINTS.md     # full endpoint inventory
test_api.py           # standalone smoke test, no Home Assistant required
hacs.json
README.md
```

---

## Installation

### HACS (recommended)
1. In HACS → **Integrations** → ⋮ → **Custom repositories**
2. Add this repository URL, category **Integration**
3. Search for **Sit Solar** and install
4. Restart Home Assistant
5. Go to **Settings → Devices & Services → Add Integration → Sit Solar**

### Manual
1. Copy `custom_components/sitsolar` into your Home Assistant `config/custom_components/` directory
2. Restart Home Assistant
3. Add the integration via the UI

---

## Configuration

| Field | Description |
|-------|-------------|
| **Host** | Cloud host. Default `https://enjoysolar.si-neng.com`. Demo: `https://demoenjoysolar.si-neng.com:448` |
| **Username** | Your Sit Solar account login name |
| **Password** | Your password. Leave empty to use the demo account (`loginExperience`) |
| **Scan interval** | Poll interval in seconds (default 300) |

The integration logs in via `/auth/login`. Passwords are AES-128-ECB encrypted with the per-session key from `/auth/aesKey`, exactly like the mobile app.

---

## Hosts

| Name | URL |
|------|-----|
| Production | `https://enjoysolar.si-neng.com` |
| Demo | `https://demoenjoysolar.si-neng.com:448` |
| Test / CIM | `https://testcim.si-neng.com:448` |
| Test EnjoySolar | `https://testenjoysolar.si-neng.com:448` |
| Bugfix EnjoySolar | `https://bugfixenjoysolar.si-neng.com:448` |

All hosts expose the same `/prod-api` REST base and the same `/auth/aesKey`.

---

## Backend API overview

### Base

```
https://<host>/prod-api
```

### Authentication

1. Get AES key:

   ```
   GET /auth/aesKey
   -> {"code":20000,"data":"<base64 16-byte key>"}
   ```

2. Encrypt password:

   - Cipher: AES-128-ECB
   - Key: decoded bytes of the base64 AES key
   - Padding: PKCS#7
   - Output: base64

3. Login:

   ```
   POST /auth/login
   Body: {"username":..., "password":"<base64 ciphertext>", "loginType":2, "app":true}
   -> {"code":20000,"data":"<bearer token>"}
   ```

4. Attach header to every request:

   ```
   Authorization: Bearer <token>
   ```

### Standard response envelope

```json
{
  "code": 20000,
  "data": { ... },
  "msg": null,
  "success": true
}
```

Other codes:
- `10008` — login failure (with `deCode`/`phvList` details)
- `50008/50012/50014/50016` — token invalid/expired (integration re-logs-in)
- `20000` — success

### Key device/monitoring endpoints used by this integration

| Purpose | Method | Path |
|---------|--------|------|
| Login | POST | `/auth/login` |
| Demo login | POST | `/auth/loginExperience` |
| Device list (inverters) | POST | `/dev/info/app/v1/devmonitor/appPageInverterMoniterList` |
| Inverter monitor (generic) | GET | `/dev/info/app/v1/devmonitor/getAppInverterDevMonitorDetailMonitor/{devId}` |
| Stored-inverter monitor | GET | `/dev/info/devmonitor/getStoredInverterDevMonitorDetailMonitor/{devId}` |
| Battery monitor | GET | `/dev/info/devmonitor/getStoredInverterBatteryMonitor/{devId}` |
| Station overview | GET | `/business/app/v1/single/overview/appSingleStationOverviewData?stationCode=...` |
| Station power flow | GET | `/business/single/overview/stationEnergyFlowDiagram?stationCode=...` |

### Complete endpoint inventory

- Full documented API reference: [`docs/API.md`](docs/API.md) (~500 endpoints with inferred purpose, method, and observed examples)
- Compact path list: [`docs/ENDPOINTS.md`](docs/ENDPOINTS.md)

---

## App data model notes

### Device list response (`appPageInverterMoniterList`)
Each record contains fields such as:

- `devId`, `devName`, `devModel`, `devTypeId`
- `snCode`, `pnCode`, `parentSn`, `parentId`
- `stationCode`, `stationName`
- `devStatus`, `alarmed`, `attention`
- `activePower`, `totalCap`, `capacity`, `updateTime`
- `timeZone`, `onlineType`, `externalmodel`

Device types seen in the demo:
- `1` — string inverter
- `3` — data collector
- `17` — gate energy meter
- `51` — storage inverter (EMS / hybrid)

### Inverter monitor (`...DevMonitorDetailMonitor`)
- `monitorInformation`: `active_power`, `pv_total_power`, `reactive_power`, `power_factor`, `temperature`, `uwINVSink_Temp`, `uwBatSink1_Temp`, `devStatus`, `alarmed`, `stationOnlineType`, ...
- `generationPowerInfo`: phase voltages/currents/frequencies, `pvNum`, etc.
- `electricInformation` (storage): `total_cap`, `day_*` energies
- `energyFlowInformation`: `uwBatPower_BMS`, `stationOnlineType`
- `appendinfo1`, `timeZone`

### Battery monitor
- `batteryInformation`: `uwBatSoc`, `battery_SOH`, `uwBatVolt_BMS`, `uwBatCurr_BMS`, `uwBatPower_BMS`, `uw_bat_cycle_times`, limits, etc.

### Station overview
Cumulative energies (TOTAL_INCREASING in the integration):
- `totalProductPower`, `totalGfProductPower`
- `totalCellCharge`, `totalCellDischarge`
- `totalBuyGridPower`, `totalOngridPower`
- `totalSelfUsePower`
- `totalLoadUsePower`, `totalLoadUsePvPower`, `totalLoadUseBatteryPower`, `totalLoadUseGridPower`
- `totalPvToGridProductPower`, `totalPvToBatteryProductPower`

Real-time flow:
- `mpptPower`, `buyPower`, `ongridPower`, `loadPower`, `batteryPower`, `batterySocAver`, `acCoupleGfActivePower`

---

## Testing without Home Assistant

A standalone smoke test is included:

```bash
cd /path/to/sitsolar
python3 test_api.py
```

Override host/user/password:

```bash
SITSOLAR_HOST="https://enjoysolar.si-neng.com" \
SITSOLAR_USER="your_username" \
SITSOLAR_PASSWORD="your_password" \
python3 test_api.py
```

Leave `SITSOLAR_PASSWORD` empty to exercise the demo `loginExperience` path.

The script:
1. Fetches `/auth/aesKey`
2. AES-128-ECB encrypts the password (PKCS#7)
3. Logs in via `/auth/login`
4. Lists devices
5. Fetches monitor data per device
6. Fetches battery data for storage inverters
7. Fetches station overview + power flow for each station

---

## Reverse-engineering notes

- The APK is a **UniApp** package. The real logic lives in `assets/apps/__UNI__5F80E0E/www/app-service.js`.
- The base host can be overridden at runtime via `ids-app-url-key` storage (the app's "set URL" screen). The production default is `https://enjoysolar.si-neng.com`, with the demo host `https://demoenjoysolar.si-neng.com:448`.
- REST base is `<host>/prod-api`.
- All calls go through a single wrapper (`utils/request.js`) that attaches `Authorization: Bearer <token>`, logs errors to `/system/log/error/log/create`, and redirects to login on `50008/50012/50014/50016`.
- Tokens come from `/auth/login` (user password) or `/auth/loginExperience` (demo).
- Passwords are AES-encrypted with the key from `/auth/aesKey` (AES-128-ECB, PKCS#7).
- Station data is polled from `/business/app/v1/single/overview/appSingleStationOverviewData` and `/business/single/overview/stationEnergyFlowDiagram`.

---

## Limitations

- Cloud-polling only (no push/local protocol reverse-engineered).
- Controls (work modes, setpoints) are not exposed as Home Assistant services yet.
- Energy sensors model cumulative API totals as `TOTAL_INCREASING`.

---

## License

Reverse-engineering of the official app for personal/interoperability use. Not affiliated with SiNeng / Sit Solar.