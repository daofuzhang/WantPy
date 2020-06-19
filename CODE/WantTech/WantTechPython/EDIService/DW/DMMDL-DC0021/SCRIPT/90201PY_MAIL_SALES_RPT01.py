import os
import sys
import logging
import xlsxwriter
from Utility import Common
from Utility import Message
from Entity import DBEntity
from Entity import MariaEntity
from EDI import EDIEntity

def getSalesRPT01HeadList(strEDIConnection, strEDIDB, strDataDate):
    strSQL = "SELECT DATA_DATE, DATA_DATE1, DATA_DATE2 " + \
             "     , WORKDAYS, WORKDAY_TOTAL, ROUND(WORKDAY_PC, 3) AS WORKDAY_PC " + \
             "     , ROUND(BU_AMT_SD/1000, 0) AS BU_AMT_SD " + \
             "     , ROUND(BU_AMT_D/1000, 0) AS BU_AMT_D " + \
             "     , ROUND(BU_AMT_POSTING/1000, 0) AS BU_AMT_POSTING " + \
             "     , ROUND(BU_AMT_LAST_ALL/1000, 0) AS BU_AMT_LAST_ALL " + \
             "     , ROUND(BU_AMT_PC/1000, 0) AS BU_AMT_PC " + \
             "     , ROUND(BU_REQ/1000, 0) AS BU_REQ " + \
             "FROM DMMDL.DC0021_SALES_RPT01_HEAD " + \
             "WHERE {DATA_DATE}; "

    dictMariaParameter = {
        "DATA_DATE": MariaEntity.MariaParameter(strOperator="=", objValue=strDataDate, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listSalesRPT01Head = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listSalesRPT01Head

def getSalesRPT01List(strEDIConnection, strEDIDB, strDataDate):
    strSQL = "SELECT C.CODE_ID AS BU01_ID, C.CODE_NM AS BU01_NM " + \
             "     , ROUND(R.BU_AMT_SD2/1000, 0) AS BU_AMT_SD2 " + \
             "     , ROUND(R.BU_AMT_SD1/1000, 0) AS BU_AMT_SD1 " + \
             "     , ROUND(R.BU_AMT_SD/1000, 0) AS BU_AMT_SD " + \
             "     , ROUND(R.BU_AMT_D/1000, 0) AS BU_AMT_D " + \
             "     , ROUND(R.BU_AMT_LAST_ALL/1000, 0) AS BU_AMT_LAST_ALL " + \
             "     , ROUND(R.BU_AMT_PC, 3) AS BU_AMT_PC " + \
             "     , ROUND(R.BU_AMT_DIF_ALL/1000, 0) AS BU_AMT_DIF_ALL " + \
             "     , ROUND(R.BU_AMT_LAST/1000, 0) AS BU_AMT_LAST " + \
             "     , ROUND(R.BU_AMT_GR, 3) AS BU_AMT_GR " + \
             "     , ROUND(R.BU_AMT_DIF/1000, 0) AS BU_AMT_DIF " + \
             "     , ROUND(R.BU_AMT_STMT/1000, 0) AS BU_AMT_STMT " + \
             "     , ROUND(R.BU_AMT_STMT_DIF/1000, 0) AS BU_AMT_STMT_DIF " + \
             "     , ROUND(R.BU_REQ/1000, 0) AS BU_REQ " + \
             "     , ROUND(R.BU_REQ_PC, 3) AS BU_REQ_PC " + \
             "     , ROUND(R.BU_REQ_DIF/1000, 0) AS BU_REQ_DIF " + \
             "FROM DMMDL.CM_CODE C " + \
             "LEFT JOIN (SELECT * FROM DMMDL.DC0021_SALES_RPT01 WHERE DATA_DATE={DATA_DATE}) R " + \
             "ON C.CODE_KIND='0001' AND C.CODE_ID=R.BU01_ID " + \
             "WHERE C.IS_DELETED='N' AND C.CODE_ID<>'NULL' " + \
             "ORDER BY C.SORT_ORDER; "

    dictMariaParameter = {
        "DATA_DATE": MariaEntity.MariaParameter(objValue=strDataDate, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listSalesRPT01 = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listSalesRPT01

def getSalesRPT01SubTotalList(strEDIConnection, strEDIDB, strDataDate):
    strSQL = "SELECT ROUND(SUM(R.BU_AMT_SD2)/1000, 0) AS BU_AMT_SD2 " + \
             "     , ROUND(SUM(R.BU_AMT_SD1)/1000, 0) AS BU_AMT_SD1 " + \
             "     , ROUND(SUM(R.BU_AMT_SD)/1000, 0) AS BU_AMT_SD " + \
             "     , ROUND(SUM(R.BU_AMT_D)/1000, 0) AS BU_AMT_D " + \
             "     , ROUND(SUM(R.BU_AMT_LAST_ALL)/1000, 0) AS BU_AMT_LAST_ALL " + \
             "     , ROUND((CASE WHEN SUM(R.BU_AMT_LAST_ALL)=0 THEN 0 ELSE SUM(R.BU_AMT_D)/SUM(R.BU_AMT_LAST_ALL) END), 3) AS BU_AMT_PC " + \
             "     , ROUND(SUM(R.BU_AMT_DIF_ALL)/1000, 0) AS BU_AMT_DIF_ALL " + \
             "     , ROUND(SUM(R.BU_AMT_LAST)/1000, 0) AS BU_AMT_LAST " + \
             "     , ROUND((CASE WHEN SUM(R.BU_AMT_LAST)=0 THEN 0 ELSE (SUM(R.BU_AMT_D)-SUM(R.BU_AMT_LAST))/SUM(R.BU_AMT_LAST) END), 3) AS BU_AMT_GR " + \
             "     , ROUND(SUM(R.BU_AMT_DIF)/1000, 0) AS BU_AMT_DIF " + \
             "     , ROUND(SUM(R.BU_AMT_STMT)/1000, 0) AS BU_AMT_STMT " + \
             "     , ROUND(SUM(R.BU_AMT_STMT_DIF)/1000, 0) AS BU_AMT_STMT_DIF " + \
             "     , ROUND(SUM(R.BU_REQ)/1000, 0) AS BU_REQ " + \
             "     , ROUND((CASE WHEN SUM(R.BU_REQ)=0 THEN 0 ELSE (SUM(R.BU_AMT_D)/SUM(R.BU_REQ)) END), 3) AS BU_REQ_PC " + \
             "     , ROUND(SUM(R.BU_REQ_DIF)/1000, 0) AS BU_REQ_DIF " + \
             "FROM DMMDL.DC0021_SALES_RPT01 R " + \
             "WHERE R.DATA_DATE={DATA_DATE} " + \
             " AND R.BU01_ID IN ('BU01', 'BU02', 'BU03', 'BU04', 'BU05', 'BU06', 'BU07', 'BU08'); "

    dictMariaParameter = {
        "DATA_DATE": MariaEntity.MariaParameter(objValue=strDataDate, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listSalesRPT01SubTotal = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listSalesRPT01SubTotal

def getSalesRPT01TotalList(strEDIConnection, strEDIDB, strDataDate):
    strSQL = "SELECT ROUND(SUM(R.BU_AMT_SD2)/1000, 0) AS BU_AMT_SD2 " + \
             "     , ROUND(SUM(R.BU_AMT_SD1)/1000, 0) AS BU_AMT_SD1 " + \
             "     , ROUND(SUM(R.BU_AMT_SD)/1000, 0) AS BU_AMT_SD " + \
             "     , ROUND(SUM(R.BU_AMT_D)/1000, 0) AS BU_AMT_D " + \
             "     , ROUND(SUM(R.BU_AMT_LAST_ALL)/1000, 0) AS BU_AMT_LAST_ALL " + \
             "     , ROUND((CASE WHEN SUM(R.BU_AMT_LAST_ALL)=0 THEN 0 ELSE SUM(R.BU_AMT_D)/SUM(R.BU_AMT_LAST_ALL) END), 3) AS BU_AMT_PC " + \
             "     , ROUND(SUM(R.BU_AMT_DIF_ALL)/1000, 0) AS BU_AMT_DIF_ALL " + \
             "     , ROUND(SUM(R.BU_AMT_LAST)/1000, 0) AS BU_AMT_LAST " + \
             "     , ROUND((CASE WHEN SUM(R.BU_AMT_LAST)=0 THEN 0 ELSE (SUM(R.BU_AMT_D)-SUM(R.BU_AMT_LAST))/SUM(R.BU_AMT_LAST) END), 3) AS BU_AMT_GR " + \
             "     , ROUND(SUM(R.BU_AMT_DIF)/1000, 0) AS BU_AMT_DIF " + \
             "     , ROUND(SUM(R.BU_AMT_STMT)/1000, 0) AS BU_AMT_STMT " + \
             "     , ROUND(SUM(R.BU_AMT_STMT_DIF)/1000, 0) AS BU_AMT_STMT_DIF " + \
             "     , ROUND(SUM(R.BU_REQ)/1000, 0) AS BU_REQ " + \
             "     , ROUND((CASE WHEN SUM(R.BU_REQ)=0 THEN 0 ELSE (SUM(R.BU_AMT_D)/SUM(R.BU_REQ)) END), 3) AS BU_REQ_PC " + \
             "     , ROUND(SUM(R.BU_REQ_DIF)/1000, 0) AS BU_REQ_DIF " + \
             "FROM DMMDL.DC0021_SALES_RPT01 R " + \
             "WHERE R.DATA_DATE={DATA_DATE}; "

    dictMariaParameter = {
        "DATA_DATE": MariaEntity.MariaParameter(objValue=strDataDate, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listSalesRPT01Total = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listSalesRPT01Total

def getSalesRPT01GRList(strEDIConnection, strEDIDB, strDataDate):
    strSQL = "SELECT A.BU01_NM, A.BU_AMT_GR " + \
             "FROM (SELECT BU01_NM, ROUND(BU_AMT_GR, 3) AS BU_AMT_GR " + \
             "      FROM DMMDL.DC0021_SALES_RPT01 " + \
             "      WHERE DATA_DATE={DATA_DATE} " + \
             "        AND BU01_ID IN ('BU01', 'BU02', 'BU03', 'BU04', 'BU05', 'BU06', 'BU07', 'BU08')) A " + \
             "ORDER BY A.BU_AMT_GR DESC; "

    dictMariaParameter = {
        "DATA_DATE": MariaEntity.MariaParameter(objValue=strDataDate, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listSalesRPT01GR = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listSalesRPT01GR

def getProgressBar(strValue):
    if strValue == "-" or strValue == "":
        strProgressBar = ""
    elif strValue > 0 and strValue <= 0.05:
        strProgressBar = "▌"
    elif strValue > 0.05 and strValue <= 0.1:
        strProgressBar = "█"
    elif strValue > 0.1 and strValue <= 0.15:
        strProgressBar = "█▌"
    elif strValue > 0.15 and strValue <= 0.2:
        strProgressBar = "██"
    elif strValue > 0.2 and strValue <= 0.25:
        strProgressBar = "██▌"
    elif strValue > 0.25 and strValue <= 0.3:
        strProgressBar = "███"
    elif strValue > 0.3 and strValue <= 0.35:
        strProgressBar = "███▌"
    elif strValue > 0.35 and strValue <= 0.4:
        strProgressBar = "████"
    elif strValue > 0.4 and strValue <= 0.45:
        strProgressBar = "████▌"
    elif strValue > 0.45 and strValue <= 0.5:
        strProgressBar = "█████"
    elif strValue > 0.5 and strValue <= 0.55:
        strProgressBar = "█████▌"
    elif strValue > 0.55 and strValue <= 0.6:
        strProgressBar = "██████"
    elif strValue > 0.6 and strValue <= 0.65:
        strProgressBar = "██████▌"
    elif strValue > 0.65 and strValue <= 0.7:
        strProgressBar = "███████"
    elif strValue > 0.7 and strValue <= 0.75:
        strProgressBar = "███████▌"
    elif strValue > 0.75 and strValue <= 0.8:
        strProgressBar = "████████"
    elif strValue > 0.8 and strValue <= 0.85:
        strProgressBar = "████████▌"
    elif strValue > 0.85 and strValue <= 0.9:
        strProgressBar = "█████████"
    elif strValue > 0.9 and strValue <= 0.95:
        strProgressBar = "█████████▌"
    elif strValue > 0.95:
        strProgressBar = "██████████"
    else:
        strProgressBar = ""
    return strProgressBar


def execWriteWorkbook(strJobPathRES, listSalesRPT01Head, listSalesRPT01, listSalesRPT01SubTotal, listSalesRPT01Total, listSalesRPT01GR):
    if len(listSalesRPT01Head) == 0 or len(listSalesRPT01) == 0 or len(listSalesRPT01SubTotal) == 0 or len(listSalesRPT01Total) == 0:
        return False
    else:
        strWorkPath = None
        objBook = None
        objSheet = None
        intRowIndex = 0
        
        strWorkPath = os.path.dirname(os.path.realpath(__file__))

        objBook = xlsxwriter.Workbook(strJobPathRES)
        objSheet = objBook.add_worksheet("营业部日进度")
        objSheet.protect("n674-PtVT$aq", { "select_locked_cells": False, "select_unlocked_cells": False })

        objSheet.set_default_row(30)
        objSheet.set_row(3, 36)
        objSheet.set_row(4, 36)
        objSheet.set_row(5, 36)
        objSheet.set_row(6, 36)
        objSheet.set_row(7, 36)
        objSheet.set_row(14, 36)

        objSheet.set_column(0, 0, 5)
        objSheet.set_column(1, 1, 5)
        objSheet.set_column(2, 2, 5)
        objSheet.set_column(3, 3, 7.5)
        objSheet.set_column(4, 4, 7.5)
        objSheet.set_column(5, 5, 7.5)
        objSheet.set_column(6, 6, 13)
        objSheet.set_column(7, 7, 8)
        objSheet.set_column(8, 8, 10)
        objSheet.set_column(9, 9, 13)
        objSheet.set_column(10, 10, 8)
        objSheet.set_column(11, 11, 10)
        objSheet.set_column(12, 12, 10)
        objSheet.set_column(13, 13, 9)
        objSheet.set_column(14, 14, 9)
        objSheet.set_column(15, 15, 9)
        objSheet.set_column(16, 16, 8)
        objSheet.set_column(17, 17, 8)
        objSheet.set_column(18, 18, 8)
        objSheet.set_column(19, 19, 8)

        objFormatBlank = objBook.add_format({ 
            "fg_color": "#FFFFFF",
            "border": 1, "top_color": "#FFFFFF", "bottom_color": "#FFFFFF", "left_color": "#FFFFFF", "right_color": "#FFFFFF", "left": 1, "right": 1, "top": 1, "bottom": 1
        })

        intBUAmtPC = listSalesRPT01Total[0]["BU_AMT_PC"]*100
        strBUAmtPC = "BU_AMT_PC.png"
        if intBUAmtPC > 100:
            strBUAmtPC = "BU_AMT_PC_100.png"
        elif intBUAmtPC > 0 and intBUAmtPC%2 == 0:
            strBUAmtPC = "BU_AMT_PC_" + ("0" + str(round(intBUAmtPC//2*2, 0)))[-2:] + ".png"
        elif intBUAmtPC > 0:
            strBUAmtPC = "BU_AMT_PC_" + ("0" + str(round((intBUAmtPC//2*2)+2, 0)))[-2:] + ".png"

        objSheet.insert_image("N4", strWorkPath + "/IMG/" + strBUAmtPC, { "x_scale": 0.75, "y_scale": 0.8, "x_offset": 0, "y_offset": 0 })

        objOption = { "width": 80, "height": 30, "x_offset": 25, "y_offset": 0, "font": { "size": 18, "name": "Aharoni" }, "fill": { "none": True }, "line": { "none": True }, "rotation": 45 }
        objSheet.insert_textbox("O7", str(round(intBUAmtPC, 1)) + "%", objOption)

        strMonth = str(int(listSalesRPT01Head[0]["DATA_DATE"][-4:][:2]))
        strDate = str(int(listSalesRPT01Head[0]["DATA_DATE"][-2:]))
        objFormat = objBook.add_format({ 
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 26, "font_name": "Microsoft YaHei", "fg_color": "#FFFFFF",
            "border": 1, "top_color": "#FFFFFF", "bottom_color": "#FFFFFF", "left_color": "#FFFFFF", "right_color": "#FFFFFF", "left": 1, "right": 1, "top": 1, "bottom": 1 })
        objSheet.merge_range("A1:T1", strMonth + "月-各事业部业绩达成-截止" + strDate + "日（千元）", objFormat)

        objFormat = objBook.add_format({ 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "fg_color": "#FFFFFF",
            "border": 1, "top_color": "#FFFFFF", "bottom_color": "#FFFFFF", "left_color": "#FFFFFF", "right_color": "#FFFFFF", "left": 1, "right": 1, "top": 1, "bottom": 1 })
        objSheet.merge_range("A2:B2", "标准进度：", objFormat)

        objFormat = objBook.add_format({ 
            "num_format": "0.0%_ ", 
            "align": "left", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "font_color": "#0020F5", "fg_color": "#FFFFFF",
            "border": 1, "top_color": "#FFFFFF", "bottom_color": "#FFFFFF", "left_color": "#FFFFFF", "right_color": "#FFFFFF", "left": 1, "right": 1, "top": 1, "bottom": 1 })
        objSheet.merge_range("C2:D2", listSalesRPT01Head[0]["WORKDAY_PC"], objFormat)

        objSheet.merge_range("E2:R2", "", objFormatBlank)

        objFormat = objBook.add_format({ 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "font_color": "#0020F5", "fg_color": "#FFFFFF",
            "border": 1, "top_color": "#FFFFFF", "bottom_color": "#FFFFFF", "left_color": "#FFFFFF", "right_color": "#FFFFFF", "left": 1, "right": 1, "top": 1, "bottom": 1 })
        objSheet.write("S2", "第" + str(listSalesRPT01Head[0]["WORKDAYS"]) + "天", objFormat)

        objFormat = objBook.add_format({ 
            "align": "left", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "fg_color": "#FFFFFF",
            "border": 1, "top_color": "#FFFFFF", "bottom_color": "#FFFFFF", "left_color": "#FFFFFF", "right_color": "#FFFFFF", "left": 1, "right": 1, "top": 1, "bottom": 1 })
        objSheet.write("T2", "/ " + str(listSalesRPT01Head[0]["WORKDAY_TOTAL"]) + "天", objFormat)

        objSheet.merge_range("A3:T3", "", objFormatBlank)

        objFormat = objBook.add_format({ 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 18, "font_name": "STKaiti", "fg_color": "#FFFFFF",
            "border": 1, "top_color": "#FFFFFF", "bottom_color": "#FFFFFF", "left_color": "#FFFFFF", "right_color": "#D9D9D9", "left": 1, "right": 2, "top": 1, "bottom": 1 })
        objSheet.merge_range("A4:D4", "昨日开单：", objFormat)

        objFormat = objBook.add_format({ 
            "num_format": "#,##0_ ", 
            "align": "right", "valign": "vcenter", "font_size": 22, "font_name": "Aharoni", "font_color": "#FFFFFF", "fg_color": "#93B3DE", 
            "border": 1, "top_color": "#D9D9D9", "bottom_color": "#D9D9D9", "left_color": "#D9D9D9", "right_color": "#D9D9D9", "left": 2, "right": 2, "top": 2, "bottom": 2 })
        objSheet.merge_range("E4:G4", listSalesRPT01Head[0]["BU_AMT_SD"], objFormat)

        objSheet.merge_range("H4:T4", "", objFormatBlank)
        
        objFormat = objBook.add_format({ 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 18, "font_name": "STKaiti", "fg_color": "#FFFFFF",
            "border": 1, "top_color": "#FFFFFF", "bottom_color": "#FFFFFF", "left_color": "#FFFFFF", "right_color": "#D9D9D9", "left": 1, "right": 2, "top": 1, "bottom": 1 })
        objSheet.merge_range("A5:D5", "月度开单：", objFormat)

        objFormat = objBook.add_format({ 
            "num_format": "#,##0_ ", 
            "align": "right", "valign": "vcenter", "font_size": 22, "font_name": "Aharoni", "font_color": "#FFFFFF", "fg_color": "#567EB7", 
            "border": 1, "top_color": "#D9D9D9", "bottom_color": "#D9D9D9", "left_color": "#D9D9D9", "right_color": "#D9D9D9", "left": 2, "right": 2, "top": 2, "bottom": 2 })
        objSheet.merge_range("E5:G5", listSalesRPT01Head[0]["BU_AMT_D"], objFormat)

        objSheet.merge_range("H5:T5", "", objFormatBlank)
        
        objFormat = objBook.add_format({ 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 18, "font_name": "STKaiti", "fg_color": "#FFFFFF",
            "border": 1, "top_color": "#FFFFFF", "bottom_color": "#FFFFFF", "left_color": "#FFFFFF", "right_color": "#D9D9D9", "left": 1, "right": 2, "top": 1, "bottom": 1 })
        objSheet.merge_range("A6:D6", "未  过  账：", objFormat)

        objFormat = objBook.add_format({ 
            "num_format": "#,##0_ ", 
            "align": "right", "valign": "vcenter", "font_size": 22, "font_name": "Aharoni", "font_color": "#FFFFFF", "fg_color": "#567EB7", 
            "border": 1, "top_color": "#D9D9D9", "bottom_color": "#D9D9D9", "left_color": "#D9D9D9", "right_color": "#D9D9D9", "left": 2, "right": 2, "top": 2, "bottom": 2 })
        objSheet.merge_range("E6:G6", listSalesRPT01Head[0]["BU_AMT_POSTING"], objFormat)

        objSheet.merge_range("H6:T6", "", objFormatBlank)
        
        objFormat = objBook.add_format({ 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 18, "font_name": "STKaiti", "fg_color": "#FFFFFF",
            "border": 1, "top_color": "#FFFFFF", "bottom_color": "#FFFFFF", "left_color": "#FFFFFF", "right_color": "#D9D9D9", "left": 1, "right": 2, "top": 1, "bottom": 1 })
        objSheet.merge_range("A7:D7", "全月同期：", objFormat)

        objFormat = objBook.add_format({ 
            "num_format": "#,##0_ ", 
            "align": "right", "valign": "vcenter", "font_size": 22, "font_name": "Aharoni", "font_color": "#B12318", "fg_color": "#FFFFFF", 
            "border": 1, "top_color": "#D9D9D9", "bottom_color": "#D9D9D9", "left_color": "#D9D9D9", "right_color": "#D9D9D9", "left": 2, "right": 2, "top": 2, "bottom": 2 })
        objSheet.merge_range("E7:G7", listSalesRPT01Head[0]["BU_AMT_LAST_ALL"], objFormat)

        objSheet.merge_range("H7:T7", "", objFormatBlank)
        
        objFormat = objBook.add_format({ 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 18, "font_name": "STKaiti", "fg_color": "#FFFFFF",
            "border": 1, "top_color": "#FFFFFF", "bottom_color": "#FFFFFF", "left_color": "#FFFFFF", "right_color": "#D9D9D9", "left": 1, "right": 2, "top": 1, "bottom": 1 })
        objSheet.merge_range("A8:D8", "销售预估：", objFormat)

        objFormat = objBook.add_format({ 
            "num_format": "#,##0_ ", 
            "align": "right", "valign": "vcenter", "font_size": 22, "font_name": "Aharoni", "font_color": "#0733C6", "fg_color": "#FFFFFF", 
            "border": 1, "top_color": "#D9D9D9", "bottom_color": "#D9D9D9", "left_color": "#D9D9D9", "right_color": "#D9D9D9", "left": 2, "right": 2, "top": 2, "bottom": 2 })
        objSheet.merge_range("E8:G8", listSalesRPT01Head[0]["BU_REQ"], objFormat)
        
        objSheet.merge_range("H8:T8", "", objFormatBlank)

        objSheet.merge_range("A9:T9", "", objFormatBlank)

        objFormat = objBook.add_format({ 
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 18, "font_name": "STKaiti", "font_color": "#FFFFFF", "fg_color": "#BFBEBF", 
            "border": 1, "top_color": "#FFFFFF", "bottom_color": "#FFFFFF", "left_color": "#FFFFFF", "right_color": "#FFFFFF" })
        objSheet.merge_range("A10:C11", "乳饮休闲", objFormat)

        strGRUpDesc = ""
        strGRDownDesc = ""
        for dictSalesRPT01GR in listSalesRPT01GR:
            if dictSalesRPT01GR["BU_AMT_GR"] != None and dictSalesRPT01GR["BU_AMT_GR"] >= 0:
                strGRUpDesc = strGRUpDesc + dictSalesRPT01GR["BU01_NM"] + "、"
            elif dictSalesRPT01GR["BU_AMT_GR"] != None and dictSalesRPT01GR["BU_AMT_GR"] < 0:
                strGRDownDesc = dictSalesRPT01GR["BU01_NM"] + "、" + strGRDownDesc

        if strGRUpDesc != "":
            strGRUpDesc = strGRUpDesc[:-1]
        if strGRDownDesc != "":
            strGRDownDesc = strGRDownDesc[:-1]

        objFormat = objBook.add_format({ 
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 18, "font_name": "STKaiti", "font_color": "#132CEE", "fg_color": "#BFBEBF", 
            "border": 1, "top_color": "#FFFFFF", "bottom_color": "#FFFFFF", "left_color": "#FFFFFF", "right_color": "#FFFFFF" })
        objSheet.write("D10", "成长", objFormat)

        objFormat = objBook.add_format({ 
            "align": "left", "valign": "vcenter", "bold": 1, "font_size": 20, "font_name": "STKaiti", "font_color": "#132CEE", "fg_color": "#FFFFFF",
            "border": 1, "top_color": "#FFFFFF", "bottom_color": "#FFFFFF", "left_color": "#FFFFFF", "right_color": "#FFFFFF", "left": 1, "right": 1, "top": 1, "bottom": 1 })
        objSheet.merge_range("E10:T10", strGRUpDesc, objFormat)

        objFormat = objBook.add_format({ 
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 18, "font_name": "STKaiti", "font_color": "#E73426", "fg_color": "#BFBEBF", 
            "border": 1, "top_color": "#FFFFFF", "bottom_color": "#FFFFFF", "left_color": "#FFFFFF", "right_color": "#FFFFFF" })
        objSheet.write("D11", "衰退", objFormat)

        objFormat = objBook.add_format({ 
            "align": "left", "valign": "vcenter", "bold": 1, "font_size": 20, "font_name": "STKaiti", "font_color": "#E73426", "fg_color": "#FFFFFF",
            "border": 1, "top_color": "#FFFFFF", "bottom_color": "#FFFFFF", "left_color": "#FFFFFF", "right_color": "#FFFFFF", "left": 1, "right": 1, "top": 1, "bottom": 1 })
        objSheet.merge_range("E11:T11", strGRDownDesc, objFormat)

        objFormat = objBook.add_format({ 
            "fg_color": "#FFFFFF",
            "border": 1, "top_color": "#FFFFFF", "bottom_color": "#000000", "left_color": "#FFFFFF", "right_color": "#FFFFFF", "left": 1, "right": 1, "top": 1, "bottom": 2
        })
        objSheet.merge_range("A12:T12", "", objFormat)

        objFormat = objBook.add_format({ 
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "font_color": "#FFFFFF", "fg_color": "#3F5F8E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 2, "top": 2, "right": 1, "bottom": 1 })
        objSheet.merge_range("A13:C15", "事业部", objFormat)

        objFormat = objBook.add_format({ 
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "font_color": "#FFFFFF", "fg_color": "#3F5F8E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 2, "right": 1, "bottom": 1 })
        objSheet.merge_range("D13:H13", "开单状况", objFormat)

        objFormat = objBook.add_format({ 
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "font_color": "#FFFFFF", "fg_color": "#3F5F8E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 2, "right": 1, "bottom": 1 })
        objSheet.merge_range("I13:O13", "同期达成状况", objFormat)

        objFormat = objBook.add_format({ 
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "font_color": "#FFFFFF", "fg_color": "#3F5F8E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 2, "right": 1, "bottom": 1 })
        objSheet.merge_range("P13:R13", "预估达成状况", objFormat)

        objFormat = objBook.add_format({ 
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "font_color": "#FFFFFF", "fg_color": "#3F5F8E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 2, "right": 2, "bottom": 1 })
        objSheet.merge_range("S13:T13", "账余状况", objFormat)

        objFormat = objBook.add_format({ 
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "font_color": "#FFFFFF", "fg_color": "#3F5F8E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
        objSheet.merge_range("D14:F14", "近三期开单", objFormat)

        strValue = str(int(listSalesRPT01Head[0]["DATA_DATE"][-4:][:2])) + "月累计开单"
        objFormat = objBook.add_format({ 
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "font_color": "#FFFFFF", "fg_color": "#3F5F8E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
        objSheet.merge_range("G14:H14", strValue, objFormat)

        objFormat = objBook.add_format({ 
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "font_color": "#FFFFFF", "fg_color": "#3F5F8E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
        objSheet.merge_range("I14:L14", "全月同期达成", objFormat)

        objFormat = objBook.add_format({ 
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "font_color": "#FFFFFF", "fg_color": "#3F5F8E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
        objSheet.merge_range("M14:O14", "当日同期达成", objFormat)

        objFormat = objBook.add_format({ 
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "font_color": "#FFFFFF", "fg_color": "#3F5F8E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
        objSheet.merge_range("P14:P15", "全月预估", objFormat)

        objFormat = objBook.add_format({ 
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "font_color": "#FFFFFF", "fg_color": "#3F5F8E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
        objSheet.merge_range("Q14:R14", "预估达成进度", objFormat)

        objFormat = objBook.add_format({ 
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "font_color": "#FFFFFF", "fg_color": "#3F5F8E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
        objSheet.merge_range("S14:S15", "客户账余", objFormat)

        objFormat = objBook.add_format({ 
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "font_color": "#FFFFFF", "fg_color": "#3F5F8E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 2, "bottom": 1 })
        objSheet.merge_range("T14:T15", "账款落差", objFormat)

        strValue = str(int(listSalesRPT01Head[0]["DATA_DATE2"][-2:])) + "日"
        objFormat = objBook.add_format({ 
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "font_color": "#FFFFFF", "fg_color": "#3F5F8E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
        objSheet.write("D15", strValue, objFormat)

        strValue = str(int(listSalesRPT01Head[0]["DATA_DATE1"][-2:])) + "日"
        objFormat = objBook.add_format({ 
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "font_color": "#FFFFFF", "fg_color": "#3F5F8E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
        objSheet.write("E15", strValue, objFormat)

        strValue = str(int(listSalesRPT01Head[0]["DATA_DATE"][-2:])) + "日"
        objFormat = objBook.add_format({ 
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "font_color": "#FFFFFF", "fg_color": "#3F5F8E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
        objSheet.write("F15", strValue, objFormat)

        strValue = "截止" + str(int(listSalesRPT01Head[0]["DATA_DATE"][-2:])) + "日"
        objFormat = objBook.add_format({ 
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "font_color": "#FFFFFF", "fg_color": "#3F5F8E",
            "border": 1, "top_color": "#000000", "bottom_color": "#3040F5", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 5 })
        objSheet.merge_range("G15:H15", strValue, objFormat)

        objFormat = objBook.add_format({ 
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "font_color": "#FFFFFF", "fg_color": "#3F5F8E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
        objSheet.write("I15", "全月同期", objFormat)

        objFormat = objBook.add_format({ 
            "text_wrap": 1,
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "font_color": "#FFFFFF", "fg_color": "#3F5F8E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
        objSheet.merge_range("J15:K15", "同期\n达成率", objFormat)

        objFormat = objBook.add_format({ 
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "font_color": "#FFFFFF", "fg_color": "#3F5F8E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
        objSheet.write("L15", "全月落差", objFormat)

        objFormat = objBook.add_format({ 
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "font_color": "#FFFFFF", "fg_color": "#3F5F8E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
        objSheet.write("M15", "进度同期", objFormat)

        objFormat = objBook.add_format({ 
            "text_wrap": 1,
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "font_color": "#FFFFFF", "fg_color": "#3F5F8E",
            "border": 1, "top_color": "#000000", "bottom_color": "#3040F5", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 5 })
        objSheet.write("N15", "同期\n成长率", objFormat)

        objFormat = objBook.add_format({ 
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "font_color": "#FFFFFF", "fg_color": "#3F5F8E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
        objSheet.write("O15", "进度落差", objFormat)

        objFormat = objBook.add_format({ 
            "text_wrap": 1,
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "font_color": "#FFFFFF", "fg_color": "#3F5F8E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
        objSheet.write("Q15", "预估\n达成率", objFormat)

        objFormat = objBook.add_format({ 
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "font_color": "#FFFFFF", "fg_color": "#3F5F8E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
        objSheet.write("R15", "进度落差", objFormat)

        objFormat = objBook.add_format({ 
            "text_wrap": 1,
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "font_color": "#0020F5", "fg_color": "#FFFFFF", 
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 2, "top": 1, "right": 1, "bottom": 1 })
        objSheet.merge_range("A16:A23", "乳\n饮\n休\n闲", objFormat)

        decMaxBUAMTD = 0
        for dictSalesRPT01 in listSalesRPT01:
            if dictSalesRPT01["BU01_ID"] != None and dictSalesRPT01["BU01_ID"] != "BU99" and dictSalesRPT01["BU_AMT_D"] != None and dictSalesRPT01["BU_AMT_D"] > decMaxBUAMTD:
                decMaxBUAMTD = dictSalesRPT01["BU_AMT_D"]

        intRowIndex = 15
        while(intRowIndex < 38):
            if intRowIndex == 23:
                intRowIndex += 1

            intSubTotal = 0
            intBorderLeft = 1
            intFirstIndex = 1
            intFontBold = 0
            strFontColor = "#000000"
            if intRowIndex >= 23:
                intSubTotal = 1
                intBorderLeft = 6
                intFirstIndex = 0
                intFontBold = 1
                strFontColor = "#0020F5"

            dictSalesRPT01 = listSalesRPT01[intRowIndex - 15 - intSubTotal]

            objFormat = objBook.add_format({ 
                "align": "center", "valign": "vcenter", "bold": intFontBold, "font_size": 11, "font_name": "Microsoft YaHei", "font_color": strFontColor, "fg_color": "#FFFFFF",
                "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": intBorderLeft, "top": 1, "right": 1, "bottom": 1 })
            objSheet.merge_range(intRowIndex, intFirstIndex, intRowIndex, 2, dictSalesRPT01["BU01_NM"], objFormat)

            objFormat = objBook.add_format({ 
                "num_format": "#,##0_ ", 
                "align": "right", "valign": "vcenter", "font_size": 11, "font_name": "Arial", "fg_color": "#FFFFFF",
                "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
            objSheet.write(intRowIndex, 3, dictSalesRPT01["BU_AMT_SD2"], objFormat)

            objFormat = objBook.add_format({ 
                "num_format": "#,##0_ ", 
                "align": "right", "valign": "vcenter", "font_size": 11, "font_name": "Arial", "fg_color": "#FFFFFF",
                "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
            objSheet.write(intRowIndex, 4, dictSalesRPT01["BU_AMT_SD1"], objFormat)

            objFormat = objBook.add_format({ 
                "num_format": "#,##0_ ", 
                "align": "right", "valign": "vcenter", "font_size": 11, "font_name": "Arial", "fg_color": "#FFFFFF",
                "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#3040F5", "left": 1, "top": 1, "right": 5, "bottom": 1 })
            objSheet.write(intRowIndex, 5, dictSalesRPT01["BU_AMT_SD"], objFormat)

            strValue = ""
            if dictSalesRPT01["BU_AMT_D"] != None and dictSalesRPT01["BU_AMT_D"] < 0:
                strValue = 0
            elif dictSalesRPT01["BU_AMT_D"] != None and dictSalesRPT01["BU_AMT_D"] >= 0:
                strValue = dictSalesRPT01["BU_AMT_D"] / decMaxBUAMTD

            objFormat = objBook.add_format({ 
                "align": "left", "valign": "vcenter", "font_size": 11, "font_color": "#FFC107", "font_name": "Arial", "fg_color": "#FFFFFF",
                "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#3040F5", "right_color": "#FFFFFF", "left": 5, "top": 1, "right": 1, "bottom": 1 })
            objSheet.write(intRowIndex, 6, getProgressBar(strValue), objFormat)

            objFormat = objBook.add_format({ 
                "num_format": "#,##0_ ", 
                "align": "right", "valign": "vcenter", "font_size": 11, "font_name": "Arial", "fg_color": "#FFFFFF",
                "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#FFFFFF", "right_color": "#3040F5", "left": 1, "top": 1, "right": 5, "bottom": 1 })
            objSheet.write(intRowIndex, 7, dictSalesRPT01["BU_AMT_D"], objFormat)

            strValue = ""
            if dictSalesRPT01["BU_AMT_LAST_ALL"] != None and dictSalesRPT01["BU_AMT_LAST_ALL"] > 0:
                strValue = dictSalesRPT01["BU_AMT_LAST_ALL"]
            objFormat = objBook.add_format({ 
                "num_format": "#,##0_ ", 
                "align": "right", "valign": "vcenter", "font_size": 11, "font_name": "Arial", "fg_color": "#FFFFFF",
                "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#3040F5", "right_color": "#000000", "left": 5, "top": 1, "right": 1, "bottom": 1 })
            objSheet.write(intRowIndex, 8, strValue, objFormat)

            strValue = ""
            if dictSalesRPT01["BU_AMT_LAST_ALL"] != None and dictSalesRPT01["BU_AMT_LAST_ALL"] <= 0:
                strValue = "-"
            elif dictSalesRPT01["BU_AMT_PC"] != None and dictSalesRPT01["BU_AMT_PC"] < 0:
                strValue = 0
            elif dictSalesRPT01["BU_AMT_PC"] != None and dictSalesRPT01["BU_AMT_PC"] >= 0:
                strValue = dictSalesRPT01["BU_AMT_PC"]

            objFormat = objBook.add_format({ 
                "align": "left", "valign": "vcenter", "font_size": 11, "font_color": "#FFC107", "font_name": "Arial", "fg_color": "#FFFFFF",
                "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#FFFFFF", "left": 1, "top": 1, "right": 1, "bottom": 1 })
            objSheet.write(intRowIndex, 9, getProgressBar(strValue), objFormat)

            objFormat = objBook.add_format({ 
                "num_format": "0.0%_ ", 
                "align": "right", "valign": "vcenter", "font_size": 11, "font_color": "#000000", "font_name": "Arial", "fg_color": "#FFFFFF",
                "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#FFFFFF", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
            objSheet.write(intRowIndex, 10, strValue, objFormat)

            objFormat = objBook.add_format({ 
                "num_format": "#,##0_ ", 
                "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Arial", "fg_color": "#FFFFFF",
                "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
            objSheet.write(intRowIndex, 11, dictSalesRPT01["BU_AMT_DIF_ALL"], objFormat)

            strValue = ""
            if dictSalesRPT01["BU_AMT_LAST"] != None and dictSalesRPT01["BU_AMT_LAST"] > 0:
                strValue = dictSalesRPT01["BU_AMT_LAST"]
            objFormat = objBook.add_format({ 
                "num_format": "#,##0_ ", 
                "align": "right", "valign": "vcenter", "font_size": 11, "font_name": "Arial", "fg_color": "#FFFFFF",
                "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#3040F5", "left": 1, "top": 1, "right": 5, "bottom": 1 })
            objSheet.write(intRowIndex, 12, strValue, objFormat)

            strValue = ""
            if dictSalesRPT01["BU_AMT_LAST"] != None and dictSalesRPT01["BU_AMT_LAST"] <= 0:
                strValue = "-"
            else:
                strValue = dictSalesRPT01["BU_AMT_GR"]
    
            intFontBold = 0
            strFontColor = "#000000"
            if dictSalesRPT01["BU_AMT_GR"] != None and dictSalesRPT01["BU_AMT_GR"] < 0:
                intFontBold = 1
                strFontColor = "#EB3324"
            objFormat = objBook.add_format({ 
                "num_format": "0.0%_ ", 
                "align": "right", "valign": "vcenter", "bold": intFontBold, "font_size": 11, "font_name": "Arial", "font_color": strFontColor, "fg_color": "#FFFFFF",
                "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#3040F5", "right_color": "#3040F5", "left": 5, "top": 1, "right": 5, "bottom": 1 })
            objSheet.write(intRowIndex, 13, strValue, objFormat)

            objFormat = objBook.add_format({ 
                "num_format": "#,##0_ ", 
                "align": "right", "valign": "vcenter", "font_size": 11, "font_name": "Arial", "fg_color": "#FFFFFF",
                "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#3040F5", "right_color": "#000000", "left": 5, "top": 1, "right": 1, "bottom": 1 })
            objSheet.write(intRowIndex, 14, dictSalesRPT01["BU_AMT_DIF"], objFormat)

            objFormat = objBook.add_format({ 
                "num_format": "#,##0_ ", 
                "align": "right", "valign": "vcenter", "font_size": 11, "font_name": "Arial", "fg_color": "#FFFFFF",
                "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
            objSheet.write(intRowIndex, 15, dictSalesRPT01["BU_REQ"], objFormat)

            objFormat = objBook.add_format({ 
                "num_format": "0.0%_ ", 
                "align": "right", "valign": "vcenter", "font_size": 11, "font_name": "Arial", "fg_color": "#FFFFFF",
                "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
            objSheet.write(intRowIndex, 16, dictSalesRPT01["BU_REQ_PC"], objFormat)

            objFormat = objBook.add_format({ 
                "num_format": "#,##0_ ", 
                "align": "right", "valign": "vcenter", "font_size": 11, "font_name": "Arial", "fg_color": "#FFFFFF",
                "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
            objSheet.write(intRowIndex, 17, dictSalesRPT01["BU_REQ_DIF"], objFormat)

            strValue = ""
            if dictSalesRPT01["BU_AMT_STMT"] != None and dictSalesRPT01["BU_AMT_STMT"]>0:
                strValue = dictSalesRPT01["BU_AMT_STMT"]

            strFGColor = "#FFFFFF"
            if (intRowIndex >= 29 and intRowIndex <=31) or (intRowIndex >= 33 and intRowIndex <=36):
                strFGColor = "#D9D8D9"
            objFormat = objBook.add_format({ 
                "num_format": "#,##0_ ", 
                "align": "right", "valign": "vcenter", "font_size": 11, "font_name": "Arial", "fg_color": strFGColor,
                "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
            objSheet.write(intRowIndex, 18, strValue, objFormat)

            objFormat = objBook.add_format({ 
                "num_format": "#,##0_ ", 
                "align": "right", "valign": "vcenter", "font_size": 11, "font_name": "Arial", "fg_color": strFGColor,
                "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 2, "bottom": 1 })
            objSheet.write(intRowIndex, 19, dictSalesRPT01["BU_AMT_STMT_DIF"], objFormat)

            intRowIndex += 1

        objFormat = objBook.add_format({ 
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "font_color": "#FFFFFF", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 2, "top": 1, "right": 1, "bottom": 1 })
        objSheet.merge_range(23, 0, 23, 2, "乳饮休闲合计", objFormat)

        objFormat = objBook.add_format({ 
            "num_format": "#,##0_ ", 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Arial", "font_color": "#FFFFFF", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
        objSheet.write(23, 3, listSalesRPT01SubTotal[0]["BU_AMT_SD2"], objFormat)

        objFormat = objBook.add_format({ 
            "num_format": "#,##0_ ", 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Arial", "font_color": "#FFFFFF", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
        objSheet.write(23, 4, listSalesRPT01SubTotal[0]["BU_AMT_SD1"], objFormat)

        objFormat = objBook.add_format({ 
            "num_format": "#,##0_ ", 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Arial", "font_color": "#FFFFFF", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#3040F5", "left": 1, "top": 1, "right": 5, "bottom": 1 })
        objSheet.write(23, 5, listSalesRPT01SubTotal[0]["BU_AMT_SD"], objFormat)

        objFormat = objBook.add_format({ 
            "num_format": "#,##0_ ", 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Arial", "font_color": "#FFFFFF", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#3F608E", "right_color": "#3040F5", "left": 1, "top": 1, "right": 5, "bottom": 1 })
        objSheet.merge_range(23, 6, 23, 7, listSalesRPT01SubTotal[0]["BU_AMT_D"], objFormat)

        strValue = ""
        if listSalesRPT01SubTotal[0]["BU_AMT_LAST_ALL"] > 0:
            strValue = listSalesRPT01SubTotal[0]["BU_AMT_LAST_ALL"]
        objFormat = objBook.add_format({ 
            "num_format": "#,##0_ ", 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Arial", "font_color": "#FFFFFF", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#3040F5", "right_color": "#000000", "left": 5, "top": 1, "right": 1, "bottom": 1 })
        objSheet.write(23, 8, strValue, objFormat)

        strValue = ""
        if listSalesRPT01SubTotal[0]["BU_AMT_LAST_ALL"] <= 0:
            strValue = "-"
        elif listSalesRPT01SubTotal[0]["BU_AMT_PC"] < 0:
            strValue = 0
        elif listSalesRPT01SubTotal[0]["BU_AMT_PC"] >= 0:
            strValue = listSalesRPT01SubTotal[0]["BU_AMT_PC"]     

        objFormat = objBook.add_format({ 
            "align": "left", "valign": "vcenter", "bold": 1, "font_size": 11, "font_color": "#FFC107", "font_name": "Arial", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#3F608E", "left": 1, "top": 1, "right": 1, "bottom": 1 })
        objSheet.write(23, 9, getProgressBar(strValue), objFormat)

        objFormat = objBook.add_format({ 
            "num_format": "0.0%_ ", 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_color": "#FFFFFF", "font_name": "Arial", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#3F608E", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
        objSheet.write(23, 10, strValue, objFormat)

        objFormat = objBook.add_format({ 
            "num_format": "#,##0_ ", 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Arial", "font_color": "#FFFFFF", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
        objSheet.write(23, 11, listSalesRPT01SubTotal[0]["BU_AMT_DIF_ALL"], objFormat)

        strValue = ""
        if listSalesRPT01SubTotal[0]["BU_AMT_LAST"] > 0:
            strValue = listSalesRPT01SubTotal[0]["BU_AMT_LAST"]        
        objFormat = objBook.add_format({ 
            "num_format": "#,##0_ ", 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Arial", "font_color": "#FFFFFF", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#3040F5", "left": 1, "top": 1, "right": 5, "bottom": 1 })
        objSheet.write(23, 12, strValue, objFormat)

        strValue = ""
        if listSalesRPT01SubTotal[0]["BU_AMT_LAST"] <= 0:
            strValue = "-"
        else:
            strValue = listSalesRPT01SubTotal[0]["BU_AMT_GR"]

        strFontColor = "#FFFFFF"
        if listSalesRPT01SubTotal[0]["BU_AMT_GR"] < 0:
            strFontColor = "#EB3324"

        objFormat = objBook.add_format({ 
            "num_format": "0.0%_ ", 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Arial", "font_color": strFontColor, "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#3040F5", "right_color": "#3040F5", "left": 5, "top": 1, "right": 5, "bottom": 1 })
        objSheet.write(23, 13, strValue, objFormat)

        objFormat = objBook.add_format({ 
            "num_format": "#,##0_ ", 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Arial", "font_color": "#FFFFFF", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#3040F5", "right_color": "#000000", "left": 5, "top": 1, "right": 1, "bottom": 1 })
        objSheet.write(23, 14, listSalesRPT01SubTotal[0]["BU_AMT_DIF"], objFormat)

        objFormat = objBook.add_format({ 
            "num_format": "#,##0_ ", 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Arial", "font_color": "#FFFFFF", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
        objSheet.write(23, 15, listSalesRPT01SubTotal[0]["BU_REQ"], objFormat)

        objFormat = objBook.add_format({ 
            "num_format": "0.0%_ ", 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Arial", "font_color": "#FFFFFF", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
        objSheet.write(23, 16, listSalesRPT01SubTotal[0]["BU_REQ_PC"], objFormat)

        objFormat = objBook.add_format({ 
            "num_format": "#,##0_ ", 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Arial", "font_color": "#FFFFFF", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
        objSheet.write(23, 17, listSalesRPT01SubTotal[0]["BU_REQ_DIF"], objFormat)

        objFormat = objBook.add_format({ 
            "num_format": "#,##0_ ", 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Arial", "font_color": "#FFFFFF", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 1 })
        objSheet.write(23, 18, listSalesRPT01SubTotal[0]["BU_AMT_STMT"], objFormat)

        objFormat = objBook.add_format({ 
            "num_format": "#,##0_ ", 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Arial", "font_color": "#FFFFFF", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 2, "bottom": 1 })
        objSheet.write(23, 19, listSalesRPT01SubTotal[0]["BU_AMT_STMT_DIF"], objFormat)

        objFormat = objBook.add_format({ 
            "align": "center", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "font_color": "#FFFFFF", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 2, "top": 1, "right": 1, "bottom": 2 })
        objSheet.merge_range(intRowIndex, 0, intRowIndex, 2, "总计", objFormat)

        objFormat = objBook.add_format({ 
            "num_format": "#,##0_ ", 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Arial", "font_color": "#FFFFFF", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 2 })
        objSheet.write(intRowIndex, 3, listSalesRPT01Total[0]["BU_AMT_SD2"], objFormat)

        objFormat = objBook.add_format({ 
            "num_format": "#,##0_ ", 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Arial", "font_color": "#FFFFFF", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 2 })
        objSheet.write(intRowIndex, 4, listSalesRPT01Total[0]["BU_AMT_SD1"], objFormat)

        objFormat = objBook.add_format({ 
            "num_format": "#,##0_ ", 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Arial", "font_color": "#FFFFFF", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#3040F5", "left": 1, "top": 1, "right": 5, "bottom": 2 })
        objSheet.write(intRowIndex, 5, listSalesRPT01Total[0]["BU_AMT_SD"], objFormat)

        objFormat = objBook.add_format({ 
            "num_format": "#,##0_ ", 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Arial", "font_color": "#FFFFFF", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#3040F5", "left_color": "#3F608E", "right_color": "#3040F5", "left": 1, "top": 1, "right": 5, "bottom": 5 })
        objSheet.merge_range(intRowIndex, 6, intRowIndex, 7, listSalesRPT01Total[0]["BU_AMT_D"], objFormat)

        strValue = ""
        if listSalesRPT01Total[0]["BU_AMT_LAST_ALL"] > 0:
            strValue = listSalesRPT01Total[0]["BU_AMT_LAST_ALL"]        
        objFormat = objBook.add_format({ 
            "num_format": "#,##0_ ", 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Arial", "font_color": "#FFFFFF", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#3040F5", "right_color": "#000000", "left": 5, "top": 1, "right": 1, "bottom": 2 })
        objSheet.write(intRowIndex, 8, strValue, objFormat)

        strValue = ""
        if listSalesRPT01Total[0]["BU_AMT_LAST_ALL"] <= 0:
            strValue = "-"
        elif listSalesRPT01Total[0]["BU_AMT_PC"] < 0:
            strValue = 0
        elif listSalesRPT01Total[0]["BU_AMT_PC"] >= 0:
            strValue = listSalesRPT01Total[0]["BU_AMT_PC"]        

        objFormat = objBook.add_format({ 
            "align": "left", "valign": "vcenter", "bold": 1, "font_size": 11, "font_color": "#FFC107", "font_name": "Arial", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#3F608E", "left": 1, "top": 1, "right": 1, "bottom": 2 })
        objSheet.write(intRowIndex, 9, getProgressBar(strValue), objFormat)

        objFormat = objBook.add_format({ 
            "num_format": "0.0%_ ", 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_color": "#FFFFFF", "font_name": "Arial", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#3F608E", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 2 })
        objSheet.write(intRowIndex, 10, strValue, objFormat)

        objFormat = objBook.add_format({ 
            "num_format": "#,##0_ ", 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Arial", "font_color": "#FFFFFF", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 2 })
        objSheet.write(intRowIndex, 11, listSalesRPT01Total[0]["BU_AMT_DIF_ALL"], objFormat)

        strValue = ""
        if listSalesRPT01Total[0]["BU_AMT_LAST"] > 0:
            strValue = listSalesRPT01Total[0]["BU_AMT_LAST"]
        objFormat = objBook.add_format({ 
            "num_format": "#,##0_ ", 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Arial", "font_color": "#FFFFFF", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#3040F5", "left": 1, "top": 1, "right": 5, "bottom": 2 })
        objSheet.write(intRowIndex, 12, strValue, objFormat)

        strValue = ""
        if listSalesRPT01Total[0]["BU_AMT_LAST"] <= 0:
            strValue = "-"
        else:
            strValue = listSalesRPT01Total[0]["BU_AMT_GR"]

        strFontColor = "#FFFFFF"
        if listSalesRPT01Total[0]["BU_AMT_GR"] < 0:
            strFontColor = "#EB3324"
        objFormat = objBook.add_format({ 
            "num_format": "0.0%_ ", 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Arial", "font_color": strFontColor, "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#3040F5", "left_color": "#3040F5", "right_color": "#3040F5", "left": 5, "top": 1, "right": 5, "bottom": 5 })
        objSheet.write(intRowIndex, 13, strValue, objFormat)

        objFormat = objBook.add_format({ 
            "num_format": "#,##0_ ", 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Arial", "font_color": "#FFFFFF", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#3040F5", "right_color": "#000000", "left": 5, "top": 1, "right": 1, "bottom": 2 })
        objSheet.write(intRowIndex, 14, listSalesRPT01Total[0]["BU_AMT_DIF"], objFormat)

        objFormat = objBook.add_format({ 
            "num_format": "#,##0_ ", 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Arial", "font_color": "#FFFFFF", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 2 })
        objSheet.write(intRowIndex, 15, listSalesRPT01Total[0]["BU_REQ"], objFormat)

        objFormat = objBook.add_format({ 
            "num_format": "0.0%_ ", 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Arial", "font_color": "#FFFFFF", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 2 })
        objSheet.write(intRowIndex, 16, listSalesRPT01Total[0]["BU_REQ_PC"], objFormat)

        objFormat = objBook.add_format({ 
            "num_format": "#,##0_ ", 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Arial", "font_color": "#FFFFFF", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 2 })
        objSheet.write(intRowIndex, 17, listSalesRPT01Total[0]["BU_REQ_DIF"], objFormat)

        objFormat = objBook.add_format({ 
            "num_format": "#,##0_ ", 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Arial", "font_color": "#FFFFFF", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 1, "bottom": 2 })
        objSheet.write(intRowIndex, 18, listSalesRPT01Total[0]["BU_AMT_STMT"], objFormat)

        objFormat = objBook.add_format({ 
            "num_format": "#,##0_ ", 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Arial", "font_color": "#FFFFFF", "fg_color": "#3F608E",
            "border": 1, "top_color": "#000000", "bottom_color": "#000000", "left_color": "#000000", "right_color": "#000000", "left": 1, "top": 1, "right": 2, "bottom": 2 })
        objSheet.write(intRowIndex, 19, listSalesRPT01Total[0]["BU_AMT_STMT_DIF"], objFormat)

        objFormat = objBook.add_format({ 
            "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_name": "Microsoft YaHei", "fg_color": "#FFFFFF",
            "border": 1, "top_color": "#FFFFFF", "bottom_color": "#FFFFFF", "left_color": "#FFFFFF", "right_color": "#FFFFFF", "left": 1, "right": 1, "top": 1, "bottom": 1 })
        objSheet.merge_range("A40:T40", "®营运管理中心制", objFormat)

        objSheet.set_row(37, None, None, { "hidden": True })

        objBook.close()
        return True

def execMailSalesRPT01(strJobPathRES, strDataDate):
    strEDIConnection = "3DW-DWuser@tpe-centos7-maria10-dw"
    strEDIDB = "DMMDL"

    listSalesRPT01Head = getSalesRPT01HeadList(strEDIConnection, strEDIDB, strDataDate)
    listSalesRPT01 = getSalesRPT01List(strEDIConnection, strEDIDB, strDataDate)
    listSalesRPT01SubTotal = getSalesRPT01SubTotalList(strEDIConnection, strEDIDB, strDataDate)
    listSalesRPT01Total = getSalesRPT01TotalList(strEDIConnection, strEDIDB, strDataDate)
    listSalesRPT01GR = getSalesRPT01GRList(strEDIConnection, strEDIDB, strDataDate)

    if execWriteWorkbook(strJobPathRES, listSalesRPT01Head, listSalesRPT01, listSalesRPT01SubTotal, listSalesRPT01Total, listSalesRPT01GR) == True:
        strMessageSMTPServer = "tw-mail02.want-want.com"
        strMessageSMTPFrom = "Data.Center@want-want.com"
        arrayMessageSMTPTo = [
            "Guo_Yan@want-want.com",
            "Yan_HongMei@want-want.com",
            "Xie_Wei3@want-want.com",
            "Li_Tong3@want-want.com",
            "Zoe.Hsu@want-want.com"
        ]
        strMessageSubject = "[测试]【各事业部当日／月累计业绩达成进度报表】- %s" % strDataDate
        strAttachFileName = "[测试]各事业部当日／月累计业绩达成进度报表-%s.xlsx" % strDataDate
        strContent = "尊敬的长官：早上好！\n敬请查阅：截止" + strDataDate[4:6] + "月" + strDataDate[-2:] + "日【各事业部当日／月累计业绩达成进度报表】\n\n"

        Message.sendSMTPMail(strMessageSMTPServer, strMessageSMTPFrom, arrayMessageSMTPTo, strMessageSubject, strContent, strJobPathRES, strAttachFileName)
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

    execMailSalesRPT01(strJobPathRES, strDataDate)

if __name__ == "__main__":
    main()
