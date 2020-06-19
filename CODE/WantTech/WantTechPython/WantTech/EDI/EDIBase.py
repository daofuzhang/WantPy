import os
import shutil
import datetime
import json
import threading
from Utility import Common
from EDI import EDIEnum
from EDI import EDIFlow
from EDI import EDIEntity

def validateScheduleContinuity(strEDIConnection, strEDIDB, jsonEDIFlows, jsonEDIFlow, intIntervalSeconds, datetimeNow):
    pass

def validateScheduleDaily(strEDIConnection, strEDIDB, jsonEDIFlows, jsonEDIFlow, intIntervalSeconds, datetimeNow):
    datetimeStart = Common.getDateTime(jsonEDIFlow["scheduleStartDate"] + " " + jsonEDIFlow["scheduleStartTime"])
    datetimeToday = Common.getDateTime(Common.getDateString(datetimeNow) + " " + jsonEDIFlow["scheduleStartTime"])
    if datetimeNow >= datetimeStart and \
        datetimeNow >= datetimeToday+datetime.timedelta(seconds=-1) and \
        datetimeNow < datetimeToday+datetime.timedelta(seconds=intIntervalSeconds*1.5):
        strEDIDate = Common.getDateSimple(datetimeNow)
        strEDIID = jsonEDIFlows["ediID"]
        strEDIFlowID = jsonEDIFlow["flowID"]
        strDataDate = Common.getDateSimple(datetimeNow+datetime.timedelta(days=jsonEDIFlow["scheduleDataDelay"]))
        EDIEntity.insertNewFlow(strEDIConnection, strEDIDB, strEDIDate, strEDIID, strEDIFlowID, strDataDate)

def validateScheduleMonthly(strEDIConnection, strEDIDB, jsonEDIFlows, jsonEDIFlow, intIntervalSeconds, datetimeNow):
    strDayToday = Common.getDateSimple(datetimeNow)[-2:]
    if int(strDayToday) in jsonEDIFlow["scheduleRegulareDays"]:
        validateScheduleDaily(strEDIConnection, strEDIDB, jsonEDIFlows, jsonEDIFlow, intIntervalSeconds, datetimeNow)

switch = {
    "Continuity": validateScheduleContinuity,
    "Daily": validateScheduleDaily,
    "Monthly": validateScheduleMonthly,
}

def validateSchedule(strEDIConnection, strEDIDB, jsonEDIFlows, intIntervalSeconds):
    datetimeNow = datetime.datetime.now()
    for jsonEDIFlow in jsonEDIFlows["flowList"]:
        switch[jsonEDIFlow["scheduleFrequency"]](strEDIConnection, strEDIDB, jsonEDIFlows, jsonEDIFlow, intIntervalSeconds, datetimeNow)
    return True

def executeWaitingFlows(strEDIPath, strEDIConnection, strEDIDB, jsonEDIFlows, 
    intFileBlockSize, strMessageSMTPServer, strMessageSMTPFrom, arrayMessageSMTPSuccessTo, arrayMessageSMTPFailureTo):
    listWaitingFlows = EDIEntity.getWaitingFlowList(strEDIConnection, strEDIDB, jsonEDIFlows["ediID"])
    if len(listWaitingFlows) > 0:
        for listWaitingFlow in listWaitingFlows:
            jsonFlow = Common.filterJsonListFirst(jsonEDIFlows["flowList"], "flowID", listWaitingFlow["EDI_FLOW_ID"])
            strRunningFlow = jsonEDIFlows["ediID"] + "." + jsonFlow["flowID"] + ".run"
            if jsonFlow != None and os.path.exists(strRunningFlow) == False:
                fileRunningFlow = open(strRunningFlow, "w")
                fileRunningFlow.close()

                thread = threading.Thread(target=executeFlow, args=(strEDIPath, jsonEDIFlows["ediID"], strEDIConnection, strEDIDB, listWaitingFlow, jsonFlow, 
                    intFileBlockSize, strMessageSMTPServer, strMessageSMTPFrom, arrayMessageSMTPSuccessTo, arrayMessageSMTPFailureTo))
                thread.start()
            else:
                pass
    return True

def executeFlow(*args):
    strEDIPath = args[0]
    strEDIID = args[1]
    strEDIConnection = args[2]
    strEDIDB = args[3]
    dictFlow = args[4]
    jsonFlow = args[5]
    intFileBlockSize = args[6]
    strMessageSMTPServer = args[7]
    strMessageSMTPFrom = args[8]
    arrayMessageSMTPSuccessTo = args[9]
    arrayMessageSMTPFailureTo = args[10]

    flow = EDIFlow.Flow(strEDIPath, strEDIID, strEDIConnection, strEDIDB, dictFlow, jsonFlow, 
        intFileBlockSize, strMessageSMTPServer, strMessageSMTPFrom, arrayMessageSMTPSuccessTo, arrayMessageSMTPFailureTo)
    flow.executeFlow()

def deleteFlowLog(jsonEDIFlows):
    for jsonEDIFlow in jsonEDIFlows["flowList"]:
        if os.path.exists(jsonEDIFlow["flowID"]):
            arrayObjects = os.listdir(jsonEDIFlow["flowID"])
            arrayObjects.remove("CMD")
            arrayObjects.remove("SCRIPT")
            if len(arrayObjects) > 0:
                strMaxObjectName = max(arrayObjects)
                for strObjectName in arrayObjects:
                    strDirPath = jsonEDIFlow["flowID"] + "/" + strObjectName
                    if strObjectName != strMaxObjectName and os.path.isdir(strDirPath):
                        shutil.rmtree(strDirPath)
    return True
