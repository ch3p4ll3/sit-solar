# Sit Solar (SiNeng EnjoySolar) for Home Assistant

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![HACS: Custom](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://hacs.xyz)
[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-2024.1%2B-41BDF5.svg)](https://www.home-assistant.io)

A Home Assistant custom integration for **Sit Solar / SiNeng EnjoySolar** solar inverters and EMS stations. It reads your plant's data from the SiNeng cloud and exposes it as Home Assistant sensors, ready for the Energy dashboard.

> **Unofficial project.** Not affiliated with, endorsed by or supported by SiNeng or Sit Solar. It was built by reverse-engineering the official Android app (`Sit Solar.apk`), with AI tools helping to make sense of the app's code. Use it at your own risk.

**Status:** early version (`0.1.0`). Read-only, cloud polling only.

[![Open your Home Assistant instance and open this repository inside HACS.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=ch3p4ll3&repository=sit-solar&category=integration)

---

## Features

- UI-based setup (host, username, password) and an options screen for the scan interval
- Demo mode: leave the password empty
- Same login as the official app, including its AES-128-ECB password encryption
- Automatic discovery of inverters, gateways, meters, EMS and data collectors (up to 100 devices)
- Sensors per device, when the device reports them:
  - Active, PV and reactive power
  - Temperatures: inverter, heatsink, battery
  - Grid frequency, phase voltages and currents (A/B/C)
- Extra sensors for storage inverters (EMS / hybrid):
  - Battery SOC, SOH, voltage, current, power and cycles
  - Daily and total energy counters (PV to grid, battery charge/discharge, consumption)
- One **station** device per plant, with:
  - Cumulative energy totals: solar production, grid import/export, battery charge/discharge, house load (and its split by PV, battery and grid), PV to grid, PV to battery
  - Real-time power flow: station active power, PV, grid import/export, house load, battery power, battery SOC average
  - **Solar power** = `mpptPower + acCoupleGfActivePower`, which matches the app's home card
- Online/offline connectivity binary sensor per device
- Powers are exposed in kW and energies in kWh
- HACS compatible

---

## Installation

**Requirements:** Home Assistant 2024.1.0 or newer, and a Sit Solar account (the same login you use in the app).

### HACS (recommended)

1. In HACS, open **Integrations** → ⋮ → **Custom repositories**
2. Add this repository URL with category **Integration**
3. Search for **Sit Solar** and install it
4. Restart Home Assistant
5. Go to **Settings → Devices & Services → Add Integration → Sit Solar**

### Manual

1. Copy `custom_components/sitsolar` into your Home Assistant `config/custom_components/` directory
2. Restart Home Assistant
3. Add the integration from the UI

---

## Configuration

| Field | Description |
|-------|-------------|
| **Host** | Cloud host. Default `https://enjoysolar.si-neng.com`. Demo: `https://demoenjoysolar.si-neng.com:448` |
| **Username** | Your Sit Solar account login name |
| **Password** | Your password. Leave empty to use the demo account (`loginExperience`) |

After setup, use **Configure** on the integration card to change the **scan interval** (60 to 3600 seconds, default 300). The integration reloads when you save.

The integration logs in via `/auth/login`. Passwords are AES-128-ECB encrypted with the per-session key from `/auth/aesKey`, exactly like the mobile app.

> Entities are created from the data available when the integration starts. If a sensor is missing (for example because the inverter was offline), reload the integration once the data is back.

### Energy dashboard

The station totals are cumulative energy sensors, so they can be used in **Settings → Dashboards → Energy**. A suggested mapping (names are prefixed with your station name):

| Energy dashboard | Sensor |
|------------------|--------|
| Grid consumption | Grid import total |
| Return to grid | Grid export total |
| Solar production | Solar production total |
| Battery: energy going in | Battery charge total |
| Battery: energy coming out | Battery discharge total |

These are the totals reported by the cloud, so compare them with the app before relying on them.

---

## Troubleshooting

- **Invalid authentication:** use the same username and password as in the Sit Solar app, and check the **Host** field.
- **No devices found:** the account has no devices visible in the app.
- **Cannot connect:** the cloud could not be reached or returned an error. Try again later.
- **A sensor is missing:** see the note under *Configuration*; reload the integration.
- **Debug logging:** add this to `configuration.yaml`, restart, and reproduce the problem:

  ```yaml
  logger:
    default: warning
    logs:
      custom_components.sitsolar: debug
  ```

This is an unofficial client of a private API, so the cloud may change without notice.

### Reporting issues

Please include your Home Assistant version, the integration version, your device model and type (`devTypeId`), and the debug log. **Remove passwords, tokens, serial numbers (`snCode`), station codes and station names before posting anything.** Note that `test_api.py` prints the AES key and the bearer token to the terminal, so never paste its output unredacted.

Devices seen so far are types `1`, `3`, `17` and `51` (see below). If yours is different, an issue with anonymised output of `test_api.py` helps a lot. Pull requests are welcome.

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
docs/API.md           # full API reference (inferred from the app)
docs/ENDPOINTS.md     # compact endpoint list
test_api.py           # standalone smoke test, no Home Assistant required
hacs.json
LICENSE
README.md
```

---

## Technical notes

### Hosts

| Name | URL |
|------|-----|
| Production | `https://enjoysolar.si-neng.com` |
| Demo | `https://demoenjoysolar.si-neng.com:448` |
| Test / CIM | `https://testcim.si-neng.com:448` |
| Test EnjoySolar | `https://testenjoysolar.si-neng.com:448` |
| Bugfix EnjoySolar | `https://bugfixenjoysolar.si-neng.com:448` |

All hosts expose the same `/prod-api` REST base and the same `/auth/aesKey`.

### Backend API overview

#### Base

```
https://<host>/prod-api
```

#### Authentication

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

#### Standard response envelope

```json
{
  "code": 20000,
  "data": { ... },
  "msg": null,
  "success": true
}
```

Other codes:
- `10008`: login failure (with `deCode`/`phvList` details)
- `50008/50012/50014/50016`: token invalid/expired (the integration logs in again)
- `20000`: success

#### Key device/monitoring endpoints used by this integration

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

#### Complete endpoint inventory

- Full API reference: [`docs/API.md`](docs/API.md) (about 500 endpoints with inferred purpose, method and observed examples; most of them are untested)
- Compact path list: [`docs/ENDPOINTS.md`](docs/ENDPOINTS.md)

### App data model

#### Device list response (`appPageInverterMoniterList`)

Each record contains fields such as:

- `devId`, `devName`, `devModel`, `devTypeId`
- `snCode`, `pnCode`, `parentSn`, `parentId`
- `stationCode`, `stationName`
- `devStatus`, `alarmed`, `attention`
- `activePower`, `totalCap`, `capacity`, `updateTime`
- `timeZone`, `onlineType`, `externalmodel`

Device types seen in the demo:
- `1`: string inverter
- `3`: data collector
- `17`: gate energy meter
- `51`: storage inverter (EMS / hybrid)

#### Inverter monitor (`...DevMonitorDetailMonitor`)

- `monitorInformation`: `active_power`, `pv_total_power`, `reactive_power`, `power_factor`, `temperature`, `uwINVSink_Temp`, `uwBatSink1_Temp`, `devStatus`, `alarmed`, `stationOnlineType`, ...
- `generationPowerInfo`: phase voltages/currents/frequencies, `pvNum`, etc.
- `electricInformation` (storage): `total_cap`, `day_*` energies
- `energyFlowInformation`: `uwBatPower_BMS`, `stationOnlineType`
- `appendinfo1`, `timeZone`

#### Battery monitor

- `batteryInformation`: `uwBatSoc`, `battery_SOH`, `uwBatVolt_BMS`, `uwBatCurr_BMS`, `uwBatPower_BMS`, `uw_bat_cycle_times`, limits, etc.

#### Station overview

Cumulative energies (`TOTAL_INCREASING` in the integration):
- `totalProductPower`, `totalGfProductPower`
- `totalCellCharge`, `totalCellDischarge`
- `totalBuyGridPower`, `totalOngridPower`
- `totalSelfUsePower`
- `totalLoadUsePower`, `totalLoadUsePvPower`, `totalLoadUseBatteryPower`, `totalLoadUseGridPower`
- `totalPvToGridProductPower`, `totalPvToBatteryProductPower`

Real-time flow:
- `mpptPower`, `buyPower`, `ongridPower`, `loadPower`, `batteryPower`, `batterySocAver`, `acCoupleGfActivePower`

### Reverse-engineering notes

- The APK is a **UniApp** (Vue) package. The real logic lives in `assets/apps/__UNI__5F80E0E/www/app-service.js`. AI tools were used to help read and understand this bundle.
- The base host can be overridden at runtime via `ids-app-url-key` storage (the app's "set URL" screen). The production default is `https://enjoysolar.si-neng.com`, with the demo host `https://demoenjoysolar.si-neng.com:448`.
- REST base is `<host>/prod-api`.
- All calls go through a single wrapper (`utils/request.js`) that attaches `Authorization: Bearer <token>`, logs errors to `/system/log/error/log/create`, and redirects to login on `50008/50012/50014/50016`.
- Tokens come from `/auth/login` (user password) or `/auth/loginExperience` (demo).
- Passwords are AES-encrypted with the key from `/auth/aesKey` (AES-128-ECB, PKCS#7).
- Station data is polled from `/business/app/v1/single/overview/appSingleStationOverviewData` and `/business/single/overview/stationEnergyFlowDiagram`.

### Testing without Home Assistant

A standalone test script is included. It needs Python 3, the `python-dotenv` package and the `openssl` command-line tool:

```bash
pip install python-dotenv
python3 test_api.py
```

By default it talks to the demo host. Override host, user and password with environment variables or a `.env` file (already in `.gitignore`):

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

## Limitations

- Cloud polling only (no push or local protocol reverse-engineered). The minimum scan interval is 60 seconds.
- Read-only: controls (work modes, setpoints) are not exposed as Home Assistant services.
- **TLS certificate verification is currently disabled** for requests to the cloud, including the login request (`ssl=False` in `api.py`).
- Energy sensors model the cumulative API totals as `TOTAL_INCREASING`.
- Only the first 100 devices of an account are listed.

---

## License

Released under the [GNU General Public License v3.0](LICENSE).

Reverse-engineering of the official app for personal and interoperability use. Not affiliated with SiNeng / Sit Solar. Provided as is, without warranty.