# Sit Solar (SiNeng EnjoySolar) API reference
This document is generated from the strings and request calls found in `assets/apps/__UNI__5F80E0E/www/app-service.js` inside `Sit Solar.apk`.

All REST endpoints are relative to:

- Production: `https://enjoysolar.si-neng.com/prod-api`
- Demo: `https://demoenjoysolar.si-neng.com:448/prod-api`

Every endpoint returns the standard envelope:

```json
{"code":20000,"data":{...},"msg":null,"success":true}
```

Authentication: `Authorization: Bearer <token>` for all non-auth endpoints.

## How authentication works
1. `GET /auth/aesKey` returns a base64 16-byte AES key.
2. Password is AES-128-ECB encrypted with PKCS#7 padding using that key.
3. `POST /auth/login` sends `{username, password:<base64 ciphertext>, loginType:2, app:true}` and returns a bearer token.
4. Demo mode uses `POST /auth/loginExperience` with `{isApp:true}` instead of a password.
5. Token failures (`50008/50012/50014/50016`) require re-login.

## Home Assistant integration endpoint usage
| Purpose | Method | Path |
|---|---|---|
| Login | POST | `/auth/login` |
| AES key | GET | `/auth/aesKey` |
| Demo login | POST | `/auth/loginExperience` |
| Device list | POST | `/dev/info/app/v1/devmonitor/appPageInverterMoniterList` |
| Generic inverter monitor | GET | `/dev/info/app/v1/devmonitor/getAppInverterDevMonitorDetailMonitor/{devId}` |
| Stored inverter monitor | GET | `/dev/info/devmonitor/getStoredInverterDevMonitorDetailMonitor/{devId}` |
| Battery monitor | GET | `/dev/info/devmonitor/getStoredInverterBatteryMonitor/{devId}` |
| Station overview | GET | `/business/app/v1/single/overview/appSingleStationOverviewData` |
| Station power flow | GET | `/business/single/overview/stationEnergyFlowDiagram` |

## Endpoint groups

### alarm/config
| Method | Path | Inferred purpose |
|---|---|---|
| POST | `/alarm/config/getSignalVersons?devTypeId=` | Alarm lifecycle, notifications, and alarm details. get Signal Versons?dev Type Id= |
| POST | `/alarm/config/listAlarmModel` | Alarm lifecycle, notifications, and alarm details. list Alarm Model |
| POST | `/alarm/config/updateAlarmModel` | Alarm lifecycle, notifications, and alarm details. update Alarm Model |

### alarm/deadly
| Method | Path | Inferred purpose |
|---|---|---|
| POST | `/alarm/deadly/push/getAlarmUnreadNumByUserId` | Alarm lifecycle, notifications, and alarm details. get Alarm Unread Num By User Id |
| GET | `/alarm/deadly/push/getByUserId` | Alarm lifecycle, notifications, and alarm details. get By User Id |
| POST | `/alarm/deadly/push/getInfoList` | Alarm lifecycle, notifications, and alarm details. get Info List |
| POST | `/alarm/deadly/push/saveOrUpdate` | Alarm lifecycle, notifications, and alarm details. save Or Update |
| POST | `/alarm/deadly/read/deleteAlarmReadByUserId` | Alarm lifecycle, notifications, and alarm details. delete Alarm Read By User Id |
| POST | `/alarm/deadly/read/deleteAlarmReadMessageByUserId` | Alarm lifecycle, notifications, and alarm details. delete Alarm Read Message By User Id |

### alarm/email
| Method | Path | Inferred purpose |
|---|---|---|
| POST | `/alarm/email/rule/create` | Alarm lifecycle, notifications, and alarm details. create |
| GET | `/alarm/email/rule/info/` | Alarm lifecycle, notifications, and alarm details. rule info |
| DELETE | `/alarm/email/rule/remove/` | Alarm lifecycle, notifications, and alarm details. remove |
| PUT | `/alarm/email/rule/update` | Alarm lifecycle, notifications, and alarm details. update |

### alarm/ignore
| Method | Path | Inferred purpose |
|---|---|---|
| POST | `/alarm/ignore/rule/delete/` | Alarm lifecycle, notifications, and alarm details. delete |
| GET | `/alarm/ignore/rule/detail/` | Alarm lifecycle, notifications, and alarm details. detail |
| POST | `/alarm/ignore/rule/insert` | Alarm lifecycle, notifications, and alarm details. insert |
| GET | `/alarm/ignore/rule/list` | Alarm lifecycle, notifications, and alarm details. rule list |
| POST | `/alarm/ignore/rule/modify/` | Alarm lifecycle, notifications, and alarm details. modify |

### alarm/judgementAlarmsExistUnfinishDefect?devAlarms=
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/alarm/judgementAlarmsExistUnfinishDefect?devAlarms=` | Alarm lifecycle, notifications, and alarm details. judgement Alarms Exist Unfinish Defect?dev Alarms= |

### alarm/model
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/alarm/model/pageAlarmModel` | Alarm lifecycle, notifications, and alarm details. page Alarm Model |

### analysis/alarm
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/analysis/alarm/model/pageAnalysisAlarmModel` | Alarm lifecycle, notifications, and alarm details. page Analysis Alarm Model |

### app
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/app/v1/alarm/appAlarmMessageNum` | Alarm lifecycle, notifications, and alarm details. app Alarm Message Num |
| GET | `/app/v1/alarm/appAlarmMessageSet` | Alarm lifecycle, notifications, and alarm details. app Alarm Message Set |
| POST | `/app/v1/alarm/appGetAlarmMessageList` | Alarm lifecycle, notifications, and alarm details. app Get Alarm Message List |
| GET | `/app/v1/alarm/appListByCreateDefect` | Alarm lifecycle, notifications, and alarm details. app List By Create Defect |
| GET | `/app/v1/alarm/appMonitorCompletePercent` | Alarm lifecycle, notifications, and alarm details. app Monitor Complete Percent |
| GET | `/app/v1/alarm/appPageDevAlarmDeadly` | Alarm lifecycle, notifications, and alarm details. app Page Dev Alarm Deadly |
| GET | `/app/v1/alarm/appPageDevAlarmDeadlySet` | Alarm lifecycle, notifications, and alarm details. app Page Dev Alarm Deadly Set |
| POST | `/app/v1/alarm/appPageDevAlarmExport` | Alarm lifecycle, notifications, and alarm details. app Page Dev Alarm Export |
| GET | `/app/v1/alarm/clear/list` | Alarm lifecycle, notifications, and alarm details. clear list |
| GET | `/app/v1/alarm/list` | Alarm lifecycle, notifications, and alarm details. alarm list |
| POST | `/app/v1/alarm/pageAlarmSearchList` | Alarm lifecycle, notifications, and alarm details. page Alarm Search List |
| POST | `/app/v1/alarm/pageAlarmSearchListMore` | Alarm lifecycle, notifications, and alarm details. page Alarm Search List More |
| POST | `/app/v1/alarm/pageAlarmSearchNum` | Alarm lifecycle, notifications, and alarm details. page Alarm Search Num |
| POST | `/app/v1/alarm/pageAlarmSearchNumMore` | Alarm lifecycle, notifications, and alarm details. page Alarm Search Num More |
| POST | `/app/v1/dev/info/appStationBindDevs?idList=` | Device, devmonitor, remote maintenance, or data-collection operations. app Station Bind Devs?id List= |
| GET | `/app/v1/dev/info/pageDevPvSet` | Device, devmonitor, remote maintenance, or data-collection operations. page Dev Pv Set |
| GET | `/app/v1/devmonitor/appDevList` | Device/station monitoring and real-time metrics. app Dev List |
| GET | `/app/v1/devmonitor/appUpdateDevName` | Device/station monitoring and real-time metrics. app Update Dev Name |
| GET | `/app/v1/devmonitor/pageParentNullDev` | Device/station monitoring and real-time metrics. page Parent Null Dev |
| GET | `/app/v1/station/info/appSearchStation` | Station management, sharing, pricing, and station-level metadata. app Search Station |

### app/workflow
| Method | Path | Inferred purpose |
|---|---|---|
| POST | `/app/workflow/defect/operDefect` | Defect/workflow management. oper Defect |
| POST | `/app/workflow/defect/saveAndAssignDefect` | Defect/workflow management. save And Assign Defect |
| POST | `/app/workflow/defect/saveDefect` | Defect/workflow management. save Defect |

### appAddLabel?labelName=
| Method | Path | Inferred purpose |
|---|---|---|
| POST | `/appAddLabel?labelName=` | app Add Label?label Name=. |

### appAddStation
| Method | Path | Inferred purpose |
|---|---|---|
| POST | `/appAddStation` | app Add Station. |

### appCancelAccount
| Method | Path | Inferred purpose |
|---|---|---|
| DELETE | `/appCancelAccount` | app Cancel Account. |

### appDefectSearch
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/appDefectSearch` | app Defect Search. |

### appDeleteLabel?id=
| Method | Path | Inferred purpose |
|---|---|---|
| DELETE | `/appDeleteLabel?id=` | app Delete Label?id=. |

### appDevMonitorStatistic
| Method | Path | Inferred purpose |
|---|---|---|
| POST | `/appDevMonitorStatistic` | Device/station monitoring and real-time metrics. app Dev Monitor Statistic |

### appEnergyFlowGraph?stationCode=
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/appEnergyFlowGraph?stationCode=` | app Energy Flow Graph?station Code=. |

### appEnergyFlowGraphNew?stationCode=
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/appEnergyFlowGraphNew?stationCode=` | app Energy Flow Graph New?station Code=. |

### appEnvironmentalContribution
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/appEnvironmentalContribution` | app Environmental Contribution. |

### appEnvironmentalContribution?stationCode=
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/appEnvironmentalContribution?stationCode=` | app Environmental Contribution?station Code=. |

### appGeneratePowerAndPower
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/appGeneratePowerAndPower` | app Generate Power And Power. |

### appGeneratePowerProfile
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/appGeneratePowerProfile` | app Generate Power Profile. |

### appGetAllSmDepInfo?name=
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/appGetAllSmDepInfo?name=` | app Get All Sm Dep Info?name=. |

### appGetAllSmDepInfoNoLimit
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/appGetAllSmDepInfoNoLimit` | app Get All Sm Dep Info No Limit. |

### appGetCurrentUserInfo
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/appGetCurrentUserInfo` | app Get Current User Info. |

### appGetWeatherDaily?stationCode=
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/appGetWeatherDaily?stationCode=` | app Get Weather Daily?station Code=. |

### appIncomeProfile?stationCode=
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/appIncomeProfile?stationCode=` | app Income Profile?station Code=. |

### appInverterAlarm
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/appInverterAlarm` | app Inverter Alarm. |

### appInverterKpi
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/appInverterKpi` | app Inverter Kpi. |

### appInverterKpiDataGraph
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/appInverterKpiDataGraph` | app Inverter Kpi Data Graph. |

### appMonitorRelTime
| Method | Path | Inferred purpose |
|---|---|---|
| POST | `/appMonitorRelTime` | Device/station monitoring and real-time metrics. app Monitor Rel Time |

### appMyAttentionDev
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/appMyAttentionDev` | app My Attention Dev. |

### appMyAttentionStation
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/appMyAttentionStation` | app My Attention Station. |

### appOperateAttention?stationCode=
| Method | Path | Inferred purpose |
|---|---|---|
| POST | `/appOperateAttention?stationCode=` | app Operate Attention?station Code=. |

### appPageBySnCode
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/appPageBySnCode` | app Page By Sn Code. |

### appPageInverterMoniterAllList
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/appPageInverterMoniterAllList` | Device/station monitoring and real-time metrics. app Page Inverter Monitor All List |

### appPageInverterMoniterList
| Method | Path | Inferred purpose |
|---|---|---|
| GET* | `/appPageInverterMoniterList` | Device/station monitoring and real-time metrics. app Page Inverter Monitor List |

### appPageNumberCollectMoniterList
| Method | Path | Inferred purpose |
|---|---|---|
| POST | `/appPageNumberCollectMoniterList` | Device/station monitoring and real-time metrics. app Page Number Collect Monitor List |

### appPageStationByCurrentUser
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/appPageStationByCurrentUser` | app Page Station By Current User. |

### appPowerCurve
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/appPowerCurve` | app Power Curve. |

### appRemoteMaintain
| Method | Path | Inferred purpose |
|---|---|---|
| POST | `/appRemoteMaintain` | app Remote Maintain. |

### appStationBusinessList
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/appStationBusinessList` | app Station Business List. |

### appStationBusinessPage
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/appStationBusinessPage` | app Station Business Page. |

### appTodayPowerCurve
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/appTodayPowerCurve` | app Today Power Curve. |

### appUdateCurrentUserPassword
| Method | Path | Inferred purpose |
|---|---|---|
| PUT | `/appUdateCurrentUserPassword` | app Udate Current User Password. |

### appUnsubscribeDev?devId=
| Method | Path | Inferred purpose |
|---|---|---|
| POST | `/appUnsubscribeDev?devId=` | app Unsubscribe Dev?dev Id=. |

### appUnsubscribeStation?stationCode=
| Method | Path | Inferred purpose |
|---|---|---|
| POST | `/appUnsubscribeStation?stationCode=` | app Unsubscribe Station?station Code=. |

### appUpdateCurrentUserInfo
| Method | Path | Inferred purpose |
|---|---|---|
| PUT | `/appUpdateCurrentUserInfo` | app Update Current User Info. |

### auth
| Method | Path | Inferred purpose |
|---|---|---|
| PUT | `/auth` | auth. |

### auth/checkOff?checkInfo=
| Method | Path | Inferred purpose |
|---|---|---|
| POST | `/auth/checkOff?checkInfo=` | Authentication / account security. check Off?check Info= |

### auth/loginExperience
| Method | Path | Inferred purpose |
|---|---|---|
| POST | `/auth/loginExperience` | Authentication / account security. login Experience |

### business
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/business/app/dev/dataStatic/getEnvironmentVocDetailInfoData` | Device, devmonitor, remote maintenance, or data-collection operations. get Environment Voc Detail Info Data |
| GET | `/business/app/dev/dataStatic/getGateEneryMeterDetailInfoData` | Device, devmonitor, remote maintenance, or data-collection operations. get Gate Enery Meter Detail Info Data |
| GET | `/business/app/dev/dataStatic/getNumCollectDetailInfoData` | Device, devmonitor, remote maintenance, or data-collection operations. get Num Collect Detail Info Data |
| GET | `/business/app/dev/dataStatic/getSeriesInverterDetailInfoData` | Device, devmonitor, remote maintenance, or data-collection operations. get Series Inverter Detail Info Data |
| GET | `/business/app/v1/inverter/report` | Business/overview/reporting feature. report |
| GET | `/business/app/v1/single/overview` | Business/overview/reporting feature. overview |
| GET | `/business/app/v1/single/overview/appSingleStationOverviewData` | Business/overview/reporting feature. app Single Station Overview Data |
| POST | `/business/app/v1/station/business/appStationPage` | Station management, sharing, pricing, and station-level metadata. app Station Page |
| POST | `/business/app/v1/station/business/pageSearchList` | Station management, sharing, pricing, and station-level metadata. page Search List |
| GET | `/business/app/v1/total/overview` | Business/overview/reporting feature. overview |
| GET | `/business/app/v1/total/overview/appListExceptionStation` | Business/overview/reporting feature. app List Exception Station |
| GET | `/business/app/v1/total/overview/appStationOverviewData` | Business/overview/reporting feature. app Station Overview Data |
| GET | `/business/app/v1/total/overview/appStationRanking` | Business/overview/reporting feature. app Station Ranking |
| GET | `/business/app/v1/user/project` | Business/overview/reporting feature. project |
| GET | `/business/app/v1/user/project/appListEnterpriseByUserId` | Business/overview/reporting feature. app List Enterprise By User Id |
| GET | `/business/app/v1/user/project/appSearchUserForAddWorkOder` | Business/overview/reporting feature. app Search User For Add Work Oder |

### business/dev
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/business/dev/dataStatic/curveStatistic` | Device, devmonitor, remote maintenance, or data-collection operations. curve Statistic |
| GET | `/business/dev/dataStatic/getBatteryClusterDetailInfoData` | Device, devmonitor, remote maintenance, or data-collection operations. get Battery Cluster Detail Info Data |
| GET | `/business/dev/dataStatic/getBatteryClusterDetailInfoDataPoint` | Device, devmonitor, remote maintenance, or data-collection operations. get Battery Cluster Detail Info Data Point |
| GET | `/business/dev/dataStatic/getCentralizedInverterDetailInfoData` | Device, devmonitor, remote maintenance, or data-collection operations. get Centralized Inverter Detail Info Data |
| GET | `/business/dev/dataStatic/getCentralizedInverterDetailInfoDataPoint` | Device, devmonitor, remote maintenance, or data-collection operations. get Centralized Inverter Detail Info Data Point |
| GET | `/business/dev/dataStatic/getEnergyBankDetailInfoData` | Device, devmonitor, remote maintenance, or data-collection operations. get Energy Bank Detail Info Data |
| GET | `/business/dev/dataStatic/getEnergyQualityDetailInfoData` | Device, devmonitor, remote maintenance, or data-collection operations. get Energy Quality Detail Info Data |
| GET | `/business/dev/dataStatic/getEnergyQualityDetailInfoDataPoint` | Device, devmonitor, remote maintenance, or data-collection operations. get Energy Quality Detail Info Data Point |
| GET | `/business/dev/dataStatic/getEnvironmentVocDetailInfoDataPoint` | Device, devmonitor, remote maintenance, or data-collection operations. get Environment Voc Detail Info Data Point |
| GET | `/business/dev/dataStatic/getGateEneryMeterDetailInfoDataPoint` | Device, devmonitor, remote maintenance, or data-collection operations. get Gate Enery Meter Detail Info Data Point |
| GET | `/business/dev/dataStatic/getNumCollectDetailInfoDataPoint` | Device, devmonitor, remote maintenance, or data-collection operations. get Num Collect Detail Info Data Point |
| GET | `/business/dev/dataStatic/getSeriesInverterDetailInfoDataPoint` | Device, devmonitor, remote maintenance, or data-collection operations. get Series Inverter Detail Info Data Point |
| GET | `/business/dev/dataStatic/getStoredInverterDetailInfoData` | Device, devmonitor, remote maintenance, or data-collection operations. get Stored Inverter Detail Info Data |
| GET | `/business/dev/dataStatic/getStoredInverterDetailInfoDataPoint` | Device, devmonitor, remote maintenance, or data-collection operations. get Stored Inverter Detail Info Data Point |
| GET | `/business/dev/project/generalSelectStation` | Device, devmonitor, remote maintenance, or data-collection operations. general Select Station |
| GET | `/business/dev/project/pageAlarmEmailRule` | Device, devmonitor, remote maintenance, or data-collection operations. page Alarm Email Rule |
| DELETE | `/business/dev/project/removeStationByCode?stationCode=` | Device, devmonitor, remote maintenance, or data-collection operations. remove Station By Code?station Code= |

### business/inverter
| Method | Path | Inferred purpose |
|---|---|---|
| GET* | `/business/inverter/report/page?stationCode=` | Business/overview/reporting feature. page?station Code= |

### business/single
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/business/single/overview/generatePowerAndPowerStatistic` | Business/overview/reporting feature. generate Power And Power Statistic |
| GET | `/business/single/overview/listStationEquivalentHourSingle` | Business/overview/reporting feature. list Station Equivalent Hour Single |
| GET | `/business/single/overview/radiationAndPower` | Business/overview/reporting feature. radiation And Power |
| GET | `/business/single/overview/singleStationKpiData` | Business/overview/reporting feature. single Station Kpi Data |
| GET | `/business/single/overview/socSohAndPower` | Business/overview/reporting feature. soc Soh And Power |
| GET | `/business/single/overview/stationEnergyFlowDiagram` | Station management, sharing, pricing, and station-level metadata. station Energy Flow Diagram |
| GET | `/business/single/overview/stationEnergyFlowDiagramReTime` | Station management, sharing, pricing, and station-level metadata. station Energy Flow Diagram Re Time |

### business/station
| Method | Path | Inferred purpose |
|---|---|---|
| POST | `/business/station/business/page` | Station management, sharing, pricing, and station-level metadata. page |
| POST | `/business/station/business/stationPageExport` | Station management, sharing, pricing, and station-level metadata. station Page Export |
| POST | `/business/station/business/stationStatusCount` | Station management, sharing, pricing, and station-level metadata. station Status Count |
| POST | `/business/station/report/pageMonthReportByCurrentUser` | Station management, sharing, pricing, and station-level metadata. page Month Report By Current User |
| POST | `/business/station/report/singleMonthReportByStationCode` | Station management, sharing, pricing, and station-level metadata. single Month Report By Station Code |

### business/total
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/business/total/overview/generatePowerAndPowerStatistic` | Business/overview/reporting feature. generate Power And Power Statistic |
| GET | `/business/total/overview/getPowerCurve` | Business/overview/reporting feature. get Power Curve |
| GET | `/business/total/overview/stationEquivalentHour` | Station management, sharing, pricing, and station-level metadata. station Equivalent Hour |
| GET | `/business/total/overview/stationOverviewData` | Station management, sharing, pricing, and station-level metadata. station Overview Data |

### business/workflow
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/business/workflow/defect/assignDefect?workflowDefectId=` | Business/overview/reporting feature. assign Defect?workflow Defect Id= |
| GET | `/business/workflow/defect/remark?workflowDefectId=` | Business/overview/reporting feature. remark?workflow Defect Id= |
| DELETE | `/business/workflow/defect/remove/` | Business/overview/reporting feature. remove |

### change/alarm
| Method | Path | Inferred purpose |
|---|---|---|
| POST | `/change/alarm/relation/getAlarmRelationList` | Alarm lifecycle, notifications, and alarm details. get Alarm Relation List |
| POST | `/change/alarm/relation/stationAdjust/` | Alarm lifecycle, notifications, and alarm details. station Adjust |

### command/model
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/command/model/details/queryCommandModelDetailsByDevId` | Command and firmware/parameter model management. query Command Model Details By Dev Id |

### config/nav
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/config/nav/assistance/conf/listByPageIdAndType` | System configuration parameters. list By Page Id And Type |

### config/system
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/config/system/config/param/getListByModule` | System configuration parameters. get List By Module |

### dev
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/dev/info` | Device, devmonitor, remote maintenance, or data-collection operations. dev info |
| GET | `/dev/info/alarm/alarmMonitorStatistic` | Alarm lifecycle, notifications, and alarm details. alarm Monitor Statistic |
| GET | `/dev/info/alarm/deadly/read/updateDealyStatusId` | Alarm lifecycle, notifications, and alarm details. update Dealy Status Id |
| GET | `/dev/info/alarm/getUnreadAlarmCountSingle` | Alarm lifecycle, notifications, and alarm details. get Unread Alarm Count Single |
| GET | `/dev/info/alarm/pageDevAlarmDeadly` | Alarm lifecycle, notifications, and alarm details. page Dev Alarm Deadly |
| GET | `/dev/info/app/alarm/deadly/read/alarmReadMessageByUserId` | Alarm lifecycle, notifications, and alarm details. alarm Read Message By User Id |
| GET | `/dev/info/app/v1` | Device, devmonitor, remote maintenance, or data-collection operations. v1 |
| GET* | `/dev/info/app/v1/alarm/appAlarmMessageNum` | Alarm lifecycle, notifications, and alarm details. app Alarm Message Num |
| GET | `/dev/info/app/v1/alarm/appAlarmStatistic` | Alarm lifecycle, notifications, and alarm details. app Alarm Statistic |
| GET | `/dev/info/app/v1/alarm/appAlarmStatisticSingle` | Alarm lifecycle, notifications, and alarm details. app Alarm Statistic Single |
| POST | `/dev/info/app/v1/alarm/appConfirmAlarm?id=` | Alarm lifecycle, notifications, and alarm details. app Confirm Alarm?id= |
| GET | `/dev/info/app/v1/alarm/appDevAlarmDeadly` | Alarm lifecycle, notifications, and alarm details. app Dev Alarm Deadly |
| GET | `/dev/info/app/v1/alarm/appGetAlarmDetail?id=` | Alarm lifecycle, notifications, and alarm details. app Get Alarm Detail?id= |
| GET | `/dev/info/app/v1/alarm/appGetUnreadAlarmCount` | Alarm lifecycle, notifications, and alarm details. app Get Unread Alarm Count |
| POST | `/dev/info/app/v1/alarm/appGetUnreadAlarmList?alarmType=` | Alarm lifecycle, notifications, and alarm details. app Get Unread Alarm List?alarm Type= |
| POST | `/dev/info/app/v1/alarm/appManualClearAlarm?id=` | Alarm lifecycle, notifications, and alarm details. app Manual Clear Alarm?id= |
| GET* | `/dev/info/app/v1/alarm/appMonitorCompletePercent` | Alarm lifecycle, notifications, and alarm details. app Monitor Complete Percent |
| PUT | `/dev/info/app/v1/alarm/appReadAlarm` | Alarm lifecycle, notifications, and alarm details. app Read Alarm |
| GET | `/dev/info/app/v1/alarm/appSingleStationSearch` | Alarm lifecycle, notifications, and alarm details. app Single Station Search |
| GET | `/dev/info/app/v1/alarm/appUpdateRemarks` | Alarm lifecycle, notifications, and alarm details. app Update Remarks |
| GET | `/dev/info/app/v1/alarm/listAll` | Alarm lifecycle, notifications, and alarm details. list All |
| GET | `/dev/info/app/v1/dev/info` | Device, devmonitor, remote maintenance, or data-collection operations. dev info |
| GET | `/dev/info/app/v1/dev/info/appDevCountStatistic` | Device, devmonitor, remote maintenance, or data-collection operations. app Dev Count Statistic |
| GET | `/dev/info/app/v1/dev/info/appGetDevCountByCurrentUser` | Device, devmonitor, remote maintenance, or data-collection operations. app Get Dev Count By Current User |
| GET | `/dev/info/app/v1/dev/info/appJudgementHaveBind` | Device, devmonitor, remote maintenance, or data-collection operations. app Judgement Have Bind |
| GET | `/dev/info/app/v1/dev/info/appJudgementHaveBindStation` | Device, devmonitor, remote maintenance, or data-collection operations. app Judgement Have Bind Station |
| GET | `/dev/info/app/v1/dev/info/appSingleStationSearch` | Device, devmonitor, remote maintenance, or data-collection operations. app Single Station Search |
| POST | `/dev/info/app/v1/dev/info/appUnbindStationWithDev?id=` | Device, devmonitor, remote maintenance, or data-collection operations. app Unbind Station With Dev?id= |
| DELETE | `/dev/info/app/v1/dev/info/remove/` | Device, devmonitor, remote maintenance, or data-collection operations. remove |
| POST | `/dev/info/app/v1/devmonitor` | Device/station monitoring and real-time metrics. devmonitor |
| GET* | `/dev/info/app/v1/devmonitor/appPageInverterMoniterList` | Device/station monitoring and real-time metrics. app Page Inverter Monitor List |
| POST | `/dev/info/app/v1/devmonitor/appPageStoredInverterMoniterList` | Device/station monitoring and real-time metrics. app Page Stored Inverter Monitor List |
| POST | `/dev/info/app/v1/devmonitor/pageAppTigoPanelMoniterList` | Device/station monitoring and real-time metrics. page App Tigo Panel Monitor List |
| POST | `/dev/info/app/v1/devmonitor/pageDevSearchList` | Device/station monitoring and real-time metrics. page Dev Search List |
| POST | `/dev/info/app/v1/devmonitor/pageSearchList` | Device/station monitoring and real-time metrics. page Search List |
| GET | `/dev/info/app/v1/station/info/appCurrentUserStationInfo` | Station management, sharing, pricing, and station-level metadata. app Current User Station Info |
| GET | `/dev/info/app/v1/station/info/appGetStationDetail` | Station management, sharing, pricing, and station-level metadata. app Get Station Detail |
| GET | `/dev/info/app/v1/station/info/appGetStationDetail?stationCode=` | Station management, sharing, pricing, and station-level metadata. app Get Station Detail?station Code= |
| GET | `/dev/info/app/v1/station/info/appGetStationDetailV2` | Station management, sharing, pricing, and station-level metadata. app Get Station Detail V2 |
| GET | `/dev/info/app/v1/station/info/appGetStationPrice` | Station management, sharing, pricing, and station-level metadata. app Get Station Price |
| GET | `/dev/info/app/v1/station/info/appListAreaIdByStation` | Station management, sharing, pricing, and station-level metadata. app List Area Id By Station |
| GET | `/dev/info/app/v1/station/info/appListUserOwnedStationType` | Station management, sharing, pricing, and station-level metadata. app List User Owned Station Type |
| POST | `/dev/info/app/v1/station/info/appPageStationBusinessNew` | Station management, sharing, pricing, and station-level metadata. app Page Station Business New |
| POST | `/dev/info/app/v1/station/info/appPageStationBusinessNewCount` | Station management, sharing, pricing, and station-level metadata. app Page Station Business New Count |
| GET | `/dev/info/app/v1/station/info/appStationCount` | Station management, sharing, pricing, and station-level metadata. app Station Count |
| POST | `/dev/info/app/v1/station/info/appStationSearchList` | Station management, sharing, pricing, and station-level metadata. app Station Search List |
| GET | `/dev/info/app/v1/station/info/appStationStatistic` | Station management, sharing, pricing, and station-level metadata. app Station Statistic |
| POST | `/dev/info/app/v1/station/info/appStationStatusCount` | Station management, sharing, pricing, and station-level metadata. app Station Status Count |
| GET | `/dev/info/app/v1/station/info/appStationStatusStatistic` | Station management, sharing, pricing, and station-level metadata. app Station Status Statistic |
| PUT | `/dev/info/app/v1/station/info/appUpdate` | Station management, sharing, pricing, and station-level metadata. app Update |
| PUT | `/dev/info/app/v1/station/info/appUpdateStationBasic` | Station management, sharing, pricing, and station-level metadata. app Update Station Basic |
| GET | `/dev/info/app/v1/station/label` | Station management, sharing, pricing, and station-level metadata. label |
| GET | `/dev/info/app/v1/station/label/appListByStationCode?stationCode=` | Station management, sharing, pricing, and station-level metadata. app List By Station Code?station Code= |
| GET | `/dev/info/app/v1/station/label/getListByCurrentStationList` | Station management, sharing, pricing, and station-level metadata. get List By Current Station List |
| GET | `/dev/info/app/v1/station/price/history/page` | Station management, sharing, pricing, and station-level metadata. page |
| POST | `/dev/info/app/v1/user/dev/attention/appFollowOrUnfollowDev?devId=` | Device, devmonitor, remote maintenance, or data-collection operations. app Follow Or Unfollow Dev?dev Id= |
| GET | `/dev/info/app/workflow/defect` | Device, devmonitor, remote maintenance, or data-collection operations. defect |
| GET | `/dev/info/app/workflow/defect/appSingleStationSearch` | Device, devmonitor, remote maintenance, or data-collection operations. app Single Station Search |
| GET | `/dev/info/app/workflow/defect/appWorkflowDefectStatistic` | Device, devmonitor, remote maintenance, or data-collection operations. app Workflow Defect Statistic |
| GET | `/dev/info/app/workflow/defect/queryDefectDealing` | Device, devmonitor, remote maintenance, or data-collection operations. query Defect Dealing |
| POST | `/dev/info/appBindBySnCodeAndStation` | Device, devmonitor, remote maintenance, or data-collection operations. app Bind By Sn Code And Station |
| POST | `/dev/info/appInsertDev` | Device, devmonitor, remote maintenance, or data-collection operations. app Insert Dev |
| GET | `/dev/info/area/info/getAllAreaList` | Device, devmonitor, remote maintenance, or data-collection operations. get All Area List |
| POST | `/dev/info/area/info/page` | Device, devmonitor, remote maintenance, or data-collection operations. page |
| GET | `/dev/info/change/alarm/relation/setIgnore/` | Alarm lifecycle, notifications, and alarm details. set Ignore |
| GET | `/dev/info/charge/strategy/issue/task/countFailTask` | Device, devmonitor, remote maintenance, or data-collection operations. count Fail Task |
| GET | `/dev/info/charge/strategy/issue/task/pageStrategyIssueTask` | Device, devmonitor, remote maintenance, or data-collection operations. page Strategy Issue Task |
| GET | `/dev/info/charge/strategy/issue/task/pageStrategyIssueTaskDetail` | Device, devmonitor, remote maintenance, or data-collection operations. page Strategy Issue Task Detail |
| GET | `/dev/info/command/model/getAllCommand` | Device, devmonitor, remote maintenance, or data-collection operations. get All Command |
| GET | `/dev/info/command/model/getAllCommandTwo` | Device, devmonitor, remote maintenance, or data-collection operations. get All Command Two |
| POST | `/dev/info/command/setting/log/query` | Device, devmonitor, remote maintenance, or data-collection operations. query |
| PUT | `/dev/info/dev/authorize/task/confirmAuthorizeTask` | Device, devmonitor, remote maintenance, or data-collection operations. confirm Authorize Task |
| GET | `/dev/info/dev/authorize/task/countUnreadAuthorizeTask` | Device, devmonitor, remote maintenance, or data-collection operations. count Unread Authorize Task |
| GET | `/dev/info/dev/authorize/task/latestUnreadAuthorizeTask` | Device, devmonitor, remote maintenance, or data-collection operations. latest Unread Authorize Task |
| GET | `/dev/info/dev/authorize/task/pageAuthorizeTask` | Device, devmonitor, remote maintenance, or data-collection operations. page Authorize Task |
| PUT | `/dev/info/dev/authorize/task/readAllByUser` | Device, devmonitor, remote maintenance, or data-collection operations. read All By User |
| PUT | `/dev/info/dev/authorize/task/readAuthorizeTask` | Device, devmonitor, remote maintenance, or data-collection operations. read Authorize Task |
| DELETE | `/dev/info/dev/authorize/task/removeAuthorizeTask` | Device, devmonitor, remote maintenance, or data-collection operations. remove Authorize Task |
| GET | `/dev/info/dev/charge/operate/strategy/listStrategyDataByDev` | Device, devmonitor, remote maintenance, or data-collection operations. list Strategy Data By Dev |
| POST | `/dev/info/dev/charge/operate/strategy/manualDevIssue` | Device, devmonitor, remote maintenance, or data-collection operations. manual Dev Issue |
| POST | `/dev/info/dev/charge/record/getAppRecordList` | Device, devmonitor, remote maintenance, or data-collection operations. get App Record List |
| POST | `/dev/info/dev/charge/record/getRecordList` | Device, devmonitor, remote maintenance, or data-collection operations. get Record List |
| POST | `/dev/info/dev/flow/flowEndTimeOver` | Device, devmonitor, remote maintenance, or data-collection operations. flow End Time Over |
| GET | `/dev/info/dev/model/soft/info/listByProductMaintenanceId?productMaintenanceId=` | Device, devmonitor, remote maintenance, or data-collection operations. list By Product Maintenance Id?product Maintenance Id= |
| GET | `/dev/info/dev/product/maintenance/getNearEndSafetyData` | Device, devmonitor, remote maintenance, or data-collection operations. get Near End Safety Data |
| GET | `/dev/info/dev/product/maintenance/getProductCommondDetailList` | Device, devmonitor, remote maintenance, or data-collection operations. get Product Commond Detail List |
| GET | `/dev/info/dev/product/maintenance/listAllEmiAndMeter` | Device, devmonitor, remote maintenance, or data-collection operations. list All Emi And Meter |
| GET | `/dev/info/dev/product/maintenance/listByDevType?devType=` | Device, devmonitor, remote maintenance, or data-collection operations. list By Dev Type?dev Type= |
| GET | `/dev/info/dev/product/maintenance/listByDevTypeList` | Device, devmonitor, remote maintenance, or data-collection operations. list By Dev Type List |
| GET | `/dev/info/dev/product/maintenance/pageInverter` | Device, devmonitor, remote maintenance, or data-collection operations. page Inverter |
| POST | `/dev/info/dev/remote/maintain/addAntiCounterEnable` | Device, devmonitor, remote maintenance, or data-collection operations. add Anti Counter Enable |
| POST | `/dev/info/dev/remote/maintain/addIntelligentDevice` | Device, devmonitor, remote maintenance, or data-collection operations. add Intelligent Device |
| GET | `/dev/info/dev/remote/maintain/configDcTimeZone` | Device, devmonitor, remote maintenance, or data-collection operations. config Dc Time Zone |
| POST | `/dev/info/dev/remote/maintain/customizeCommond` | Device, devmonitor, remote maintenance, or data-collection operations. customize Commond |
| POST | `/dev/info/dev/remote/maintain/dcAddressAllocation` | Device, devmonitor, remote maintenance, or data-collection operations. dc Address Allocation |
| GET | `/dev/info/dev/remote/maintain/getAlreadyIntelligentDeviceNum` | Device, devmonitor, remote maintenance, or data-collection operations. get Already Intelligent Device Num |
| GET* | `/dev/info/dev/remote/maintain/getSignalValue` | Device, devmonitor, remote maintenance, or data-collection operations. get Signal Value |
| GET | `/dev/info/dev/remote/maintain/getSignalValue?signalList=` | Device, devmonitor, remote maintenance, or data-collection operations. get Signal Value?signal List= |
| GET | `/dev/info/dev/remote/maintain/getStartSignalValue` | Device, devmonitor, remote maintenance, or data-collection operations. get Start Signal Value |
| GET | `/dev/info/dev/remote/maintain/ipsSelfCheckRecord?devId=` | Device, devmonitor, remote maintenance, or data-collection operations. ips Self Check Record?dev Id= |
| POST | `/dev/info/dev/remote/maintain/ipsSelfCheckStart` | Device, devmonitor, remote maintenance, or data-collection operations. ips Self Check Start |
| POST | `/dev/info/dev/remote/maintain/ipsSelfCheckStop` | Device, devmonitor, remote maintenance, or data-collection operations. ips Self Check Stop |
| POST | `/dev/info/dev/remote/maintain/parallelDevCommondBatch` | Device, devmonitor, remote maintenance, or data-collection operations. parallel Dev Commond Batch |
| GET | `/dev/info/dev/remote/maintain/selectDcTimeZone` | Device, devmonitor, remote maintenance, or data-collection operations. select Dc Time Zone |
| GET | `/dev/info/dev/remote/maintain/setStationWorkMode` | Device, devmonitor, remote maintenance, or data-collection operations. set Station Work Mode |
| POST | `/dev/info/dev/task/info/connectionConfiguration` | Device, devmonitor, remote maintenance, or data-collection operations. connection Configuration |
| GET | `/dev/info/dev/task/info/getConnectionConfiguration` | Device, devmonitor, remote maintenance, or data-collection operations. get Connection Configuration |
| GET | `/dev/info/dev/temp/data/handle/upload/task/tempDataStatusQuery` | Device, devmonitor, remote maintenance, or data-collection operations. temp Data Status Query |
| POST | `/dev/info/dev/temp/data/handle/upload/task/tempDataStatusStart` | Device, devmonitor, remote maintenance, or data-collection operations. temp Data Status Start |
| GET | `/dev/info/dev/user/unit/getUnitByUserId` | Device, devmonitor, remote maintenance, or data-collection operations. get Unit By User Id |
| GET | `/dev/info/dev/user/unit/getUserUnit` | Device, devmonitor, remote maintenance, or data-collection operations. get User Unit |
| PUT | `/dev/info/dev/user/unit/update` | Device, devmonitor, remote maintenance, or data-collection operations. update |
| POST | `/dev/info/devmonitor/centralizedInverterRelTime` | Device/station monitoring and real-time metrics. centralized Inverter Rel Time |
| GET | `/dev/info/devmonitor/confirmUser?userame=` | Device/station monitoring and real-time metrics. confirm User?userame= |
| POST | `/dev/info/devmonitor/currentTempData` | Device/station monitoring and real-time metrics. current Temp Data |
| GET | `/dev/info/devmonitor/getBatteryClusterMonitorDetailInfo/` | Device/station monitoring and real-time metrics. get Battery Cluster Monitor Detail Info |
| POST | `/dev/info/devmonitor/getCentralizedInverterMonitorDetailMonitor` | Device/station monitoring and real-time metrics. get Centralized Inverter Monitor Detail Monitor |
| POST | `/dev/info/devmonitor/nfcDataCal` | Device/station monitoring and real-time metrics. nfc Data Cal |
| POST | `/dev/info/devmonitor/pageBatteryClusterMoniterList` | Device/station monitoring and real-time metrics. page Battery Cluster Monitor List |
| POST | `/dev/info/devmonitor/pageCentralizedInverterMoniterList` | Device/station monitoring and real-time metrics. page Centralized Inverter Monitor List |
| POST | `/dev/info/devmonitor/pageEnergyQualityMoniterList` | Device/station monitoring and real-time metrics. page Energy Quality Monitor List |
| POST | `/dev/info/devmonitor/pageGscSesMoniterList` | Device/station monitoring and real-time metrics. page Gsc Ses Monitor List |
| POST | `/dev/info/devmonitor/pageStoredInverterMoniterList` | Device/station monitoring and real-time metrics. page Stored Inverter Monitor List |
| GET | `/dev/info/dynamic/price/area/listPowerCompany` | Device, devmonitor, remote maintenance, or data-collection operations. list Power Company |
| GET | `/dev/info/dynamic/price/area/pageAreaCode` | Device, devmonitor, remote maintenance, or data-collection operations. page Area Code |
| POST | `/dev/info/dynamic/price/inner/devIssueRetry` | Device, devmonitor, remote maintenance, or data-collection operations. dev Issue Retry |
| GET | `/dev/info/dynamic/price/interface/record/pageDynamicInterfaceRecord` | Device, devmonitor, remote maintenance, or data-collection operations. page Dynamic Interface Record |
| GET | `/dev/info/dynamic/price/pageMarketDynamicPrice` | Device, devmonitor, remote maintenance, or data-collection operations. page Market Dynamic Price |
| GET | `/dev/info/expand/getBatteryNameByDevId` | Device, devmonitor, remote maintenance, or data-collection operations. get Battery Name By Dev Id |
| POST | `/dev/info/expand/updateBatteryName` | Device, devmonitor, remote maintenance, or data-collection operations. update Battery Name |
| GET | `/dev/info/getDatatCollectType` | Device, devmonitor, remote maintenance, or data-collection operations. get Datat Collect Type |
| GET | `/dev/info/getDevCountByCurrentUser` | Device, devmonitor, remote maintenance, or data-collection operations. get Dev Count By Current User |
| GET* | `/dev/info/getScheduleByDevIds` | Device, devmonitor, remote maintenance, or data-collection operations. get Schedule By Dev Ids |
| GET | `/dev/info/getSonDevListByParentSn` | Device, devmonitor, remote maintenance, or data-collection operations. get Son Dev List By Parent Sn |
| GET | `/dev/info/health/check/task` | Device, devmonitor, remote maintenance, or data-collection operations. task |
| GET | `/dev/info/net/check/insertNetCheck` | Device, devmonitor, remote maintenance, or data-collection operations. insert Net Check |
| PUT | `/dev/info/net/check/setNetCheckByStationCode` | Device, devmonitor, remote maintenance, or data-collection operations. set Net Check By Station Code |
| GET | `/dev/info/pv/module/removeStationPvModule` | Device, devmonitor, remote maintenance, or data-collection operations. remove Station Pv Module |
| GET | `/dev/info/search/model/delete/` | Device, devmonitor, remote maintenance, or data-collection operations. delete |
| GET | `/dev/info/search/model/getSearchModelList` | Device, devmonitor, remote maintenance, or data-collection operations. get Search Model List |
| POST | `/dev/info/search/model/saveOrUpdate` | Device, devmonitor, remote maintenance, or data-collection operations. save Or Update |
| GET | `/dev/info/station/dynamic/price/data/listPriceByStation` | Station management, sharing, pricing, and station-level metadata. list Price By Station |
| GET | `/dev/info/station/dynamic/price/info/pageStationDynamicPriceInfo` | Station management, sharing, pricing, and station-level metadata. page Station Dynamic Price Info |
| GET | `/dev/info/station/flow/getByUserId` | Station management, sharing, pricing, and station-level metadata. get By User Id |
| POST | `/dev/info/station/flow/saveOrUpdate` | Station management, sharing, pricing, and station-level metadata. save Or Update |
| GET | `/dev/info/station/info/judgeStationBelongUser` | Station management, sharing, pricing, and station-level metadata. judge Station Belong User |
| GET | `/dev/info/station/info/listMoneyType` | Station management, sharing, pricing, and station-level metadata. list Money Type |
| GET | `/dev/info/station/info/singleOverviewStationData` | Station management, sharing, pricing, and station-level metadata. single Overview Station Data |
| PUT | `/dev/info/station/info/updateStationBasic` | Station management, sharing, pricing, and station-level metadata. update Station Basic |
| POST | `/dev/info/station/presentation/message/getStationPresentMessageList` | Station management, sharing, pricing, and station-level metadata. get Station Present Message List |
| GET | `/dev/info/station/presentation/message/getStationPresentMessageStatus` | Station management, sharing, pricing, and station-level metadata. get Station Present Message Status |
| GET | `/dev/info/station/presentation/message/readAll` | Station management, sharing, pricing, and station-level metadata. read All |
| DELETE | `/dev/info/station/presentation/message/remove/` | Station management, sharing, pricing, and station-level metadata. remove |
| GET | `/dev/info/station/presentation/message/setStationPresentMessageReadStatus` | Station management, sharing, pricing, and station-level metadata. set Station Present Message Read Status |
| GET | `/dev/info/station/share/getCreateUserNameByStationCode` | Station management, sharing, pricing, and station-level metadata. get Create User Name By Station Code |
| GET | `/dev/info/station/share/updateUsed/` | Station management, sharing, pricing, and station-level metadata. update Used |
| GET | `/dev/info/third/station/middle/getByThirdStationId` | Station management, sharing, pricing, and station-level metadata. get By Third Station Id |
| GET | `/dev/info/traffic/query/record/pageTrafficQueryRecord` | Device, devmonitor, remote maintenance, or data-collection operations. page Traffic Query Record |
| GET | `/dev/info/weather/getWeatherDailyHf` | Device, devmonitor, remote maintenance, or data-collection operations. get Weather Daily Hf |
| GET | `/dev/info/weather/getWeatherDailyXz` | Device, devmonitor, remote maintenance, or data-collection operations. get Weather Daily Xz |

### dev/change
| Method | Path | Inferred purpose |
|---|---|---|
| POST | `/dev/change/record` | Device, devmonitor, remote maintenance, or data-collection operations. record |

### dev/product
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/dev/product/maintenance/pageEmiOrMeter` | Device, devmonitor, remote maintenance, or data-collection operations. page Emi Or Meter |
| GET | `/dev/product/maintenance/pageEmiOrMeterNoAuth` | Device, devmonitor, remote maintenance, or data-collection operations. page Emi Or Meter No Auth |

### dev/remote
| Method | Path | Inferred purpose |
|---|---|---|
| GET* | `/dev/remote/maintain/` | Device, devmonitor, remote maintenance, or data-collection operations. maintain |
| POST | `/dev/remote/maintain/addMeterMultiple` | Device, devmonitor, remote maintenance, or data-collection operations. add Meter Multiple |
| POST | `/dev/remote/maintain/allowGridCharge` | Device, devmonitor, remote maintenance, or data-collection operations. allow Grid Charge |
| POST | `/dev/remote/maintain/antiBackFlowValue` | Device, devmonitor, remote maintenance, or data-collection operations. anti Back Flow Value |
| POST | `/dev/remote/maintain/armBuzzer` | Device, devmonitor, remote maintenance, or data-collection operations. arm Buzzer |
| POST | `/dev/remote/maintain/batteryAwaken` | Device, devmonitor, remote maintenance, or data-collection operations. battery Awaken |
| POST | `/dev/remote/maintain/batteryDischargeMinimumSoc` | Device, devmonitor, remote maintenance, or data-collection operations. battery Discharge Minimum Soc |
| POST | `/dev/remote/maintain/batteryMaximumChargeCurrent` | Device, devmonitor, remote maintenance, or data-collection operations. battery Maximum Charge Current |
| POST | `/dev/remote/maintain/batteryMaximumChargeVoltage` | Device, devmonitor, remote maintenance, or data-collection operations. battery Maximum Charge Voltage |
| POST | `/dev/remote/maintain/batteryMaximumDischargeCurrent` | Device, devmonitor, remote maintenance, or data-collection operations. battery Maximum Discharge Current |
| POST | `/dev/remote/maintain/batteryModel` | Device, devmonitor, remote maintenance, or data-collection operations. battery Model |
| POST | `/dev/remote/maintain/batteryStrongChargeCommond` | Device, devmonitor, remote maintenance, or data-collection operations. battery Strong Charge Commond |
| POST | `/dev/remote/maintain/chargeModel` | Device, devmonitor, remote maintenance, or data-collection operations. charge Model |
| POST | `/dev/remote/maintain/clearOverloadFault` | Device, devmonitor, remote maintenance, or data-collection operations. clear Overload Fault |
| POST | `/dev/remote/maintain/coldStart` | Device, devmonitor, remote maintenance, or data-collection operations. cold Start |
| POST | `/dev/remote/maintain/compensateRatio` | Device, devmonitor, remote maintenance, or data-collection operations. compensate Ratio |
| POST | `/dev/remote/maintain/cosP` | Device, devmonitor, remote maintenance, or data-collection operations. cos P |
| POST | `/dev/remote/maintain/cosPSingle` | Device, devmonitor, remote maintenance, or data-collection operations. cos PSingle |
| POST | `/dev/remote/maintain/drmEnable` | Device, devmonitor, remote maintenance, or data-collection operations. drm Enable |
| POST | `/dev/remote/maintain/dryContactSet` | Device, devmonitor, remote maintenance, or data-collection operations. dry Contact Set |
| POST | `/dev/remote/maintain/epsEnable` | Device, devmonitor, remote maintenance, or data-collection operations. eps Enable |
| POST | `/dev/remote/maintain/exampleCurveParameterSet` | Device, devmonitor, remote maintenance, or data-collection operations. example Curve Parameter Set |
| POST | `/dev/remote/maintain/fautlRecoverGridtime` | Device, devmonitor, remote maintenance, or data-collection operations. fautl Recover Gridtime |
| POST | `/dev/remote/maintain/fixActive` | Device, devmonitor, remote maintenance, or data-collection operations. fix Active |
| POST | `/dev/remote/maintain/fixPowerFactor` | Device, devmonitor, remote maintenance, or data-collection operations. fix Power Factor |
| POST | `/dev/remote/maintain/fixReactive` | Device, devmonitor, remote maintenance, or data-collection operations. fix Reactive |
| POST | `/dev/remote/maintain/functionSetting` | Device, devmonitor, remote maintenance, or data-collection operations. function Setting |
| POST | `/dev/remote/maintain/generalCommondIssue` | Device, devmonitor, remote maintenance, or data-collection operations. general Commond Issue |
| POST | `/dev/remote/maintain/generalCommondIssueAndCustomCommondBatch` | Device, devmonitor, remote maintenance, or data-collection operations. general Commond Issue And Custom Commond Batch |
| POST | `/dev/remote/maintain/generalCustomCommond` | Device, devmonitor, remote maintenance, or data-collection operations. general Custom Commond |
| POST | `/dev/remote/maintain/generalDataExport` | Device, devmonitor, remote maintenance, or data-collection operations. general Data Export |
| POST | `/dev/remote/maintain/gfciTestEnable` | Device, devmonitor, remote maintenance, or data-collection operations. gfci Test Enable |
| POST | `/dev/remote/maintain/grid10MinOverVoltage` | Device, devmonitor, remote maintenance, or data-collection operations. grid10Min Over Voltage |
| POST | `/dev/remote/maintain/grid10MinOverVoltageDisableAndEnable` | Device, devmonitor, remote maintenance, or data-collection operations. grid10Min Over Voltage Disable And Enable |
| POST | `/dev/remote/maintain/grid10MinOverVoltageSingle` | Device, devmonitor, remote maintenance, or data-collection operations. grid10Min Over Voltage Single |
| POST | `/dev/remote/maintain/gridConnectModeSn` | Device, devmonitor, remote maintenance, or data-collection operations. grid Connect Mode Sn |
| POST | `/dev/remote/maintain/gridFrequency` | Device, devmonitor, remote maintenance, or data-collection operations. grid Frequency |
| POST | `/dev/remote/maintain/gridFrequencyGf` | Device, devmonitor, remote maintenance, or data-collection operations. grid Frequency Gf |
| POST | `/dev/remote/maintain/gridLevel1OverFrequencyProtectTime` | Device, devmonitor, remote maintenance, or data-collection operations. grid Level1Over Frequency Protect Time |
| POST | `/dev/remote/maintain/gridLevel1OverVoltageProtectTime` | Device, devmonitor, remote maintenance, or data-collection operations. grid Level1Over Voltage Protect Time |
| POST | `/dev/remote/maintain/gridMeterInstallPosition` | Device, devmonitor, remote maintenance, or data-collection operations. grid Meter Install Position |
| POST | `/dev/remote/maintain/gridVoltageImbalance` | Device, devmonitor, remote maintenance, or data-collection operations. grid Voltage Imbalance |
| POST | `/dev/remote/maintain/groundCurrentDetect` | Device, devmonitor, remote maintenance, or data-collection operations. ground Current Detect |
| POST | `/dev/remote/maintain/hdfDataAndWaveSet` | Device, devmonitor, remote maintenance, or data-collection operations. hdf Data And Wave Set |
| POST | `/dev/remote/maintain/insulateResistanceTestEnable` | Device, devmonitor, remote maintenance, or data-collection operations. insulate Resistance Test Enable |
| POST | `/dev/remote/maintain/insulateType` | Device, devmonitor, remote maintenance, or data-collection operations. insulate Type |
| POST | `/dev/remote/maintain/islandTestEnable` | Device, devmonitor, remote maintenance, or data-collection operations. island Test Enable |
| POST | `/dev/remote/maintain/isoProtectPoint` | Device, devmonitor, remote maintenance, or data-collection operations. iso Protect Point |
| GET | `/dev/remote/maintain/judgeCurrentDevExecuteStatus?devId=` | Device, devmonitor, remote maintenance, or data-collection operations. judge Current Dev Execute Status?dev Id= |
| POST | `/dev/remote/maintain/lowVoltageCrossEnable` | Device, devmonitor, remote maintenance, or data-collection operations. low Voltage Cross Enable |
| POST | `/dev/remote/maintain/mainsAbnormalMointorMode` | Device, devmonitor, remote maintenance, or data-collection operations. mains Abnormal Mointor Mode |
| POST | `/dev/remote/maintain/manualControlEnableBit` | Device, devmonitor, remote maintenance, or data-collection operations. manual Control Enable Bit |
| POST | `/dev/remote/maintain/manualControlPower` | Device, devmonitor, remote maintenance, or data-collection operations. manual Control Power |
| POST | `/dev/remote/maintain/meterEnable` | Device, devmonitor, remote maintenance, or data-collection operations. meter Enable |
| POST | `/dev/remote/maintain/meterModel` | Device, devmonitor, remote maintenance, or data-collection operations. meter Model |
| POST | `/dev/remote/maintain/meterScheduleEnable` | Device, devmonitor, remote maintenance, or data-collection operations. meter Schedule Enable |
| POST | `/dev/remote/maintain/meterSelfCheckStart` | Device, devmonitor, remote maintenance, or data-collection operations. meter Self Check Start |
| POST | `/dev/remote/maintain/npeVoltageMonitorEnable` | Device/station monitoring and real-time metrics. npe Voltage Monitor Enable |
| POST | `/dev/remote/maintain/offgridDischargeMinimumSoc` | Device, devmonitor, remote maintenance, or data-collection operations. offgrid Discharge Minimum Soc |
| POST | `/dev/remote/maintain/onGridVoltage` | Device, devmonitor, remote maintenance, or data-collection operations. on Grid Voltage |
| POST | `/dev/remote/maintain/onGridVoltageGf` | Device, devmonitor, remote maintenance, or data-collection operations. on Grid Voltage Gf |
| POST | `/dev/remote/maintain/onGridVoltageOdm` | Device, devmonitor, remote maintenance, or data-collection operations. on Grid Voltage Odm |
| POST | `/dev/remote/maintain/optimizeParameterSet` | Device, devmonitor, remote maintenance, or data-collection operations. optimize Parameter Set |
| POST | `/dev/remote/maintain/optimizeParameterSetDisableAndEnable` | Device, devmonitor, remote maintenance, or data-collection operations. optimize Parameter Set Disable And Enable |
| POST | `/dev/remote/maintain/optionSetting` | Device, devmonitor, remote maintenance, or data-collection operations. option Setting |
| POST | `/dev/remote/maintain/outputActivepowerScheduleCenInv` | Device, devmonitor, remote maintenance, or data-collection operations. output Activepower Schedule Cen Inv |
| POST | `/dev/remote/maintain/outputReactivepowerSchedule` | Device, devmonitor, remote maintenance, or data-collection operations. output Reactivepower Schedule |
| POST | `/dev/remote/maintain/outputReactivepowerScheduleCenInv` | Device, devmonitor, remote maintenance, or data-collection operations. output Reactivepower Schedule Cen Inv |
| POST | `/dev/remote/maintain/overFrequencyRange` | Device, devmonitor, remote maintenance, or data-collection operations. over Frequency Range |
| POST | `/dev/remote/maintain/overFrequencyRangeDisableAndEnable` | Device, devmonitor, remote maintenance, or data-collection operations. over Frequency Range Disable And Enable |
| POST | `/dev/remote/maintain/overVoltageAndFrequencyProtect` | Device, devmonitor, remote maintenance, or data-collection operations. over Voltage And Frequency Protect |
| POST | `/dev/remote/maintain/overVoltageDropPoint` | Device, devmonitor, remote maintenance, or data-collection operations. over Voltage Drop Point |
| POST | `/dev/remote/maintain/overVoltageRange` | Device, devmonitor, remote maintenance, or data-collection operations. over Voltage Range |
| POST | `/dev/remote/maintain/overVoltageRangeDisableAndEnable` | Device, devmonitor, remote maintenance, or data-collection operations. over Voltage Range Disable And Enable |
| POST | `/dev/remote/maintain/overfrequencyReduceloadCoefficient` | Device, devmonitor, remote maintenance, or data-collection operations. overfrequency Reduceload Coefficient |
| POST | `/dev/remote/maintain/overvoltageReduceloadFunction` | Device, devmonitor, remote maintenance, or data-collection operations. overvoltage Reduceload Function |
| POST | `/dev/remote/maintain/pFreq` | Device, devmonitor, remote maintenance, or data-collection operations. p Freq |
| POST | `/dev/remote/maintain/pFreqDisableAndEnable` | Device, devmonitor, remote maintenance, or data-collection operations. p Freq Disable And Enable |
| POST | `/dev/remote/maintain/pVolt` | Device, devmonitor, remote maintenance, or data-collection operations. p Volt |
| POST | `/dev/remote/maintain/pVoltDisableAndEnable` | Device, devmonitor, remote maintenance, or data-collection operations. p Volt Disable And Enable |
| POST | `/dev/remote/maintain/paramProtect` | Device, devmonitor, remote maintenance, or data-collection operations. param Protect |
| POST | `/dev/remote/maintain/paramProtectDisableAndEnable` | Device, devmonitor, remote maintenance, or data-collection operations. param Protect Disable And Enable |
| POST | `/dev/remote/maintain/paramProtectDisableAndEnableSn` | Device, devmonitor, remote maintenance, or data-collection operations. param Protect Disable And Enable Sn |
| POST | `/dev/remote/maintain/paramProtectSingle` | Device, devmonitor, remote maintenance, or data-collection operations. param Protect Single |
| POST | `/dev/remote/maintain/passwordIssuing` | Device, devmonitor, remote maintenance, or data-collection operations. password Issuing |
| POST | `/dev/remote/maintain/pcConfigurateOver1Point1Times` | Device, devmonitor, remote maintenance, or data-collection operations. pc Configurate Over1Point1Times |
| POST | `/dev/remote/maintain/pidSn` | Device, devmonitor, remote maintenance, or data-collection operations. pid Sn |
| POST | `/dev/remote/maintain/powerDispatch` | Device, devmonitor, remote maintenance, or data-collection operations. power Dispatch |
| POST | `/dev/remote/maintain/powerDispatchSeniorParamSetting` | Device, devmonitor, remote maintenance, or data-collection operations. power Dispatch Senior Param Setting |
| POST | `/dev/remote/maintain/powerFactorRegulate` | Device, devmonitor, remote maintenance, or data-collection operations. power Factor Regulate |
| POST | `/dev/remote/maintain/powerFactorRegulateCenInv` | Device, devmonitor, remote maintenance, or data-collection operations. power Factor Regulate Cen Inv |
| POST | `/dev/remote/maintain/qP` | Device, devmonitor, remote maintenance, or data-collection operations. q P |
| POST | `/dev/remote/maintain/qu` | Device, devmonitor, remote maintenance, or data-collection operations. qu |
| POST | `/dev/remote/maintain/quDisableAndEnable` | Device, devmonitor, remote maintenance, or data-collection operations. qu Disable And Enable |
| POST | `/dev/remote/maintain/rateActivepowerPercentage` | Device, devmonitor, remote maintenance, or data-collection operations. rate Activepower Percentage |
| POST | `/dev/remote/maintain/rateReactivePercentage` | Device, devmonitor, remote maintenance, or data-collection operations. rate Reactive Percentage |
| POST | `/dev/remote/maintain/reactiveControlResponseTime` | Device, devmonitor, remote maintenance, or data-collection operations. reactive Control Response Time |
| POST | `/dev/remote/maintain/reactivePowerOutputMode` | Device, devmonitor, remote maintenance, or data-collection operations. reactive Power Output Mode |
| POST | `/dev/remote/maintain/reconnectSoftRate` | Device, devmonitor, remote maintenance, or data-collection operations. reconnect Soft Rate |
| POST | `/dev/remote/maintain/resetArmOffChipMemory` | Device, devmonitor, remote maintenance, or data-collection operations. reset Arm Off Chip Memory |
| POST | `/dev/remote/maintain/resetArmParameter` | Device, devmonitor, remote maintenance, or data-collection operations. reset Arm Parameter |
| POST | `/dev/remote/maintain/resetBms` | Device, devmonitor, remote maintenance, or data-collection operations. reset Bms |
| POST | `/dev/remote/maintain/resonanceDetectSensitiveSet` | Device, devmonitor, remote maintenance, or data-collection operations. resonance Detect Sensitive Set |
| POST | `/dev/remote/maintain/safety` | Device, devmonitor, remote maintenance, or data-collection operations. safety |
| POST | `/dev/remote/maintain/safetyGf` | Device, devmonitor, remote maintenance, or data-collection operations. safety Gf |
| POST | `/dev/remote/maintain/safetyOdm` | Device, devmonitor, remote maintenance, or data-collection operations. safety Odm |
| POST | `/dev/remote/maintain/salesLimitValue` | Device, devmonitor, remote maintenance, or data-collection operations. sales Limit Value |
| POST | `/dev/remote/maintain/shieldSetting` | Device, devmonitor, remote maintenance, or data-collection operations. shield Setting |
| POST | `/dev/remote/maintain/stringDetect` | Device, devmonitor, remote maintenance, or data-collection operations. string Detect |
| POST | `/dev/remote/maintain/switchMachine` | Device, devmonitor, remote maintenance, or data-collection operations. switch Machine |
| POST | `/dev/remote/maintain/switchMachineCenInv` | Device, devmonitor, remote maintenance, or data-collection operations. switch Machine Cen Inv |
| POST | `/dev/remote/maintain/switchMachineGf` | Device, devmonitor, remote maintenance, or data-collection operations. switch Machine Gf |
| POST | `/dev/remote/maintain/switchMachinePowerquality` | Device, devmonitor, remote maintenance, or data-collection operations. switch Machine Powerquality |
| GET | `/dev/remote/maintain/syncMeterInfo?devId=` | Device, devmonitor, remote maintenance, or data-collection operations. sync Meter Info?dev Id= |
| POST | `/dev/remote/maintain/systemSet` | Device, devmonitor, remote maintenance, or data-collection operations. system Set |
| POST | `/dev/remote/maintain/systemSetDisableAndEnable` | Device, devmonitor, remote maintenance, or data-collection operations. system Set Disable And Enable |
| POST | `/dev/remote/maintain/threePhaseUnbalancedPower` | Device, devmonitor, remote maintenance, or data-collection operations. three Phase Unbalanced Power |
| POST | `/dev/remote/maintain/virtualConnect` | Device, devmonitor, remote maintenance, or data-collection operations. virtual Connect |
| POST | `/dev/remote/maintain/weaverFunctionEnable` | Device, devmonitor, remote maintenance, or data-collection operations. weaver Function Enable |

### dev/status
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/dev/status/exchange/pageByDev` | Device, devmonitor, remote maintenance, or data-collection operations. page By Dev |
| GET | `/dev/status/exchange/pageByDevType` | Device, devmonitor, remote maintenance, or data-collection operations. page By Dev Type |

### devRelationReview
| Method | Path | Inferred purpose |
|---|---|---|
| POST | `/devRelationReview` | Device, devmonitor, remote maintenance, or data-collection operations. dev Relation Review |

### devRelationVerify
| Method | Path | Inferred purpose |
|---|---|---|
| POST | `/devRelationVerify` | Device, devmonitor, remote maintenance, or data-collection operations. dev Relation Verify |

### devStatistic
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/devStatistic` | Device, devmonitor, remote maintenance, or data-collection operations. dev Statistic |

### devmonitor/getEnergyBankDevMonitorDetailInfo
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/devmonitor/getEnergyBankDevMonitorDetailInfo/` | Device/station monitoring and real-time metrics. get Energy Bank Dev Monitor Detail Info |

### devmonitor/getEnergyBankDevMonitorDetailMonitor
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/devmonitor/getEnergyBankDevMonitorDetailMonitor/` | Device/station monitoring and real-time metrics. get Energy Bank Dev Monitor Detail Monitor |

### devmonitor/getEnergyBankSemsPowerStrategyChart
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/devmonitor/getEnergyBankSemsPowerStrategyChart/` | Device/station monitoring and real-time metrics. get Energy Bank Sems Power Strategy Chart |

### devmonitor/getEnergyQualityDevMonitorDetailMonitor
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/devmonitor/getEnergyQualityDevMonitorDetailMonitor/` | Device/station monitoring and real-time metrics. get Energy Quality Dev Monitor Detail Monitor |

### devmonitor/getStoredInverterAmmeterMonitor
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/devmonitor/getStoredInverterAmmeterMonitor/` | Device/station monitoring and real-time metrics. get Stored Inverter Ammeter Monitor |

### devmonitor/getStoredInverterBatteryMonitor
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/devmonitor/getStoredInverterBatteryMonitor/` | Device/station monitoring and real-time metrics. get Stored Inverter Battery Monitor |

### devmonitor/getStoredInverterDevMonitorDetailMonitor
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/devmonitor/getStoredInverterDevMonitorDetailMonitor/` | Device/station monitoring and real-time metrics. get Stored Inverter Dev Monitor Detail Monitor |

### devmonitor/judgeChangeDevStatus
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/devmonitor/judgeChangeDevStatus` | Device/station monitoring and real-time metrics. judge Change Dev Status |

### devmonitor/pageEnergyBankMoniterList
| Method | Path | Inferred purpose |
|---|---|---|
| POST | `/devmonitor/pageEnergyBankMoniterList` | Device/station monitoring and real-time metrics. page Energy Bank Monitor List |

### devmonitor/updatejoinCalc
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/devmonitor/updatejoinCalc` | Device/station monitoring and real-time metrics. updatejoin Calc |

### fs/getFileInfo
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/fs/getFileInfo` | get File Info. |

### fs/upload
| Method | Path | Inferred purpose |
|---|---|---|
| GET* | `/fs/upload` | upload. |

### info/appGetByEnterpriseName?enterpriseName=
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/info/appGetByEnterpriseName?enterpriseName=` | app Get By Enterprise Name?enterprise Name=. |

### international/config
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/international/config/getInternationalConfigByType` | System configuration parameters. get International Config By Type |

### kpi/overview
| Method | Path | Inferred purpose |
|---|---|---|
| DELETE | `/kpi/overview/station/kpi/deleteByStation` | Station management, sharing, pricing, and station-level metadata. delete By Station |

### over/limit
| Method | Path | Inferred purpose |
|---|---|---|
| POST | `/over/limit/config/create` | System configuration parameters. create |
| GET | `/over/limit/config/queryNormalizedModelOverLimit` | System configuration parameters. query Normalized Model Over Limit |
| DELETE | `/over/limit/config/remove/` | System configuration parameters. remove |
| PUT | `/over/limit/config/update` | System configuration parameters. update |

### pv/capacity
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/pv/capacity/getPvCapacityByDevId` | PV module/capacity management. get Pv Capacity By Dev Id |

### pv/module
| Method | Path | Inferred purpose |
|---|---|---|
| POST | `/pv/module/saveStationPvModule` | PV module/capacity management. save Station Pv Module |

### signal/model
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/signal/model/getDevIdsByTreeBatch` | Signal model/version management. get Dev Ids By Tree Batch |
| GET | `/signal/model/querySignalModelOverLimit` | Signal model/version management. query Signal Model Over Limit |
| GET | `/signal/model/queryTree` | Signal model/version management. query Tree |
| GET | `/signal/model/signalVersionList` | Signal model/version management. signal Version List |
| POST | `/signal/model/updateList` | Signal model/version management. update List |

### signal/version
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/signal/version/listByProtocolCodeAndDevType?protocolCode=` | Signal model/version management. list By Protocol Code And Dev Type?protocol Code= |
| GET | `/signal/version/pageSignalVersion` | Signal model/version management. page Signal Version |
| GET | `/signal/version/queryNormalizedByDevTypeSingle` | Signal model/version management. query Normalized By Dev Type Single |

### sm
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/sm/app/v1/dep/info` | Service/enterprise/user management. dep info |
| GET | `/sm/app/v1/dep/info/appGetAllEnterDepUser` | Service/enterprise/user management. app Get All Enter Dep User |
| GET | `/sm/app/v1/enterprise` | Service/enterprise/user management. enterprise |
| GET | `/sm/app/v1/enterprise/info/appGetAllAgentEnterprise` | Service/enterprise/user management. app Get All Agent Enterprise |
| GET | `/sm/app/v1/enterprise/info/appGetAllInstallEnterprise` | Service/enterprise/user management. app Get All Install Enterprise |
| POST | `/sm/app/v1/station/info` | Station management, sharing, pricing, and station-level metadata. station info |
| GET | `/sm/app/v1/user` | Service/enterprise/user management. user |

### sm/cim
| Method | Path | Inferred purpose |
|---|---|---|
| POST | `/sm/cim` | Service/enterprise/user management. cim |
| GET* | `/sm/cim/message/getPushPrefix` | Service/enterprise/user management. get Push Prefix |
| POST | `/sm/cim/message/read/sign/readAll` | Service/enterprise/user management. read All |
| POST | `/sm/cim/message/readMessage` | Service/enterprise/user management. read Message |
| GET* | `/sm/cim/room/getRoom` | Service/enterprise/user management. get Room |
| GET* | `/sm/cim/room/getRoomNew` | Service/enterprise/user management. get Room New |

### sm/dep
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/sm/dep/info/getAllSmDepInfo` | Service/enterprise/user management. get All Sm Dep Info |
| GET | `/sm/dep/info/pageByEnterprise` | Service/enterprise/user management. page By Enterprise |
| GET | `/sm/dep/info/pageByEnterpriseNoAuth` | Service/enterprise/user management. page By Enterprise No Auth |

### sm/enterprise
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/sm/enterprise/info/info/` | Service/enterprise/user management. info info |
| GET | `/sm/enterprise/info/pageEnterpriseByAppUser` | Service/enterprise/user management. page Enterprise By App User |
| GET | `/sm/enterprise/info/pageSelect` | Service/enterprise/user management. page Select |

### sm/user
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/sm/user/info/getByContact` | Service/enterprise/user management. get By Contact |
| GET | `/sm/user/info/getCode` | Service/enterprise/user management. get Code |
| GET | `/sm/user/info/judgementLoginNameUnique` | Service/enterprise/user management. judgement Login Name Unique |
| GET | `/sm/user/info/newPasswordSetTime` | Service/enterprise/user management. new Password Set Time |
| GET | `/sm/user/info/searchSharePerson` | Service/enterprise/user management. search Share Person |
| PUT | `/sm/user/location/updateUserLocation` | Service/enterprise/user management. update User Location |

### station
| Method | Path | Inferred purpose |
|---|---|---|
| POST | `/station/info/appQuickAddStation` | Station management, sharing, pricing, and station-level metadata. app Quick Add Station |
| GET | `/station/info/listByEnterpriseIds` | Station management, sharing, pricing, and station-level metadata. list By Enterprise Ids |
| GET | `/station/info/pageStationByCurrentUser` | Station management, sharing, pricing, and station-level metadata. page Station By Current User |
| GET | `/station/info/queryStationNominalPower` | Station management, sharing, pricing, and station-level metadata. query Station Nominal Power |

### station/share
| Method | Path | Inferred purpose |
|---|---|---|
| GET | `/station/share/getShareStationCodeList` | Station management, sharing, pricing, and station-level metadata. get Share Station Code List |
| PUT | `/station/share/insert` | Station management, sharing, pricing, and station-level metadata. insert |
| PUT | `/station/share/insertAssign` | Station management, sharing, pricing, and station-level metadata. insert Assign |
| GET | `/station/share/judgeShare` | Station management, sharing, pricing, and station-level metadata. judge Share |
| POST | `/station/share/page` | Station management, sharing, pricing, and station-level metadata. page |
| DELETE | `/station/share/removeById/` | Station management, sharing, pricing, and station-level metadata. remove By Id |

### strategy
| Method | Path | Inferred purpose |
|---|---|---|
| POST | `/strategy/info/create` | Energy strategy and time-of-use configuration. create |
| DELETE | `/strategy/info/delete/?strategyId=` | Energy strategy and time-of-use configuration. ?strategy Id= |
| GET | `/strategy/info/query` | Energy strategy and time-of-use configuration. query |
| GET | `/strategy/info/queryExecutionStrategy` | Energy strategy and time-of-use configuration. query Execution Strategy |
| GET | `/strategy/info/queryStrategyRuntimeCurve` | Energy strategy and time-of-use configuration. query Strategy Runtime Curve |
| GET | `/strategy/info/start` | Energy strategy and time-of-use configuration. start |
| GET | `/strategy/info/stop` | Energy strategy and time-of-use configuration. stop |
| POST | `/strategy/info/update` | Energy strategy and time-of-use configuration. update |

### ws/dev
| Method | Path | Inferred purpose |
|---|---|---|
| GET* | `/ws/dev/` | Device, devmonitor, remote maintenance, or data-collection operations. dev |

`GET*` means the method could not be statically identified; the app default is GET, but actual calls may be POST/PUT/DELETE depending on the caller.

## Observed response examples
### `/auth/aesKey`
```json
{"code":20000,"data":"RjVNV1l5UVNCRGpiV0RhMw==","success":true}
```
### `/auth/login`
```json
{"code":20000,"data":"<bearer-token>","success":true}
```
### `/dev/info/app/v1/devmonitor/appPageInverterMoniterList` (POST)
Returns `data.records[]`, each with `devId`, `devName`, `devModel`, `devTypeId`, `stationCode`, `activePower`, `totalCap`, `updateTime`, etc.
### `/dev/info/devmonitor/getStoredInverterDevMonitorDetailMonitor/{devId}`
Returns `monitorInformation` (active_power, pv_total_power, temperature, reactive_power, devStatus), `generationPowerInfo` (phase V/A/Hz), `electricInformation` (energy totals), `energyFlowInformation` (`uwBatPower_BMS`), `devProductMaintenance`, `parallelList`.
### `/dev/info/devmonitor/getStoredInverterBatteryMonitor/{devId}`
Returns `batteryInformation` with `uwBatSoc`, `battery_SOH`, `uwBatVolt_BMS`, `uwBatCurr_BMS`, `uwBatPower_BMS`, `uw_bat_cycle_times`, etc.
### `/business/app/v1/single/overview/appSingleStationOverviewData`
Returns cumulative energies: `totalProductPower`, `totalGfProductPower`, `totalCellCharge`, `totalCellDischarge`, `totalBuyGridPower`, `totalOngridPower`, `totalLoadUsePower`, etc.
### `/business/single/overview/stationEnergyFlowDiagram`
Returns real-time flow: `mpptPower`, `buyPower`, `ongridPower`, `loadPower`, `batteryPower`, `batterySocAver`, `acCoupleGfActivePower`, `ammeterEnableSign`, `ammeter2EnableSign`.

## Notes
- The app is a UniApp container; the real application logic is in `assets/apps/__UNI__5F80E0E/www/app-service.js`.
- Many endpoints are never used by the HA integration; only the ones needed for monitoring are wired.
- Endpoint names contain some original typos (for example `Moniter` instead of `Monitor`); paths are preserved exactly as in the app.
- Return shapes can vary slightly by device type (inverter vs. storage inverter vs. gate meter vs. data collector).



## Non-GET payloads

Most write/search endpoints in the app are thin wrappers around a domain object passed in as `data: e`. In other words, the app helper usually has the form:

```js
t.foo = function(e) {
  return request({ url: "/.../foo", method: "post", data: e });
};
```

The exact body is therefore defined by the calling page, not by the generic request wrapper. Common fields observed across the app include:

```json
{ "page": 1, "size": 10, "stationCode": "..." }
{ "devId": 3000134, "signalList": ["activePower", "..."] }
{ "devId": 3000134, "signalMap": { "key": "value" }, "updateRuntimeDataCache": true }
{ "stationCode": "...", "timeDim": "day", "startTime": 1700000000000, "type": 1 }
```

Known request bodies:

### `POST /auth/login`
```json
{ "username": "demoUser", "password": "<base64 AES ciphertext>", "loginType": 2, "app": true }
```

### `POST /auth/loginExperience`
```json
{ "isApp": true }
```

### `POST /dev/info/app/v1/devmonitor/appPageInverterMoniterList`
```json
{ "page": 1, "size": 100 }
```

### `GET /config/system/config/param/getListByModule`
Query: `?params=demoStation`  
Returns the demo host, demo user name, and demo URL visibility flag.

### `POST /dev/info/dev/remote/maintain/getSignalValue`
```json
{ "devId": 3000134, "signalList": ["activePower", "pv_total_power", "..."] }
```

### `POST /dev/info/dev/remote/maintain/generalCommondIssue`
```json
{ "devId": 3000134, "signalMap": { "signalName": "value" }, "updateRuntimeDataCache": true }
```

### `POST /dev/info/dev/remote/maintain/parallelDevCommondBatch`
```json
{ "devIdList": [3000134], "signalMap": { "signalName": "value" }, "parallelBatch": true, "updateRuntimeDataCache": true }
```

For any other non-GET endpoint not listed here, pass the same object the corresponding app page builds and submit it as JSON. The response is always the standard `{code, data, msg, success}` envelope.
