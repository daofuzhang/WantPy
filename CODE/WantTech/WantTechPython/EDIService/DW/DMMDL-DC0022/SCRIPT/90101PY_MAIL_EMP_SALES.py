import sys
import logging
import xlsxwriter
from Utility import Common
from Utility import Message
from Entity import DBEntity
from Entity import MariaEntity
from EDI import EDIEntity

def getEMPSalesList(strEDIConnection, strEDIDB, strDataDate):
    strSQL = "SELECT EMP_ID, EMP_NM, EMP_GENDER_NM " + \
             "     , ONBOARD_YMD, SENIORITY " + \
             "     , HR_COM_NM, HR_OFF_NM " + \
             "     , EMP_POS_NM, EMP_POS_PROP_NM, EMP_POS_TYPE_NM, EMP_POS_FLAG " + \
             "     , EMP_POS_TITLE_NM, EMP_POS_LEVEL_ID, EMP_POS_LEVEL_NM " + \
             "FROM DMMDL.DC0022_EMP_SALES " + \
             "WHERE {DATA_DATE} " + \
             "ORDER BY EMP_POS_PROP_ID, HR_COM_ID, HR_OFF_ID, EMP_POS_LEVEL_ID; "

    dictMariaParameter = {
        "DATA_DATE": MariaEntity.MariaParameter(strOperator="=", objValue=strDataDate, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listEMPSales = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listEMPSales

def execWriteWorkbook(strJobPathRES, listEMPSales):
    if len(listEMPSales) == 0:
        return False
    else:
        objExcelWorkbook = None
        objExcelWorksheet = None
        
        objExcelWorkbook = xlsxwriter.Workbook(strJobPathRES)

        objExcelColumnFormat = objExcelWorkbook.add_format({
            "bold": 1, "align": "center", "valign": "vcenter", "font_size": 11, "font_color": "#FFFFFF", 
            "fg_color": "#305496", 
            "border": 0})

        objExcelRowCenterFormat = objExcelWorkbook.add_format({
            "bold": 1, "align": "center", "valign": "vcenter", "font_size": 11, "font_color": "#000000",
            "border": 0})
        objExcelRowLeftFormat = objExcelWorkbook.add_format({
            "bold": 1, "align": "left", "valign": "vcenter", "font_size": 11, "font_color": "#000000",
            "border": 0})
        objExcelRowRightFormat = objExcelWorkbook.add_format({
            "bold": 1, "align": "right", "valign": "vcenter", "font_size": 11, "font_color": "#000000",
            "border": 0})
        objExcelRowRightFormat.set_num_format("0.00")

        objExcelRow = 0
        objExcelWorksheet = objExcelWorkbook.add_worksheet("业务人员花名册")

        objExcelWorksheet.set_default_row(20)

        objExcelWorksheet.set_column(0, 0, 10)
        objExcelWorksheet.set_column(1, 1, 10)
        objExcelWorksheet.set_column(2, 2, 6)
        objExcelWorksheet.set_column(3, 3, 15)
        objExcelWorksheet.set_column(4, 4, 8)
        objExcelWorksheet.set_column(5, 5, 15)
        objExcelWorksheet.set_column(6, 6, 15)
        objExcelWorksheet.set_column(7, 7, 18)
        objExcelWorksheet.set_column(8, 8, 18)
        objExcelWorksheet.set_column(9, 9, 15)
        objExcelWorksheet.set_column(10, 10, 10)
        objExcelWorksheet.set_column(11, 11, 15)
        objExcelWorksheet.set_column(12, 12, 10)
        objExcelWorksheet.set_column(13, 13, 6)

        objExcelWorksheet.write(objExcelRow, 0, "人员编号", objExcelColumnFormat)
        objExcelWorksheet.write(objExcelRow, 1, "人员姓名", objExcelColumnFormat) 
        objExcelWorksheet.write(objExcelRow, 2, "性别", objExcelColumnFormat)
        objExcelWorksheet.write(objExcelRow, 3, "加入日期", objExcelColumnFormat)
        objExcelWorksheet.write(objExcelRow, 4, "年资", objExcelColumnFormat)
        objExcelWorksheet.write(objExcelRow, 5, "所属部门", objExcelColumnFormat)
        objExcelWorksheet.write(objExcelRow, 6, "分公司", objExcelColumnFormat)
        objExcelWorksheet.write(objExcelRow, 7, "营业所", objExcelColumnFormat)
        objExcelWorksheet.write(objExcelRow, 8, "职位", objExcelColumnFormat)
        objExcelWorksheet.write(objExcelRow, 9, "职位类型", objExcelColumnFormat)
        objExcelWorksheet.write(objExcelRow, 10, "职位注记", objExcelColumnFormat)
        objExcelWorksheet.write(objExcelRow, 11, "职务", objExcelColumnFormat)
        objExcelWorksheet.write(objExcelRow, 12, "职等编号", objExcelColumnFormat)
        objExcelWorksheet.write(objExcelRow, 13, "职等", objExcelColumnFormat)
        objExcelRow += 1

        for dictEMPSales in listEMPSales:
            objExcelWorksheet.write(objExcelRow, 0, dictEMPSales["EMP_ID"], objExcelRowCenterFormat)
            objExcelWorksheet.write(objExcelRow, 1, dictEMPSales["EMP_NM"], objExcelRowLeftFormat)
            objExcelWorksheet.write(objExcelRow, 2, dictEMPSales["EMP_GENDER_NM"], objExcelRowCenterFormat)
            objExcelWorksheet.write(objExcelRow, 3, Common.formatDateString(dictEMPSales["ONBOARD_YMD"]), objExcelRowCenterFormat)
            objExcelWorksheet.write(objExcelRow, 4, dictEMPSales["SENIORITY"], objExcelRowRightFormat)
            objExcelWorksheet.write(objExcelRow, 5, dictEMPSales["EMP_POS_PROP_NM"], objExcelRowLeftFormat)
            objExcelWorksheet.write(objExcelRow, 6, dictEMPSales["HR_COM_NM"], objExcelRowLeftFormat)
            objExcelWorksheet.write(objExcelRow, 7, dictEMPSales["HR_OFF_NM"], objExcelRowLeftFormat)
            objExcelWorksheet.write(objExcelRow, 8, dictEMPSales["EMP_POS_NM"], objExcelRowLeftFormat)
            objExcelWorksheet.write(objExcelRow, 9, dictEMPSales["EMP_POS_TYPE_NM"], objExcelRowLeftFormat)
            objExcelWorksheet.write(objExcelRow, 10, dictEMPSales["EMP_POS_FLAG"], objExcelRowCenterFormat)
            objExcelWorksheet.write(objExcelRow, 11, dictEMPSales["EMP_POS_TITLE_NM"], objExcelRowLeftFormat)
            objExcelWorksheet.write(objExcelRow, 12, dictEMPSales["EMP_POS_LEVEL_ID"], objExcelRowCenterFormat)
            objExcelWorksheet.write(objExcelRow, 13, dictEMPSales["EMP_POS_LEVEL_NM"], objExcelRowCenterFormat)
            objExcelRow += 1

        objExcelWorkbook.close()
        return True

def execMailEMPSales(strJobPathRES, strDataDate):
    strEDIConnection = "3DW-DWuser@tpe-centos7-maria10-dw"
    strEDIDB = "DMMDL"

    listEMPSales = getEMPSalesList(strEDIConnection, strEDIDB, strDataDate)

    if execWriteWorkbook(strJobPathRES, listEMPSales) == True:
        strMessageSMTPServer = "tw-mail02.want-want.com"
        strMessageSMTPFrom = "Data.Center@want-want.com"
        arrayMessageSMTPTo = [
            "Guo_Yan@want-want.com",
            "Miao_Qi@want-want.com",
            "Zhu_HongMei@want-want.com",
            "Wang_Wenyu@want-want.com",
            "Teng_Yun@want-want.com",
            "Yu_HuiJing@want-want.com",
            "Ou_XiaoJing@want-want.com",
            "Liang_WenLing@want-want.com",
            "Wang_Xue@want-want.com",
            "Xu_QiuWen@want-want.com",
            "Zoe.Hsu@want-want.com"
        ]
        strMessageSubject = "业务人员花名册-%s" % strDataDate
        strAttachFileName = "业务人员花名册-%s.xlsx" % strDataDate

        Message.sendSMTPMail(strMessageSMTPServer, strMessageSMTPFrom, arrayMessageSMTPTo, strMessageSubject, "", strJobPathRES, strAttachFileName)
        return True
    else:
        return False

def main():
    strLoggerName = sys.argv[1]

    strEDIConnection = sys.argv[2]
    strEDIDB = sys.argv[3]
    strEDINo = sys.argv[4]

    strJobPathRES = sys.argv[5]
    # strDependOnJobPathRES = sys.argv[6]

    Common.setLogging(strLoggerName)
    # logger = logging.getLogger(strLoggerName)

    dictFlow = EDIEntity.getFlow(strEDIConnection, strEDIDB, strEDINo)
    strDataDate = dictFlow["DATA_DATE"]

    execMailEMPSales(strJobPathRES, strDataDate)

if __name__ == "__main__":
    main()
