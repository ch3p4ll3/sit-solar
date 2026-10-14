# Sit Solar (SiNeng) Home Assistant integration

Custom integration for solar inverters monitored via the Sit Solar / SiNeng cloud API.

## Setup
Install via HACS or copy `custom_components/sitsolar` into your Home Assistant configuration directory, then add the integration in the UI. Use your Sit Solar account credentials. Default host is `https://enjoysolar.si-neng.com`; use `https://demoenjoysolar.si-neng.com:448` for the demo account.

## Notes
Reverse engineered from the Sit Solar Android app (UniApp). Cloud polling.