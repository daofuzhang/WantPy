import os

def getCurrentFileExtension(strFile):
    return os.path.splitext(strFile)[1]

def getCurrentFileName(strFilePath):
    strCurrentFileName = os.path.basename(strFilePath)
    strCurrentFileName = os.path.splitext(strCurrentFileName)[0]
    return strCurrentFileName

def getCurrentFileNameExtension(strFilePath):
    strFileName = os.path.basename(strFilePath)
    return strFileName

def getCurrentFileNamePath(strFile):
    return os.path.splitext(strFile)[0]

def getCurrentFileDirectoryPath(strFilePath):
    strDirectoryPath = os.path.join(os.path.dirname(os.path.abspath(strFilePath)), "")
    return strDirectoryPath

def getSpecialExtensionFileNameList(strInputPath, listExtension):
    listSpecialExtensionFile = []
    for f in os.listdir(strInputPath):
        if os.path.splitext(f)[1] in listExtension:
            listSpecialExtensionFile.append(f)
    return listSpecialExtensionFile

def readFileBlocks(streamFile, intSize):
    while True:
        blocks = streamFile.read(intSize)
        if not blocks: break
        yield blocks

def getFileLineCount(strFilePath, intSize):
    intCount = 0
    with open(strFilePath, mode="r", encoding="utf-8", errors="ignore") as streamFile:
        intCount = sum(blocks.count("\n") for blocks in readFileBlocks(streamFile, intSize))
    return intCount
