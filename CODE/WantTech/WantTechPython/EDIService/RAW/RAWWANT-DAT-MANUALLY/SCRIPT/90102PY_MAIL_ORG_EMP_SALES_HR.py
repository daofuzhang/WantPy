import sys
import logging
from Utility import Message
from EDI import EDIEntity

def main():
    strLoggerName = sys.argv[1]

    strEDIConnection = sys.argv[2]
    strEDIDB = sys.argv[3]
    strEDINo = sys.argv[4]
    strJobPathRES = sys.argv[5]
    strDependOnJobPathRES = sys.argv[6]

    # logger = logging.getLogger(strLoggerName)
    # logger.info(str(sys.argv))

    dictFlow = EDIEntity.getFlow(strEDIConnection, strEDIDB, strEDINo)
    strDataDate = dictFlow["DATA_DATE"]

    strMessageSMTPServer = "tw-mail02.want-want.com"
    strMessageSMTPFrom = "zoe.hsu@want-want.com"
    arrayMessageSMTPTo = [
        "zoe.hsu@want-want.com",
        "daniel.chen@want-want.com"
    ]
    strMessageSubject = "[测试] 业务人员花名册-%s" % strDataDate
    strAttachFileName = "[测试] 业务人员花名册-%s.xls" % strDataDate

    arrayColumnTitle = [
        "员工号",
        "姓名",
        "人事范围",
        "人事子范围",
        "雇佣日期",
        "部门名称",
        "三级部门",
        "四级部门",
        "五级部门",
        "六级部门",
        "七级部门",
        "八级部门",
        "职位代码",
        "职位",
        "职位属性",
        "职位类型",
        "职位区域注记",
        "职位注记",
        "职务",
        "职等",
        "性别",
        "年资",
    ]

    with open(strDependOnJobPathRES, "r") as fileOriginal: 
        objData = fileOriginal.read()

    with open(strJobPathRES, "w") as fileTarget: 
        fileTarget.write(",".join(arrayColumnTitle) + "\n" + objData)

    Message.sendSMTPMail(strMessageSMTPServer, strMessageSMTPFrom, arrayMessageSMTPTo, strMessageSubject, "", strJobPathRES, strAttachFileName)

if __name__ == "__main__":
    main()
