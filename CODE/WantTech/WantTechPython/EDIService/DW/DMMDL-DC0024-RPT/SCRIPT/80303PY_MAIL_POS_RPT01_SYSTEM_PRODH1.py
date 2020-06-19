import sys
import logging
import xlsxwriter
from Utility import Common
from Utility import Message
from Entity import DBEntity
from Entity import MariaEntity
from EDI import EDIEntity

def getWeekNumList(strEDIConnection, strEDIDB, strDataDate):
    strSQL = "SELECT WEEK_NUM, WEEK_FIRST_DATE " + \
             "FROM DMMDL.DC0024_WEEK_NUM " + \
             "WHERE CONVERT(WEEK_NUM, INT)>=(CONVERT(LEFT({DATA_DATE}, 4), INT) - 1)*100+49 " + \
             "ORDER BY WEEK_NUM DESC; "

    dictMariaParameter = {
        "DATA_DATE": MariaEntity.MariaParameter(objValue=strDataDate, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listWeekNum = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listWeekNum

def getPOSRPT01List(strEDIConnection, strEDIDB, strDataDate):
    strSQL = "SELECT POS_DATE, DWWANT.FN_GET_WEEK_LAST_DATE(POS_DATE) AS WEEK_LAST_DATE " + \
             "FROM DMMDL.DC0024_POS_RPT01 " + \
             "WHERE {DATA_DATE}; "

    dictMariaParameter = {
        "DATA_DATE": MariaEntity.MariaParameter(strOperator="=", objValue=strDataDate, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listPOSRPT01 = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listPOSRPT01

def getPOSRPT01SystemList(strEDIConnection, strEDIDB, strDataDate):
    strSQL = "SELECT KA_SYSTEM_CODE, MAX(KA_SYSTEM_NM) AS KA_SYSTEM_NM " + \
             "FROM DMMDL.DC0024_POS_RPT01_SYSTEM " + \
             "WHERE CONVERT(POS_WEEK_NUM, INT)>=(CONVERT(LEFT({DATA_DATE}, 4), INT) - 1)*100+49 " + \
             "GROUP BY KA_SYSTEM_CODE " + \
             "ORDER BY KA_SYSTEM_CODE; "

    dictMariaParameter = {
        "DATA_DATE": MariaEntity.MariaParameter(objValue=strDataDate, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listPOSRPT01System = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listPOSRPT01System

def getPOSRPT01SystemPCSList(strEDIConnection, strEDIDB, strDataDate):
    strSQL = "SELECT KA_SYSTEM_CODE, KA_SYSTEM_NM, KA_SYSTEM_ACT_NM, POS_WEEK_NUM " + \
             "     , ROUND(POS_QTY_PCS, 0) AS POS_QTY_PCS " + \
             "FROM DMMDL.DC0024_POS_RPT01_SYSTEM " + \
             "WHERE CONVERT(POS_WEEK_NUM, INT)>=(CONVERT(LEFT({DATA_DATE}, 4), INT) - 1)*100+49 " + \
             "ORDER BY KA_SYSTEM_CODE, POS_WEEK_NUM DESC; "

    dictMariaParameter = {
        "DATA_DATE": MariaEntity.MariaParameter(objValue=strDataDate, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listPOSRPT01SystemPCS = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listPOSRPT01SystemPCS

def getPOSRPT01SystemSKUList(strEDIConnection, strEDIDB, strDataDate):
    strSQL = "SELECT KA_SYSTEM_CODE, KA_SYSTEM_NM, KA_SYSTEM_ACT_NM, POS_WEEK_NUM " + \
             "     , POS_SKU " + \
             "FROM DMMDL.DC0024_POS_RPT01_SYSTEM " + \
             "WHERE CONVERT(POS_WEEK_NUM, INT)>=(CONVERT(LEFT({DATA_DATE}, 4), INT) - 1)*100+49 " + \
             "ORDER BY KA_SYSTEM_CODE, POS_WEEK_NUM DESC; "

    dictMariaParameter = {
        "DATA_DATE": MariaEntity.MariaParameter(objValue=strDataDate, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listPOSRPT01SystemSKU = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listPOSRPT01SystemSKU

def getPOSRPT01ProdH1PCSList(strEDIConnection, strEDIDB, strDataDate):
    strSQL = "SELECT KA_SYSTEM_CODE, KA_SYSTEM_NM, KA_SYSTEM_ACT_NM " + \
             "     , SALES_COM_ID_SA, SALES_COM_ABR_SA " + \
             "     , PROD_H1_ID, PROD_H1_NM, POS_WEEK_NUM " + \
             "     , ROUND(POS_QTY_PCS, 0) AS POS_QTY_PCS " + \
             "FROM DMMDL.DC0024_POS_RPT01_PRODH1 " + \
             "WHERE CONVERT(POS_WEEK_NUM, INT)>=(CONVERT(LEFT({DATA_DATE}, 4), INT) - 1)*100+49 " + \
             "ORDER BY KA_SYSTEM_CODE, SALES_COM_ID_SA, PROD_H1_ID, POS_WEEK_NUM DESC; "

    dictMariaParameter = {
        "DATA_DATE": MariaEntity.MariaParameter(objValue=strDataDate, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listPOSRPT01ProdH1PCS = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listPOSRPT01ProdH1PCS

def getPOSRPT01ProdH1SKUList(strEDIConnection, strEDIDB, strDataDate):
    strSQL = "SELECT KA_SYSTEM_CODE, KA_SYSTEM_NM, KA_SYSTEM_ACT_NM " + \
             "     , SALES_COM_ID_SA, SALES_COM_ABR_SA " + \
             "     , PROD_H1_ID, PROD_H1_NM, POS_WEEK_NUM " + \
             "     , POS_SKU " + \
             "FROM DMMDL.DC0024_POS_RPT01_PRODH1 " + \
             "WHERE CONVERT(POS_WEEK_NUM, INT)>=(CONVERT(LEFT({DATA_DATE}, 4), INT) - 1)*100+49 " + \
             "ORDER BY KA_SYSTEM_CODE, SALES_COM_ID_SA, PROD_H1_ID, POS_WEEK_NUM DESC; "

    dictMariaParameter = {
        "DATA_DATE": MariaEntity.MariaParameter(objValue=strDataDate, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listPOSRPT01ProdH1SKU = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listPOSRPT01ProdH1SKU

def getExcelColumnName(intNumber):
    intTemp = intNumber
    intTimes = 0

    while intTemp > 90:
        intTemp -= 26
        intTimes += 1

    strChar = chr(intTemp)
    if intTimes > 0:
        strChar = chr(intTimes + 64) + strChar

    return strChar

def execWriteWorkbook(strJobPathRES, listWeekNum, listPOSRPT01, listPOSRPT01System, listPOSRPT01SystemPCS, listPOSRPT01SystemSKU, listPOSRPT01ProdH1PCS, listPOSRPT01ProdH1SKU):
    if len(listWeekNum) == 0 or len(listPOSRPT01) == 0 or len(listPOSRPT01ProdH1PCS) != len(listPOSRPT01ProdH1SKU) or len(listPOSRPT01SystemPCS) != len(listPOSRPT01SystemSKU):
        return False
    else:
        objExcelWorkbook = None
        objExcelWorksheet = None
        
        objExcelRowCenterFormat = None
        objExcelRowLeftFormat = None
        objExcelRowRightFormat = None

        strKA_SYSTEM_ACT_NM = None
        strKA_SYSTEM_CODE = None
        strKA_SYSTEM_NM = None

        intPOSRPT01SystemIndex = 0
        intPOSRPT01ProdH1Index = 0

        intExcelRow = 0

        intNowDates = (Common.getDate(listPOSRPT01[0]["POS_DATE"]) - Common.getDate(listWeekNum[0]["WEEK_FIRST_DATE"])).days + 1

        while intPOSRPT01ProdH1Index < len(listPOSRPT01ProdH1PCS):
            if strKA_SYSTEM_CODE != listPOSRPT01ProdH1PCS[intPOSRPT01ProdH1Index]["KA_SYSTEM_CODE"]:
                strKA_SYSTEM_ACT_NM = listPOSRPT01ProdH1PCS[intPOSRPT01ProdH1Index]["KA_SYSTEM_ACT_NM"]
                strKA_SYSTEM_CODE = listPOSRPT01ProdH1PCS[intPOSRPT01ProdH1Index]["KA_SYSTEM_CODE"]
                strKA_SYSTEM_NM = listPOSRPT01ProdH1PCS[intPOSRPT01ProdH1Index]["KA_SYSTEM_NM"]

                if objExcelWorksheet != None:
                    objExcelWorksheet.freeze_panes("K8")
                    objExcelWorksheet.autofilter("A7:CF" + str(intExcelRow))
                    objExcelWorksheet.set_column('F:G', None, None, {'hidden': True})

                if objExcelWorkbook != None:
                    objExcelWorkbook.close()
                
                objExcelWorkbook = xlsxwriter.Workbook(strJobPathRES.replace(".dat", "-" + strKA_SYSTEM_CODE + ".dat"))

                objExcelTitleFormat = objExcelWorkbook.add_format({
                    "bold": 1, "align": "left", "valign": "vcenter", "font_size": 16, "font_color": "#305496", 
                    "fg_color": "#D6DCE4", 
                    "border": 0})
                objExcelSubTitleFormat = objExcelWorkbook.add_format({
                    "bold": 1, "align": "left", "valign": "vcenter", "font_size": 11, "font_color": "#305496", 
                    "fg_color": "#D6DCE4", 
                    "border": 0})
                objExcelColumnFormat = objExcelWorkbook.add_format({
                    "text_wrap": 1,
                    "bold": 1, "align": "center", "valign": "vcenter", "font_size": 11, "font_color": "#FFFFFF", 
                    "fg_color": "#305496", 
                    "border": 0})
                objExcelWeekFormat = objExcelWorkbook.add_format({
                    "bold": 1, "align": "center", "valign": "vcenter", "font_size": 11, "font_color": "#FFFFFF", 
                    "fg_color": "#305496", 
                    "border": 1, "top_color": "#305496", "bottom_color": "#FFFFFF", "left_color": "#305496", "right_color": "#305496"})

                objExcelRowFilterFormat = objExcelWorkbook.add_format({
                    "bold": 1, "align": "center", "valign": "vcenter", "font_size": 11, "font_color": "#000000",
                    "fg_color": "#BFBEBF", 
                    "border": 1, "top_color": "#F2F2F2", "bottom_color": "#F2F2F2", "left_color": "#BFBEBF", "right_color": "#BFBEBF"})

                objExcelRowCenter1Format = objExcelWorkbook.add_format({
                    "bold": 1, "align": "center", "valign": "vcenter", "font_size": 11, "font_color": "#000000",
                    "fg_color": "#FFFFFF", 
                    "border": 1, "top_color": "#F2F2F2", "bottom_color": "#F2F2F2", "left_color": "#305496", "right_color": "#305496"})
                objExcelRowCenter2Format = objExcelWorkbook.add_format({
                    "bold": 1, "align": "center", "valign": "vcenter", "font_size": 11, "font_color": "#000000",
                    "fg_color": "#D9E1F2", 
                    "border": 1, "top_color": "#F2F2F2", "bottom_color": "#F2F2F2", "left_color": "#305496", "right_color": "#305496"})
                objExcelRowLeft1Format = objExcelWorkbook.add_format({
                    "bold": 1, "align": "left", "valign": "vcenter", "font_size": 11, "font_color": "#000000",
                    "fg_color": "#FFFFFF", 
                    "border": 1, "top_color": "#F2F2F2", "bottom_color": "#F2F2F2", "left_color": "#305496", "right_color": "#305496"})
                objExcelRowLeft2Format = objExcelWorkbook.add_format({
                    "bold": 1, "align": "left", "valign": "vcenter", "font_size": 11, "font_color": "#000000",
                    "fg_color": "#D9E1F2", 
                    "border": 1, "top_color": "#F2F2F2", "bottom_color": "#F2F2F2", "left_color": "#305496", "right_color": "#305496"})
                objExcelRowRight1Format = objExcelWorkbook.add_format({
                    "num_format": "#,##0", 
                    "bold": 1, "align": "right", "valign": "vcenter", "font_size": 11, "font_color": "#000000",
                    "fg_color": "#FFFFFF", 
                    "border": 1, "top_color": "#F2F2F2", "bottom_color": "#F2F2F2", "left_color": "#FFFFFF", "right_color": "#FFFFFF"})
                objExcelRowRight2Format = objExcelWorkbook.add_format({
                    "num_format": "#,##0", 
                    "bold": 1, "align": "right", "valign": "vcenter", "font_size": 11, "font_color": "#000000",
                    "fg_color": "#D9E1F2", 
                    "border": 1, "top_color": "#F2F2F2", "bottom_color": "#F2F2F2", "left_color": "#D9E1F2", "right_color": "#D9E1F2"})

                objExcelRowIcon1Format = objExcelWorkbook.add_format({
                    "bold": 1, "align": "center", "valign": "vcenter", "font_size": 11, "font_color": "#000000",
                    "fg_color": "#FFFFFF", 
                    "border": 1, "top_color": "#F2F2F2", "bottom_color": "#F2F2F2", "left_color": "#FFFFFF", "right_color": "#305496"})
                objExcelRowIcon1UpFormat = objExcelWorkbook.add_format({
                    "bold": 1, "align": "center", "valign": "vcenter", "font_size": 11, "font_color": "#B02317",
                    "fg_color": "#FFFFFF", 
                    "border": 1, "top_color": "#F2F2F2", "bottom_color": "#F2F2F2", "left_color": "#FFFFFF", "right_color": "#305496"})
                objExcelRowIcon1DownFormat = objExcelWorkbook.add_format({
                    "bold": 1, "align": "center", "valign": "vcenter", "font_size": 11, "font_color": "#4EAD5B",
                    "fg_color": "#FFFFFF", 
                    "border": 1, "top_color": "#F2F2F2", "bottom_color": "#F2F2F2", "left_color": "#FFFFFF", "right_color": "#305496"})
                objExcelRowIcon1FlatFormat = objExcelWorkbook.add_format({
                    "bold": 1, "align": "center", "valign": "vcenter", "font_size": 11, "font_color": "#EBA064",
                    "fg_color": "#FFFFFF", 
                    "border": 1, "top_color": "#F2F2F2", "bottom_color": "#F2F2F2", "left_color": "#FFFFFF", "right_color": "#305496"})
                objExcelRowIcon2Format = objExcelWorkbook.add_format({
                    "bold": 1, "align": "center", "valign": "vcenter", "font_size": 11, "font_color": "#000000",
                    "fg_color": "#D9E1F2", 
                    "border": 1, "top_color": "#F2F2F2", "bottom_color": "#F2F2F2", "left_color": "#D9E1F2", "right_color": "#305496"})
                objExcelRowIcon2UpFormat = objExcelWorkbook.add_format({
                    "bold": 1, "align": "center", "valign": "vcenter", "font_size": 11, "font_color": "#B02317",
                    "fg_color": "#D9E1F2", 
                    "border": 1, "top_color": "#F2F2F2", "bottom_color": "#F2F2F2", "left_color": "#D9E1F2", "right_color": "#305496"})
                objExcelRowIcon2DownFormat = objExcelWorkbook.add_format({
                    "bold": 1, "align": "center", "valign": "vcenter", "font_size": 11, "font_color": "#4EAD5B",
                    "fg_color": "#D9E1F2", 
                    "border": 1, "top_color": "#F2F2F2", "bottom_color": "#F2F2F2", "left_color": "#D9E1F2", "right_color": "#305496"})
                objExcelRowIcon2FlatFormat = objExcelWorkbook.add_format({
                    "bold": 1, "align": "center", "valign": "vcenter", "font_size": 11, "font_color": "#EBA064",
                    "fg_color": "#D9E1F2", 
                    "border": 1, "top_color": "#F2F2F2", "bottom_color": "#F2F2F2", "left_color": "#D9E1F2", "right_color": "#305496"})

                objExcelWorksheet = objExcelWorkbook.add_worksheet(strKA_SYSTEM_CODE + "-" + strKA_SYSTEM_NM)

                objExcelWorksheet.set_default_row(20)
                objExcelWorksheet.set_row(3, 30)

                objExcelWorksheet.set_column(0, 6, 8)
                objExcelWorksheet.set_column(7, 7, 10)
                objExcelWorksheet.set_column(8, 8, 20)
                objExcelWorksheet.set_column(9, 9, 11)

                objExcelRowCenterFormat = objExcelRowCenter1Format
                objExcelRowLeftFormat = objExcelRowLeft1Format
                objExcelRowRightFormat = objExcelRowRight1Format
                objExcelRowIconFormat = objExcelRowIcon1Format

                intExcelRow = 0

                intTemp = 0
                for dictWeekNum in listWeekNum:
                    objExcelWorksheet.set_column(10 + intTemp * 2, 10 + intTemp * 2, 11)
                    objExcelWorksheet.set_column(10 + intTemp * 2 + 1, 10 + intTemp * 2 + 1, 2.5)
                    intTemp += 1

                objExcelWorksheet.merge_range("A1:I1", "现代渠道发展营业部业绩－通路系统品类周别POS推移", objExcelTitleFormat)
                objExcelWorksheet.write(intExcelRow, 8, "", objExcelTitleFormat)
                objExcelWorksheet.write(intExcelRow, 9, "", objExcelTitleFormat)
                intTemp = 0
                for dictWeekNum in listWeekNum:
                    objExcelWorksheet.write(intExcelRow, 10 + intTemp * 2, "", objExcelTitleFormat)
                    objExcelWorksheet.write(intExcelRow, 10 + intTemp * 2 + 1, "", objExcelTitleFormat)
                    intTemp += 1
                intExcelRow += 1

                objExcelWorksheet.merge_range("A2:H2", Common.formatDateString(listPOSRPT01[0]["POS_DATE"]) + " 销售数量为最小单位加总", objExcelSubTitleFormat)
                objExcelWorksheet.write(intExcelRow, 8, "", objExcelTitleFormat)
                objExcelWorksheet.write(intExcelRow, 9, "", objExcelTitleFormat)
                intTemp = 0
                for dictWeekNum in listWeekNum:
                    objExcelWorksheet.write(intExcelRow, 10 + intTemp * 2, "", objExcelTitleFormat)
                    objExcelWorksheet.write(intExcelRow, 10 + intTemp * 2 + 1, "", objExcelTitleFormat)
                    intTemp += 1
                intExcelRow += 1

                objExcelWorksheet.merge_range("A3:A4", "通路", objExcelColumnFormat)
                objExcelWorksheet.merge_range("B3:B4", "系统编码", objExcelColumnFormat)
                objExcelWorksheet.merge_range("C3:C4", "系统名称", objExcelColumnFormat)
                objExcelWorksheet.merge_range("D3:D4", "分公司\n编码", objExcelColumnFormat)
                objExcelWorksheet.merge_range("E3:E4", "分公司\n名称", objExcelColumnFormat)
                objExcelWorksheet.merge_range("F3:F4", "统仓地\n编码", objExcelColumnFormat)
                objExcelWorksheet.merge_range("G3:G4", "统仓地\n名称", objExcelColumnFormat)
                objExcelWorksheet.merge_range("H3:H4", "品类编码", objExcelColumnFormat)
                objExcelWorksheet.merge_range("I3:I4", "品类名称", objExcelColumnFormat)
                objExcelWorksheet.write(intExcelRow, 9, "周数", objExcelColumnFormat)
                intTemp = 0
                for dictWeekNum in listWeekNum:
                    objExcelWorksheet.merge_range(getExcelColumnName(65 + 10 + intTemp * 2) + "3:" + getExcelColumnName(65 + 10 + intTemp * 2 + 1) + "3", int(dictWeekNum["WEEK_NUM"][-2:]), objExcelWeekFormat)
                    intTemp += 1
                intExcelRow += 1

                objExcelWorksheet.write(intExcelRow, 9, "KPI", objExcelColumnFormat)
                intTemp = 0
                for dictWeekNum in listWeekNum:
                    objExcelWorksheet.merge_range(getExcelColumnName(65 + 10 + intTemp * 2) + "4:" + getExcelColumnName(65 + 10 + intTemp * 2 + 1) + "4", Common.formatDateString(dictWeekNum["WEEK_FIRST_DATE"]), objExcelColumnFormat)
                    intTemp += 1
                intExcelRow += 1

                objExcelWorksheet.write(intExcelRow, 0, strKA_SYSTEM_ACT_NM, objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 1, strKA_SYSTEM_CODE, objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 2, strKA_SYSTEM_NM, objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 3, "", objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 4, "", objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 5, "", objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 6, "", objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 7, "", objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 8, "合计", objExcelRowLeftFormat)
                objExcelWorksheet.write(intExcelRow, 9, "销售数量", objExcelRowCenterFormat)

                intIndexCount = 0
                intIndexTemp = 0
                intTemp = 0
                for dictWeekNum in listWeekNum:
                    intIndexTemp = intPOSRPT01SystemIndex + intIndexCount
                    if intIndexTemp < len(listPOSRPT01SystemPCS) and \
                       listPOSRPT01SystemPCS[intIndexTemp]["KA_SYSTEM_CODE"] == strKA_SYSTEM_CODE and \
                       listPOSRPT01SystemPCS[intIndexTemp]["POS_WEEK_NUM"] == listWeekNum[intTemp]["WEEK_NUM"]:

                        strDirection = ""
                        decTarget = 0
                        objExcelRowIconDirFormat = objExcelRowIconFormat
                        if (intIndexTemp + 1) < len(listPOSRPT01SystemPCS) and (intTemp + 1) < len(listWeekNum) and \
                           listPOSRPT01SystemPCS[intIndexTemp + 1]["KA_SYSTEM_CODE"] == strKA_SYSTEM_CODE and \
                           listPOSRPT01SystemPCS[intIndexTemp + 1]["POS_WEEK_NUM"] == listWeekNum[intTemp + 1]["WEEK_NUM"]:

                            if intTemp == 0:
                                decTarget = round(listPOSRPT01SystemPCS[intIndexTemp + 1]["POS_QTY_PCS"] / 7 * intNowDates, 0)
                            else:
                                decTarget = listPOSRPT01SystemPCS[intIndexTemp + 1]["POS_QTY_PCS"]

                            if listPOSRPT01SystemPCS[intIndexTemp]["POS_QTY_PCS"] > decTarget:
                                strDirection = "▲"
                                if objExcelRowIconFormat == objExcelRowIcon1Format:
                                    objExcelRowIconDirFormat = objExcelRowIcon1UpFormat
                                else:
                                    objExcelRowIconDirFormat = objExcelRowIcon2UpFormat

                            elif listPOSRPT01SystemPCS[intIndexTemp]["POS_QTY_PCS"] < decTarget:
                                strDirection = "▼"
                                if objExcelRowIconFormat == objExcelRowIcon1Format:
                                    objExcelRowIconDirFormat = objExcelRowIcon1DownFormat
                                else:
                                    objExcelRowIconDirFormat = objExcelRowIcon2DownFormat

                            else:
                                strDirection = "━"
                                if objExcelRowIconFormat == objExcelRowIcon1Format:
                                    objExcelRowIconDirFormat = objExcelRowIcon1FlatFormat
                                else:
                                    objExcelRowIconDirFormat = objExcelRowIcon2FlatFormat

                        objExcelWorksheet.write(intExcelRow, 10 + intTemp * 2, listPOSRPT01SystemPCS[intIndexTemp]["POS_QTY_PCS"], objExcelRowRightFormat)
                        objExcelWorksheet.write(intExcelRow, 10 + intTemp * 2 + 1, strDirection, objExcelRowIconDirFormat)
                        intIndexCount += 1
                        intTemp += 1
                    else:
                        objExcelWorksheet.write(intExcelRow, 10 + intTemp * 2, "-", objExcelRowRightFormat)
                        objExcelWorksheet.write(intExcelRow, 10 + intTemp * 2 + 1, "", objExcelRowIconFormat)
                        intTemp += 1
                intExcelRow += 1

                objExcelWorksheet.write(intExcelRow, 0, strKA_SYSTEM_ACT_NM, objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 1, strKA_SYSTEM_CODE, objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 2, strKA_SYSTEM_NM, objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 3, "", objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 4, "", objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 5, "", objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 6, "", objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 7, "", objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 8, "合计", objExcelRowLeftFormat)
                objExcelWorksheet.write(intExcelRow, 9, "品项数", objExcelRowCenterFormat)

                intIndexCount = 0
                intIndexTemp = 0
                intTemp = 0
                for dictWeekNum in listWeekNum:
                    intIndexTemp = intPOSRPT01SystemIndex + intIndexCount
                    if intIndexTemp < len(listPOSRPT01SystemSKU) and \
                       listPOSRPT01SystemSKU[intIndexTemp]["KA_SYSTEM_CODE"] == strKA_SYSTEM_CODE and \
                       listPOSRPT01SystemSKU[intIndexTemp]["POS_WEEK_NUM"] == listWeekNum[intTemp]["WEEK_NUM"]:

                        strDirection = ""
                        decTarget = 0
                        objExcelRowIconDirFormat = objExcelRowIconFormat
                        if (intIndexTemp + 1) < len(listPOSRPT01SystemSKU) and (intTemp + 1) < len(listWeekNum) and \
                           listPOSRPT01SystemSKU[intIndexTemp + 1]["KA_SYSTEM_CODE"] == strKA_SYSTEM_CODE and \
                           listPOSRPT01SystemSKU[intIndexTemp + 1]["POS_WEEK_NUM"] == listWeekNum[intTemp + 1]["WEEK_NUM"]:

                            decTarget = listPOSRPT01SystemSKU[intIndexTemp + 1]["POS_SKU"]

                            if listPOSRPT01SystemSKU[intIndexTemp]["POS_SKU"] > decTarget:
                                strDirection = "▲"
                                if objExcelRowIconFormat == objExcelRowIcon1Format:
                                    objExcelRowIconDirFormat = objExcelRowIcon1UpFormat
                                else:
                                    objExcelRowIconDirFormat = objExcelRowIcon2UpFormat

                            elif listPOSRPT01SystemSKU[intIndexTemp]["POS_SKU"] < decTarget:
                                strDirection = "▼"
                                if objExcelRowIconFormat == objExcelRowIcon1Format:
                                    objExcelRowIconDirFormat = objExcelRowIcon1DownFormat
                                else:
                                    objExcelRowIconDirFormat = objExcelRowIcon2DownFormat

                            else:
                                strDirection = "━"
                                if objExcelRowIconFormat == objExcelRowIcon1Format:
                                    objExcelRowIconDirFormat = objExcelRowIcon1FlatFormat
                                else:
                                    objExcelRowIconDirFormat = objExcelRowIcon2FlatFormat

                        objExcelWorksheet.write(intExcelRow, 10 + intTemp * 2, listPOSRPT01SystemSKU[intIndexTemp]["POS_SKU"], objExcelRowRightFormat)
                        objExcelWorksheet.write(intExcelRow, 10 + intTemp * 2 + 1, strDirection, objExcelRowIconDirFormat)
                        intIndexCount += 1
                        intTemp += 1
                    else:
                        objExcelWorksheet.write(intExcelRow, 10 + intTemp * 2, "-", objExcelRowRightFormat)
                        objExcelWorksheet.write(intExcelRow, 10 + intTemp * 2 + 1, "", objExcelRowIconFormat)
                        intTemp += 1
                intExcelRow += 1

                intPOSRPT01SystemIndex += intIndexCount

                objExcelWorksheet.write(intExcelRow, 0, "", objExcelRowFilterFormat)
                objExcelWorksheet.write(intExcelRow, 1, "", objExcelRowFilterFormat)
                objExcelWorksheet.write(intExcelRow, 2, "", objExcelRowFilterFormat)
                objExcelWorksheet.write(intExcelRow, 3, "", objExcelRowFilterFormat)
                objExcelWorksheet.write(intExcelRow, 4, "", objExcelRowFilterFormat)
                objExcelWorksheet.write(intExcelRow, 5, "", objExcelRowFilterFormat)
                objExcelWorksheet.write(intExcelRow, 6, "", objExcelRowFilterFormat)
                objExcelWorksheet.write(intExcelRow, 7, "", objExcelRowFilterFormat)
                objExcelWorksheet.write(intExcelRow, 8, "", objExcelRowFilterFormat)
                objExcelWorksheet.write(intExcelRow, 9, "筛选", objExcelRowFilterFormat)
                intTemp = 0
                for dictWeekNum in listWeekNum:
                    objExcelWorksheet.write(intExcelRow, 10 + intTemp * 2, "", objExcelRowFilterFormat)
                    objExcelWorksheet.write(intExcelRow, 10 + intTemp * 2 + 1, "", objExcelRowFilterFormat)
                    intTemp += 1
                intExcelRow += 1

            if objExcelRowCenterFormat == objExcelRowCenter2Format:
                objExcelRowCenterFormat = objExcelRowCenter1Format
                objExcelRowLeftFormat = objExcelRowLeft1Format
                objExcelRowRightFormat = objExcelRowRight1Format
                objExcelRowIconFormat = objExcelRowIcon1Format
            else:
                objExcelRowCenterFormat = objExcelRowCenter2Format
                objExcelRowLeftFormat = objExcelRowLeft2Format
                objExcelRowRightFormat = objExcelRowRight2Format
                objExcelRowIconFormat = objExcelRowIcon2Format

            objExcelWorksheet.write(intExcelRow, 0, listPOSRPT01ProdH1PCS[intPOSRPT01ProdH1Index]["KA_SYSTEM_ACT_NM"], objExcelRowCenterFormat)
            objExcelWorksheet.write(intExcelRow, 1, listPOSRPT01ProdH1PCS[intPOSRPT01ProdH1Index]["KA_SYSTEM_CODE"], objExcelRowCenterFormat)
            objExcelWorksheet.write(intExcelRow, 2, listPOSRPT01ProdH1PCS[intPOSRPT01ProdH1Index]["KA_SYSTEM_NM"], objExcelRowCenterFormat)
            objExcelWorksheet.write(intExcelRow, 3, listPOSRPT01ProdH1PCS[intPOSRPT01ProdH1Index]["SALES_COM_ID_SA"], objExcelRowCenterFormat)
            objExcelWorksheet.write(intExcelRow, 4, listPOSRPT01ProdH1PCS[intPOSRPT01ProdH1Index]["SALES_COM_ABR_SA"], objExcelRowCenterFormat)
            objExcelWorksheet.write(intExcelRow, 5, "", objExcelRowCenterFormat)
            objExcelWorksheet.write(intExcelRow, 6, "", objExcelRowCenterFormat)
            objExcelWorksheet.write(intExcelRow, 7, listPOSRPT01ProdH1PCS[intPOSRPT01ProdH1Index]["PROD_H1_ID"], objExcelRowCenterFormat)
            objExcelWorksheet.write(intExcelRow, 8, listPOSRPT01ProdH1PCS[intPOSRPT01ProdH1Index]["PROD_H1_NM"], objExcelRowLeftFormat)
            objExcelWorksheet.write(intExcelRow, 9, "销售数量", objExcelRowCenterFormat)

            intIndexCount = 0
            intIndexTemp = 0
            intTemp = 0
            for dictWeekNum in listWeekNum:
                intIndexTemp = intPOSRPT01ProdH1Index + intIndexCount
                if intIndexTemp < len(listPOSRPT01ProdH1PCS) and \
                   listPOSRPT01ProdH1PCS[intIndexTemp]["KA_SYSTEM_CODE"] == strKA_SYSTEM_CODE and \
                   listPOSRPT01ProdH1PCS[intIndexTemp]["PROD_H1_ID"] == listPOSRPT01ProdH1PCS[intPOSRPT01ProdH1Index]["PROD_H1_ID"] and \
                   listPOSRPT01ProdH1PCS[intIndexTemp]["POS_WEEK_NUM"] == listWeekNum[intTemp]["WEEK_NUM"]:

                    strDirection = ""
                    decTarget = 0
                    objExcelRowIconDirFormat = objExcelRowIconFormat
                    if (intIndexTemp + 1) < len(listPOSRPT01ProdH1PCS) and (intTemp + 1) < len(listWeekNum) and \
                       listPOSRPT01ProdH1PCS[intIndexTemp + 1]["KA_SYSTEM_CODE"] == strKA_SYSTEM_CODE and \
                       listPOSRPT01ProdH1PCS[intIndexTemp + 1]["PROD_H1_ID"] == listPOSRPT01ProdH1PCS[intPOSRPT01ProdH1Index]["PROD_H1_ID"] and \
                       listPOSRPT01ProdH1PCS[intIndexTemp + 1]["POS_WEEK_NUM"] == listWeekNum[intTemp + 1]["WEEK_NUM"]:

                        if intTemp == 0:
                            decTarget = round(listPOSRPT01ProdH1PCS[intIndexTemp + 1]["POS_QTY_PCS"] / 7 * intNowDates, 0)
                        else:
                            decTarget = listPOSRPT01ProdH1PCS[intIndexTemp + 1]["POS_QTY_PCS"]

                        if listPOSRPT01ProdH1PCS[intIndexTemp]["POS_QTY_PCS"] > decTarget:
                            strDirection = "▲"
                            if objExcelRowIconFormat == objExcelRowIcon1Format:
                                objExcelRowIconDirFormat = objExcelRowIcon1UpFormat
                            else:
                                objExcelRowIconDirFormat = objExcelRowIcon2UpFormat

                        elif listPOSRPT01ProdH1PCS[intIndexTemp]["POS_QTY_PCS"] < decTarget:
                            strDirection = "▼"
                            if objExcelRowIconFormat == objExcelRowIcon1Format:
                                objExcelRowIconDirFormat = objExcelRowIcon1DownFormat
                            else:
                                objExcelRowIconDirFormat = objExcelRowIcon2DownFormat

                        else:
                            strDirection = "━"
                            if objExcelRowIconFormat == objExcelRowIcon1Format:
                                objExcelRowIconDirFormat = objExcelRowIcon1FlatFormat
                            else:
                                objExcelRowIconDirFormat = objExcelRowIcon2FlatFormat

                    objExcelWorksheet.write(intExcelRow, 10 + intTemp * 2, listPOSRPT01ProdH1PCS[intIndexTemp]["POS_QTY_PCS"], objExcelRowRightFormat)
                    objExcelWorksheet.write(intExcelRow, 10 + intTemp * 2 + 1, strDirection, objExcelRowIconDirFormat)
                    intIndexCount += 1
                    intTemp += 1
                else:
                    objExcelWorksheet.write(intExcelRow, 10 + intTemp * 2, "-", objExcelRowRightFormat)
                    objExcelWorksheet.write(intExcelRow, 10 + intTemp * 2 + 1, "", objExcelRowIconFormat)
                    intTemp += 1
            intExcelRow += 1

            objExcelWorksheet.write(intExcelRow, 0, listPOSRPT01ProdH1SKU[intPOSRPT01ProdH1Index]["KA_SYSTEM_ACT_NM"], objExcelRowCenterFormat)
            objExcelWorksheet.write(intExcelRow, 1, listPOSRPT01ProdH1SKU[intPOSRPT01ProdH1Index]["KA_SYSTEM_CODE"], objExcelRowCenterFormat)
            objExcelWorksheet.write(intExcelRow, 2, listPOSRPT01ProdH1SKU[intPOSRPT01ProdH1Index]["KA_SYSTEM_NM"], objExcelRowCenterFormat)
            objExcelWorksheet.write(intExcelRow, 3, listPOSRPT01ProdH1SKU[intPOSRPT01ProdH1Index]["SALES_COM_ID_SA"], objExcelRowCenterFormat)
            objExcelWorksheet.write(intExcelRow, 4, listPOSRPT01ProdH1SKU[intPOSRPT01ProdH1Index]["SALES_COM_ABR_SA"], objExcelRowCenterFormat)
            objExcelWorksheet.write(intExcelRow, 5, "", objExcelRowCenterFormat)
            objExcelWorksheet.write(intExcelRow, 6, "", objExcelRowCenterFormat)
            objExcelWorksheet.write(intExcelRow, 7, listPOSRPT01ProdH1SKU[intPOSRPT01ProdH1Index]["PROD_H1_ID"], objExcelRowCenterFormat)
            objExcelWorksheet.write(intExcelRow, 8, listPOSRPT01ProdH1SKU[intPOSRPT01ProdH1Index]["PROD_H1_NM"], objExcelRowLeftFormat)
            objExcelWorksheet.write(intExcelRow, 9, "品项数", objExcelRowCenterFormat)

            intIndexCount = 0
            intIndexTemp = 0
            intTemp = 0
            for dictWeekNum in listWeekNum:
                intIndexTemp = intPOSRPT01ProdH1Index + intIndexCount
                if intIndexTemp < len(listPOSRPT01ProdH1SKU) and \
                   listPOSRPT01ProdH1SKU[intIndexTemp]["KA_SYSTEM_CODE"] == strKA_SYSTEM_CODE and \
                   listPOSRPT01ProdH1SKU[intIndexTemp]["PROD_H1_ID"] == listPOSRPT01ProdH1SKU[intPOSRPT01ProdH1Index]["PROD_H1_ID"] and \
                   listPOSRPT01ProdH1SKU[intIndexTemp]["POS_WEEK_NUM"] == listWeekNum[intTemp]["WEEK_NUM"]:

                    strDirection = ""
                    decTarget = 0
                    objExcelRowIconDirFormat = objExcelRowIconFormat
                    if (intIndexTemp + 1) < len(listPOSRPT01ProdH1SKU) and (intTemp + 1) < len(listWeekNum) and \
                       listPOSRPT01ProdH1SKU[intIndexTemp + 1]["KA_SYSTEM_CODE"] == strKA_SYSTEM_CODE and \
                       listPOSRPT01ProdH1SKU[intIndexTemp + 1]["PROD_H1_ID"] == listPOSRPT01ProdH1SKU[intPOSRPT01ProdH1Index]["PROD_H1_ID"] and \
                       listPOSRPT01ProdH1SKU[intIndexTemp + 1]["POS_WEEK_NUM"] == listWeekNum[intTemp + 1]["WEEK_NUM"]:

                        decTarget = listPOSRPT01ProdH1SKU[intIndexTemp + 1]["POS_SKU"]

                        if listPOSRPT01ProdH1SKU[intIndexTemp]["POS_SKU"] > decTarget:
                            strDirection = "▲"
                            if objExcelRowIconFormat == objExcelRowIcon1Format:
                                objExcelRowIconDirFormat = objExcelRowIcon1UpFormat
                            else:
                                objExcelRowIconDirFormat = objExcelRowIcon2UpFormat

                        elif listPOSRPT01ProdH1SKU[intIndexTemp]["POS_SKU"] < decTarget:
                            strDirection = "▼"
                            if objExcelRowIconFormat == objExcelRowIcon1Format:
                                objExcelRowIconDirFormat = objExcelRowIcon1DownFormat
                            else:
                                objExcelRowIconDirFormat = objExcelRowIcon2DownFormat

                        else:
                            strDirection = "━"
                            if objExcelRowIconFormat == objExcelRowIcon1Format:
                                objExcelRowIconDirFormat = objExcelRowIcon1FlatFormat
                            else:
                                objExcelRowIconDirFormat = objExcelRowIcon2FlatFormat

                    objExcelWorksheet.write(intExcelRow, 10 + intTemp * 2, listPOSRPT01ProdH1SKU[intIndexTemp]["POS_SKU"], objExcelRowRightFormat)
                    objExcelWorksheet.write(intExcelRow, 10 + intTemp * 2 + 1, strDirection, objExcelRowIconDirFormat)
                    intIndexCount += 1
                    intTemp += 1
                else:
                    objExcelWorksheet.write(intExcelRow, 10 + intTemp * 2, "-", objExcelRowRightFormat)
                    objExcelWorksheet.write(intExcelRow, 10 + intTemp * 2 + 1, "", objExcelRowIconFormat)
                    intTemp += 1
            intExcelRow += 1

            intPOSRPT01ProdH1Index += intIndexCount

        if objExcelWorksheet != None:
            objExcelWorksheet.freeze_panes("K8")
            objExcelWorksheet.autofilter("A7:CF" + str(intExcelRow))
            objExcelWorksheet.set_column('F:G', None, None, {'hidden': True})

        if objExcelWorkbook != None:
            objExcelWorkbook.close()
        return True

def execMailPOSRPT01(strJobPathRES, strDataDate):
    strEDIConnection = "3DW-DWuser@tpe-centos7-maria10-dw"
    strEDIDB = "DMMDL"

    listPOSRPT01 = getPOSRPT01List(strEDIConnection, strEDIDB, strDataDate)

    if listPOSRPT01[0]["POS_DATE"] == listPOSRPT01[0]["WEEK_LAST_DATE"]:

        listWeekNum = getWeekNumList(strEDIConnection, strEDIDB, strDataDate)
        listPOSRPT01System = getPOSRPT01SystemList(strEDIConnection, strEDIDB, strDataDate)
        listPOSRPT01SystemPCS = getPOSRPT01SystemPCSList(strEDIConnection, strEDIDB, strDataDate)
        listPOSRPT01SystemSKU = getPOSRPT01SystemSKUList(strEDIConnection, strEDIDB, strDataDate)
        listPOSRPT01ProdH1PCS = getPOSRPT01ProdH1PCSList(strEDIConnection, strEDIDB, strDataDate)
        listPOSRPT01ProdH1SKU = getPOSRPT01ProdH1SKUList(strEDIConnection, strEDIDB, strDataDate)
        
        if execWriteWorkbook(strJobPathRES, listWeekNum, listPOSRPT01, listPOSRPT01System, listPOSRPT01SystemPCS, listPOSRPT01SystemSKU, listPOSRPT01ProdH1PCS, listPOSRPT01ProdH1SKU) == True:
            strMessageSMTPServer = "tw-mail02.want-want.com"
            strMessageSMTPFrom = "Data.Center@want-want.com"

            for dictPOSRPT01System in listPOSRPT01System:
                strMessageSubject = dictPOSRPT01System["KA_SYSTEM_NM"] + "-现代渠道发展营业部业绩-通路系统品类周别POS推移-" + listPOSRPT01[0]["POS_DATE"]
                strContent = "尊敬的长官：早上好！\n敬请查阅：截止" + listPOSRPT01[0]["POS_DATE"][4:6] + "月" + listPOSRPT01[0]["POS_DATE"][-2:] + "日【" + dictPOSRPT01System["KA_SYSTEM_NM"] + "-现代渠道发展营业部业绩-通路系统品类周别POS推移报表】\n\n"
                strAttachFilePath = strJobPathRES.replace(".dat", "-" + dictPOSRPT01System["KA_SYSTEM_CODE"] + ".dat")
                strAttachFileName = dictPOSRPT01System["KA_SYSTEM_NM"] + "-现代渠道发展营业部业绩-通路系统品类周别POS推移-" + listPOSRPT01[0]["POS_DATE"] + ".xlsx"

                if dictPOSRPT01System["KA_SYSTEM_CODE"] == "H002":
                    #  H002 大润发 : 成骏 / 郭丹丹
                    arrayMessageSMTPTo = [ "Cheng_Jun2@want-want.com", "Guo_DanDan@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01System["KA_SYSTEM_CODE"] == "H005":
                    #  H005 麦德龙 : 左晓云 / 成骏 / 崔建辉
                    arrayMessageSMTPTo = [ "Zuo_XiaoYun2@want-want.com", "Cheng_Jun2@want-want.com", "Cui_JianHui@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01System["KA_SYSTEM_CODE"] == "H007":
                    #  H007 人人乐 : 郭鹏 / 宋涛
                    arrayMessageSMTPTo = [ "Guo_Peng@want-want.com", "Song_Tao2@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01System["KA_SYSTEM_CODE"] == "H009":
                    #  H009 世纪联华 : 郭鹏 / 成骏 / 宋涛
                    arrayMessageSMTPTo = [ "Guo_Peng@want-want.com", "Cheng_Jun2@want-want.com", "Song_Tao2@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01System["KA_SYSTEM_CODE"] == "H010":
                    #  H010 沃尔玛 : 郭鹏 / 王勇 / 成骏
                    arrayMessageSMTPTo = [ "Guo_Peng@want-want.com", "Wang_Yong@want-want.com", "Cheng_Jun2@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01System["KA_SYSTEM_CODE"] == "H011":
                    #  H011 物美 : 陈寿明 / 胡雪斌 / 黄华 / 王珑 / 鲍冠杰
                    arrayMessageSMTPTo = [ "chen_shouming@want-want.com", "hu_xuebin@want-want.com", "Huang_Hua@want-want.com", "Wang_Long2@want-want.com", "Bao_GuanJie@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01System["KA_SYSTEM_CODE"] == "H013":
                    #  H013 易初莲花 : 左晓云 / 成骏 / 崔建辉
                    arrayMessageSMTPTo = [ "Zuo_XiaoYun2@want-want.com", "Cheng_Jun2@want-want.com", "Cui_JianHui@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01System["KA_SYSTEM_CODE"] == "H016":
                    #  H016 丹尼斯 : 黄艳丽
                    arrayMessageSMTPTo = [ "huang_yanli2@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01System["KA_SYSTEM_CODE"] == "H017":
                    #  H017 天虹 : 章丽萍 / 张健 / 何丽琴
                    arrayMessageSMTPTo = [ "Zhang_LiPing2@want-want.com", "Zhang_Jian7@want-want.com", "he_liqin@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01System["KA_SYSTEM_CODE"] == "H018":
                    #  H018 华润万家 : 郭鹏 / 高贺 / 成骏
                    arrayMessageSMTPTo = [ "Guo_Peng@want-want.com", "Gao_He@want-want.com", "Cheng_Jun2@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01System["KA_SYSTEM_CODE"] == "H021":
                    #  H021 美特好 : 杨文卿
                    arrayMessageSMTPTo = [ "yang_wenqing@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01System["KA_SYSTEM_CODE"] == "H042":
                    #  H042 百佳华 : 王从阳 / 雷艳红 / 何丽琴
                    arrayMessageSMTPTo = [ "wang_chongyang@want-want.com", "lei_yanhong@want-want.com", "he_liqin@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01System["KA_SYSTEM_CODE"] == "H060":
                    #  H060 北国系统 : 艾贵银
                    arrayMessageSMTPTo = [ "ai_guiyin@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01System["KA_SYSTEM_CODE"] == "S001":
                    #  S001 农工商 : 郭鹏 / 成骏
                    arrayMessageSMTPTo = [ "Guo_Peng@want-want.com", "Cheng_Jun2@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01System["KA_SYSTEM_CODE"] == "S004":
                    #  S004 上海联华 : 郭鹏 / 成骏 / 宋涛
                    arrayMessageSMTPTo = [ "Guo_Peng@want-want.com", "Cheng_Jun2@want-want.com", "Song_Tao2@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01System["KA_SYSTEM_CODE"] == "S006":
                    #  S006 苏果 : 杨斯竣 / 成骏
                    arrayMessageSMTPTo = [ "Yang_SiJun@want-want.com", "Cheng_Jun2@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01System["KA_SYSTEM_CODE"] == "S009":
                    #  S009 中百便民 : 王宁
                    arrayMessageSMTPTo = [ "wang_ning2@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01System["KA_SYSTEM_CODE"] == "S010":
                    #  S010 中百仓储 : 王宁
                    arrayMessageSMTPTo = [ "wang_ning2@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01System["KA_SYSTEM_CODE"] == "S011":
                    #  S011 中商 : 王宁
                    arrayMessageSMTPTo = [ "wang_ning2@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01System["KA_SYSTEM_CODE"] == "S014":
                    #  S014 永辉 : 徐俊 / 张利霞 / 成骏
                    arrayMessageSMTPTo = [ "Xu_Jun6@want-want.com", "Zhang_LiXia@want-want.com", "Cheng_Jun2@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01System["KA_SYSTEM_CODE"] == "S018":
                    #  S018 武商 : 王宁
                    arrayMessageSMTPTo = [ "wang_ning2@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01System["KA_SYSTEM_CODE"] == "S020":
                    #  S020 威海糖酒 : 陈寿明 / 徐瑞虎
                    arrayMessageSMTPTo = [ "chen_shouming@want-want.com", "Xu_Ruihu@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01System["KA_SYSTEM_CODE"] == "S026":
                    #  S026 新世纪 : 刘爱民
                    arrayMessageSMTPTo = [ "Liu_AiMin@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01System["KA_SYSTEM_CODE"] == "S030":
                    #  S030 红旗连锁 : 向君
                    arrayMessageSMTPTo = [ "xiang_jun@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01System["KA_SYSTEM_CODE"] == "S031":
                    #  S031 银座 : 陈寿明 / 黄艳丽 / 徐瑞虎 / 王冰冰
                    arrayMessageSMTPTo = [ "chen_shouming@want-want.com", "huang_yanli2@want-want.com", "Xu_Ruihu@want-want.com", "wang_bingbing@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01System["KA_SYSTEM_CODE"] == "S044":
                    #  S044 北京华冠 : 陈寿明
                    arrayMessageSMTPTo = [ "chen_shouming@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01System["KA_SYSTEM_CODE"] == "S052":
                    #  S052 步步高 : 张健
                    arrayMessageSMTPTo = [ "Zhang_Jian7@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01System["KA_SYSTEM_CODE"] == "S063":
                    #  S063 新华都 : 朱巧燕
                    arrayMessageSMTPTo = [ "zhu_qiaoyan@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01System["KA_SYSTEM_CODE"] == "S110":
                    #  S110 联华华商 : 胡雪斌 / 鲍冠杰
                    arrayMessageSMTPTo = [ "hu_xuebin@want-want.com", "Bao_GuanJie@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01System["KA_SYSTEM_CODE"] == "S151":
                    #  S151 华联系统 : 王冰冰
                    arrayMessageSMTPTo = [ "wang_bingbing@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01System["KA_SYSTEM_CODE"] == "S219":
                    #  S219 介休吉隆斯 : 杨文卿
                    arrayMessageSMTPTo = [ "yang_wenqing@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01System["KA_SYSTEM_CODE"] == "S284":
                    #  S284 重客隆 : 刘爱民
                    arrayMessageSMTPTo = [ "Liu_AiMin@want-want.com", "Zoe.Hsu@want-want.com" ]
                else:
                    arrayMessageSMTPTo = [ "Zoe.Hsu@want-want.com" ]

                Message.sendSMTPMail(strMessageSMTPServer, strMessageSMTPFrom, arrayMessageSMTPTo, strMessageSubject, strContent, strAttachFilePath, strAttachFileName)

            return True
        else:
            return False
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

    execMailPOSRPT01(strJobPathRES, strDataDate)

if __name__ == "__main__":
    main()
