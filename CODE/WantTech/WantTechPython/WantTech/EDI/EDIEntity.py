import datetime
from Utility import Common
from Entity import DBEntity
from Entity import MariaEntity
from EDI import EDIEnum

def getWaitingFlowList(strEDIConnection, strEDIDB, strEDIID):
    strSQL = "SELECT M.* " + \
             "FROM DWWANT.EDI_FLOW M " + \
             "JOIN (SELECT EDI_NO " + \
             "      FROM DWWANT.EDI_FLOW " + \
             "      WHERE {EDI_ID} AND STATUS_ID='W' AND IS_DELETED='N') G " + \
             "ON M.EDI_NO=G.EDI_NO " + \
             "ORDER BY M.EDI_NO; "

    dictMariaParameter = {
        "EDI_ID": MariaEntity.MariaParameter(strOperator="=", objValue=strEDIID, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listWaitingFlows = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listWaitingFlows

def insertNewFlow(strEDIConnection, strEDIDB, strEDIDate, strEDIID, strEDIFlowID, strDataDate):
    arrayArguments = [
        strEDIID, strEDIFlowID, strEDIDate, strDataDate, "EDIService", "N"
    ]
    strSPResult = DBEntity.executeMariaProcedure(strEDIConnection, strEDIDB, "SP_EDI_INSERT_NEW_FLOW", arrayArguments)

    if strSPResult == "Y":
        return True
    else:
        return False

def insertNextFlow(strEDIConnection, strEDIDB, strEDIDate, strEDIID, strEDIFlowID, strAutoEDINo, strDataDate):
    strSQL = "INSERT INTO DWWANT.EDI_FLOW VALUES ( " + \
             "    DWWANT.FN_GET_EDI_NO({EDI_DATE}), {EDI_ID}, {EDI_FLOW_ID} " + \
             "  , NULL, NULL " + \
             "  , {DATA_DATE}, 'W', NULL, NULL, NULL " + \
             "  , 'Y', NOW(), {AUTO_EDI_NO}, 'N' " + \
             "  , {UPD_USER_ID}, NOW() " + \
             "); "

    dictMariaParameter = {
        "EDI_DATE": MariaEntity.MariaParameter(objValue=strEDIDate, enumType=MariaEntity.EnumMariaParameterType.Char),
        "EDI_ID": MariaEntity.MariaParameter(objValue=strEDIID, enumType=MariaEntity.EnumMariaParameterType.Char),
        "EDI_FLOW_ID": MariaEntity.MariaParameter(objValue=strEDIFlowID, enumType=MariaEntity.EnumMariaParameterType.Char),
        "DATA_DATE": MariaEntity.MariaParameter(objValue=strDataDate, enumType=MariaEntity.EnumMariaParameterType.Char),
        "AUTO_EDI_NO": MariaEntity.MariaParameter(objValue=strAutoEDINo, enumType=MariaEntity.EnumMariaParameterType.Char),
        "UPD_USER_ID": MariaEntity.MariaParameter(objValue="EDIService", enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    return DBEntity.executeMariaData(strEDIConnection, strEDIDB, strSQL)

def updateFlowBeginData(strEDIConnection, strEDIDB, strEDINo, strEDIDate, strEDITime):
    strSQL = "UPDATE DWWANT.EDI_FLOW SET " + \
             "    {EDI_DATE}, {EDI_TIME} " + \
             "  , {STATUS_ID}, {DT_BEGIN} " + \
             "  , {UPD_USER_ID}, UPD_DT=NOW() " + \
             "WHERE {EDI_NO}; "

    dictMariaParameter = {
        "EDI_DATE": MariaEntity.MariaParameter(strOperator="=", objValue=strEDIDate, enumType=MariaEntity.EnumMariaParameterType.Char),
        "EDI_TIME": MariaEntity.MariaParameter(strOperator="=", objValue=strEDITime, enumType=MariaEntity.EnumMariaParameterType.Char),
        "STATUS_ID": MariaEntity.MariaParameter(strOperator="=", objValue=EDIEnum.EnumEDIStatusID.B.name, enumType=MariaEntity.EnumMariaParameterType.Char),
        "DT_BEGIN": MariaEntity.MariaParameter(strOperator="=", objValue=datetime.datetime.now(), enumType=MariaEntity.EnumMariaParameterType.DateTime),
        "UPD_USER_ID": MariaEntity.MariaParameter(strOperator="=", objValue="EDIService", enumType=MariaEntity.EnumMariaParameterType.Char),
        "EDI_NO": MariaEntity.MariaParameter(strOperator="=", objValue=strEDINo, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    return DBEntity.executeMariaData(strEDIConnection, strEDIDB, strSQL)

def updateFlowEndData(strEDIConnection, strEDIDB, strEDINo, enumFlowResult):
    strSQL = "UPDATE DWWANT.EDI_FLOW SET " + \
             "    {STATUS_ID}, {RESULT_ID}, {DT_END} " + \
             "  , {UPD_USER_ID}, UPD_DT=NOW() " + \
             "WHERE {EDI_NO}; "

    enumEDIResultID = EDIEnum.EnumEDIResultID.F
    if enumFlowResult == EDIEnum.EnumFlowResult.Success:
        enumEDIResultID = EDIEnum.EnumEDIResultID.S
    elif enumFlowResult == EDIEnum.EnumFlowResult.Cancel:
        enumEDIResultID = EDIEnum.EnumEDIResultID.C

    dictMariaParameter = {
        "STATUS_ID": MariaEntity.MariaParameter(strOperator="=", objValue=EDIEnum.EnumEDIStatusID.F.name, enumType=MariaEntity.EnumMariaParameterType.Char),
        "RESULT_ID": MariaEntity.MariaParameter(strOperator="=", objValue=enumEDIResultID.name, enumType=MariaEntity.EnumMariaParameterType.Char),
        "DT_END": MariaEntity.MariaParameter(strOperator="=", objValue=datetime.datetime.now(), enumType=MariaEntity.EnumMariaParameterType.DateTime),
        "UPD_USER_ID": MariaEntity.MariaParameter(strOperator="=", objValue="EDIService", enumType=MariaEntity.EnumMariaParameterType.Char),
        "EDI_NO": MariaEntity.MariaParameter(strOperator="=", objValue=strEDINo, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    return DBEntity.executeMariaData(strEDIConnection, strEDIDB, strSQL)

def insertNewJob(strEDIConnection, strEDIDB, strEDINo, strJobID, strJobType, strObjectName, strDependOn):
    strSQL = "INSERT INTO DWWANT.EDI_JOB VALUES ( " + \
             "    {EDI_NO}, {EDI_JOB_ID}, {EDI_JOB_TYPE}, {EDI_OBJ_NM}, {EDI_DEP_JOB_ID} " + \
             "  , {STATUS_ID}, NULL " + \
             "  , {DT_BEGIN}, NULL, NULL, NULL, NULL " + \
             "  , {UPD_USER_ID}, NOW() " + \
             "); "

    dictMariaParameter = {
        "EDI_NO": MariaEntity.MariaParameter(objValue=strEDINo, enumType=MariaEntity.EnumMariaParameterType.Char),
        "EDI_JOB_ID": MariaEntity.MariaParameter(objValue=strJobID, enumType=MariaEntity.EnumMariaParameterType.Char),
        "EDI_JOB_TYPE": MariaEntity.MariaParameter(objValue=strJobType, enumType=MariaEntity.EnumMariaParameterType.Char),
        "EDI_OBJ_NM": MariaEntity.MariaParameter(objValue=strObjectName, enumType=MariaEntity.EnumMariaParameterType.Char),
        "EDI_DEP_JOB_ID": MariaEntity.MariaParameter(objValue=strDependOn, enumType=MariaEntity.EnumMariaParameterType.Char),
        "STATUS_ID": MariaEntity.MariaParameter(objValue=EDIEnum.EnumEDIStatusID.B.name, enumType=MariaEntity.EnumMariaParameterType.Char),
        "DT_BEGIN": MariaEntity.MariaParameter(objValue=datetime.datetime.now(), enumType=MariaEntity.EnumMariaParameterType.DateTime),
        "UPD_USER_ID": MariaEntity.MariaParameter(objValue="EDIService", enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    return DBEntity.executeMariaData(strEDIConnection, strEDIDB, strSQL)

def updateJobEndData(strEDIConnection, strEDIDB, strEDINo, strJobID, enumJobResult):
    strSQL = "UPDATE DWWANT.EDI_JOB SET " + \
             "    {STATUS_ID}, {RESULT_ID}, {DT_END} " + \
             "  , {UPD_USER_ID}, UPD_DT=NOW() " + \
             "WHERE {EDI_NO} AND {EDI_JOB_ID}; "

    enumEDIResultID = EDIEnum.EnumEDIResultID.F
    if enumJobResult == EDIEnum.EnumJobResult.Success:
        enumEDIResultID = EDIEnum.EnumEDIResultID.S
    elif enumJobResult == EDIEnum.EnumJobResult.Cancel:
        enumEDIResultID = EDIEnum.EnumEDIResultID.C

    dictMariaParameter = {
        "STATUS_ID": MariaEntity.MariaParameter(strOperator="=", objValue=EDIEnum.EnumEDIStatusID.F.name, enumType=MariaEntity.EnumMariaParameterType.Char),
        "RESULT_ID": MariaEntity.MariaParameter(strOperator="=", objValue=enumEDIResultID.name, enumType=MariaEntity.EnumMariaParameterType.Char),
        "DT_END": MariaEntity.MariaParameter(strOperator="=", objValue=datetime.datetime.now(), enumType=MariaEntity.EnumMariaParameterType.DateTime),
        "UPD_USER_ID": MariaEntity.MariaParameter(strOperator="=", objValue="EDIService", enumType=MariaEntity.EnumMariaParameterType.Char),
        "EDI_NO": MariaEntity.MariaParameter(strOperator="=", objValue=strEDINo, enumType=MariaEntity.EnumMariaParameterType.Char),
        "EDI_JOB_ID": MariaEntity.MariaParameter(strOperator="=", objValue=strJobID, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    return DBEntity.executeMariaData(strEDIConnection, strEDIDB, strSQL)

def updateJobCountData(strEDIConnection, strEDIDB, strEDINo, strJobID, intDataCount, intDataVolume):
    strSQL = "UPDATE DWWANT.EDI_JOB J " + \
             "LEFT JOIN DWWANT.EDI_JOB D " + \
             "ON J.EDI_NO=D.EDI_NO AND J.EDI_DEP_JOB_ID=D.EDI_JOB_ID " + \
             "SET J.DATA_COUNT={DATA_COUNT}, J.DATA_VOLUME={DATA_VOLUME} " + \
             "  , J.DATA_COUNT_DIF=(CASE WHEN J.EDI_JOB_TYPE='MariaDBImport' THEN (IFNULL(D.DATA_COUNT,0)-{DATA_COUNT}) ELSE NULL END) " + \
             "  , J.UPD_USER_ID={UPD_USER_ID}, J.UPD_DT=NOW() " + \
             "WHERE J.EDI_NO={EDI_NO} AND J.EDI_JOB_ID={EDI_JOB_ID}; "

    dictMariaParameter = {
        "DATA_COUNT": MariaEntity.MariaParameter(objValue=intDataCount, enumType=MariaEntity.EnumMariaParameterType.Int),
        "DATA_VOLUME": MariaEntity.MariaParameter(objValue=intDataVolume, enumType=MariaEntity.EnumMariaParameterType.Int),
        "UPD_USER_ID": MariaEntity.MariaParameter(objValue="EDIService", enumType=MariaEntity.EnumMariaParameterType.Char),
        "EDI_NO": MariaEntity.MariaParameter(objValue=strEDINo, enumType=MariaEntity.EnumMariaParameterType.Char),
        "EDI_JOB_ID": MariaEntity.MariaParameter(objValue=strJobID, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    return DBEntity.executeMariaData(strEDIConnection, strEDIDB, strSQL)

def getDependOnJobList(strEDIConnection, strEDIDB, strEDINo, strJobID):
    strSQL = "SELECT * " + \
             "FROM DWWANT.EDI_JOB " + \
             "WHERE {EDI_NO} AND {EDI_JOB_ID}; "

    dictMariaParameter = {
        "EDI_NO": MariaEntity.MariaParameter(strOperator="=", objValue=strEDINo, enumType=MariaEntity.EnumMariaParameterType.Char),
        "EDI_JOB_ID": MariaEntity.MariaParameter(strOperator="=", objValue=strJobID, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listDependOnJobs = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listDependOnJobs

def getDataCountDifJobList(strEDIConnection, strEDIDB, strEDINo, strJobID):
    strSQL = "SELECT * " + \
             "FROM DWWANT.EDI_JOB " + \
             "WHERE {EDI_NO} AND {EDI_JOB_ID} AND IFNULL(DATA_COUNT_DIF,-1)>0; "

    dictMariaParameter = {
        "EDI_NO": MariaEntity.MariaParameter(strOperator="=", objValue=strEDINo, enumType=MariaEntity.EnumMariaParameterType.Char),
        "EDI_JOB_ID": MariaEntity.MariaParameter(strOperator="=", objValue=strJobID, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listDataCountDifJobs = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listDataCountDifJobs

def getFlow(strEDIConnection, strEDIDB, strEDINo):
    strSQL = "SELECT * FROM DWWANT.EDI_FLOW WHERE {EDI_NO}; "

    dictMariaParameter = {
        "EDI_NO": MariaEntity.MariaParameter(strOperator="=", objValue=strEDINo, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listFlows = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listFlows[0]

def getMariaDBImportDataCount(strJobConnection, strJobDB, strJobObjectName):
    strSQL = "SELECT COUNT(1) AS CN " + \
             "FROM {DB_NAME}.{TABLE_NAME}; "

    dictMariaParameter = {
        "DB_NAME": MariaEntity.MariaParameter(objValue=strJobDB, enumType=MariaEntity.EnumMariaParameterType.Object),
        "TABLE_NAME": MariaEntity.MariaParameter(objValue=strJobObjectName, enumType=MariaEntity.EnumMariaParameterType.Object),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listCN = DBEntity.getMariaDataList(strJobConnection, strJobDB, strSQL)
    return listCN[0]["CN"]
