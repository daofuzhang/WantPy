import pyhdb
from Utility import Common
from Utility import Security

def getHanaExportConnectionString(strConnection):
    strPassword = ""
    strReturn = ""

    if strConnection == "1SRC-BW2DC@sh-hana-test":
        strPassword = "UnyhsyrYCnSC0ylMSQ9N/ekaW8/hjo3qcY+hJUsuB9A="
        strReturn = "hdbsql -n 10.0.0.27:30015 -i 00 -u BW2DC -p \"%s\""
    elif strConnection == "1SRC-BW2DC2@sh-hana-prod":
        strPassword = "Mo/AsK+FslcRiMqUh0s7IAcMkQe12Tn4dQsirwhVK0Q="
        strReturn = "hdbsql -n 10.0.1.52:30015 -i 00 -u BW2DC2 -p \"%s\""
    elif strConnection == "1SRC-BW2DCHR@sh-hana-prod":
        strPassword = "cH9sO4w8ZUyTH8CjIW6Ar8TIJLan2nz/ImKzVPMlEAw="
        strReturn = "hdbsql -n 10.0.1.52:30015 -i 00 -u BW2DCHR -p \"%s\""

    return (strReturn % Security.decrypt(strPassword))

def getHanaPermission(strConnection):
    strHost = ""
    strUser = ""
    strPassword = ""
    dictPermission = dict()

    if strConnection == "1SRC-BW2DC@sh-hana-test":
        strHost = "10.0.0.27"
        strUser = "BW2DC"
        strPassword = "UnyhsyrYCnSC0ylMSQ9N/ekaW8/hjo3qcY+hJUsuB9A="
    elif strConnection == "1SRC-BW2DC2@sh-hana-prod":
        strHost = "10.0.1.52"
        strUser = "BW2DC2"
        strPassword = "Mo/AsK+FslcRiMqUh0s7IAcMkQe12Tn4dQsirwhVK0Q="
    elif strConnection == "1SRC-BW2DCHR@sh-hana-prod":
        strHost = "10.0.1.52"
        strUser = "BW2DCHR"
        strPassword = "cH9sO4w8ZUyTH8CjIW6Ar8TIJLan2nz/ImKzVPMlEAw="

    dictPermission = {"strHost": strHost, "strUser": strUser, "strPassword": Security.decrypt(strPassword)}
    return dictPermission

def getHanaSQLCommand(strConnection, strSQL, dictParameter):
    strSQLCommand = strSQL

    if dictParameter != None:
        for strParameterKey in dictParameter:
            entryParameter = dictParameter[strParameterKey]
            entryParameter.setParameterKey(strParameterKey)
            strSQLCommand = strSQLCommand.replace("{" + strParameterKey + "}", entryParameter.getSQLCommand())

    if strConnection == "1SRC-BW2DC@sh-hana-test":
        strSQLCommand = strSQLCommand.replace("SAPBHP", "SAPBHD")

    return strSQLCommand

def getHanaDataList(strConnection, strSQL):
    dictPermission = getHanaPermission(strConnection)

    connect = pyhdb.connect(host=dictPermission["strHost"], port=30015,
                            user=dictPermission["strUser"], password=dictPermission["strPassword"])
    cursor = connect.cursor()
    cursor.execute(strSQL)
    listData = Common.getFetchAllList(cursor)
    cursor.close()
    connect.close()

    return listData
