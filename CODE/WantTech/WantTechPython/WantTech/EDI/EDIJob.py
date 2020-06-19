import os
import sys
import shutil
import json
import datetime
import subprocess
import traceback
import logging
from Utility import Common
from Utility import Message
from Utility import File
from Entity import DBEntity
from Entity import MariaEntity
from Entity import HanaEntity
from Entity import OracleEntity
from EDI import EDIEnum
from EDI import EDIEntity

class Job:
    strLoggerName = None
    logger = None
    
    strEDIID = None
    strEDIConnection = None
    strEDIDB = None

    dictFlow = None
    jsonFlow = None
    jsonJob = None

    strEDIDate = None
    strEDITime = None

    intFileBlockSize = None

    strMessageSMTPServer = None
    strMessageSMTPFrom = None
    arrayMessageSMTPSuccessTo = None
    arrayMessageSMTPFailureTo = None

    strPathBAK = None

    strPathCMD = None
    strPathSCRIPT = None
    strPathSRC = None
    strPathRES = None
    strPathBAD = None
    strPathLOG = None

    strJobConnection = None
    strJobDB = None

    def __init__(self, strEDIID, strEDIConnection, strEDIDB, dictFlow, jsonFlow, jsonJob, strEDIDate, strEDITime, 
        intFileBlockSize, strMessageSMTPServer, strMessageSMTPFrom, arrayMessageSMTPSuccessTo, arrayMessageSMTPFailureTo):
        self.strLoggerName = strEDIID + "." + jsonFlow["flowID"]
        Common.setLogging(self.strLoggerName)
        self.logger = logging.getLogger(self.strLoggerName)

        self.strEDIID = strEDIID
        self.strEDIConnection = strEDIConnection
        self.strEDIDB = strEDIDB

        self.dictFlow = dictFlow
        self.jsonFlow = jsonFlow
        self.jsonJob = jsonJob

        self.strEDIDate = strEDIDate
        self.strEDITime = strEDITime

        self.intFileBlockSize = intFileBlockSize

        self.strMessageSMTPServer = strMessageSMTPServer
        self.strMessageSMTPFrom = strMessageSMTPFrom
        self.arrayMessageSMTPSuccessTo = arrayMessageSMTPSuccessTo
        self.arrayMessageSMTPFailureTo = arrayMessageSMTPFailureTo

        self.strPathBAK = self.formatPath(self.jsonFlow["pathBAK"], self.jsonJob["jobID"])

        self.strPathCMD = self.formatPath(self.jsonFlow["pathCMD"], self.jsonJob["jobID"])
        self.strPathSCRIPT = self.formatPath(self.jsonFlow["pathSCRIPT"], self.jsonJob["jobID"])
        self.strPathSRC = self.formatPath(self.jsonFlow["pathSRC"], self.jsonJob["jobID"])
        self.strPathRES = self.formatPath(self.jsonFlow["pathRES"], self.jsonJob["jobID"])
        self.strPathBAD = self.formatPath(self.jsonFlow["pathBAD"], self.jsonJob["jobID"])
        self.strPathLOG = self.formatPath(self.jsonFlow["pathLOG"], self.jsonJob["jobID"])

        if (EDIEnum.EnumJobType[self.jsonJob["jobType"]] == EDIEnum.EnumJobType.EDITrigNextFlow or EDIEnum.EnumJobType[self.jsonJob["jobType"]] == EDIEnum.EnumJobType.PythonExecute):
            self.strJobConnection = self.strEDIConnection
            self.strJobDB = self.strEDIDB
        else:
            jsonConnection = Common.filterJsonListFirst(self.jsonFlow["connectionList"], "connectionID", self.jsonJob["connectionID"])
            self.strJobConnection = jsonConnection["connection"]
            self.strJobDB = jsonConnection["db"]

    def formatPath(self, strPath, strJobID):
        strPathReturn = strPath
        strPathReturn = strPathReturn.replace("{ediid}", self.strEDIID)
        strPathReturn = strPathReturn.replace("{flowid}", self.jsonFlow["flowID"])
        strPathReturn = strPathReturn.replace("{edidate}", self.strEDIDate)
        strPathReturn = strPathReturn.replace("{editime}", self.strEDITime)
        strPathReturn = strPathReturn.replace("{jobid}", strJobID)

        strDirectory = strPathReturn[:strPathReturn.rindex("/") + 1]
        if not os.path.exists(strDirectory):
            os.makedirs(strDirectory)

        return strPathReturn

    def sendSMTPMail(self, strExceptionMessage):
        strMessageSMTPSubject = "!!!!! {ediID} {flowID} Exception !!!!! EDINo:{ediNo}".format(ediID=self.strEDIID, flowID=self.jsonFlow["flowID"], ediNo=self.dictFlow["EDI_NO"])
        Message.sendSMTPMail(self.strMessageSMTPServer, self.strMessageSMTPFrom, self.arrayMessageSMTPFailureTo, strMessageSMTPSubject, strExceptionMessage, None, None)

    def executeEDITrigNextFlow(self):
        strEDIDate = Common.getDateSimple(datetime.datetime.now())
        if EDIEntity.insertNextFlow(self.strEDIConnection, self.strEDIDB, strEDIDate,
                                    Common.filterJsonListFirst(self.jsonJob["parameterList"],"parameterID","EDI_ID")["parameterValue"], 
                                    Common.filterJsonListFirst(self.jsonJob["parameterList"],"parameterID","EDI_FLOW_ID")["parameterValue"], 
                                    self.dictFlow["EDI_NO"], self.dictFlow["DATA_DATE"]):
            return EDIEnum.EnumJobResult.Success
        else:
            return EDIEnum.EnumJobResult.Failure

    def executeHanaDBExport(self):
        try:
            strSQL = ""
            with open(self.strPathCMD, "r") as streamFileContent:
                strSQL = streamFileContent.read()
            
            if strSQL != "":
                dictParameter = {
                    "edino": HanaEntity.HanaParameter(objValue=self.dictFlow["EDI_NO"], enumType=HanaEntity.EnumHanaParameterType.Char),
                    "flowid": HanaEntity.HanaParameter(objValue=self.jsonFlow["flowID"], enumType=HanaEntity.EnumHanaParameterType.Char),
                    "edidate": HanaEntity.HanaParameter(objValue=self.strEDIDate, enumType=HanaEntity.EnumHanaParameterType.Char),
                    "editime": HanaEntity.HanaParameter(objValue=self.strEDITime, enumType=HanaEntity.EnumHanaParameterType.Char),
                    "jobid": HanaEntity.HanaParameter(objValue=self.jsonJob["jobID"], enumType=HanaEntity.EnumHanaParameterType.Char),
                    "datadate": HanaEntity.HanaParameter(objValue=self.dictFlow["DATA_DATE"], enumType=HanaEntity.EnumHanaParameterType.Char),
                }
                strSQL = DBEntity.getHanaSQLCommand(self.strJobConnection, strSQL, dictParameter)
                strSQL = strSQL.replace("\"", "\\\"").replace("\n", " ").replace("\r", " ").replace("\r\n", " ")

                strSAPHome = os.environ.get("SAP_HOME")

                strCommand = strSAPHome + "/"+ \
                             DBEntity.getHanaExportConnectionString(self.strJobConnection) + \
                             " -x -resultencoding UTF8 -a -o \"" + self.strPathRES + "\" \"" + strSQL + "\""
                self.logger.debug(strCommand)

                tupleOutput = subprocess.Popen(strCommand, shell=True, stderr=subprocess.PIPE).communicate()
                strErrorOutput = tupleOutput[1].decode('utf-8')
                if strErrorOutput != "":
                    self.logger.error(strErrorOutput)
                    return EDIEnum.EnumJobResult.Failure
                else:
                    intDataCount = File.getFileLineCount(self.strPathRES, self.intFileBlockSize)
                    intDataVolume = os.stat(self.strPathRES).st_size
                    EDIEntity.updateJobCountData(self.strEDIConnection, self.strEDIDB, self.dictFlow["EDI_NO"], self.jsonJob["jobID"], intDataCount, intDataVolume)
                    return EDIEnum.EnumJobResult.Success
            else:
                return EDIEnum.EnumJobResult.Failure
        except Exception:
            strExceptionMessage = traceback.format_exc()
            self.logger.error(strExceptionMessage)
            self.sendSMTPMail(strExceptionMessage)
            return EDIEnum.EnumJobResult.Failure

    def executeOracleDBExport(self):
        try:
            strSQL = ""
            strPathCMDFileName = self.strPathCMD[self.strPathCMD.rindex("/") + 1:]

            with open(self.strPathCMD, "r") as streamFileContent:
                strSQL = streamFileContent.read()
            
            if strSQL != "":
                dictParameter = {
                    "edino": OracleEntity.OracleParameter(objValue=self.dictFlow["EDI_NO"], enumType=OracleEntity.EnumOracleParameterType.Char),
                    "flowid": OracleEntity.OracleParameter(objValue=self.jsonFlow["flowID"], enumType=OracleEntity.EnumOracleParameterType.Char),
                    "edidate": OracleEntity.OracleParameter(objValue=self.strEDIDate, enumType=OracleEntity.EnumOracleParameterType.Char),
                    "editime": OracleEntity.OracleParameter(objValue=self.strEDITime, enumType=OracleEntity.EnumOracleParameterType.Char),
                    "jobid": OracleEntity.OracleParameter(objValue=self.jsonJob["jobID"], enumType=OracleEntity.EnumOracleParameterType.Char),
                    "datadate": OracleEntity.OracleParameter(objValue=self.dictFlow["DATA_DATE"], enumType=OracleEntity.EnumOracleParameterType.Char),
                }
                strSQL = DBEntity.getOracleSQLCommand(strSQL, dictParameter)

                strSQL = "set termout off newpage none pages 0 feedback off linesize 32767 trimspool on \n" + \
                         "spool &1 \n" + \
                         strSQL + " \n" + \
                         "spool off \n" + \
                         "exit;"

                with open(self.strPathBAK + strPathCMDFileName, 'w') as streamFileContent:
                    streamFileContent.write(strSQL)

                strOracleHome = os.environ.get("ORACLE_HOME")
                strNLSLang = os.environ.get("NLS_LANG")
                strLibraryName = "DYLD_LIBRARY_PATH"
                strLibraryPath = os.environ.get(strLibraryName)
                if strLibraryPath == None:
                    strLibraryName = "LD_LIBRARY_PATH"
                    strLibraryPath = os.environ.get(strLibraryName)

                strCommand = strLibraryName + "=" + strLibraryPath + " NLS_LANG=" + strNLSLang + " " + os.path.join(strOracleHome, "bin/") + \
                             DBEntity.getOracleExportConnectionString(self.strJobConnection) + \
                             " @" + self.strPathBAK + strPathCMDFileName + " " + self.strPathRES
                self.logger.debug(strCommand)

                tupleOutput = subprocess.Popen(strCommand, shell=True, stderr=subprocess.PIPE).communicate()
                strErrorOutput = tupleOutput[1].decode('utf-8')
                if strErrorOutput != "":
                    self.logger.error(strErrorOutput)
                    return EDIEnum.EnumJobResult.Failure
                else:
                    intDataCount = File.getFileLineCount(self.strPathRES, self.intFileBlockSize)
                    intDataVolume = os.stat(self.strPathRES).st_size
                    EDIEntity.updateJobCountData(self.strEDIConnection, self.strEDIDB, self.dictFlow["EDI_NO"], self.jsonJob["jobID"], intDataCount, intDataVolume)
                    return EDIEnum.EnumJobResult.Success
            else:
                return EDIEnum.EnumJobResult.Failure
        except Exception:
            strExceptionMessage = traceback.format_exc()
            self.logger.error(strExceptionMessage)
            self.sendSMTPMail(strExceptionMessage)
            return EDIEnum.EnumJobResult.Failure

    def executeMariaDBExport(self):
        try:
            strSQL = ""
            with open(self.strPathCMD, "r") as streamFileContent:
                strSQL = streamFileContent.read()
            
            if strSQL != "":
                dictParameter = {
                    "edino": MariaEntity.MariaParameter(objValue=self.dictFlow["EDI_NO"], enumType=MariaEntity.EnumMariaParameterType.Char),
                    "flowid": MariaEntity.MariaParameter(objValue=self.jsonFlow["flowID"], enumType=MariaEntity.EnumMariaParameterType.Char),
                    "edidate": MariaEntity.MariaParameter(objValue=self.strEDIDate, enumType=MariaEntity.EnumMariaParameterType.Char),
                    "editime": MariaEntity.MariaParameter(objValue=self.strEDITime, enumType=MariaEntity.EnumMariaParameterType.Char),
                    "jobid": MariaEntity.MariaParameter(objValue=self.jsonJob["jobID"], enumType=MariaEntity.EnumMariaParameterType.Char),
                    "datadate": MariaEntity.MariaParameter(objValue=self.dictFlow["DATA_DATE"], enumType=MariaEntity.EnumMariaParameterType.Char),
                }
                strSQL = DBEntity.getMariaSQLCommand(strSQL, dictParameter)
                strSQL = strSQL.replace("\"", "\\\"").replace("\n", " ").replace("\r", " ").replace("\r\n", " ")

                strCommand = DBEntity.getMariaExportConnectionString(self.strJobConnection) + \
                            " " + self.strJobDB + " -sN -B -e \"" + strSQL + "\" | sed \"s/\\\"/\\\\\\\\\\\\\\\"/g;s/^/\\\"/;s/\\\t/\\\",\\\"/g;s/$/\\\"/;\" > " + self.strPathRES
                self.logger.debug(strCommand)

                i = 0
                strErrorOutput = ""
                while i < 20:
                    tupleOutput = subprocess.Popen(strCommand, shell=True, stderr=subprocess.PIPE).communicate()
                    strErrorOutput = tupleOutput[1].decode("utf-8")
                    if strErrorOutput == "":
                        intDataCount = File.getFileLineCount(self.strPathRES, self.intFileBlockSize)
                        intDataVolume = os.stat(self.strPathRES).st_size
                        EDIEntity.updateJobCountData(self.strEDIConnection, self.strEDIDB, self.dictFlow["EDI_NO"], self.jsonJob["jobID"], intDataCount, intDataVolume)
                        return EDIEnum.EnumJobResult.Success
                    elif strErrorOutput.find("Can't connect to MySQL server") > -1:
                        self.logger.error(strErrorOutput)
                    else:
                        self.logger.error(strErrorOutput)
                        return EDIEnum.EnumJobResult.Failure
                    i += 1

                if strErrorOutput.find("Can't connect to MySQL server") > -1:
                    return EDIEnum.EnumJobResult.Failure
            else:
                return EDIEnum.EnumJobResult.Failure
        except Exception:
            strExceptionMessage = traceback.format_exc()
            self.logger.error(strExceptionMessage)
            self.sendSMTPMail(strExceptionMessage)
            return EDIEnum.EnumJobResult.Failure

    def executeMariaDBImport(self):
        try:
            strDependOnJobPathRES = self.formatPath(self.jsonFlow["pathRES"], self.jsonJob["jobDependOn"])
            strObjectNamePathRES = self.formatPath(self.jsonFlow["pathRES"], self.jsonJob["objectName"])

            if self.jsonJob["objectName"] != "" and self.jsonJob["jobDependOn"] != "" and os.path.isfile(strDependOnJobPathRES):
                strCommand = "mv {0} {1}".format(strDependOnJobPathRES, strObjectNamePathRES)
                self.logger.debug(strCommand)
                subprocess.call(strCommand, shell=True)

                strCommand = DBEntity.getMariaImportConnectionString(self.strJobConnection) + \
                            " --default-character-set=utf8 --fields-terminated-by=, --fields-enclosed-by=\\\" --local=1 " + self.strJobDB + " " + strObjectNamePathRES
                self.logger.debug(strCommand)

                tupleOutput = subprocess.Popen(strCommand, shell=True, stderr=subprocess.PIPE).communicate()
                strErrorOutput = tupleOutput[1].decode('utf-8')
                if strErrorOutput != "":
                    self.logger.error(strErrorOutput)
                    return EDIEnum.EnumJobResult.Failure
                else:
                    intDataCount = EDIEntity.getMariaDBImportDataCount(self.strJobConnection, self.strJobDB, self.jsonJob["objectName"])
                    intDataVolume = os.stat(strObjectNamePathRES).st_size
                    EDIEntity.updateJobCountData(self.strEDIConnection, self.strEDIDB, self.dictFlow["EDI_NO"], self.jsonJob["jobID"], intDataCount, intDataVolume)

                    listDataCountDifJobs = EDIEntity.getDataCountDifJobList(self.strEDIConnection, self.strEDIDB, self.dictFlow["EDI_NO"], self.jsonJob["jobID"])
                    if len(listDataCountDifJobs) > 0:
                        strMessageSMTPSubject = "!!!!! {ediID} {flowID} Data Error !!!!! EDINo:{ediNo} JobID:{jobID}({dataCountDif}) ".format(
                            ediID=self.strEDIID, flowID=self.jsonFlow["flowID"], 
                            ediNo=self.dictFlow["EDI_NO"], jobID=self.jsonJob["jobID"], dataCountDif=str(listDataCountDifJobs[0]["DATA_COUNT_DIF"]))
                        self.logger.error("DataCountDif:" + str(listDataCountDifJobs[0]["DATA_COUNT_DIF"]))
                        Message.sendSMTPMail(self.strMessageSMTPServer, self.strMessageSMTPFrom, self.arrayMessageSMTPFailureTo, strMessageSMTPSubject, "", None, None)
                        return EDIEnum.EnumJobResult.Failure
                    else:
                        return EDIEnum.EnumJobResult.Success
            else:
                return EDIEnum.EnumJobResult.Failure
        except Exception:
            strExceptionMessage = traceback.format_exc()
            self.logger.error(strExceptionMessage)
            self.sendSMTPMail(strExceptionMessage)
            return EDIEnum.EnumJobResult.Failure

    def executeMariaDBExecuteProcedures(self):
        try:
            if self.jsonJob["objectName"] != "":
                arrayArguments = [
                    self.dictFlow["EDI_NO"], self.dictFlow["DATA_DATE"], "N"
                ]
                strResult = DBEntity.executeMariaProcedure(self.strJobConnection, self.strJobDB, self.jsonJob["objectName"], arrayArguments)

                if strResult == "Y":
                    return EDIEnum.EnumJobResult.Success
                else:
                    return EDIEnum.EnumJobResult.Failure
            else:
                return EDIEnum.EnumJobResult.Failure
        except Exception:
            strExceptionMessage = traceback.format_exc()
            self.logger.error(strExceptionMessage)
            self.sendSMTPMail(strExceptionMessage)
            return EDIEnum.EnumJobResult.Failure

    def executePythonExecute(self):
        try:
            strJobPathRES = self.formatPath(self.jsonFlow["pathRES"], self.jsonJob["jobID"])
            strDependOnJobPathRES = self.formatPath(self.jsonFlow["pathRES"], self.jsonJob["jobDependOn"])

            strCommand = sys.executable + " " + self.strPathSCRIPT + " " + \
                self.strLoggerName + " " + self.strEDIConnection + " " + self.strEDIDB + " " + self.dictFlow["EDI_NO"] + " " + strJobPathRES + " " + strDependOnJobPathRES
            self.logger.debug(strCommand)

            tupleOutput = subprocess.Popen(strCommand, shell=True, stderr=subprocess.PIPE).communicate()
            strErrorOutput = tupleOutput[1].decode('utf-8')
            if strErrorOutput != "":
                self.logger.error(strErrorOutput)
                return EDIEnum.EnumJobResult.Failure
            else:
                return EDIEnum.EnumJobResult.Success
        except Exception:
            strExceptionMessage = traceback.format_exc()
            self.logger.error(strExceptionMessage)
            self.sendSMTPMail(strExceptionMessage)
            return EDIEnum.EnumJobResult.Failure

    switch = {
        "EDITrigNextFlow": executeEDITrigNextFlow,
        "HanaDBExport": executeHanaDBExport,
        "OracleDBExport": executeOracleDBExport,
        "MariaDBExport": executeMariaDBExport,
        "MariaDBImport": executeMariaDBImport,
        "MariaDBExecuteProcedures": executeMariaDBExecuteProcedures,
        "PythonExecute": executePythonExecute,
    }

    def executeJob(self):
        strLog = "EDI_JOB_ID: " + self.jsonJob["jobID"]
        self.logger.info(strLog)

        strObjectName = None
        if "objectName" in self.jsonJob:
            strObjectName = self.jsonJob["objectName"]

        strJobDependOn = None
        if "jobDependOn" in self.jsonJob:
            strJobDependOn = self.jsonJob["jobDependOn"]

        EDIEntity.insertNewJob(self.strEDIConnection, self.strEDIDB, self.dictFlow["EDI_NO"], self.jsonJob["jobID"], self.jsonJob["jobType"], strObjectName, strJobDependOn)

        enumJobResult = EDIEnum.EnumJobResult.Null
        if self.jsonJob.get("jobDependOn") != None and self.jsonJob.get("jobDependOn") != "":
            listDependOnJobs = EDIEntity.getDependOnJobList(self.strEDIConnection, self.strEDIDB, self.dictFlow["EDI_NO"], self.jsonJob.get("jobDependOn"))
            if len(listDependOnJobs) >= 1 and listDependOnJobs[0]["RESULT_ID"] != EDIEnum.EnumEDIResultID.S.name:
                enumJobResult = EDIEnum.EnumJobResult.Cancel

        if enumJobResult == EDIEnum.EnumJobResult.Null:
            if os.path.exists(self.strPathCMD):
                strPathCMDFileName = self.strPathCMD[self.strPathCMD.rindex("/") + 1:]
                shutil.copy(self.strPathCMD, os.path.join(self.strPathBAK, strPathCMDFileName))
            if os.path.exists(self.strPathSCRIPT):
                strPathSCRIPTFileName = self.strPathSCRIPT[self.strPathSCRIPT.rindex("/") + 1:]
                shutil.copy(self.strPathSCRIPT, os.path.join(self.strPathBAK, strPathSCRIPTFileName))
            enumJobResult = self.switch[self.jsonJob["jobType"]](self)

        EDIEntity.updateJobEndData(self.strEDIConnection, self.strEDIDB, self.dictFlow["EDI_NO"], self.jsonJob["jobID"], enumJobResult)

        strLog = "enumJobResult: " + enumJobResult.name
        if enumJobResult == EDIEnum.EnumJobResult.Failure or enumJobResult == EDIEnum.EnumJobResult.Null:
            self.logger.error(strLog)
        elif enumJobResult == EDIEnum.EnumJobResult.Cancel:
            self.logger.warning(strLog)
        else:
            self.logger.info(strLog)

        return enumJobResult
