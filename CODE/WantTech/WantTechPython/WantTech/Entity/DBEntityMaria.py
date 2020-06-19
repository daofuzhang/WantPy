import pymysql
import pandas 
from Utility import Common
from Utility import Security

def getMariaExportConnectionString(strConnection):
    strPassword = ""
    strReturn = ""

    if strConnection == "1SRC-DCreader@aws-mysql57-ka-prod-slave":
        strPassword = "3dQq6ir0aSN2+AfyK2E3BWpzBP+WIfn0D4AOTELDV0Aue6nJ3Gd6zcNj6QAejy5G"
        strReturn = "mysql -h 10.128.83.245 -uDCreader -p%s"

    elif strConnection == "2RAW-RAWreader@tpe-centos7-maria10-raw":
        strPassword = "l1l8ayJitRrS8eQs6JUD/WbtG2Ypw1mUtYqXZxZYVpo="
        strReturn = "mysql -h 10.231.8.163 -uRAWreader -p%s"

    elif strConnection == "2RAW-RAWuser@tpe-centos7-maria10-raw":
        strPassword = "qAofc+PM+7emuFPaeJlUFk1yRasFT5fDW8pF8RhvXvs="
        strReturn = "mysql -h 10.231.8.163 -uRAWuser -p%s"

    elif strConnection == "3DW-DWreader@tpe-centos7-maria10-dw":
        strPassword = "FT0E5P65l70CKMOlsjy0OuALJxgZAQHOmW/tF+9SCK4="
        strReturn = "mysql -h 10.231.8.164 -uDWreader -p%s"

    elif strConnection == "3DW-DWuser@tpe-centos7-maria10-dw":
        strPassword = "iV2Qw8WFWrBx0rWELvs5a8NwyhnkIToX42wXUPXRWWg="
        strReturn = "mysql -h 10.231.8.164 -uDWuser -p%s"

    elif strConnection == "4DM-DMreader@tpe-centos7-maria10-dm":
        strPassword = "dlUxqqtYrjf83sLtvkOmbCmaw3b5sFCQwfA4s0Zao1s="
        strReturn = "mysql -h 10.231.8.165 -uDMreader -p%s"

    elif strConnection == "4DM-DMuser@tpe-centos7-maria10-dm":
        strPassword = "dlUxqqtYrjf83sLtvkOmbCmaw3b5sFCQwfA4s0Zao1s="
        strReturn = "mysql -h 10.231.8.165 -uDMuser -p%s"

    elif strConnection == "5AP1-APreader@tpe-centos7-maria10-ap1":
        strPassword = "Q7NjNOiYBT8fuAkMeDCSad7zKkv7MUOs8va7OLfOxYg="
        strReturn = "mysql -h 10.231.8.166 -uAPreader -p%s"

    elif strConnection == "5AP1-APuser@tpe-centos7-maria10-ap1":
        strPassword = "KiANuT5d/kQYcgwj4wSGYLABUyfutIxqGwTfTxfoKVU="
        strReturn = "mysql -h 10.231.8.166 -uAPuser -p%s"

    return (strReturn % Security.decrypt(strPassword))

def getMariaImportConnectionString(strConnection):
    strPassword = ""
    strReturn = ""

    if strConnection == "1SRC-DCreader@aws-mysql57-ka-prod-slave":
        strPassword = "3dQq6ir0aSN2+AfyK2E3BWpzBP+WIfn0D4AOTELDV0Aue6nJ3Gd6zcNj6QAejy5G"
        strReturn = "mysqlimport -h 10.128.83.245 -uDCreader -p%s"

    elif strConnection == "2RAW-RAWreader@tpe-centos7-maria10-raw":
        strPassword = "l1l8ayJitRrS8eQs6JUD/WbtG2Ypw1mUtYqXZxZYVpo="
        strReturn = "mysqlimport -h 10.231.8.163 -uRAWreader -p%s"

    elif strConnection == "2RAW-RAWuser@tpe-centos7-maria10-raw":
        strPassword = "qAofc+PM+7emuFPaeJlUFk1yRasFT5fDW8pF8RhvXvs="
        strReturn = "mysqlimport -h 10.231.8.163 -uRAWuser -p%s"

    elif strConnection == "3DW-DWreader@tpe-centos7-maria10-dw":
        strPassword = "FT0E5P65l70CKMOlsjy0OuALJxgZAQHOmW/tF+9SCK4="
        strReturn = "mysqlimport -h 10.231.8.164 -uDWreader -p%s"

    elif strConnection == "3DW-DWuser@tpe-centos7-maria10-dw":
        strPassword = "iV2Qw8WFWrBx0rWELvs5a8NwyhnkIToX42wXUPXRWWg="
        strReturn = "mysqlimport -h 10.231.8.164 -uDWuser -p%s"

    elif strConnection == "4DM-DMreader@tpe-centos7-maria10-dm":
        strPassword = "dlUxqqtYrjf83sLtvkOmbCmaw3b5sFCQwfA4s0Zao1s="
        strReturn = "mysqlimport -h 10.231.8.165 -uDMreader -p%s"

    elif strConnection == "4DM-DMuser@tpe-centos7-maria10-dm":
        strPassword = "dlUxqqtYrjf83sLtvkOmbCmaw3b5sFCQwfA4s0Zao1s="
        strReturn = "mysqlimport -h 10.231.8.165 -uDMuser -p%s"

    elif strConnection == "5AP1-APreader@tpe-centos7-maria10-ap1":
        strPassword = "Q7NjNOiYBT8fuAkMeDCSad7zKkv7MUOs8va7OLfOxYg="
        strReturn = "mysqlimport -h 10.231.8.166 -uAPreader -p%s"

    elif strConnection == "5AP1-APuser@tpe-centos7-maria10-ap1":
        strPassword = "KiANuT5d/kQYcgwj4wSGYLABUyfutIxqGwTfTxfoKVU="
        strReturn = "mysqlimport -h 10.231.8.166 -uAPuser -p%s"

    return (strReturn % Security.decrypt(strPassword))

def getMariaPermission(strConnection):
    strHost = ""
    strUser = ""
    strPasswd = ""
    dictPermission = dict()

    if strConnection == "1SRC-DCreader@aws-mysql57-ka-prod-slave":
        strHost = "10.128.83.245"
        strUser = "DCreader"
        strPasswd = "3dQq6ir0aSN2+AfyK2E3BWpzBP+WIfn0D4AOTELDV0Aue6nJ3Gd6zcNj6QAejy5G"

    elif strConnection == "2RAW-RAWreader@tpe-centos7-maria10-raw":
        strHost = "10.231.8.163"
        strUser = "RAWreader"
        strPasswd = "l1l8ayJitRrS8eQs6JUD/WbtG2Ypw1mUtYqXZxZYVpo="

    elif strConnection == "2RAW-RAWuser@tpe-centos7-maria10-raw":
        strHost = "10.231.8.163"
        strUser = "RAWuser"
        strPasswd = "qAofc+PM+7emuFPaeJlUFk1yRasFT5fDW8pF8RhvXvs="

    elif strConnection == "3DW-DWreader@tpe-centos7-maria10-dw":
        strHost = "10.231.8.164"
        strUser = "DWreader"
        strPasswd = "FT0E5P65l70CKMOlsjy0OuALJxgZAQHOmW/tF+9SCK4="

    elif strConnection == "3DW-DWuser@tpe-centos7-maria10-dw":
        strHost = "10.231.8.164"
        strUser = "DWuser"
        strPasswd = "iV2Qw8WFWrBx0rWELvs5a8NwyhnkIToX42wXUPXRWWg="

    elif strConnection == "4DM-DMreader@tpe-centos7-maria10-dm":
        strHost = "10.231.8.165"
        strUser = "DMreader"
        strPasswd = "dlUxqqtYrjf83sLtvkOmbCmaw3b5sFCQwfA4s0Zao1s="

    elif strConnection == "4DM-DMuser@tpe-centos7-maria10-dm":
        strHost = "10.231.8.165"
        strUser = "DMuser"
        strPasswd = "dlUxqqtYrjf83sLtvkOmbCmaw3b5sFCQwfA4s0Zao1s="

    elif strConnection == "5AP1-APreader@tpe-centos7-maria10-ap1":
        strHost = "10.231.8.166"
        strUser = "APreader"
        strPasswd = "Q7NjNOiYBT8fuAkMeDCSad7zKkv7MUOs8va7OLfOxYg="

    elif strConnection == "5AP1-APuser@tpe-centos7-maria10-ap1":
        strHost = "10.231.8.166"
        strUser = "APuser"
        strPasswd = "KiANuT5d/kQYcgwj4wSGYLABUyfutIxqGwTfTxfoKVU="

    dictPermission = {"strHost": strHost, "strUser": strUser, "strPasswd": Security.decrypt(strPasswd)}
    return dictPermission

def getMariaSQLCommand(strSQL, dictParameter):
    strSQLCommand = strSQL

    if dictParameter != None:
        for strParameterKey in dictParameter:
            entryParameter = dictParameter[strParameterKey]
            entryParameter.setParameterKey(strParameterKey)
            strSQLCommand = strSQLCommand.replace("{" + strParameterKey + "}", entryParameter.getSQLCommand())

    return strSQLCommand

def getMariaDataList(strConnection, strDB, strSQL):
    dictPermission = getMariaPermission(strConnection)

    connect = pymysql.connect(host=dictPermission["strHost"], user=dictPermission["strUser"],
                              passwd=dictPermission["strPasswd"], db=strDB, charset="utf8")
    cursor = connect.cursor()
    cursor.execute(strSQL)
    listData = Common.getFetchAllList(cursor)
    cursor.close()
    connect.close()

    return listData

def getMariaDataFrame(strConnection, strDB, strSQL):
    dictPermission = getMariaPermission(strConnection)

    connect = pymysql.connect(host=dictPermission["strHost"], user=dictPermission["strUser"],
                              passwd=dictPermission["strPasswd"], db=strDB, charset="utf8")
    cursor = connect.cursor()
    cursor.execute(strSQL)
    listDataFrame = Common.getFetchAllList(cursor)
    listDataFrame = pandas.DataFrame(listDataFrame)
    cursor.close()
    connect.close()

    return listDataFrame   

def executeMariaData(strConnection, strDB, strSQL):
    dictPermission = getMariaPermission(strConnection)

    connect = pymysql.connect(host=dictPermission["strHost"], user=dictPermission["strUser"],
                              passwd=dictPermission["strPasswd"], db=strDB, charset="utf8")
    cursor = connect.cursor()
    cursor.execute(strSQL)
    connect.commit()
    cursor.close()
    connect.close()

    return True

def executeMariaProcedure(strConnection, strDB, strProcName, arrayArguments):
    dictPermission = getMariaPermission(strConnection)

    connect = pymysql.connect(host=dictPermission["strHost"], user=dictPermission["strUser"],
                              passwd=dictPermission["strPasswd"], db=strDB, charset="utf8")
    cursor = connect.cursor()
    cursor.callproc(strProcName, arrayArguments)
    cursor.execute("SELECT @_" + strProcName + "_" + str(len(arrayArguments) - 1) + " AS SP_RESULT;")
    listData = Common.getFetchAllList(cursor)
    cursor.close()
    connect.close()

    return listData[0]["SP_RESULT"]
