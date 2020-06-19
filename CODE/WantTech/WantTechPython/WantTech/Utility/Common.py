import os
import logging
import json
from datetime import datetime

def getFetchAllList(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def getDatetimeString(datetimeValue):
    try:
        return datetimeValue.strftime("%Y/%m/%d %H:%M:%S.%f")[:-3]
    except ValueError:
        return None

def getDateString(datetimeValue):
    try:
        return datetimeValue.strftime("%Y/%m/%d")
    except ValueError:
        return None

def formatDateString(strValue):
    try:
        return datetime.strptime(strValue, "%Y%m%d").strftime("%Y/%m/%d")
    except ValueError:
        return None

def getDateSimple(datetimeValue):
    try:
        return datetimeValue.strftime("%Y%m%d")
    except ValueError:
        return None

def getTimeSimple(datetimeValue):
    try:
        return datetimeValue.strftime("%H%M%S%f")[:-3]
    except ValueError:
        return None

def getDateTime(strDateTimeString):
    try:
        return datetime.strptime(strDateTimeString, "%Y/%m/%d %H:%M:%S.%f")
    except ValueError:
        return None

def getDate(strDateString):
    try:
        return datetime.strptime(strDateString, "%Y%m%d")
    except ValueError:
        return None

def getLogDirectoryName():
    return "log"

def setLogging(strLogName):
    strDirectory = getLogDirectoryName()
    if not os.path.exists(strDirectory):
        os.makedirs(strDirectory)

    strNowLogDate = getDateSimple(datetime.now())

    logger = logging.getLogger(strLogName)
    logger.level = logging.INFO

    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    strFileName = getLogDirectoryName() + "/" + strLogName + "." + strNowLogDate + ".log"
    handler = logging.FileHandler(strFileName, "a", "utf-8")
    formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return strNowLogDate

def loadJsonFile(strJsonName):
    jsonReturn = None
    with open(strJsonName, "r", encoding="utf8") as fileJson:
        jsonReturn = json.load(fileJson)
    return jsonReturn

def writeJsonFile(strJsonName, jsonContent):
    with open(strJsonName, "w", encoding="utf8") as fileJson:
        json.dump(jsonContent, fileJson, ensure_ascii=False)
    return True

def filterJsonListFirst(jsonList, strFilterKey, strFilterValue):
    jsonReturnObject = None
    for jsonNowObject in jsonList:
        if jsonNowObject[strFilterKey] == strFilterValue:
            jsonReturnObject = jsonNowObject
    return jsonReturnObject

def filterJsonListAll(jsonList, strFilterKey, strFilterValue):
    jsonReturnObjectList = []
    for jsonNowObject in jsonList:
        if jsonNowObject[strFilterKey] == strFilterValue:
            jsonReturnObjectList.append(jsonNowObject)
    return jsonReturnObjectList
