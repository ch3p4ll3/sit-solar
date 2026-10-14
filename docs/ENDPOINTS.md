# Sit Solar (SiNeng EnjoySolar) – backend API endpoints

Extracted from the bundled `Sit Solar.apk` (UniApp frontend). All REST calls are prefixed with `/prod-api`.

Example base URL:

- Production: `https://enjoysolar.si-neng.com/prod-api`

- Demo: `https://demoenjoysolar.si-neng.com:448/prod-api`


Standard response envelope:

```json
{"code":20000,"data":{...},"msg":null,"success":true}
```

Authentication: `Authorization: Bearer <token>`.


## alarm/config

- `/alarm/config/getSignalVersons?devTypeId=`
- `/alarm/config/listAlarmModel`
- `/alarm/config/updateAlarmModel`

## alarm/deadly

- `/alarm/deadly/push/getAlarmUnreadNumByUserId`
- `/alarm/deadly/push/getByUserId`
- `/alarm/deadly/push/getInfoList`
- `/alarm/deadly/push/saveOrUpdate`
- `/alarm/deadly/read/deleteAlarmReadByUserId`
- `/alarm/deadly/read/deleteAlarmReadMessageByUserId`

## alarm/email

- `/alarm/email/rule/create`
- `/alarm/email/rule/info/`
- `/alarm/email/rule/remove/`
- `/alarm/email/rule/update`

## alarm/ignore

- `/alarm/ignore/rule/delete/`
- `/alarm/ignore/rule/detail/`
- `/alarm/ignore/rule/insert`
- `/alarm/ignore/rule/list`
- `/alarm/ignore/rule/modify/`

## alarm/judgementAlarmsExistUnfinishDefect?devAlarms=

- `/alarm/judgementAlarmsExistUnfinishDefect?devAlarms=`

## alarm/model

- `/alarm/model/pageAlarmModel`

## analysis

- `/analysis/alarm/model/pageAnalysisAlarmModel`

## app

- `/app/v1/alarm/appAlarmMessageNum`
- `/app/v1/alarm/appAlarmMessageSet`
- `/app/v1/alarm/appGetAlarmMessageList`
- `/app/v1/alarm/appListByCreateDefect`
- `/app/v1/alarm/appMonitorCompletePercent`
- `/app/v1/alarm/appPageDevAlarmDeadly`
- `/app/v1/alarm/appPageDevAlarmDeadlySet`
- `/app/v1/alarm/appPageDevAlarmExport`
- `/app/v1/alarm/clear/list`
- `/app/v1/alarm/list`
- `/app/v1/alarm/pageAlarmSearchList`
- `/app/v1/alarm/pageAlarmSearchListMore`
- `/app/v1/alarm/pageAlarmSearchNum`
- `/app/v1/alarm/pageAlarmSearchNumMore`
- `/app/v1/dev/info/appStationBindDevs?idList=`
- `/app/v1/dev/info/pageDevPvSet`
- `/app/v1/devmonitor/appDevList`
- `/app/v1/devmonitor/appUpdateDevName`
- `/app/v1/devmonitor/pageParentNullDev`
- `/app/v1/station/info/appSearchStation`
- `/app/workflow/defect/operDefect`
- `/app/workflow/defect/saveAndAssignDefect`
- `/app/workflow/defect/saveDefect`

## auth/checkOff?checkInfo=

- `/auth/checkOff?checkInfo=`

## auth/loginExperience

- `/auth/loginExperience`

## business/app

- `/business/app/dev/dataStatic/getEnvironmentVocDetailInfoData`
- `/business/app/dev/dataStatic/getGateEneryMeterDetailInfoData`
- `/business/app/dev/dataStatic/getNumCollectDetailInfoData`
- `/business/app/dev/dataStatic/getSeriesInverterDetailInfoData`
- `/business/app/v1/inverter/report`
- `/business/app/v1/single/overview`
- `/business/app/v1/single/overview/appSingleStationOverviewData`
- `/business/app/v1/station/business/appStationPage`
- `/business/app/v1/station/business/pageSearchList`
- `/business/app/v1/total/overview`
- `/business/app/v1/total/overview/appListExceptionStation`
- `/business/app/v1/total/overview/appStationOverviewData`
- `/business/app/v1/total/overview/appStationRanking`
- `/business/app/v1/user/project`
- `/business/app/v1/user/project/appListEnterpriseByUserId`
- `/business/app/v1/user/project/appSearchUserForAddWorkOder`

## business/dev

- `/business/dev/dataStatic/curveStatistic`
- `/business/dev/dataStatic/getBatteryClusterDetailInfoData`
- `/business/dev/dataStatic/getBatteryClusterDetailInfoDataPoint`
- `/business/dev/dataStatic/getCentralizedInverterDetailInfoData`
- `/business/dev/dataStatic/getCentralizedInverterDetailInfoDataPoint`
- `/business/dev/dataStatic/getEnergyBankDetailInfoData`
- `/business/dev/dataStatic/getEnergyQualityDetailInfoData`
- `/business/dev/dataStatic/getEnergyQualityDetailInfoDataPoint`
- `/business/dev/dataStatic/getEnvironmentVocDetailInfoDataPoint`
- `/business/dev/dataStatic/getGateEneryMeterDetailInfoDataPoint`
- `/business/dev/dataStatic/getNumCollectDetailInfoDataPoint`
- `/business/dev/dataStatic/getSeriesInverterDetailInfoDataPoint`
- `/business/dev/dataStatic/getStoredInverterDetailInfoData`
- `/business/dev/dataStatic/getStoredInverterDetailInfoDataPoint`
- `/business/dev/project/generalSelectStation`
- `/business/dev/project/pageAlarmEmailRule`
- `/business/dev/project/removeStationByCode?stationCode=`

## business/inverter

- `/business/inverter/report/page?stationCode=`

## business/single

- `/business/single/overview/generatePowerAndPowerStatistic`
- `/business/single/overview/listStationEquivalentHourSingle`
- `/business/single/overview/radiationAndPower`
- `/business/single/overview/singleStationKpiData`
- `/business/single/overview/socSohAndPower`
- `/business/single/overview/stationEnergyFlowDiagram`
- `/business/single/overview/stationEnergyFlowDiagramReTime`

## business/station

- `/business/station/business/page`
- `/business/station/business/stationPageExport`
- `/business/station/business/stationStatusCount`
- `/business/station/report/pageMonthReportByCurrentUser`
- `/business/station/report/singleMonthReportByStationCode`

## business/total

- `/business/total/overview/generatePowerAndPowerStatistic`
- `/business/total/overview/getPowerCurve`
- `/business/total/overview/stationEquivalentHour`
- `/business/total/overview/stationOverviewData`

## business/workflow

- `/business/workflow/defect/assignDefect?workflowDefectId=`
- `/business/workflow/defect/remark?workflowDefectId=`
- `/business/workflow/defect/remove/`

## change

- `/change/alarm/relation/getAlarmRelationList`
- `/change/alarm/relation/stationAdjust/`

## command

- `/command/model/details/queryCommandModelDetailsByDevId`

## config/nav

- `/config/nav/assistance/conf/listByPageIdAndType`

## config/system

- `/config/system/config/param/getListByModule`

## dev

- `/dev/info`
- `/dev/info/alarm/alarmMonitorStatistic`
- `/dev/info/alarm/deadly/read/updateDealyStatusId`
- `/dev/info/alarm/getUnreadAlarmCountSingle`
- `/dev/info/alarm/pageDevAlarmDeadly`
- `/dev/info/app/alarm/deadly/read/alarmReadMessageByUserId`
- `/dev/info/app/v1`
- `/dev/info/app/v1/alarm/appAlarmMessageNum`
- `/dev/info/app/v1/alarm/appAlarmStatistic`
- `/dev/info/app/v1/alarm/appAlarmStatisticSingle`
- `/dev/info/app/v1/alarm/appConfirmAlarm?id=`
- `/dev/info/app/v1/alarm/appDevAlarmDeadly`
- `/dev/info/app/v1/alarm/appGetAlarmDetail?id=`
- `/dev/info/app/v1/alarm/appGetUnreadAlarmCount`
- `/dev/info/app/v1/alarm/appGetUnreadAlarmList?alarmType=`
- `/dev/info/app/v1/alarm/appManualClearAlarm?id=`
- `/dev/info/app/v1/alarm/appMonitorCompletePercent`
- `/dev/info/app/v1/alarm/appReadAlarm`
- `/dev/info/app/v1/alarm/appSingleStationSearch`
- `/dev/info/app/v1/alarm/appUpdateRemarks`
- `/dev/info/app/v1/alarm/listAll`
- `/dev/info/app/v1/dev/info`
- `/dev/info/app/v1/dev/info/appDevCountStatistic`
- `/dev/info/app/v1/dev/info/appGetDevCountByCurrentUser`
- `/dev/info/app/v1/dev/info/appJudgementHaveBind`
- `/dev/info/app/v1/dev/info/appJudgementHaveBindStation`
- `/dev/info/app/v1/dev/info/appSingleStationSearch`
- `/dev/info/app/v1/dev/info/appUnbindStationWithDev?id=`
- `/dev/info/app/v1/dev/info/remove/`
- `/dev/info/app/v1/devmonitor`
- `/dev/info/app/v1/devmonitor/appPageInverterMoniterList`
- `/dev/info/app/v1/devmonitor/appPageStoredInverterMoniterList`
- `/dev/info/app/v1/devmonitor/pageAppTigoPanelMoniterList`
- `/dev/info/app/v1/devmonitor/pageDevSearchList`
- `/dev/info/app/v1/devmonitor/pageSearchList`
- `/dev/info/app/v1/station/info/appCurrentUserStationInfo`
- `/dev/info/app/v1/station/info/appGetStationDetail`
- `/dev/info/app/v1/station/info/appGetStationDetail?stationCode=`
- `/dev/info/app/v1/station/info/appGetStationDetailV2`
- `/dev/info/app/v1/station/info/appGetStationPrice`
- `/dev/info/app/v1/station/info/appListAreaIdByStation`
- `/dev/info/app/v1/station/info/appListUserOwnedStationType`
- `/dev/info/app/v1/station/info/appPageStationBusinessNew`
- `/dev/info/app/v1/station/info/appPageStationBusinessNewCount`
- `/dev/info/app/v1/station/info/appStationCount`
- `/dev/info/app/v1/station/info/appStationSearchList`
- `/dev/info/app/v1/station/info/appStationStatistic`
- `/dev/info/app/v1/station/info/appStationStatusCount`
- `/dev/info/app/v1/station/info/appStationStatusStatistic`
- `/dev/info/app/v1/station/info/appUpdate`
- `/dev/info/app/v1/station/info/appUpdateStationBasic`
- `/dev/info/app/v1/station/label`
- `/dev/info/app/v1/station/label/appListByStationCode?stationCode=`
- `/dev/info/app/v1/station/label/getListByCurrentStationList`
- `/dev/info/app/v1/station/price/history/page`
- `/dev/info/app/v1/user/dev/attention/appFollowOrUnfollowDev?devId=`
- `/dev/info/app/workflow/defect`
- `/dev/info/app/workflow/defect/appSingleStationSearch`
- `/dev/info/app/workflow/defect/appWorkflowDefectStatistic`
- `/dev/info/app/workflow/defect/queryDefectDealing`
- `/dev/info/appBindBySnCodeAndStation`
- `/dev/info/appInsertDev`
- `/dev/info/area/info/getAllAreaList`
- `/dev/info/area/info/page`
- `/dev/info/change/alarm/relation/setIgnore/`
- `/dev/info/charge/strategy/issue/task/countFailTask`
- `/dev/info/charge/strategy/issue/task/pageStrategyIssueTask`
- `/dev/info/charge/strategy/issue/task/pageStrategyIssueTaskDetail`
- `/dev/info/command/model/getAllCommand`
- `/dev/info/command/model/getAllCommandTwo`
- `/dev/info/command/setting/log/query`
- `/dev/info/dev/authorize/task/confirmAuthorizeTask`
- `/dev/info/dev/authorize/task/countUnreadAuthorizeTask`
- `/dev/info/dev/authorize/task/latestUnreadAuthorizeTask`
- `/dev/info/dev/authorize/task/pageAuthorizeTask`
- `/dev/info/dev/authorize/task/readAllByUser`
- `/dev/info/dev/authorize/task/readAuthorizeTask`
- `/dev/info/dev/authorize/task/removeAuthorizeTask`
- `/dev/info/dev/charge/operate/strategy/listStrategyDataByDev`
- `/dev/info/dev/charge/operate/strategy/manualDevIssue`
- `/dev/info/dev/charge/record/getAppRecordList`
- `/dev/info/dev/charge/record/getRecordList`
- `/dev/info/dev/flow/flowEndTimeOver`
- `/dev/info/dev/model/soft/info/listByProductMaintenanceId?productMaintenanceId=`
- `/dev/info/dev/product/maintenance/getNearEndSafetyData`
- `/dev/info/dev/product/maintenance/getProductCommondDetailList`
- `/dev/info/dev/product/maintenance/listAllEmiAndMeter`
- `/dev/info/dev/product/maintenance/listByDevType?devType=`
- `/dev/info/dev/product/maintenance/listByDevTypeList`
- `/dev/info/dev/product/maintenance/pageInverter`
- `/dev/info/dev/remote/maintain/addAntiCounterEnable`
- `/dev/info/dev/remote/maintain/addIntelligentDevice`
- `/dev/info/dev/remote/maintain/configDcTimeZone`
- `/dev/info/dev/remote/maintain/customizeCommond`
- `/dev/info/dev/remote/maintain/dcAddressAllocation`
- `/dev/info/dev/remote/maintain/getAlreadyIntelligentDeviceNum`
- `/dev/info/dev/remote/maintain/getSignalValue`
- `/dev/info/dev/remote/maintain/getSignalValue?signalList=`
- `/dev/info/dev/remote/maintain/getStartSignalValue`
- `/dev/info/dev/remote/maintain/ipsSelfCheckRecord?devId=`
- `/dev/info/dev/remote/maintain/ipsSelfCheckStart`
- `/dev/info/dev/remote/maintain/ipsSelfCheckStop`
- `/dev/info/dev/remote/maintain/parallelDevCommondBatch`
- `/dev/info/dev/remote/maintain/selectDcTimeZone`
- `/dev/info/dev/remote/maintain/setStationWorkMode`
- `/dev/info/dev/task/info/connectionConfiguration`
- `/dev/info/dev/task/info/getConnectionConfiguration`
- `/dev/info/dev/temp/data/handle/upload/task/tempDataStatusQuery`
- `/dev/info/dev/temp/data/handle/upload/task/tempDataStatusStart`
- `/dev/info/dev/user/unit/getUnitByUserId`
- `/dev/info/dev/user/unit/getUserUnit`
- `/dev/info/dev/user/unit/update`
- `/dev/info/devmonitor/centralizedInverterRelTime`
- `/dev/info/devmonitor/confirmUser?userame=`
- `/dev/info/devmonitor/currentTempData`
- `/dev/info/devmonitor/getBatteryClusterMonitorDetailInfo/`
- `/dev/info/devmonitor/getCentralizedInverterMonitorDetailMonitor`
- `/dev/info/devmonitor/nfcDataCal`
- `/dev/info/devmonitor/pageBatteryClusterMoniterList`
- `/dev/info/devmonitor/pageCentralizedInverterMoniterList`
- `/dev/info/devmonitor/pageEnergyQualityMoniterList`
- `/dev/info/devmonitor/pageGscSesMoniterList`
- `/dev/info/devmonitor/pageStoredInverterMoniterList`
- `/dev/info/dynamic/price/area/listPowerCompany`
- `/dev/info/dynamic/price/area/pageAreaCode`
- `/dev/info/dynamic/price/inner/devIssueRetry`
- `/dev/info/dynamic/price/interface/record/pageDynamicInterfaceRecord`
- `/dev/info/dynamic/price/pageMarketDynamicPrice`
- `/dev/info/expand/getBatteryNameByDevId`
- `/dev/info/expand/updateBatteryName`
- `/dev/info/getDatatCollectType`
- `/dev/info/getDevCountByCurrentUser`
- `/dev/info/getScheduleByDevIds`
- `/dev/info/getSonDevListByParentSn`
- `/dev/info/health/check/task`
- `/dev/info/net/check/insertNetCheck`
- `/dev/info/net/check/setNetCheckByStationCode`
- `/dev/info/pv/module/removeStationPvModule`
- `/dev/info/search/model/delete/`
- `/dev/info/search/model/getSearchModelList`
- `/dev/info/search/model/saveOrUpdate`
- `/dev/info/station/dynamic/price/data/listPriceByStation`
- `/dev/info/station/dynamic/price/info/pageStationDynamicPriceInfo`
- `/dev/info/station/flow/getByUserId`
- `/dev/info/station/flow/saveOrUpdate`
- `/dev/info/station/info/judgeStationBelongUser`
- `/dev/info/station/info/listMoneyType`
- `/dev/info/station/info/singleOverviewStationData`
- `/dev/info/station/info/updateStationBasic`
- `/dev/info/station/presentation/message/getStationPresentMessageList`
- `/dev/info/station/presentation/message/getStationPresentMessageStatus`
- `/dev/info/station/presentation/message/readAll`
- `/dev/info/station/presentation/message/remove/`
- `/dev/info/station/presentation/message/setStationPresentMessageReadStatus`
- `/dev/info/station/share/getCreateUserNameByStationCode`
- `/dev/info/station/share/updateUsed/`
- `/dev/info/third/station/middle/getByThirdStationId`
- `/dev/info/traffic/query/record/pageTrafficQueryRecord`
- `/dev/info/weather/getWeatherDailyHf`
- `/dev/info/weather/getWeatherDailyXz`

## dev/change

- `/dev/change/record`

## dev/product

- `/dev/product/maintenance/pageEmiOrMeter`
- `/dev/product/maintenance/pageEmiOrMeterNoAuth`

## dev/remote

- `/dev/remote/maintain/`
- `/dev/remote/maintain/addMeterMultiple`
- `/dev/remote/maintain/allowGridCharge`
- `/dev/remote/maintain/antiBackFlowValue`
- `/dev/remote/maintain/armBuzzer`
- `/dev/remote/maintain/batteryAwaken`
- `/dev/remote/maintain/batteryDischargeMinimumSoc`
- `/dev/remote/maintain/batteryMaximumChargeCurrent`
- `/dev/remote/maintain/batteryMaximumChargeVoltage`
- `/dev/remote/maintain/batteryMaximumDischargeCurrent`
- `/dev/remote/maintain/batteryModel`
- `/dev/remote/maintain/batteryStrongChargeCommond`
- `/dev/remote/maintain/chargeModel`
- `/dev/remote/maintain/clearOverloadFault`
- `/dev/remote/maintain/coldStart`
- `/dev/remote/maintain/compensateRatio`
- `/dev/remote/maintain/cosP`
- `/dev/remote/maintain/cosPSingle`
- `/dev/remote/maintain/drmEnable`
- `/dev/remote/maintain/dryContactSet`
- `/dev/remote/maintain/epsEnable`
- `/dev/remote/maintain/exampleCurveParameterSet`
- `/dev/remote/maintain/fautlRecoverGridtime`
- `/dev/remote/maintain/fixActive`
- `/dev/remote/maintain/fixPowerFactor`
- `/dev/remote/maintain/fixReactive`
- `/dev/remote/maintain/functionSetting`
- `/dev/remote/maintain/generalCommondIssue`
- `/dev/remote/maintain/generalCommondIssueAndCustomCommondBatch`
- `/dev/remote/maintain/generalCustomCommond`
- `/dev/remote/maintain/generalDataExport`
- `/dev/remote/maintain/gfciTestEnable`
- `/dev/remote/maintain/grid10MinOverVoltage`
- `/dev/remote/maintain/grid10MinOverVoltageDisableAndEnable`
- `/dev/remote/maintain/grid10MinOverVoltageSingle`
- `/dev/remote/maintain/gridConnectModeSn`
- `/dev/remote/maintain/gridFrequency`
- `/dev/remote/maintain/gridFrequencyGf`
- `/dev/remote/maintain/gridLevel1OverFrequencyProtectTime`
- `/dev/remote/maintain/gridLevel1OverVoltageProtectTime`
- `/dev/remote/maintain/gridMeterInstallPosition`
- `/dev/remote/maintain/gridVoltageImbalance`
- `/dev/remote/maintain/groundCurrentDetect`
- `/dev/remote/maintain/hdfDataAndWaveSet`
- `/dev/remote/maintain/insulateResistanceTestEnable`
- `/dev/remote/maintain/insulateType`
- `/dev/remote/maintain/islandTestEnable`
- `/dev/remote/maintain/isoProtectPoint`
- `/dev/remote/maintain/judgeCurrentDevExecuteStatus?devId=`
- `/dev/remote/maintain/lowVoltageCrossEnable`
- `/dev/remote/maintain/mainsAbnormalMointorMode`
- `/dev/remote/maintain/manualControlEnableBit`
- `/dev/remote/maintain/manualControlPower`
- `/dev/remote/maintain/meterEnable`
- `/dev/remote/maintain/meterModel`
- `/dev/remote/maintain/meterScheduleEnable`
- `/dev/remote/maintain/meterSelfCheckStart`
- `/dev/remote/maintain/npeVoltageMonitorEnable`
- `/dev/remote/maintain/offgridDischargeMinimumSoc`
- `/dev/remote/maintain/onGridVoltage`
- `/dev/remote/maintain/onGridVoltageGf`
- `/dev/remote/maintain/onGridVoltageOdm`
- `/dev/remote/maintain/optimizeParameterSet`
- `/dev/remote/maintain/optimizeParameterSetDisableAndEnable`
- `/dev/remote/maintain/optionSetting`
- `/dev/remote/maintain/outputActivepowerScheduleCenInv`
- `/dev/remote/maintain/outputReactivepowerSchedule`
- `/dev/remote/maintain/outputReactivepowerScheduleCenInv`
- `/dev/remote/maintain/overFrequencyRange`
- `/dev/remote/maintain/overFrequencyRangeDisableAndEnable`
- `/dev/remote/maintain/overVoltageAndFrequencyProtect`
- `/dev/remote/maintain/overVoltageDropPoint`
- `/dev/remote/maintain/overVoltageRange`
- `/dev/remote/maintain/overVoltageRangeDisableAndEnable`
- `/dev/remote/maintain/overfrequencyReduceloadCoefficient`
- `/dev/remote/maintain/overvoltageReduceloadFunction`
- `/dev/remote/maintain/pFreq`
- `/dev/remote/maintain/pFreqDisableAndEnable`
- `/dev/remote/maintain/pVolt`
- `/dev/remote/maintain/pVoltDisableAndEnable`
- `/dev/remote/maintain/paramProtect`
- `/dev/remote/maintain/paramProtectDisableAndEnable`
- `/dev/remote/maintain/paramProtectDisableAndEnableSn`
- `/dev/remote/maintain/paramProtectSingle`
- `/dev/remote/maintain/passwordIssuing`
- `/dev/remote/maintain/pcConfigurateOver1Point1Times`
- `/dev/remote/maintain/pidSn`
- `/dev/remote/maintain/powerDispatch`
- `/dev/remote/maintain/powerDispatchSeniorParamSetting`
- `/dev/remote/maintain/powerFactorRegulate`
- `/dev/remote/maintain/powerFactorRegulateCenInv`
- `/dev/remote/maintain/qP`
- `/dev/remote/maintain/qu`
- `/dev/remote/maintain/quDisableAndEnable`
- `/dev/remote/maintain/rateActivepowerPercentage`
- `/dev/remote/maintain/rateReactivePercentage`
- `/dev/remote/maintain/reactiveControlResponseTime`
- `/dev/remote/maintain/reactivePowerOutputMode`
- `/dev/remote/maintain/reconnectSoftRate`
- `/dev/remote/maintain/resetArmOffChipMemory`
- `/dev/remote/maintain/resetArmParameter`
- `/dev/remote/maintain/resetBms`
- `/dev/remote/maintain/resonanceDetectSensitiveSet`
- `/dev/remote/maintain/safety`
- `/dev/remote/maintain/safetyGf`
- `/dev/remote/maintain/safetyOdm`
- `/dev/remote/maintain/salesLimitValue`
- `/dev/remote/maintain/shieldSetting`
- `/dev/remote/maintain/stringDetect`
- `/dev/remote/maintain/switchMachine`
- `/dev/remote/maintain/switchMachineCenInv`
- `/dev/remote/maintain/switchMachineGf`
- `/dev/remote/maintain/switchMachinePowerquality`
- `/dev/remote/maintain/syncMeterInfo?devId=`
- `/dev/remote/maintain/systemSet`
- `/dev/remote/maintain/systemSetDisableAndEnable`
- `/dev/remote/maintain/threePhaseUnbalancedPower`
- `/dev/remote/maintain/virtualConnect`
- `/dev/remote/maintain/weaverFunctionEnable`

## dev/status

- `/dev/status/exchange/pageByDev`
- `/dev/status/exchange/pageByDevType`

## devmonitor

- `/devmonitor/getEnergyBankDevMonitorDetailInfo/`
- `/devmonitor/getEnergyBankDevMonitorDetailMonitor/`
- `/devmonitor/getEnergyBankSemsPowerStrategyChart/`
- `/devmonitor/getEnergyQualityDevMonitorDetailMonitor/`
- `/devmonitor/getStoredInverterAmmeterMonitor/`
- `/devmonitor/getStoredInverterBatteryMonitor/`
- `/devmonitor/getStoredInverterDevMonitorDetailMonitor/`
- `/devmonitor/judgeChangeDevStatus`
- `/devmonitor/pageEnergyBankMoniterList`
- `/devmonitor/updatejoinCalc`

## fs/getFileInfo

- `/fs/getFileInfo`

## fs/upload

- `/fs/upload`

## info

- `/info/appGetByEnterpriseName?enterpriseName=`

## international

- `/international/config/getInternationalConfigByType`

## kpi/overview

- `/kpi/overview/station/kpi/deleteByStation`

## over

- `/over/limit/config/create`
- `/over/limit/config/queryNormalizedModelOverLimit`
- `/over/limit/config/remove/`
- `/over/limit/config/update`

## pv/capacity

- `/pv/capacity/getPvCapacityByDevId`

## pv/module

- `/pv/module/saveStationPvModule`

## root

- `/appAddLabel?labelName=`
- `/appAddStation`
- `/appCancelAccount`
- `/appDefectSearch`
- `/appDeleteLabel?id=`
- `/appDevMonitorStatistic`
- `/appEnergyFlowGraph?stationCode=`
- `/appEnergyFlowGraphNew?stationCode=`
- `/appEnvironmentalContribution`
- `/appEnvironmentalContribution?stationCode=`
- `/appGeneratePowerAndPower`
- `/appGeneratePowerProfile`
- `/appGetAllSmDepInfo?name=`
- `/appGetAllSmDepInfoNoLimit`
- `/appGetCurrentUserInfo`
- `/appGetWeatherDaily?stationCode=`
- `/appIncomeProfile?stationCode=`
- `/appInverterAlarm`
- `/appInverterKpi`
- `/appInverterKpiDataGraph`
- `/appMonitorRelTime`
- `/appMyAttentionDev`
- `/appMyAttentionStation`
- `/appOperateAttention?stationCode=`
- `/appPageBySnCode`
- `/appPageInverterMoniterAllList`
- `/appPageInverterMoniterList`
- `/appPageNumberCollectMoniterList`
- `/appPageStationByCurrentUser`
- `/appPowerCurve`
- `/appRemoteMaintain`
- `/appStationBusinessList`
- `/appStationBusinessPage`
- `/appTodayPowerCurve`
- `/appUdateCurrentUserPassword`
- `/appUnsubscribeDev?devId=`
- `/appUnsubscribeStation?stationCode=`
- `/appUpdateCurrentUserInfo`
- `/auth`
- `/devRelationReview`
- `/devRelationVerify`
- `/devStatistic`

## signal/model

- `/signal/model/getDevIdsByTreeBatch`
- `/signal/model/querySignalModelOverLimit`
- `/signal/model/queryTree`
- `/signal/model/signalVersionList`
- `/signal/model/updateList`

## signal/version

- `/signal/version/listByProtocolCodeAndDevType?protocolCode=`
- `/signal/version/pageSignalVersion`
- `/signal/version/queryNormalizedByDevTypeSingle`

## sm/app

- `/sm/app/v1/dep/info`
- `/sm/app/v1/dep/info/appGetAllEnterDepUser`
- `/sm/app/v1/enterprise`
- `/sm/app/v1/enterprise/info/appGetAllAgentEnterprise`
- `/sm/app/v1/enterprise/info/appGetAllInstallEnterprise`
- `/sm/app/v1/station/info`
- `/sm/app/v1/user`

## sm/cim

- `/sm/cim`
- `/sm/cim/message/getPushPrefix`
- `/sm/cim/message/read/sign/readAll`
- `/sm/cim/message/readMessage`
- `/sm/cim/room/getRoom`
- `/sm/cim/room/getRoomNew`

## sm/dep

- `/sm/dep/info/getAllSmDepInfo`
- `/sm/dep/info/pageByEnterprise`
- `/sm/dep/info/pageByEnterpriseNoAuth`

## sm/enterprise

- `/sm/enterprise/info/info/`
- `/sm/enterprise/info/pageEnterpriseByAppUser`
- `/sm/enterprise/info/pageSelect`

## sm/user

- `/sm/user/info/getByContact`
- `/sm/user/info/getCode`
- `/sm/user/info/judgementLoginNameUnique`
- `/sm/user/info/newPasswordSetTime`
- `/sm/user/info/searchSharePerson`
- `/sm/user/location/updateUserLocation`

## station

- `/station/info/appQuickAddStation`
- `/station/info/listByEnterpriseIds`
- `/station/info/pageStationByCurrentUser`
- `/station/info/queryStationNominalPower`

## station/share

- `/station/share/getShareStationCodeList`
- `/station/share/insert`
- `/station/share/insertAssign`
- `/station/share/judgeShare`
- `/station/share/page`
- `/station/share/removeById/`

## strategy

- `/strategy/info/create`
- `/strategy/info/delete/?strategyId=`
- `/strategy/info/query`
- `/strategy/info/queryExecutionStrategy`
- `/strategy/info/queryStrategyRuntimeCurve`
- `/strategy/info/start`
- `/strategy/info/stop`
- `/strategy/info/update`

## ws

- `/ws/dev/`

