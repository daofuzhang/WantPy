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

def getPOSRPT01ComList(strEDIConnection, strEDIDB, strDataDate):
    strSQL = "SELECT SALES_COM_ID_SA, MAX(SALES_COM_ABR_SA) AS SALES_COM_ABR_SA " + \
             "FROM DMMDL.DC0024_POS_RPT01_COM " + \
             "WHERE CONVERT(POS_WEEK_NUM, INT)>=(CONVERT(LEFT({DATA_DATE}, 4), INT) - 1)*100+49 " + \
             "GROUP BY SALES_COM_ID_SA " + \
             "ORDER BY SALES_COM_ID_SA; "

    dictMariaParameter = {
        "DATA_DATE": MariaEntity.MariaParameter(objValue=strDataDate, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listPOSRPT01Com = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listPOSRPT01Com

def getPOSRPT01ComPCSList(strEDIConnection, strEDIDB, strDataDate):
    strSQL = "SELECT SALES_COM_ID_SA, SALES_COM_ABR_SA, POS_WEEK_NUM " + \
             "     , ROUND(POS_QTY_PCS, 0) AS POS_QTY_PCS " + \
             "FROM DMMDL.DC0024_POS_RPT01_COM " + \
             "WHERE CONVERT(POS_WEEK_NUM, INT)>=(CONVERT(LEFT({DATA_DATE}, 4), INT) - 1)*100+49 " + \
             "ORDER BY SALES_COM_ID_SA, POS_WEEK_NUM DESC; "

    dictMariaParameter = {
        "DATA_DATE": MariaEntity.MariaParameter(objValue=strDataDate, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listPOSRPT01ComPCS = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listPOSRPT01ComPCS

def getPOSRPT01ComSKUList(strEDIConnection, strEDIDB, strDataDate):
    strSQL = "SELECT SALES_COM_ID_SA, SALES_COM_ABR_SA, POS_WEEK_NUM " + \
             "     , POS_SKU " + \
             "FROM DMMDL.DC0024_POS_RPT01_COM " + \
             "WHERE CONVERT(POS_WEEK_NUM, INT)>=(CONVERT(LEFT({DATA_DATE}, 4), INT) - 1)*100+49 " + \
             "ORDER BY SALES_COM_ID_SA, POS_WEEK_NUM DESC; "

    dictMariaParameter = {
        "DATA_DATE": MariaEntity.MariaParameter(objValue=strDataDate, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listPOSRPT01ComSKU = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listPOSRPT01ComSKU

def getPOSRPT01ProdH1PCSList(strEDIConnection, strEDIDB, strDataDate):
    strSQL = "SELECT KA_SYSTEM_CODE, KA_SYSTEM_NM, KA_SYSTEM_ACT_NM " + \
             "     , SALES_COM_ID_SA, SALES_COM_ABR_SA " + \
             "     , PROD_H1_ID, PROD_H1_NM, POS_WEEK_NUM " + \
             "     , ROUND(POS_QTY_PCS, 0) AS POS_QTY_PCS " + \
             "FROM DMMDL.DC0024_POS_RPT01_PRODH1 " + \
             "WHERE CONVERT(POS_WEEK_NUM, INT)>=(CONVERT(LEFT({DATA_DATE}, 4), INT) - 1)*100+49 " + \
             "ORDER BY SALES_COM_ID_SA, KA_SYSTEM_CODE, PROD_H1_ID, POS_WEEK_NUM DESC; "

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
             "ORDER BY SALES_COM_ID_SA, KA_SYSTEM_CODE, PROD_H1_ID, POS_WEEK_NUM DESC; "

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

def execWriteWorkbook(strJobPathRES, listWeekNum, listPOSRPT01, listPOSRPT01Com, listPOSRPT01ComPCS, listPOSRPT01ComSKU, listPOSRPT01ProdH1PCS, listPOSRPT01ProdH1SKU):
    if len(listWeekNum) == 0 or len(listPOSRPT01) == 0 or len(listPOSRPT01ProdH1PCS) != len(listPOSRPT01ProdH1SKU) or len(listPOSRPT01ComPCS) != len(listPOSRPT01ComSKU):
        return False
    else:
        objExcelWorkbook = None
        objExcelWorksheet = None
        
        objExcelRowCenterFormat = None
        objExcelRowLeftFormat = None
        objExcelRowRightFormat = None

        strSALES_COM_ID_SA = None
        strSALES_COM_ABR_SA = None

        intPOSRPT01ComIndex = 0
        intPOSRPT01ProdH1Index = 0

        intExcelRow = 0

        intNowDates = (Common.getDate(listPOSRPT01[0]["POS_DATE"]) - Common.getDate(listWeekNum[0]["WEEK_FIRST_DATE"])).days + 1

        while intPOSRPT01ProdH1Index < len(listPOSRPT01ProdH1PCS):
            if strSALES_COM_ID_SA != listPOSRPT01ProdH1PCS[intPOSRPT01ProdH1Index]["SALES_COM_ID_SA"]:
                strSALES_COM_ID_SA = listPOSRPT01ProdH1PCS[intPOSRPT01ProdH1Index]["SALES_COM_ID_SA"]
                strSALES_COM_ABR_SA = listPOSRPT01ProdH1PCS[intPOSRPT01ProdH1Index]["SALES_COM_ABR_SA"]

                if objExcelWorksheet != None:
                    objExcelWorksheet.freeze_panes("K8")
                    objExcelWorksheet.autofilter("A7:CF" + str(intExcelRow))
                    objExcelWorksheet.set_column('F:G', None, None, {'hidden': True})

                if objExcelWorkbook != None:
                    objExcelWorkbook.close()
                
                objExcelWorkbook = xlsxwriter.Workbook(strJobPathRES.replace(".dat", "-" + strSALES_COM_ID_SA + ".dat"))

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

                objExcelWorksheet = objExcelWorkbook.add_worksheet(strSALES_COM_ID_SA + "-" + strSALES_COM_ABR_SA)

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

                objExcelWorksheet.merge_range("A1:I1", "现代渠道发展营业部业绩－分公司系统品类周别POS推移", objExcelTitleFormat)
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

                objExcelWorksheet.write(intExcelRow, 0, "", objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 1, "", objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 2, "", objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 3, strSALES_COM_ID_SA, objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 4, strSALES_COM_ABR_SA, objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 5, "", objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 6, "", objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 7, "", objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 8, "合计", objExcelRowLeftFormat)
                objExcelWorksheet.write(intExcelRow, 9, "销售数量", objExcelRowCenterFormat)

                intIndexCount = 0
                intIndexTemp = 0
                intTemp = 0
                for dictWeekNum in listWeekNum:
                    intIndexTemp = intPOSRPT01ComIndex + intIndexCount
                    if intIndexTemp < len(listPOSRPT01ComPCS) and \
                       listPOSRPT01ComPCS[intIndexTemp]["SALES_COM_ID_SA"] == strSALES_COM_ID_SA and \
                       listPOSRPT01ComPCS[intIndexTemp]["POS_WEEK_NUM"] == listWeekNum[intTemp]["WEEK_NUM"]:

                        strDirection = ""
                        decTarget = 0
                        objExcelRowIconDirFormat = objExcelRowIconFormat
                        if (intIndexTemp + 1) < len(listPOSRPT01ComPCS) and (intTemp + 1) < len(listWeekNum) and \
                           listPOSRPT01ComPCS[intIndexTemp + 1]["SALES_COM_ID_SA"] == strSALES_COM_ID_SA and \
                           listPOSRPT01ComPCS[intIndexTemp + 1]["POS_WEEK_NUM"] == listWeekNum[intTemp + 1]["WEEK_NUM"]:

                            if intTemp == 0:
                                decTarget = round(listPOSRPT01ComPCS[intIndexTemp + 1]["POS_QTY_PCS"] / 7 * intNowDates, 0)
                            else:
                                decTarget = listPOSRPT01ComPCS[intIndexTemp + 1]["POS_QTY_PCS"]

                            if listPOSRPT01ComPCS[intIndexTemp]["POS_QTY_PCS"] > decTarget:
                                strDirection = "▲"
                                if objExcelRowIconFormat == objExcelRowIcon1Format:
                                    objExcelRowIconDirFormat = objExcelRowIcon1UpFormat
                                else:
                                    objExcelRowIconDirFormat = objExcelRowIcon2UpFormat

                            elif listPOSRPT01ComPCS[intIndexTemp]["POS_QTY_PCS"] < decTarget:
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

                        objExcelWorksheet.write(intExcelRow, 10 + intTemp * 2, listPOSRPT01ComPCS[intIndexTemp]["POS_QTY_PCS"], objExcelRowRightFormat)
                        objExcelWorksheet.write(intExcelRow, 10 + intTemp * 2 + 1, strDirection, objExcelRowIconDirFormat)
                        intIndexCount += 1
                        intTemp += 1
                    else:
                        objExcelWorksheet.write(intExcelRow, 10 + intTemp * 2, "-", objExcelRowRightFormat)
                        objExcelWorksheet.write(intExcelRow, 10 + intTemp * 2 + 1, "", objExcelRowIconFormat)
                        intTemp += 1
                intExcelRow += 1

                objExcelWorksheet.write(intExcelRow, 0, "", objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 1, "", objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 2, "", objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 3, strSALES_COM_ID_SA, objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 4, strSALES_COM_ABR_SA, objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 5, "", objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 6, "", objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 7, "", objExcelRowCenterFormat)
                objExcelWorksheet.write(intExcelRow, 8, "合计", objExcelRowLeftFormat)
                objExcelWorksheet.write(intExcelRow, 9, "品项数", objExcelRowCenterFormat)

                intIndexCount = 0
                intIndexTemp = 0
                intTemp = 0
                for dictWeekNum in listWeekNum:
                    intIndexTemp = intPOSRPT01ComIndex + intIndexCount
                    if intIndexTemp < len(listPOSRPT01ComSKU) and \
                       listPOSRPT01ComSKU[intIndexTemp]["SALES_COM_ID_SA"] == strSALES_COM_ID_SA and \
                       listPOSRPT01ComSKU[intIndexTemp]["POS_WEEK_NUM"] == listWeekNum[intTemp]["WEEK_NUM"]:

                        strDirection = ""
                        decTarget = 0
                        objExcelRowIconDirFormat = objExcelRowIconFormat
                        if (intIndexTemp + 1) < len(listPOSRPT01ComSKU) and (intTemp + 1) < len(listWeekNum) and \
                           listPOSRPT01ComSKU[intIndexTemp + 1]["SALES_COM_ID_SA"] == strSALES_COM_ID_SA and \
                           listPOSRPT01ComSKU[intIndexTemp + 1]["POS_WEEK_NUM"] == listWeekNum[intTemp + 1]["WEEK_NUM"]:

                            decTarget = listPOSRPT01ComSKU[intIndexTemp + 1]["POS_SKU"]

                            if listPOSRPT01ComSKU[intIndexTemp]["POS_SKU"] > decTarget:
                                strDirection = "▲"
                                if objExcelRowIconFormat == objExcelRowIcon1Format:
                                    objExcelRowIconDirFormat = objExcelRowIcon1UpFormat
                                else:
                                    objExcelRowIconDirFormat = objExcelRowIcon2UpFormat

                            elif listPOSRPT01ComSKU[intIndexTemp]["POS_SKU"] < decTarget:
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

                        objExcelWorksheet.write(intExcelRow, 10 + intTemp * 2, listPOSRPT01ComSKU[intIndexTemp]["POS_SKU"], objExcelRowRightFormat)
                        objExcelWorksheet.write(intExcelRow, 10 + intTemp * 2 + 1, strDirection, objExcelRowIconDirFormat)
                        intIndexCount += 1
                        intTemp += 1
                    else:
                        objExcelWorksheet.write(intExcelRow, 10 + intTemp * 2, "-", objExcelRowRightFormat)
                        objExcelWorksheet.write(intExcelRow, 10 + intTemp * 2 + 1, "", objExcelRowIconFormat)
                        intTemp += 1
                intExcelRow += 1

                intPOSRPT01ComIndex += intIndexCount

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
                   listPOSRPT01ProdH1PCS[intIndexTemp]["SALES_COM_ID_SA"] == strSALES_COM_ID_SA and \
                   listPOSRPT01ProdH1PCS[intIndexTemp]["PROD_H1_ID"] == listPOSRPT01ProdH1PCS[intPOSRPT01ProdH1Index]["PROD_H1_ID"] and \
                   listPOSRPT01ProdH1PCS[intIndexTemp]["POS_WEEK_NUM"] == listWeekNum[intTemp]["WEEK_NUM"]:

                    strDirection = ""
                    decTarget = 0
                    objExcelRowIconDirFormat = objExcelRowIconFormat
                    if (intIndexTemp + 1) < len(listPOSRPT01ProdH1PCS) and (intTemp + 1) < len(listWeekNum) and \
                       listPOSRPT01ProdH1PCS[intIndexTemp + 1]["SALES_COM_ID_SA"] == strSALES_COM_ID_SA and \
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
                   listPOSRPT01ProdH1SKU[intIndexTemp]["SALES_COM_ID_SA"] == strSALES_COM_ID_SA and \
                   listPOSRPT01ProdH1SKU[intIndexTemp]["PROD_H1_ID"] == listPOSRPT01ProdH1SKU[intPOSRPT01ProdH1Index]["PROD_H1_ID"] and \
                   listPOSRPT01ProdH1SKU[intIndexTemp]["POS_WEEK_NUM"] == listWeekNum[intTemp]["WEEK_NUM"]:

                    strDirection = ""
                    decTarget = 0
                    objExcelRowIconDirFormat = objExcelRowIconFormat
                    if (intIndexTemp + 1) < len(listPOSRPT01ProdH1SKU) and (intTemp + 1) < len(listWeekNum) and \
                       listPOSRPT01ProdH1SKU[intIndexTemp + 1]["SALES_COM_ID_SA"] == strSALES_COM_ID_SA and \
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
        listPOSRPT01Com = getPOSRPT01ComList(strEDIConnection, strEDIDB, strDataDate)
        listPOSRPT01ComPCS = getPOSRPT01ComPCSList(strEDIConnection, strEDIDB, strDataDate)
        listPOSRPT01ComSKU = getPOSRPT01ComSKUList(strEDIConnection, strEDIDB, strDataDate)
        listPOSRPT01ProdH1PCS = getPOSRPT01ProdH1PCSList(strEDIConnection, strEDIDB, strDataDate)
        listPOSRPT01ProdH1SKU = getPOSRPT01ProdH1SKUList(strEDIConnection, strEDIDB, strDataDate)
        
        if execWriteWorkbook(strJobPathRES, listWeekNum, listPOSRPT01, listPOSRPT01Com, listPOSRPT01ComPCS, listPOSRPT01ComSKU, listPOSRPT01ProdH1PCS, listPOSRPT01ProdH1SKU) == True:
            strMessageSMTPServer = "tw-mail02.want-want.com"
            strMessageSMTPFrom = "Data.Center@want-want.com"

            for dictPOSRPT01Com in listPOSRPT01Com:
                strMessageSubject = dictPOSRPT01Com["SALES_COM_ABR_SA"] + "-现代渠道发展营业部业绩-分公司系统品类周别POS推移-" + listPOSRPT01[0]["POS_DATE"]
                strContent = "尊敬的长官：早上好！\n敬请查阅：截止" + listPOSRPT01[0]["POS_DATE"][4:6] + "月" + listPOSRPT01[0]["POS_DATE"][-2:] + "日【" + dictPOSRPT01Com["SALES_COM_ABR_SA"] + "-现代渠道发展营业部业绩-分公司系统品类周别POS推移报表】\n\n"
                strAttachFilePath = strJobPathRES.replace(".dat", "-" + dictPOSRPT01Com["SALES_COM_ID_SA"] + ".dat")
                strAttachFileName = dictPOSRPT01Com["SALES_COM_ABR_SA"] + "-现代渠道发展营业部业绩-分公司系统品类周别POS推移-" + listPOSRPT01[0]["POS_DATE"] + ".xlsx"

                if dictPOSRPT01Com["SALES_COM_ID_SA"] == "C101":
                    # C101 杭州分 : 胡雪斌
                    arrayMessageSMTPTo = [ "hu_xuebin@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C111":
                    # C111 上海分 : 黄华
                    arrayMessageSMTPTo = [ "Huang_Hua@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C121":
                    # C121 温州分 : 鲍冠杰
                    arrayMessageSMTPTo = [ "Bao_GuanJie@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C131":
                    # C131 苏州分 : 栾瑞晨
                    arrayMessageSMTPTo = [ "Luan_RuiChen@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C141":
                    # C141 南京分 : 戴萍
                    arrayMessageSMTPTo = [ "dai_ping2@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C181":
                    # C181 青岛分 : 徐瑞虎
                    arrayMessageSMTPTo = [ "Xu_Ruihu@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C191":
                    # C191 哈尔滨分 : 付涛
                    arrayMessageSMTPTo = [ "fu_tao@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C201":
                    # C201 北京分 : 陈寿明
                    arrayMessageSMTPTo = [ "chen_shouming@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C211":
                    # C211 天津分 : 王珑
                    arrayMessageSMTPTo = [ "Wang_Long2@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C221":
                    # C221 长春分 : 付涛
                    arrayMessageSMTPTo = [ "fu_tao@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C231":
                    # C231 沈阳分 : 付涛
                    arrayMessageSMTPTo = [ "fu_tao@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C241":
                    # C241 石家庄分 : 艾贵银
                    arrayMessageSMTPTo = [ "ai_guiyin@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C251":
                    # C251 太原分 : 杨文卿
                    arrayMessageSMTPTo = [ "yang_wenqing@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C271":
                    # C271 广州分 : 雷艳红
                    arrayMessageSMTPTo = [ "lei_yanhong@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C281":
                    # C281 深圳分 : 何丽琴
                    arrayMessageSMTPTo = [ "he_liqin@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C291":
                    # C291 海南分 : 雷艳红
                    arrayMessageSMTPTo = [ "lei_yanhong@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C311":
                    # C311 南昌分 : 章丽萍
                    arrayMessageSMTPTo = [ "Zhang_LiPing2@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C321":
                    # C321 福州分 : 朱巧燕
                    arrayMessageSMTPTo = [ "zhu_qiaoyan@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C341":
                    # C341 长沙分 : 张健
                    arrayMessageSMTPTo = [ "Zhang_Jian7@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C351":
                    # C351 贵阳分 : 
                    arrayMessageSMTPTo = [ "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C361":
                    # C361 成都分 : 向君
                    arrayMessageSMTPTo = [ "xiang_jun@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C371":
                    # C371 重庆分 : 刘爱民
                    arrayMessageSMTPTo = [ "Liu_AiMin@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C381":
                    # C381 昆明分 : 向君
                    arrayMessageSMTPTo = [ "xiang_jun@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C391":
                    # C391 兰州分 : 袁兴卉
                    arrayMessageSMTPTo = [ "yuan_xinghui@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C411":
                    # C411 宁波分 : 鲍冠杰
                    arrayMessageSMTPTo = [ "Bao_GuanJie@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C441":
                    # C441 包头分 : 郭鹏
                    arrayMessageSMTPTo = [ "Guo_Peng@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C461":
                    # C461 合肥分 : 陈都
                    arrayMessageSMTPTo = [ "Chen_Dou@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C491":
                    # C491 郑州分 : 黄艳丽
                    arrayMessageSMTPTo = [ "huang_yanli2@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C501":
                    # C501 济南分 : 王冰冰
                    arrayMessageSMTPTo = [ "wang_bingbing@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C551":
                    # C551 武汉分 : 王宁
                    arrayMessageSMTPTo = [ "wang_ning2@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C751":
                    # C751 漯河分 : 黄艳丽
                    arrayMessageSMTPTo = [ "huang_yanli2@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C771":
                    # C771 南宁分 : 段勇花
                    arrayMessageSMTPTo = [ "duan_yonghua2@want-want.com", "Zoe.Hsu@want-want.com" ]
                elif dictPOSRPT01Com["SALES_COM_ID_SA"] == "C781":
                    # C781 西安分 : 袁兴卉
                    arrayMessageSMTPTo = [ "yuan_xinghui@want-want.com", "Zoe.Hsu@want-want.com" ]
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
