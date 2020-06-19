import datetime, time, os, numpy
from Utility import Common

class Job:
    intSkipCount = 0
    intLimitCount = 0
    strFileName = ""

    def __init__(self, intSkipCount, intLimitCount, strFileName):
        self.intSkipCount = intSkipCount
        self.intLimitCount = intLimitCount
        self.strFileName = strFileName

    def execAction(self):
        time.sleep(1)
        os.system("mongo --eval \"" +
                  "var _evalSkipCount=" + str(self.intSkipCount) + "; " +
                  "var _evalLimitCount=" + str(self.intLimitCount) + "; " +
                  "\" " + self.strFileName + ".js")

def execJob(*args):
    queueJob = args[0]
    arrayFinished = args[1]
    intBreakSize = args[2]
    while queueJob.qsize() > 0:
        jobNow = queueJob.get()
        jobNow.execAction()
        arrayFinished.append(intBreakSize)
        print(Common.getDatetimeString(datetime.datetime.now()) + str(numpy.sum(arrayFinished)))
