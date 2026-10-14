#!/usr/bin/env python3
"""Standalone API smoke test for Sit Solar (no Home Assistant/aiohttp required)."""
import base64
import json
import os
import ssl
import subprocess
import sys
import urllib.parse
import urllib.request
import urllib.error
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("SITSOLAR_HOST", "https://demoenjoysolar.si-neng.com:448").rstrip("/")
USERNAME = os.getenv("SITSOLAR_USER", "demoUser")
PASSWORD = os.getenv("SITSOLAR_PASSWORD", "")
BASE = HOST + "/prod-api"


def request(method, path, token=None, payload=None, params=None):
    url = BASE + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Content-Type", "application/json")
    if token:
        req.add_header("Authorization", "Bearer " + token)
    try:
        with urllib.request.urlopen(req, context=ssl._create_unverified_context()) as r:
            raw = r.read()
    except urllib.error.HTTPError as e:
        raw = e.read()
    return json.loads(raw)


def aes_encrypt(plain, key):
    p = subprocess.run(
        ["openssl", "enc", "-aes-128-ecb", "-K", key.encode().hex(), "-a", "-A"],
        input=plain.encode(), capture_output=True, check=True,
    )
    return p.stdout.decode().strip()


def main():
    # AES key
    key_resp = request("GET", "/auth/aesKey")
    key = base64.b64decode(key_resp["data"]).decode()
    print("AES key:", key)

    # Login
    if not PASSWORD:
        login_resp = request("POST", "/auth/loginExperience", payload={"isApp": True})
    else:
        cipher = aes_encrypt(PASSWORD, key)
        login_resp = request("POST", "/auth/login", payload={
            "username": USERNAME,
            "password": cipher,
            "loginType": 2,
            "app": True,
        })
    print("Login:", login_resp.get("code"), login_resp.get("msg"))
    token = login_resp["data"]
    print("Token:", token)

    # Devices
    devs_resp = request("POST", "/dev/info/app/v1/devmonitor/appPageInverterMoniterList",
                        token=token, payload={"page": 1, "size": 20})
    records = (devs_resp.get("data") or {}).get("records", [])
    print("Devices:", len(records))
    for dev in records:
        dev_id = dev["devId"]
        dev_type = dev.get("devTypeId")
        print("\nDEVICE", dev_id, dev.get("devName"), "type", dev_type)

        # Monitor
        if dev_type == 51:
            mon_path = f"/dev/info/devmonitor/getStoredInverterDevMonitorDetailMonitor/{dev_id}"
        else:
            mon_path = f"/dev/info/app/v1/devmonitor/getAppInverterDevMonitorDetailMonitor/{dev_id}"
        mon = request("GET", mon_path, token=token)
        print("Monitor code:", mon.get("code"))
        mi = (mon.get("data") or {}).get("monitorInformation", {})
        print("  active_power:", mi.get("active_power"))
        print("  pv_total_power:", mi.get("pv_total_power"))
        print("  temperature:", mi.get("temperature"))
        print("  battery uwBatPower_BMS:", mi.get("uwBatPower_BMS"))

        if dev_type == 51:
            bat = request("GET", f"/dev/info/devmonitor/getStoredInverterBatteryMonitor/{dev_id}", token=token)
            print("Battery code:", bat.get("code"))
            bi = (bat.get("data") or {}).get("batteryInformation", {})
            print("  SOC:", bi.get("uwBatSoc"))
            print("  SOH:", bi.get("battery_SOH"))
            print("  voltage:", bi.get("uwBatVolt_BMS"))
            print("  current:", bi.get("uwBatCurr_BMS"))

    # Station-level home screen data
    seen = set()
    for dev in records:
        sc = dev.get("stationCode")
        if not sc or sc in seen:
            continue
        seen.add(sc)
        print("\nSTATION", sc, dev.get("stationName"))
        ov = request("GET", "/business/app/v1/single/overview/appSingleStationOverviewData",
                    token=token, params={"stationCode": sc})
        print("  overview code:", ov.get("code"))
        if ov.get("code") == 20000:
            d = ov.get("data") or {}
            for k in ("activePower", "totalProductPower", "totalCellCharge",
                      "totalCellDischarge", "totalBuyGridPower", "totalOngridPower",
                      "totalLoadUsePower"):
                print(f"    {k}: {d.get(k)}")
        flow = request("GET", "/business/single/overview/stationEnergyFlowDiagram",
                      token=token, params={"stationCode": sc})
        print("  flow code:", flow.get("code"))
        if flow.get("code") == 20000:
            d = flow.get("data") or {}
            for k in ("ongridPower", "buyPower", "loadPower", "mpptPower",
                      "batteryPower", "batterySocAver"):
                print(f"    {k}: {d.get(k)}")


if __name__ == "__main__":
    main()