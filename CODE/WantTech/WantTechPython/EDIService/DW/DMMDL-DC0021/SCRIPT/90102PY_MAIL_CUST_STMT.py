import sys
import logging
import xlsxwriter
from Utility import Common
from Utility import Message
from Entity import DBEntity
from Entity import MariaEntity
from EDI import EDIEntity

def getCustStmtList(strEDIConnection, strEDIDB, strDataDate):
    strSQL = "SELECT SALES_CREDIT_ID, SALES_CREDIT_DESC " + \
             "     , WANT_COM_NM, SALES_OFF_NM " + \
             "     , (TODAY_AMT/1000) AS TODAY_AMT " + \
             "     , (BAL_BEGIN/1000) AS BAL_BEGIN " + \
             "     , (CUM_AMT/1000) AS CUM_AMT " + \
             "     , (SALES_AMT/1000) AS SALES_AMT " + \
             "     , (BAL_END/1000) AS BAL_END " + \
             "FROM DMMDL.DC0021_CUST_STMT " + \
             "WHERE {DATA_DATE} AND RPT_YM=SUBSTR(DATA_DATE, 1, 6) " + \
             "ORDER BY SALES_CREDIT_ID, WANT_COM_ID, SALES_OFF_ID; "

    dictMariaParameter = {
        "DATA_DATE": MariaEntity.MariaParameter(strOperator="=", objValue=strDataDate, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listCustStmt = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listCustStmt

def execWriteWorkbook(strJobPathRES, listCustStmt):
    if len(listCustStmt) == 0:
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
        objExcelRowRightFormat.set_num_format('#,##0.00000')

        objExcelRow = 0
        objExcelWorksheet = objExcelWorkbook.add_worksheet("批发客户账余报表")

        objExcelWorksheet.set_default_row(20)

        objExcelWorksheet.set_column(0, 0, 12)
        objExcelWorksheet.set_column(1, 1, 22)
        objExcelWorksheet.set_column(2, 2, 12)
        objExcelWorksheet.set_column(3, 3, 15)
        objExcelWorksheet.set_column(4, 4, 15)
        objExcelWorksheet.set_column(5, 5, 15)
        objExcelWorksheet.set_column(6, 6, 15)
        objExcelWorksheet.set_column(7, 7, 15)
        objExcelWorksheet.set_column(8, 8, 15)
        objExcelWorksheet.set_column(9, 9, 15)

        objExcelWorksheet.write(objExcelRow, 0, "信用控制范围", objExcelColumnFormat)
        objExcelWorksheet.write(objExcelRow, 1, "信用控制范围描述", objExcelColumnFormat)
        objExcelWorksheet.write(objExcelRow, 2, "旺旺销售公司", objExcelColumnFormat) 
        objExcelWorksheet.write(objExcelRow, 3, "营业所", objExcelColumnFormat)
        objExcelWorksheet.write(objExcelRow, 4, "当天入金", objExcelColumnFormat)
        objExcelWorksheet.write(objExcelRow, 5, "期初", objExcelColumnFormat)
        objExcelWorksheet.write(objExcelRow, 6, "当月累计入金", objExcelColumnFormat)
        objExcelWorksheet.write(objExcelRow, 7, "当月销退金额", objExcelColumnFormat)
        objExcelWorksheet.write(objExcelRow, 8, "期末", objExcelColumnFormat)
        objExcelWorksheet.write(objExcelRow, 9, "单位：千元")
        objExcelRow += 1

        for dictCustStmt in listCustStmt:
            objExcelWorksheet.write(objExcelRow, 0, dictCustStmt["SALES_CREDIT_ID"], objExcelRowCenterFormat)
            objExcelWorksheet.write(objExcelRow, 1, dictCustStmt["SALES_CREDIT_DESC"], objExcelRowLeftFormat)
            objExcelWorksheet.write(objExcelRow, 2, dictCustStmt["WANT_COM_NM"], objExcelRowCenterFormat)
            objExcelWorksheet.write(objExcelRow, 3, dictCustStmt["SALES_OFF_NM"], objExcelRowLeftFormat)
            objExcelWorksheet.write(objExcelRow, 4, dictCustStmt["TODAY_AMT"], objExcelRowRightFormat)
            objExcelWorksheet.write(objExcelRow, 5, dictCustStmt["BAL_BEGIN"], objExcelRowRightFormat)
            objExcelWorksheet.write(objExcelRow, 6, dictCustStmt["CUM_AMT"], objExcelRowRightFormat)
            objExcelWorksheet.write(objExcelRow, 7, dictCustStmt["SALES_AMT"], objExcelRowRightFormat)
            objExcelWorksheet.write(objExcelRow, 8, dictCustStmt["BAL_END"], objExcelRowRightFormat)
            objExcelWorksheet.write(objExcelRow, 9, "")
            objExcelRow += 1

        objExcelWorkbook.close()
        return True

def execMailCustStmt(strJobPathRES, strDataDate):
    strEDIConnection = "3DW-DWuser@tpe-centos7-maria10-dw"
    strEDIDB = "DMMDL"

    listCustStmt = getCustStmtList(strEDIConnection, strEDIDB, strDataDate)

    if execWriteWorkbook(strJobPathRES, listCustStmt) == True:
        strMessageSMTPServer = "tw-mail02.want-want.com"
        strMessageSMTPFrom = "Data.Center@want-want.com"
        arrayMessageSMTPTo = [
            "Xie_Wei3@want-want.com",
            "Yan_HongMei@want-want.com",
            "Zoe.Hsu@want-want.com"
        ]
        strMessageSubject = "[测试]批发客户账余报表-%s" % strDataDate
        strAttachFileName = "[测试]批发客户账余报表-%s.xlsx" % strDataDate

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

    execMailCustStmt(strJobPathRES, strDataDate)

if __name__ == "__main__":
    main()
