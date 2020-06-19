import sys
import logging
from Utility import Common
from Utility import Message
from EDI import EDIEntity

def execMailServerNotice():
    strMessageSMTPServer = "tw-mail02.want-want.com"
    strMessageSMTPFrom = "Data.Center@want-want.com"
    arrayMessageSMTPTo = [
        "Jonsan.Chuang@want-want.com",
        "Zoe.Hsu@want-want.com"
    ]
    strMessageSubject = "!!!!! Connect to tw-mail02.want-want.com Success !!!!!"

    Message.sendSMTPMail(strMessageSMTPServer, strMessageSMTPFrom, arrayMessageSMTPTo, strMessageSubject, "", None, None)
    return True

def main():
    # strLoggerName = sys.argv[1]

    # strEDIConnection = sys.argv[2]
    # strEDIDB = sys.argv[3]
    # strEDINo = sys.argv[4]

    # strJobPathRES = sys.argv[5]
    # strDependOnJobPathRES = sys.argv[6]

    # Common.setLogging(strLoggerName)
    # logger = logging.getLogger(strLoggerName)

    # dictFlow = EDIEntity.getFlow(strEDIConnection, strEDIDB, strEDINo)
    # strDataDate = dictFlow["DATA_DATE"]

    execMailServerNotice()

if __name__ == "__main__":
    main()
