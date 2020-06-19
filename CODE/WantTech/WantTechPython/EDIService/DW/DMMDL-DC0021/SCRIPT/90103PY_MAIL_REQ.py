import sys
import logging
import xlsxwriter
from Utility import Common
from Utility import Message
from Entity import DBEntity
from Entity import MariaEntity
from EDI import EDIEntity

def getReqList(strEDIConnection, strEDIDB, strDataDate):
    strSQL = "SELECT REQ_YM, WANT_CHAN_NM, PROD_H1_NM, WANT_COM_NM, PROD_H2_NM, PROD_H3_NM " + \
             "     , (REQ_AMT/1000) AS REQ_AMT " + \
             "FROM DMMDL.DC0021_REQ " + \
             "WHERE {DATA_DATE} " + \
             "ORDER BY REQ_YM, WANT_CHAN_NM, PROD_H1_NM, WANT_COM_NM, PROD_H2_NM, PROD_H3_NM; "

    dictMariaParameter = {
        "DATA_DATE": MariaEntity.MariaParameter(strOperator="=", objValue=strDataDate, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listReq = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listReq

def execWriteWorkbook(strJobPathRES, listReq):
    if len(listReq) == 0:
        return False
    else:
        objExcelWorkbook = None
        objExcelWorksheet = None
        strREQ_YM = None

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

        for dictReq in listReq:
            if dictReq["REQ_YM"] != strREQ_YM:
                strREQ_YM = dictReq["REQ_YM"]

                objExcelRow = 0
                objExcelWorksheet = objExcelWorkbook.add_worksheet("销售预估明细报表-" + strREQ_YM)

                objExcelWorksheet.set_default_row(20)

                objExcelWorksheet.set_column(0, 0, 15)
                objExcelWorksheet.set_column(1, 1, 10)
                objExcelWorksheet.set_column(2, 2, 12)
                objExcelWorksheet.set_column(3, 3, 10)
                objExcelWorksheet.set_column(4, 4, 15)
                objExcelWorksheet.set_column(5, 5, 12)
                objExcelWorksheet.set_column(6, 6, 15)

                objExcelWorksheet.write(objExcelRow, 0, "旺旺渠道", objExcelColumnFormat)
                objExcelWorksheet.write(objExcelRow, 1, "产品大类", objExcelColumnFormat)
                objExcelWorksheet.write(objExcelRow, 2, "旺旺销售公司", objExcelColumnFormat)
                objExcelWorksheet.write(objExcelRow, 3, "PM线", objExcelColumnFormat) 
                objExcelWorksheet.write(objExcelRow, 4, "产品线", objExcelColumnFormat) 
                objExcelWorksheet.write(objExcelRow, 5, "预估金额", objExcelColumnFormat)
                objExcelWorksheet.write(objExcelRow, 6, "单位：千元")
                objExcelRow += 1

            objExcelWorksheet.write(objExcelRow, 0, dictReq["WANT_CHAN_NM"], objExcelRowLeftFormat)
            objExcelWorksheet.write(objExcelRow, 1, dictReq["PROD_H1_NM"], objExcelRowLeftFormat)
            objExcelWorksheet.write(objExcelRow, 2, dictReq["WANT_COM_NM"], objExcelRowCenterFormat)
            objExcelWorksheet.write(objExcelRow, 3, dictReq["PROD_H2_NM"], objExcelRowLeftFormat)
            objExcelWorksheet.write(objExcelRow, 4, dictReq["PROD_H3_NM"], objExcelRowLeftFormat)
            objExcelWorksheet.write(objExcelRow, 5, dictReq["REQ_AMT"], objExcelRowRightFormat)
            objExcelWorksheet.write(objExcelRow, 6, "")
            objExcelRow += 1

        objExcelWorkbook.close()
        return True

def execMailReq(strJobPathRES, strDataDate):
    strEDIConnection = "3DW-DWuser@tpe-centos7-maria10-dw"
    strEDIDB = "DMMDL"

    listCustStmt = getReqList(strEDIConnection, strEDIDB, strDataDate)

    if execWriteWorkbook(strJobPathRES, listCustStmt) == True:
        strMessageSMTPServer = "tw-mail02.want-want.com"
        strMessageSMTPFrom = "Data.Center@want-want.com"
        arrayMessageSMTPTo = [
            "Xie_Wei3@want-want.com",
            "Yan_HongMei@want-want.com",
            "Zoe.Hsu@want-want.com"
        ]
        strMessageSubject = "[测试]销售预估明细报表-%s" % strDataDate
        strAttachFileName = "[测试]销售预估明细报表-%s.xlsx" % strDataDate

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

    execMailReq(strJobPathRES, strDataDate)

if __name__ == "__main__":
    main()
