import logging
import datetime
import time
import traceback
import os
from Utility import Common
from Utility import File
from Utility import Message
from EDI import EDIBase

def main():
    strEDIName = File.getCurrentFileName(__file__)
    strEDIPath = os.getcwd()

    jsonEDIService = Common.loadJsonFile(strEDIName + ".json")
    strEDIID = jsonEDIService["id"]

    strEDIConnection = Common.filterJsonListFirst(jsonEDIService["connectionList"], "connectionID", "maria-dw-DWuser-DWWANT")["connection"]
    strEDIDB = Common.filterJsonListFirst(jsonEDIService["connectionList"], "connectionID", "maria-dw-DWuser-DWWANT")["db"]

    intIntervalSeconds = jsonEDIService["intervalSeconds"]
    intFileBlockSize = jsonEDIService["fileBlockSize"]

    strMessageSMTPServer = jsonEDIService["messageSMTPServer"]
    strMessageSMTPFrom = jsonEDIService["messageSMTPFrom"]
    arrayMessageSMTPSuccessTo = jsonEDIService["messageSMTPSuccessToList"]
    arrayMessageSMTPFailureTo = jsonEDIService["messageSMTPFailureToList"]

    strLogDate = Common.setLogging(strEDIID)
    logger = logging.getLogger(strEDIID)

    logger.info("Load EDIFlows.json file.")
    jsonEDIFlows = Common.loadJsonFile(strEDIName + "Flows.json")

    try:

        logger.warning("Start EDI Service.")
        while True:
            strNowDate = Common.getDateSimple(datetime.datetime.now())
            if strNowDate != strLogDate:
                strLogDate = Common.setLogging(strEDIID)
                logger = logging.getLogger(strEDIID)

            EDIBase.validateSchedule(strEDIConnection, strEDIDB, jsonEDIFlows, intIntervalSeconds)
            EDIBase.executeWaitingFlows(strEDIPath, strEDIConnection, strEDIDB, jsonEDIFlows, 
                intFileBlockSize, strMessageSMTPServer, strMessageSMTPFrom, arrayMessageSMTPSuccessTo, arrayMessageSMTPFailureTo)
            EDIBase.deleteFlowLog(jsonEDIFlows)

            time.sleep(intIntervalSeconds)

    except Exception:
        strExceptionMessage = traceback.format_exc()
        logger.error(strExceptionMessage)

        strMessageSMTPSubject = "!!!!! {ediID} Exception !!!!!".format(ediID=strEDIID)
        Message.sendSMTPMail(strMessageSMTPServer, strMessageSMTPFrom, arrayMessageSMTPFailureTo, strMessageSMTPSubject, strExceptionMessage, None, None)
        
        logger.error("Stop EDI Service by Exception.")
    finally:
        logger.warning("Stop EDI Service.")

if __name__ == "__main__":
    main()
