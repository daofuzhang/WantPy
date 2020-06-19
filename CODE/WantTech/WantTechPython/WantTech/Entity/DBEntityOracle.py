import cx_Oracle
from Utility import Common
from Utility import Security

def getOracleExportConnectionString(strConnection):
    strPassword = ""
    strReturn = ""

    if strConnection == "1SRC-taipei_dc@sh-oracle10g-236test":
        strPassword = "GodqUSW7fuFTZfNPJOKz37pbdxJIUcSznRKcF2tl32aldEqnjQsbWg8vasIlDuhD"
        strReturn = "sqlplus -s taipei_dc/%s@\\\"10.0.1.130:1521/SDQ\\\""
    elif strConnection == "1SRC-taipei_dc@sh-oracle10g-236prod":
        strPassword = "4gJmoOA4dinyY7sDuCIgDMMFP7wFoyRQjNqYsi8z86I="
        strReturn = "sqlplus -s taipei_dc/%s@\\\"10.0.1.236:1521/sfad\\\""
    elif strConnection == "1SRC-taipei_dc@sh-oracle11g-234test":
        strPassword = "iHn7qFokOeMKMpwlydTjW3qEdSquULZRv7akHIE67Uo="
        strReturn = "sqlplus -s taipei_dc/%s@\\\"10.0.26.56:1522/datamart\\\""
    elif strConnection == "1SRC-taipei_dc@sh-oracle11g-234prod":
        strPassword = "qUJMprHO215hZthdpGCvrqkrRj4HyYAJpqAW6K1zLvg="
        strReturn = "sqlplus -s taipei_dc/%s@\\\"10.0.0.234:1521/datamart\\\""

    return (strReturn % Security.decrypt(strPassword))

def getOraclePermission(strConnection):
    strHost = ""
    strUser = ""
    strPasswd = ""
    strServiceName = ""
    strPort = ""
    dictPermission = dict()

    if strConnection == "1SRC-taipei_dc@sh-oracle10g-236test":
        strHost = "10.0.1.130"
        strUser = "taipei_dc"
        strPasswd = "GodqUSW7fuFTZfNPJOKz37pbdxJIUcSznRKcF2tl32aldEqnjQsbWg8vasIlDuhD"
        strServiceName = "SDQ"
        strPort = "1521"
    elif strConnection == "1SRC-taipei_dc@sh-oracle10g-236prod":
        strHost = "10.0.1.236"
        strUser = "taipei_dc"
        strPasswd = "4gJmoOA4dinyY7sDuCIgDMMFP7wFoyRQjNqYsi8z86I="
        strServiceName = "sfad"
        strPort = "1521"
    elif strConnection == "1SRC-taipei_dc@sh-oracle11g-234test":
        strHost = "10.0.26.56"
        strUser = "taipei_dc"
        strPasswd = "iHn7qFokOeMKMpwlydTjW3qEdSquULZRv7akHIE67Uo="
        strServiceName = "datamart"
        strPort = "1522"
    elif strConnection == "1SRC-taipei_dc@sh-oracle11g-234prod":
        strHost = "10.0.0.234"
        strUser = "taipei_dc"
        strPasswd = "qUJMprHO215hZthdpGCvrqkrRj4HyYAJpqAW6K1zLvg="
        strServiceName = "datamart"
        strPort = "1521"

    dictPermission = {"strHost": strHost, "strUser": strUser, "strPasswd": Security.decrypt(strPasswd), "strServiceName": strServiceName, "strPort": strPort}
    return dictPermission

def getOracleSQLCommand(strSQL, dictParameter):
    strSQLCommand = strSQL

    if dictParameter != None:
        for strParameterKey in dictParameter:
            entryParameter = dictParameter[strParameterKey]
            entryParameter.setParameterKey(strParameterKey)
            strSQLCommand = strSQLCommand.replace("{" + strParameterKey + "}", entryParameter.getSQLCommand())

    return strSQLCommand

def getOracleDataList(strConnection, strSQL):
    dictPermission = getOraclePermission(strConnection)

    strConnection = "{0}/{1}@{2}:{3}/{4}".format(
        dictPermission["strUser"], dictPermission["strPasswd"], dictPermission["strHost"], dictPermission["strPort"], dictPermission["strServiceName"]
    )

    connect = cx_Oracle.connect(strConnection)
    cursor = connect.cursor()
    cursor.execute(strSQL)
    listData = Common.getFetchAllList(cursor)
    cursor.close()
    connect.close()

    return listData
