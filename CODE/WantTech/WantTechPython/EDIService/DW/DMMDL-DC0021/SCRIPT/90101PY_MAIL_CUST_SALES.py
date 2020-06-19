import sys
import logging
import xlsxwriter
from Utility import Common
from Utility import Message
from Entity import DBEntity
from Entity import MariaEntity
from EDI import EDIEntity

def getCustSalesList(strEDIConnection, strEDIDB, strDataDate):
    strSQL = "SELECT WANT_CHAN_NM, WANT_COM_NM " + \
             "     , PROD_H1_NM, PROD_H2_NM, PROD_H3_NM " + \
             "     , (POSTED_AMT_LAST_ALL/1000) AS POSTED_AMT_LAST_ALL " + \
             "     , (POSTED_AMT_LAST/1000) AS POSTED_AMT_LAST " + \
             "     , (POSTED_AMT_THIS/1000) AS POSTED_AMT_THIS " + \
             "     , (POSTING_AMT/1000) AS POSTING_AMT " + \
             "FROM DMMDL.DC0021_CUST_SALES " + \
             "WHERE {DATA_DATE} AND RPT_YM=SUBSTR(DATA_DATE, 1, 6) " + \
             "ORDER BY WANT_CHAN_ID, WANT_COM_ID " + \
             "       , PROD_H1_ID, PROD_H2_ID, PROD_H3_ID; "

    dictMariaParameter = {
        "DATA_DATE": MariaEntity.MariaParameter(strOperator="=", objValue=strDataDate, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listCustSales = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listCustSales

def execWriteWorkbook(strJobPathRES, listCustSales):
    if len(listCustSales) == 0:
        return False
    else:
        objExcelWorkbook = None
        objExcelWorksheet = None
        
        objExcelWorkbook = xlsxwriter.Workbook(strJobPathRES)

        objExcelColumnFormat = objExcelWorkbook.add_format({
            "bold": 1, "align": "center", "valign": "vcenter", "font_size": 11, "font_color": "#FFFFFF", 
            "fg_color": "#305496", 
            "border": 0})

        objExcelRowLeftFormat = objExcelWorkbook.add_format({
            "bold": 1, "align": "left", "valign": "vcenter", "font_size": 11, "font_color": "#000000",
            "border": 0})
        objExcelRowRightFormat = objExcelWorkbook.add_format({
            "bold": 1, "align": "right", "valign": "vcenter", "font_size": 11, "font_color": "#000000",
            "border": 0})
        objExcelRowRightFormat.set_num_format('#,##0.00000')

        objExcelRow = 0
        objExcelWorksheet = objExcelWorkbook.add_worksheet("客户业绩通用报表")

        objExcelWorksheet.set_default_row(20)

        objExcelWorksheet.set_column(0, 0, 18)
        objExcelWorksheet.set_column(1, 1, 10)
        objExcelWorksheet.set_column(2, 2, 18)
        objExcelWorksheet.set_column(3, 3, 14)
        objExcelWorksheet.set_column(4, 4, 20)
        objExcelWorksheet.set_column(5, 5, 15)
        objExcelWorksheet.set_column(6, 6, 15)
        objExcelWorksheet.set_column(7, 7, 15)
        objExcelWorksheet.set_column(8, 8, 15)
        objExcelWorksheet.set_column(9, 9, 15)

        objExcelWorksheet.write(objExcelRow, 0, "旺旺渠道", objExcelColumnFormat)
        objExcelWorksheet.write(objExcelRow, 1, "产品大类", objExcelColumnFormat)
        objExcelWorksheet.write(objExcelRow, 2, "旺旺销售公司", objExcelColumnFormat) 
        objExcelWorksheet.write(objExcelRow, 3, "PM线", objExcelColumnFormat)
        objExcelWorksheet.write(objExcelRow, 4, "产品线", objExcelColumnFormat)
        objExcelWorksheet.write(objExcelRow, 5, "去年全月销退金额", objExcelColumnFormat)
        objExcelWorksheet.write(objExcelRow, 6, "月同期销退金额", objExcelColumnFormat)
        objExcelWorksheet.write(objExcelRow, 7, "本月销退金额", objExcelColumnFormat)
        objExcelWorksheet.write(objExcelRow, 8, "未过帐金额", objExcelColumnFormat)
        objExcelWorksheet.write(objExcelRow, 9, "单位：千元")
        objExcelRow += 1

        for dictEMPSales in listCustSales:
            objExcelWorksheet.write(objExcelRow, 0, dictEMPSales["WANT_CHAN_NM"], objExcelRowLeftFormat)
            objExcelWorksheet.write(objExcelRow, 1, dictEMPSales["PROD_H1_NM"], objExcelRowLeftFormat)
            objExcelWorksheet.write(objExcelRow, 2, dictEMPSales["WANT_COM_NM"], objExcelRowLeftFormat)
            objExcelWorksheet.write(objExcelRow, 3, dictEMPSales["PROD_H2_NM"], objExcelRowLeftFormat)
            objExcelWorksheet.write(objExcelRow, 4, dictEMPSales["PROD_H3_NM"], objExcelRowLeftFormat)
            objExcelWorksheet.write(objExcelRow, 5, dictEMPSales["POSTED_AMT_LAST_ALL"], objExcelRowRightFormat)
            objExcelWorksheet.write(objExcelRow, 6, dictEMPSales["POSTED_AMT_LAST"], objExcelRowRightFormat)
            objExcelWorksheet.write(objExcelRow, 7, dictEMPSales["POSTED_AMT_THIS"], objExcelRowRightFormat)
            objExcelWorksheet.write(objExcelRow, 8, dictEMPSales["POSTING_AMT"], objExcelRowRightFormat)
            objExcelWorksheet.write(objExcelRow, 9, "")
            objExcelRow += 1

        objExcelWorkbook.close()
        return True

def execMailCustSales(strJobPathRES, strDataDate):
    strEDIConnection = "3DW-DWuser@tpe-centos7-maria10-dw"
    strEDIDB = "DMMDL"

    listCustSales = getCustSalesList(strEDIConnection, strEDIDB, strDataDate)

    if execWriteWorkbook(strJobPathRES, listCustSales) == True:
        strMessageSMTPServer = "tw-mail02.want-want.com"
        strMessageSMTPFrom = "Data.Center@want-want.com"
        arrayMessageSMTPTo = [
            "Xie_Wei3@want-want.com",
            "Yan_HongMei@want-want.com",
            "Zoe.Hsu@want-want.com"
        ]
        strMessageSubject = "[测试]客户业绩通用报表-%s" % strDataDate
        strAttachFileName = "[测试]客户业绩通用报表-%s.xlsx" % strDataDate

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

    execMailCustSales(strJobPathRES, strDataDate)

if __name__ == "__main__":
    main()
