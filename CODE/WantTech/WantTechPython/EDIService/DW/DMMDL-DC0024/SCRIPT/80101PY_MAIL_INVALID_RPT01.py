import sys
import logging
import xlsxwriter
from Utility import Common
from Utility import Message
from Entity import DBEntity
from Entity import MariaEntity
from EDI import EDIEntity

def getInvalidRPT01List(strEDIConnection, strEDIDB, strEDINo):
    strSQL = "SELECT POS_DATE_MIN, POS_DATE_MAX " + \
             "FROM DMMDL.DC0024_INVALID_RPT01 " + \
             "WHERE {EDI_NO}; "

    dictMariaParameter = {
        "EDI_NO": MariaEntity.MariaParameter(strOperator="=", objValue=strEDINo, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listInvalidRPT01 = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listInvalidRPT01

def getInvalidRPT01ProdPosList(strEDIConnection, strEDIDB):
    strSQL = "SELECT KA_SYSTEM_CODE, KA_SYSTEM_NM " + \
             "     , SYSTEM_PROD_CODE, SYSTEM_PROD_NM " + \
             "     , POS_DATE_MIN, POS_DATE_MAX " + \
             "FROM DMMDL.DC0024_INVALID_RPT01_PROD_POS " + \
             "ORDER BY KA_SYSTEM_CODE, POS_DATE_MIN, POS_DATE_MAX " + \
             "; "

    listInvalidRPT01ProdPos = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listInvalidRPT01ProdPos

def getInvalidRPT01ProdInvList(strEDIConnection, strEDIDB):
    strSQL = "SELECT KA_SYSTEM_CODE, KA_SYSTEM_NM " + \
             "     , SYSTEM_PROD_CODE, SYSTEM_PROD_NM " + \
             "     , INV_DATE_MIN, INV_DATE_MAX " + \
             "FROM DMMDL.DC0024_INVALID_RPT01_PROD_INV " + \
             "ORDER BY KA_SYSTEM_CODE, INV_DATE_MIN, INV_DATE_MAX " + \
             "; "

    listInvalidRPT01ProdInv = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listInvalidRPT01ProdInv

def getInvalidRPT01StorePosList(strEDIConnection, strEDIDB):
    strSQL = "SELECT KA_SYSTEM_CODE, KA_SYSTEM_NM " + \
             "     , SYSTEM_STORE_CODE, SYSTEM_STORE_NM " + \
             "     , POS_DATE_MIN, POS_DATE_MAX " + \
             "FROM DMMDL.DC0024_INVALID_RPT01_STORE_POS " + \
             "ORDER BY KA_SYSTEM_CODE, POS_DATE_MIN, POS_DATE_MAX " + \
             "; "

    listInvalidRPT01StorePos = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listInvalidRPT01StorePos

def getInvalidRPT01StoreInvList(strEDIConnection, strEDIDB):
    strSQL = "SELECT KA_SYSTEM_CODE, KA_SYSTEM_NM " + \
             "     , SYSTEM_STORE_CODE, SYSTEM_STORE_NM " + \
             "     , INV_DATE_MIN, INV_DATE_MAX " + \
             "FROM DMMDL.DC0024_INVALID_RPT01_STORE_INV " + \
             "ORDER BY KA_SYSTEM_CODE, INV_DATE_MIN, INV_DATE_MAX " + \
             "; "

    listInvalidRPT01StoreInv = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listInvalidRPT01StoreInv

def getInvalidRPT01StoreComPosList(strEDIConnection, strEDIDB):
    strSQL = "SELECT KA_SYSTEM_CODE, KA_SYSTEM_NM " + \
             "     , CONCAT(KA_SYSTEM_CODE, '-', KA_STORE_CODE) AS KA_STORE_CODE, KA_STORE_NM " + \
             "     , SALES_COM_SA_CN, SALES_COM_WH_CN, SALES_COM_DE_CN " + \
             "FROM DMMDL.DC0024_INVALID_RPT01_STORE_COM_POS " + \
             "ORDER BY KA_SYSTEM_CODE, KA_STORE_CODE " + \
             "; "

    listInvalidRPT01StoreComPos = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listInvalidRPT01StoreComPos

def getInvalidRPT01StoreComInvList(strEDIConnection, strEDIDB):
    strSQL = "SELECT KA_SYSTEM_CODE, KA_SYSTEM_NM " + \
             "     , CONCAT(KA_SYSTEM_CODE, '-', KA_STORE_CODE) AS KA_STORE_CODE, KA_STORE_NM " + \
             "     , SALES_COM_SA_CN, SALES_COM_WH_CN, SALES_COM_DE_CN " + \
             "FROM DMMDL.DC0024_INVALID_RPT01_STORE_COM_INV " + \
             "ORDER BY KA_SYSTEM_CODE, KA_STORE_CODE " + \
             "; "

    listInvalidRPT01StoreComInv = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listInvalidRPT01StoreComInv

def getInvalidRPT01WHComInvList(strEDIConnection, strEDIDB):
    strSQL = "SELECT KA_SYSTEM_CODE, KA_SYSTEM_NM " + \
             "     , CONCAT(KA_SYSTEM_CODE, '-', KA_WH_CODE) AS KA_WH_CODE, KA_WH_NM " + \
             "     , SALES_COM_WH_CN, SALES_COM_DE_CN " + \
             "FROM DMMDL.DC0024_INVALID_RPT01_WH_COM_INV " + \
             "ORDER BY KA_SYSTEM_CODE, KA_WH_CODE " + \
             "; "

    listInvalidRPT01StoreComInv = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listInvalidRPT01StoreComInv

def execAddWorksheetInvalidRPT01ProdPos(objSheet, listInvalidRPT01ProdPos, objColumnFormat, objRowCenterFormat, objRowLeftFormat, objRowRightFormat):
    objSheet.set_default_row(20)   
    objSheet.set_row(0, 40)

    objSheet.set_column(0, 0, 8)
    objSheet.set_column(1, 1, 10)
    objSheet.set_column(2, 2, 15)
    objSheet.set_column(3, 3, 30)
    objSheet.set_column(4, 4, 15)
    objSheet.set_column(5, 5, 15)

    intRowIndex = 0

    objSheet.write(intRowIndex, 0, "系统代号", objColumnFormat)
    objSheet.write(intRowIndex, 1, "系统名称", objColumnFormat)
    objSheet.write(intRowIndex, 2, "系统产品销售编码", objColumnFormat) 
    objSheet.write(intRowIndex, 3, "系统产品名称", objColumnFormat)
    objSheet.write(intRowIndex, 4, "最早未匹配数据\n销售日期", objColumnFormat)
    objSheet.write(intRowIndex, 5, "最晚未匹配数据\n销售日期", objColumnFormat)
    intRowIndex += 1

    for dictInvalidRPT01ProdPos in listInvalidRPT01ProdPos:
        objSheet.write(intRowIndex, 0, dictInvalidRPT01ProdPos["KA_SYSTEM_CODE"], objRowCenterFormat)
        objSheet.write(intRowIndex, 1, dictInvalidRPT01ProdPos["KA_SYSTEM_NM"], objRowCenterFormat)
        objSheet.write(intRowIndex, 2, dictInvalidRPT01ProdPos["SYSTEM_PROD_CODE"], objRowLeftFormat)
        objSheet.write(intRowIndex, 3, dictInvalidRPT01ProdPos["SYSTEM_PROD_NM"], objRowLeftFormat)
        objSheet.write(intRowIndex, 4, Common.formatDateString(dictInvalidRPT01ProdPos["POS_DATE_MIN"]), objRowCenterFormat)
        objSheet.write(intRowIndex, 5, Common.formatDateString(dictInvalidRPT01ProdPos["POS_DATE_MAX"]), objRowCenterFormat)
        intRowIndex += 1

    return True

def execAddWorksheetInvalidRPT01ProdInv(objSheet, listInvalidRPT01ProdInv, objColumnFormat, objRowCenterFormat, objRowLeftFormat, objRowRightFormat):
    objSheet.set_default_row(20)   
    objSheet.set_row(0, 40)

    objSheet.set_column(0, 0, 8)
    objSheet.set_column(1, 1, 10)
    objSheet.set_column(2, 2, 15)
    objSheet.set_column(3, 3, 30)
    objSheet.set_column(4, 4, 15)
    objSheet.set_column(5, 5, 15)

    intRowIndex = 0

    objSheet.write(intRowIndex, 0, "系统代号", objColumnFormat)
    objSheet.write(intRowIndex, 1, "系统名称", objColumnFormat)
    objSheet.write(intRowIndex, 2, "系统产品销售编码", objColumnFormat) 
    objSheet.write(intRowIndex, 3, "系统产品名称", objColumnFormat)
    objSheet.write(intRowIndex, 4, "最早未匹配数据\n库存日期", objColumnFormat)
    objSheet.write(intRowIndex, 5, "最晚未匹配数据\n库存日期", objColumnFormat)
    intRowIndex += 1

    for dictInvalidRPT01ProdInv in listInvalidRPT01ProdInv:
        objSheet.write(intRowIndex, 0, dictInvalidRPT01ProdInv["KA_SYSTEM_CODE"], objRowCenterFormat)
        objSheet.write(intRowIndex, 1, dictInvalidRPT01ProdInv["KA_SYSTEM_NM"], objRowCenterFormat)
        objSheet.write(intRowIndex, 2, dictInvalidRPT01ProdInv["SYSTEM_PROD_CODE"], objRowLeftFormat)
        objSheet.write(intRowIndex, 3, dictInvalidRPT01ProdInv["SYSTEM_PROD_NM"], objRowLeftFormat)
        objSheet.write(intRowIndex, 4, Common.formatDateString(dictInvalidRPT01ProdInv["INV_DATE_MIN"]), objRowCenterFormat)
        objSheet.write(intRowIndex, 5, Common.formatDateString(dictInvalidRPT01ProdInv["INV_DATE_MAX"]), objRowCenterFormat)
        intRowIndex += 1

    return True

def execAddWorksheetInvalidRPT01StorePos(objSheet, listInvalidRPT01StorePos, objColumnFormat, objRowCenterFormat, objRowLeftFormat, objRowRightFormat):
    objSheet.set_default_row(20)   
    objSheet.set_row(0, 40)

    objSheet.set_column(0, 0, 8)
    objSheet.set_column(1, 1, 10)
    objSheet.set_column(2, 2, 15)
    objSheet.set_column(3, 3, 30)
    objSheet.set_column(4, 4, 15)
    objSheet.set_column(5, 5, 15)

    intRowIndex = 0

    objSheet.write(intRowIndex, 0, "系统代号", objColumnFormat)
    objSheet.write(intRowIndex, 1, "系统名称", objColumnFormat)
    objSheet.write(intRowIndex, 2, "系统门店代号", objColumnFormat) 
    objSheet.write(intRowIndex, 3, "系统门店名称", objColumnFormat)
    objSheet.write(intRowIndex, 4, "最早未匹配数据\n销售日期", objColumnFormat)
    objSheet.write(intRowIndex, 5, "最晚未匹配数据\n销售日期", objColumnFormat)
    intRowIndex += 1

    for dictInvalidRPT01StorePos in listInvalidRPT01StorePos:
        objSheet.write(intRowIndex, 0, dictInvalidRPT01StorePos["KA_SYSTEM_CODE"], objRowCenterFormat)
        objSheet.write(intRowIndex, 1, dictInvalidRPT01StorePos["KA_SYSTEM_NM"], objRowCenterFormat)
        objSheet.write(intRowIndex, 2, dictInvalidRPT01StorePos["SYSTEM_STORE_CODE"], objRowLeftFormat)
        objSheet.write(intRowIndex, 3, dictInvalidRPT01StorePos["SYSTEM_STORE_NM"], objRowLeftFormat)
        objSheet.write(intRowIndex, 4, Common.formatDateString(dictInvalidRPT01StorePos["POS_DATE_MIN"]), objRowCenterFormat)
        objSheet.write(intRowIndex, 5, Common.formatDateString(dictInvalidRPT01StorePos["POS_DATE_MAX"]), objRowCenterFormat)
        intRowIndex += 1

    return True

def execAddWorksheetInvalidRPT01StoreInv(objSheet, listInvalidRPT01StoreInv, objColumnFormat, objRowCenterFormat, objRowLeftFormat, objRowRightFormat):
    objSheet.set_default_row(20)   
    objSheet.set_row(0, 40)

    objSheet.set_column(0, 0, 8)
    objSheet.set_column(1, 1, 10)
    objSheet.set_column(2, 2, 15)
    objSheet.set_column(3, 3, 30)
    objSheet.set_column(4, 4, 15)
    objSheet.set_column(5, 5, 15)

    intRowIndex = 0

    objSheet.write(intRowIndex, 0, "系统代号", objColumnFormat)
    objSheet.write(intRowIndex, 1, "系统名称", objColumnFormat)
    objSheet.write(intRowIndex, 2, "系统门店代号", objColumnFormat) 
    objSheet.write(intRowIndex, 3, "系统门店名称", objColumnFormat)
    objSheet.write(intRowIndex, 4, "最早未匹配数据\n库存日期", objColumnFormat)
    objSheet.write(intRowIndex, 5, "最晚未匹配数据\n库存日期", objColumnFormat)
    intRowIndex += 1

    for dictInvalidRPT01StoreInv in listInvalidRPT01StoreInv:
        objSheet.write(intRowIndex, 0, dictInvalidRPT01StoreInv["KA_SYSTEM_CODE"], objRowCenterFormat)
        objSheet.write(intRowIndex, 1, dictInvalidRPT01StoreInv["KA_SYSTEM_NM"], objRowCenterFormat)
        objSheet.write(intRowIndex, 2, dictInvalidRPT01StoreInv["SYSTEM_STORE_CODE"], objRowLeftFormat)
        objSheet.write(intRowIndex, 3, dictInvalidRPT01StoreInv["SYSTEM_STORE_NM"], objRowLeftFormat)
        objSheet.write(intRowIndex, 4, Common.formatDateString(dictInvalidRPT01StoreInv["INV_DATE_MIN"]), objRowCenterFormat)
        objSheet.write(intRowIndex, 5, Common.formatDateString(dictInvalidRPT01StoreInv["INV_DATE_MAX"]), objRowCenterFormat)
        intRowIndex += 1

    return True

def execAddWorksheetInvalidRPT01StoreComPos(objSheet, listInvalidRPT01StoreComPos, objColumnFormat, objRowCenterFormat, objRowLeftFormat, objRowRightFormat):
    objSheet.set_default_row(20)   
    objSheet.set_row(0, 40)

    objSheet.set_column(0, 0, 8)
    objSheet.set_column(1, 1, 10)
    objSheet.set_column(2, 2, 15)
    objSheet.set_column(3, 3, 30)
    objSheet.set_column(4, 4, 20)
    objSheet.set_column(5, 5, 20)
    objSheet.set_column(6, 6, 20)

    intRowIndex = 0

    objSheet.write(intRowIndex, 0, "系统代号", objColumnFormat)
    objSheet.write(intRowIndex, 1, "系统名称", objColumnFormat)
    objSheet.write(intRowIndex, 2, "旺旺系统门店编号", objColumnFormat) 
    objSheet.write(intRowIndex, 3, "旺旺系统门店名称", objColumnFormat)
    objSheet.write(intRowIndex, 4, "匹配业绩拆分地个数", objColumnFormat)
    objSheet.write(intRowIndex, 5, "匹配大仓所在地个数", objColumnFormat)
    objSheet.write(intRowIndex, 6, "匹配送货地个数", objColumnFormat)
    intRowIndex += 1

    for dictInvalidRPT01StoreComPos in listInvalidRPT01StoreComPos:
        objSheet.write(intRowIndex, 0, dictInvalidRPT01StoreComPos["KA_SYSTEM_CODE"], objRowCenterFormat)
        objSheet.write(intRowIndex, 1, dictInvalidRPT01StoreComPos["KA_SYSTEM_NM"], objRowCenterFormat)
        objSheet.write(intRowIndex, 2, dictInvalidRPT01StoreComPos["KA_STORE_CODE"], objRowLeftFormat)
        objSheet.write(intRowIndex, 3, dictInvalidRPT01StoreComPos["KA_STORE_NM"], objRowLeftFormat)
        objSheet.write(intRowIndex, 4, dictInvalidRPT01StoreComPos["SALES_COM_SA_CN"], objRowCenterFormat)
        objSheet.write(intRowIndex, 5, dictInvalidRPT01StoreComPos["SALES_COM_WH_CN"], objRowCenterFormat)
        objSheet.write(intRowIndex, 6, dictInvalidRPT01StoreComPos["SALES_COM_DE_CN"], objRowCenterFormat)
        intRowIndex += 1

    return True

def execAddWorksheetInvalidRPT01StoreComInv(objSheet, listInvalidRPT01StoreComInv, objColumnFormat, objRowCenterFormat, objRowLeftFormat, objRowRightFormat):
    objSheet.set_default_row(20)   
    objSheet.set_row(0, 40)

    objSheet.set_column(0, 0, 8)
    objSheet.set_column(1, 1, 10)
    objSheet.set_column(2, 2, 15)
    objSheet.set_column(3, 3, 30)
    objSheet.set_column(4, 4, 20)
    objSheet.set_column(5, 5, 20)
    objSheet.set_column(6, 6, 20)

    intRowIndex = 0

    objSheet.write(intRowIndex, 0, "系统代号", objColumnFormat)
    objSheet.write(intRowIndex, 1, "系统名称", objColumnFormat)
    objSheet.write(intRowIndex, 2, "旺旺系统门店编号", objColumnFormat) 
    objSheet.write(intRowIndex, 3, "旺旺系统门店名称", objColumnFormat)
    objSheet.write(intRowIndex, 4, "匹配业绩拆分地个数", objColumnFormat)
    objSheet.write(intRowIndex, 5, "匹配大仓所在地个数", objColumnFormat)
    objSheet.write(intRowIndex, 6, "匹配送货地个数", objColumnFormat)
    intRowIndex += 1

    for dictInvalidRPT01StoreComInv in listInvalidRPT01StoreComInv:
        objSheet.write(intRowIndex, 0, dictInvalidRPT01StoreComInv["KA_SYSTEM_CODE"], objRowCenterFormat)
        objSheet.write(intRowIndex, 1, dictInvalidRPT01StoreComInv["KA_SYSTEM_NM"], objRowCenterFormat)
        objSheet.write(intRowIndex, 2, dictInvalidRPT01StoreComInv["KA_STORE_CODE"], objRowLeftFormat)
        objSheet.write(intRowIndex, 3, dictInvalidRPT01StoreComInv["KA_STORE_NM"], objRowLeftFormat)
        objSheet.write(intRowIndex, 4, dictInvalidRPT01StoreComInv["SALES_COM_SA_CN"], objRowCenterFormat)
        objSheet.write(intRowIndex, 5, dictInvalidRPT01StoreComInv["SALES_COM_WH_CN"], objRowCenterFormat)
        objSheet.write(intRowIndex, 6, dictInvalidRPT01StoreComInv["SALES_COM_DE_CN"], objRowCenterFormat)
        intRowIndex += 1

    return True

def execAddWorksheetInvalidRPT01WHComInv(objSheet, listInvalidRPT01WHComInv, objColumnFormat, objRowCenterFormat, objRowLeftFormat, objRowRightFormat):
    objSheet.set_default_row(20)   
    objSheet.set_row(0, 40)

    objSheet.set_column(0, 0, 8)
    objSheet.set_column(1, 1, 10)
    objSheet.set_column(2, 2, 15)
    objSheet.set_column(3, 3, 30)
    objSheet.set_column(4, 4, 20)
    objSheet.set_column(5, 5, 20)

    intRowIndex = 0

    objSheet.write(intRowIndex, 0, "系统代号", objColumnFormat)
    objSheet.write(intRowIndex, 1, "系统名称", objColumnFormat)
    objSheet.write(intRowIndex, 2, "旺旺系统大仓编号", objColumnFormat) 
    objSheet.write(intRowIndex, 3, "旺旺系统大仓名称", objColumnFormat)
    objSheet.write(intRowIndex, 4, "匹配大仓所在地个数", objColumnFormat)
    objSheet.write(intRowIndex, 5, "匹配送货地个数", objColumnFormat)
    intRowIndex += 1

    for dictInvalidRPT01WHComInv in listInvalidRPT01WHComInv:
        objSheet.write(intRowIndex, 0, dictInvalidRPT01WHComInv["KA_SYSTEM_CODE"], objRowCenterFormat)
        objSheet.write(intRowIndex, 1, dictInvalidRPT01WHComInv["KA_SYSTEM_NM"], objRowCenterFormat)
        objSheet.write(intRowIndex, 2, dictInvalidRPT01WHComInv["KA_WH_CODE"], objRowLeftFormat)
        objSheet.write(intRowIndex, 3, dictInvalidRPT01WHComInv["KA_WH_NM"], objRowLeftFormat)
        objSheet.write(intRowIndex, 4, dictInvalidRPT01WHComInv["SALES_COM_WH_CN"], objRowCenterFormat)
        objSheet.write(intRowIndex, 5, dictInvalidRPT01WHComInv["SALES_COM_DE_CN"], objRowCenterFormat)
        intRowIndex += 1

    return True

def execWriteWorkbook(strJobPathRES, listInvalidRPT01,
                      listInvalidRPT01ProdPos, listInvalidRPT01ProdInv, listInvalidRPT01StorePos, listInvalidRPT01StoreInv, \
                      listInvalidRPT01StoreComPos, listInvalidRPT01StoreComInv, listInvalidRPT01WHComInv):
    objBook = None
    objBook = xlsxwriter.Workbook(strJobPathRES)

    objColumnFormat = objBook.add_format({
        "text_wrap": 1,
        "align": "center", "valign": "vcenter", "bold": 1, "font_size": 11, "font_color": "#FFFFFF", "fg_color": "#305496", 
        "border": 0})

    objRowCenterFormat = objBook.add_format({
        "align": "center", "valign": "vcenter", "bold": 1, "font_size": 11, "font_color": "#000000",
        "border": 0})
    objRowLeftFormat = objBook.add_format({
        "align": "left", "valign": "vcenter", "bold": 1, "font_size": 11, "font_color": "#000000",
        "border": 0})
    objRowRightFormat = objBook.add_format({
        "align": "right", "valign": "vcenter", "bold": 1, "font_size": 11, "font_color": "#000000",
        "border": 0})
    objRowRightFormat.set_num_format("0_ ")

    objSheet = objBook.add_worksheet("未匹配产品清单-销售")
    execAddWorksheetInvalidRPT01ProdPos(objSheet, listInvalidRPT01ProdPos, objColumnFormat, objRowCenterFormat, objRowLeftFormat, objRowRightFormat)

    objSheet = objBook.add_worksheet("未匹配产品清单-库存")
    execAddWorksheetInvalidRPT01ProdInv(objSheet, listInvalidRPT01ProdInv, objColumnFormat, objRowCenterFormat, objRowLeftFormat, objRowRightFormat)

    objSheet = objBook.add_worksheet("未匹配门店清单-销售")
    execAddWorksheetInvalidRPT01StorePos(objSheet, listInvalidRPT01StorePos, objColumnFormat, objRowCenterFormat, objRowLeftFormat, objRowRightFormat)

    objSheet = objBook.add_worksheet("未匹配门店清单-库存")
    execAddWorksheetInvalidRPT01StoreInv(objSheet, listInvalidRPT01StoreInv, objColumnFormat, objRowCenterFormat, objRowLeftFormat, objRowRightFormat)

    objSheet = objBook.add_worksheet("门店分公司异常清单-销售")
    execAddWorksheetInvalidRPT01StoreComPos(objSheet, listInvalidRPT01StoreComPos, objColumnFormat, objRowCenterFormat, objRowLeftFormat, objRowRightFormat)

    objSheet = objBook.add_worksheet("门店分公司异常清单-库存")
    execAddWorksheetInvalidRPT01StoreComInv(objSheet, listInvalidRPT01StoreComInv, objColumnFormat, objRowCenterFormat, objRowLeftFormat, objRowRightFormat)

    objSheet = objBook.add_worksheet("大仓分公司异常清单-库存")
    execAddWorksheetInvalidRPT01WHComInv(objSheet, listInvalidRPT01WHComInv, objColumnFormat, objRowCenterFormat, objRowLeftFormat, objRowRightFormat)

    objBook.close()
    return True

def execMailInvalidRPT01(strJobPathRES, strEDINo, strDataDate):
    strEDIConnection = "3DW-DWuser@tpe-centos7-maria10-dw"
    strEDIDB = "DMMDL"

    listInvalidRPT01 = getInvalidRPT01List(strEDIConnection, strEDIDB, strEDINo)
    listInvalidRPT01ProdPos = getInvalidRPT01ProdPosList(strEDIConnection, strEDIDB)
    listInvalidRPT01ProdInv = getInvalidRPT01ProdInvList(strEDIConnection, strEDIDB)
    listInvalidRPT01StorePos = getInvalidRPT01StorePosList(strEDIConnection, strEDIDB)
    listInvalidRPT01StoreInv = getInvalidRPT01StoreInvList(strEDIConnection, strEDIDB)
    listInvalidRPT01StoreComPos = getInvalidRPT01StoreComPosList(strEDIConnection, strEDIDB)
    listInvalidRPT01StoreComInv = getInvalidRPT01StoreComInvList(strEDIConnection, strEDIDB)
    listInvalidRPT01WHComInv = getInvalidRPT01WHComInvList(strEDIConnection, strEDIDB)

    if execWriteWorkbook(strJobPathRES, listInvalidRPT01, \
                         listInvalidRPT01ProdPos, listInvalidRPT01ProdInv, listInvalidRPT01StorePos, listInvalidRPT01StoreInv, \
                         listInvalidRPT01StoreComPos, listInvalidRPT01StoreComInv, listInvalidRPT01WHComInv) == True:
        strMessageSMTPServer = "tw-mail02.want-want.com"
        strMessageSMTPFrom = "Data.Center@want-want.com"
        arrayMessageSMTPTo = [
            "Yang_LuLu@want-want.com",
            "Hou_XuPing@want-want.com",
            "Allen.Hu@want-want.com",
            "Zoe.Hsu@want-want.com"
        ]
        strMessageSubject = "现渠自动化管理平台-异常销售及库存数据清单-" + listInvalidRPT01[0]["POS_DATE_MIN"] + "-" + listInvalidRPT01[0]["POS_DATE_MAX"]
        strAttachFileName = "现渠自动化管理平台-异常销售及库存数据清单-" + listInvalidRPT01[0]["POS_DATE_MIN"] + "-" + listInvalidRPT01[0]["POS_DATE_MAX"] + ".xlsx"

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

    execMailInvalidRPT01(strJobPathRES, strEDINo, strDataDate)

if __name__ == "__main__":
    main()
