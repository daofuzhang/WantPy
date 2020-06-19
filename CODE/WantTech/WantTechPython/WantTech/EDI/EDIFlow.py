import os
import json
import datetime
import logging
import traceback
from Utility import Common
from Utility import Message
from EDI import EDIEnum
from EDI import EDIEntity
from EDI import EDIJob

class Flow:
    logger = None

    strEDIPath = None

    strEDIID = None
    strEDIConnection = None
    strEDIDB = None

    dictFlow = None
    jsonFlow = None

    intFileBlockSize = None

    strMessageSMTPServer = None
    strMessageSMTPFrom = None
    arrayMessageSMTPSuccessTo = None
    arrayMessageSMTPFailureTo = None

    strEDIDate = None
    strEDITime = None

    strPathBAK = None

    def __init__(self, strEDIPath, strEDIID, strEDIConnection, strEDIDB, dictFlow, jsonFlow, 
        intFileBlockSize, strMessageSMTPServer, strMessageSMTPFrom, arrayMessageSMTPSuccessTo, arrayMessageSMTPFailureTo):
        Common.setLogging(strEDIID + "." + jsonFlow["flowID"])
        self.logger = logging.getLogger(strEDIID + "." + jsonFlow["flowID"])

        self.strEDIPath = strEDIPath

        self.strEDIID = strEDIID
        self.strEDIConnection = strEDIConnection
        self.strEDIDB = strEDIDB

        self.dictFlow = dictFlow
        self.jsonFlow = jsonFlow

        self.intFileBlockSize = intFileBlockSize

        self.strMessageSMTPServer = strMessageSMTPServer
        self.strMessageSMTPFrom = strMessageSMTPFrom
        self.arrayMessageSMTPSuccessTo = arrayMessageSMTPSuccessTo
        self.arrayMessageSMTPFailureTo = arrayMessageSMTPFailureTo

        self.strEDIDate = Common.getDateSimple(datetime.datetime.now())
        self.strEDITime = Common.getTimeSimple(datetime.datetime.now())

        self.strPathBAK = self.formatPath(self.jsonFlow["pathBAK"])

    def formatPath(self, strPath):
        strPathReturn = strPath
        strPathReturn = strPathReturn.replace("{ediid}", self.strEDIID)
        strPathReturn = strPathReturn.replace("{flowid}", self.jsonFlow["flowID"])
        strPathReturn = strPathReturn.replace("{edidate}", self.strEDIDate)
        strPathReturn = strPathReturn.replace("{editime}", self.strEDITime)

        strDirectory = strPathReturn[:strPathReturn.rindex("/") + 1]
        if not os.path.exists(strDirectory):
            os.makedirs(strDirectory)

        return strPathReturn

    def executeFlow(self):
        enumFlowResult = EDIEnum.EnumFlowResult.Null

        try:
            strLog = "EDI_NO: " + self.dictFlow["EDI_NO"] + \
                    " / EDI_ID: " + self.dictFlow["EDI_ID"] + \
                    " / EDI_FLOW_ID: " + self.dictFlow["EDI_FLOW_ID"]
            self.logger.info(strLog)

            EDIEntity.updateFlowBeginData(self.strEDIConnection, self.strEDIDB, self.dictFlow["EDI_NO"], self.strEDIDate, self.strEDITime)

            Common.writeJsonFile(os.path.join(self.strPathBAK, "Flows.json"), self.jsonFlow)

            for jsonJobNow in self.jsonFlow["jobList"]:
                job = EDIJob.Job(self.strEDIID, self.strEDIConnection, self.strEDIDB, self.dictFlow, self.jsonFlow, jsonJobNow, self.strEDIDate, self.strEDITime, 
                    self.intFileBlockSize, self.strMessageSMTPServer, self.strMessageSMTPFrom, self.arrayMessageSMTPSuccessTo, self.arrayMessageSMTPFailureTo)
                enumJobResult = job.executeJob()

                if enumJobResult == EDIEnum.EnumJobResult.Failure:
                    enumFlowResult = EDIEnum.EnumFlowResult.Failure
                elif enumJobResult == EDIEnum.EnumJobResult.Cancel and enumFlowResult != EDIEnum.EnumFlowResult.Failure:
                    enumFlowResult = EDIEnum.EnumFlowResult.Cancel
                elif (enumJobResult == EDIEnum.EnumJobResult.Success and
                    enumFlowResult != EDIEnum.EnumFlowResult.Failure and enumFlowResult != EDIEnum.EnumFlowResult.Cancel):
                    enumFlowResult = EDIEnum.EnumFlowResult.Success

                if enumFlowResult == EDIEnum.EnumFlowResult.Failure:
                    break

            EDIEntity.updateFlowEndData(self.strEDIConnection, self.strEDIDB, self.dictFlow["EDI_NO"], enumFlowResult)

            strLog = "enumFlowResult: " + enumFlowResult.name
            if enumFlowResult == EDIEnum.EnumFlowResult.Null or enumFlowResult == EDIEnum.EnumFlowResult.Failure:
                self.logger.error(strLog)
            elif enumFlowResult == EDIEnum.EnumFlowResult.Cancel:
                self.logger.warning(strLog)
            else:
                self.logger.info(strLog)

            if enumFlowResult == EDIEnum.EnumFlowResult.Success:
                strRunningFlow = os.path.join(self.strEDIPath, self.strEDIID + "." + self.jsonFlow["flowID"] + ".run")
                os.remove(strRunningFlow)

                strMessageSMTPSubject = "!!!!! {ediID} {flowID} Success !!!!! EDINo:{ediNo}".format(ediID=self.strEDIID, flowID=self.jsonFlow["flowID"], ediNo=self.dictFlow["EDI_NO"])
                Message.sendSMTPMail(self.strMessageSMTPServer, self.strMessageSMTPFrom, self.arrayMessageSMTPSuccessTo, strMessageSMTPSubject, "", None, None)
            else:
                strMessageSMTPSubject = "!!!!! {ediID} {flowID} Failure !!!!! EDINo:{ediNo}".format(ediID=self.strEDIID, flowID=self.jsonFlow["flowID"], ediNo=self.dictFlow["EDI_NO"])
                Message.sendSMTPMail(self.strMessageSMTPServer, self.strMessageSMTPFrom, self.arrayMessageSMTPFailureTo, strMessageSMTPSubject, "", None, None)

        except Exception:
            strExceptionMessage = traceback.format_exc()
            self.logger.error(strExceptionMessage)

            strMessageSMTPSubject = "!!!!! {ediID} {flowID} Exception !!!!! EDINo:{ediNo}".format(ediID=self.strEDIID, flowID=self.jsonFlow["flowID"], ediNo=self.dictFlow["EDI_NO"])
            Message.sendSMTPMail(self.strMessageSMTPServer, self.strMessageSMTPFrom, self.arrayMessageSMTPFailureTo, strMessageSMTPSubject, strExceptionMessage, None, None)

        return enumFlowResult
