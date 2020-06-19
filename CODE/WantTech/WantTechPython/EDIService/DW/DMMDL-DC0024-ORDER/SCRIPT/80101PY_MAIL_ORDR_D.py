import os
import sys
import logging
import subprocess
import xlsxwriter
from shutil import copyfile
from Utility import Common
from Utility import Message
from Entity import DBEntity
from Entity import MariaEntity
from EDI import EDIEntity

def getSystemOrdrYMList(strEDIConnection, strEDIDB, strDataDate):
    strSQL = "SELECT SYSTEM_ORDR_YM " + \
             "FROM (SELECT DISTINCT LEFT(SYSTEM_ORDR_DATE, 6) AS SYSTEM_ORDR_YM " + \
             "      FROM DMMDL.DC0024_ORDR_SYS_D) A " + \
             "ORDER BY SYSTEM_ORDR_YM DESC; "

    listSystemOrdrYM = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listSystemOrdrYM

def getOrdrSysDList(strEDIConnection, strEDIDB, strDataDate, strSystemOrdrYM):
    strSQL = "SELECT KA_SYSTEM_CODE, KA_SYSTEM_NM " + \
             "     , SYSTEM_ORDR_DATE " + \
             "     , ORDR_MAIN_ID, SYSTEM_ORDR_NO " + \
             "     , SALES_COM_ID_DE, SALES_COM_ABR_DE, SALES_COM_ID_BL, SALES_COM_ABR_BL " + \
             "     , SALES_CHAN_ID, PROD_DIV_ID " + \
             "     , CUST_ID " + \
             "     , SYSTEM_DEV_DATE" + \
             "     , ORDR_LINE_NUM " + \
             "     , SYSTEM_ORDR_PROD_NM " + \
             "     , PROD_H1_ID, PROD_H1_NM, PROD_H2_ID, PROD_H2_NM " + \
             "     , PROD_MATL_ID, PROD_MATL_NM " + \
             "     , PROD_AMT_PKG, TRAS_PROD_AMT_PKG, PROD_QTY_PKG " + \
             "     , SAP_QTY_PKG_APPD_SUM_DIR, SAP_QTY_PKG_APPD_SUM, SAP_QTY_PKG_APPD_SUM_DIF " + \
             "     , SHIP_QTY_PKG_DIF_SUM, SHIP_QTY_PKG_DEV_SUM, SHIP_QTY_PKG_ACT_SUM, SHIP_QTY_PKG_ACT_SUM_DIF " + \
             "     , TRAS_RETURN_PHASE_NM, TRAS_RETURN_RMK " + \
             "FROM DMMDL.DC0024_ORDR_SYS_D " + \
             "WHERE LEFT(SYSTEM_ORDR_DATE, 6)={SYSTEM_ORDR_YM} " + \
             "ORDER BY KA_SYSTEM_CODE, SYSTEM_ORDR_DATE, SYSTEM_ORDR_NO, ORDR_LINE_NUM; "

    dictMariaParameter = {
        "SYSTEM_ORDR_YM": MariaEntity.MariaParameter(objValue=strSystemOrdrYM, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listOrdrSysD = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listOrdrSysD

def getOrdrTrasDList(strEDIConnection, strEDIDB, strDataDate, strSystemOrdrYM):
    strSQL = "SELECT KA_SYSTEM_CODE, KA_SYSTEM_NM " + \
             "     , SYSTEM_ORDR_DATE " + \
             "     , ORDR_MAIN_ID, SYSTEM_ORDR_NO, SAP_ORDR_NO " + \
             "     , OPEN_ORDR_DATE " + \
             "     , CUST_ID " + \
             "     , SALES_COM_ID_DE_ORDR, SALES_COM_ABR_DE_ORDR, SALES_COM_ID_DE, SALES_COM_ABR_DE, SALES_COM_ID_BL, SALES_COM_ABR_BL " + \
             "     , SALES_CHAN_ID, PROD_DIV_ID " + \
             "     , SYSTEM_DEV_DATE, IS_FACT_DEV " + \
             "     , ORDR_LINE_NUM, SAP_LINE_NUM " + \
             "     , SYSTEM_ORDR_PROD_NM " + \
             "     , PROD_H1_ID_SYS, PROD_H1_NM_SYS, PROD_H2_ID_SYS, PROD_H2_NM_SYS " + \
             "     , PROD_MATL_ID_SYS, PROD_MATL_NM_SYS " + \
             "     , PROD_H1_ID_OPEN, PROD_H1_NM_OPEN, PROD_H2_ID_OPEN, PROD_H2_NM_OPEN " + \
             "     , PROD_MATL_ID_OPEN, PROD_MATL_NM_OPEN " + \
             "     , STORE_PLACE_CODE, IS_STORE_PLACE_DIR " + \
             "     , PROD_AMT_PKG_SYS, PROD_QTY_PKG_SYS, PROD_AMT_PKG_OPEN, PROD_QTY_PKG_OPEN " + \
             "     , SAP_AMT_PKG_OPEN, SAP_QTY_PKG_OPEN, SAP_AMT_PKG_APPD, SAP_QTY_PKG_APPD " + \
             "     , SHIP_QTY_PKG_DIF, SHIP_QTY_PKG_DEV, SHIP_QTY_PKG_ACT " + \
             "FROM DMMDL.DC0024_ORDR_TRAS_D " + \
             "WHERE LEFT(SYSTEM_ORDR_DATE, 6)={SYSTEM_ORDR_YM} " + \
             "ORDER BY KA_SYSTEM_CODE, SYSTEM_ORDR_DATE, SYSTEM_ORDR_NO, ORDR_LINE_NUM; "

    dictMariaParameter = {
        "SYSTEM_ORDR_YM": MariaEntity.MariaParameter(objValue=strSystemOrdrYM, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listOrdrTrasD = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listOrdrTrasD

def execWriteWorkbook(strJobPathRES, strSystemOrdrYM, listOrdrSysD, listOrdrTrasD):
    if len(listOrdrSysD) == 0:
        return False
    else:
        objBook = xlsxwriter.Workbook(strJobPathRES.replace(".dat", "-" + strSystemOrdrYM + ".dat"))
        intRowIndex = 0

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
        objRowRightFormat.set_num_format("0.0000_ ")
    
        objSheet = objBook.add_worksheet("订单清单-" + strSystemOrdrYM)
        objSheet.set_default_row(20)   
    
        objSheet.set_column(0, 0, 10)
        objSheet.set_column(1, 1, 10)
        objSheet.set_column(2, 2, 10)
        objSheet.set_column(3, 3, 32)
        objSheet.set_column(4, 4, 20)
        objSheet.set_column(5, 5, 15)
        objSheet.set_column(6, 6, 15)
        objSheet.set_column(7, 7, 15)
        objSheet.set_column(8, 8, 15)
        objSheet.set_column(9, 9, 10)
        objSheet.set_column(10, 10, 10)
        objSheet.set_column(11, 11, 12)
        objSheet.set_column(12, 12, 10)
        objSheet.set_column(13, 13, 5)
        objSheet.set_column(14, 14, 40)
        objSheet.set_column(15, 15, 15)
        objSheet.set_column(16, 16, 15)
        objSheet.set_column(17, 17, 10)
        objSheet.set_column(18, 18, 10)
        objSheet.set_column(19, 19, 20)
        objSheet.set_column(20, 20, 40)
        objSheet.set_column(21, 21, 10)
        objSheet.set_column(22, 22, 20)
        objSheet.set_column(23, 23, 10)
        objSheet.set_column(24, 24, 20)
        objSheet.set_column(25, 25, 20)
        objSheet.set_column(26, 26, 20)
        objSheet.set_column(27, 27, 15)
        objSheet.set_column(28, 28, 15)
        objSheet.set_column(29, 29, 15)
        objSheet.set_column(30, 30, 15)
        objSheet.set_column(31, 31, 10)
        objSheet.set_column(32, 32, 30)

        intRowIndex = 0

        objSheet.write(intRowIndex, 0, "系统编号", objColumnFormat)
        objSheet.write(intRowIndex, 1, "系统名称", objColumnFormat)
        objSheet.write(intRowIndex, 2, "订单日期", objColumnFormat) 
        objSheet.write(intRowIndex, 3, "订单唯一码", objColumnFormat)
        objSheet.write(intRowIndex, 4, "订单编号", objColumnFormat)
        objSheet.write(intRowIndex, 5, "送货分公司编号", objColumnFormat)
        objSheet.write(intRowIndex, 6, "送货分公司名称", objColumnFormat)
        objSheet.write(intRowIndex, 7, "开单分公司编号", objColumnFormat)
        objSheet.write(intRowIndex, 8, "开单分公司名称", objColumnFormat)
        objSheet.write(intRowIndex, 9, "分销渠道", objColumnFormat)
        objSheet.write(intRowIndex, 10, "产品组", objColumnFormat) 
        objSheet.write(intRowIndex, 11, "开单客户号", objColumnFormat)
        objSheet.write(intRowIndex, 12, "交货日期", objColumnFormat)
        objSheet.write(intRowIndex, 13, "行号", objColumnFormat)
        objSheet.write(intRowIndex, 14, "系统产品名称", objColumnFormat)
        objSheet.write(intRowIndex, 15, "产品大类编号", objColumnFormat)
        objSheet.write(intRowIndex, 16, "产品大类名称", objColumnFormat)
        objSheet.write(intRowIndex, 17, "PM线编号", objColumnFormat)
        objSheet.write(intRowIndex, 18, "PM线名称", objColumnFormat)
        objSheet.write(intRowIndex, 19, "物料编号", objColumnFormat)
        objSheet.write(intRowIndex, 20, "物料名称", objColumnFormat)
        objSheet.write(intRowIndex, 21, "需求箱金额", objColumnFormat)
        objSheet.write(intRowIndex, 22, "需求箱金额(加工後)", objColumnFormat)
        objSheet.write(intRowIndex, 23, "需求箱数", objColumnFormat)
        objSheet.write(intRowIndex, 24, "已开单且审核箱数-直配", objColumnFormat)
        objSheet.write(intRowIndex, 25, "已开单且审核箱数", objColumnFormat)
        objSheet.write(intRowIndex, 26, "开单审核差异箱数", objColumnFormat)
        objSheet.write(intRowIndex, 27, "储运差异箱数", objColumnFormat)
        objSheet.write(intRowIndex, 28, "实际交货数量", objColumnFormat)
        objSheet.write(intRowIndex, 29, "客户实收箱数", objColumnFormat)
        objSheet.write(intRowIndex, 30, "客户实收差异箱数", objColumnFormat)
        objSheet.write(intRowIndex, 31, "异常阶段", objColumnFormat)
        objSheet.write(intRowIndex, 32, "异常原因", objColumnFormat)

        intRowIndex += 1
    
        for dictOrdrSysD in listOrdrSysD:                
            objSheet.write(intRowIndex, 0, dictOrdrSysD["KA_SYSTEM_CODE"], objRowCenterFormat)
            objSheet.write(intRowIndex, 1, dictOrdrSysD["KA_SYSTEM_NM"], objRowCenterFormat)
            objSheet.write(intRowIndex, 2, dictOrdrSysD["SYSTEM_ORDR_DATE"], objRowCenterFormat)
            objSheet.write(intRowIndex, 3, dictOrdrSysD["ORDR_MAIN_ID"], objRowCenterFormat)
            objSheet.write(intRowIndex, 4, dictOrdrSysD["SYSTEM_ORDR_NO"], objRowLeftFormat)
            objSheet.write(intRowIndex, 5, dictOrdrSysD["SALES_COM_ID_DE"], objRowCenterFormat)
            objSheet.write(intRowIndex, 6, dictOrdrSysD["SALES_COM_ABR_DE"], objRowCenterFormat)
            objSheet.write(intRowIndex, 7, dictOrdrSysD["SALES_COM_ID_BL"], objRowCenterFormat)
            objSheet.write(intRowIndex, 8, dictOrdrSysD["SALES_COM_ABR_BL"], objRowCenterFormat)
            objSheet.write(intRowIndex, 9, dictOrdrSysD["SALES_CHAN_ID"], objRowCenterFormat)
            objSheet.write(intRowIndex, 10, dictOrdrSysD["PROD_DIV_ID"], objRowCenterFormat)
            objSheet.write(intRowIndex, 11, dictOrdrSysD["CUST_ID"], objRowCenterFormat)
            objSheet.write(intRowIndex, 12, dictOrdrSysD["SYSTEM_DEV_DATE"], objRowCenterFormat)
            objSheet.write(intRowIndex, 13, dictOrdrSysD["ORDR_LINE_NUM"], objRowCenterFormat)
            objSheet.write(intRowIndex, 14, dictOrdrSysD["SYSTEM_ORDR_PROD_NM"], objRowLeftFormat)
            objSheet.write(intRowIndex, 15, dictOrdrSysD["PROD_H1_ID"], objRowCenterFormat)
            objSheet.write(intRowIndex, 16, dictOrdrSysD["PROD_H1_NM"], objRowCenterFormat)
            objSheet.write(intRowIndex, 17, dictOrdrSysD["PROD_H2_ID"], objRowCenterFormat)
            objSheet.write(intRowIndex, 18, dictOrdrSysD["PROD_H2_NM"], objRowCenterFormat)
            objSheet.write(intRowIndex, 19, dictOrdrSysD["PROD_MATL_ID"], objRowCenterFormat)
            objSheet.write(intRowIndex, 20, dictOrdrSysD["PROD_MATL_NM"], objRowLeftFormat)
            objSheet.write(intRowIndex, 21, dictOrdrSysD["PROD_AMT_PKG"], objRowRightFormat)
            objSheet.write(intRowIndex, 22, dictOrdrSysD["TRAS_PROD_AMT_PKG"], objRowRightFormat)
            objSheet.write(intRowIndex, 23, dictOrdrSysD["PROD_QTY_PKG"], objRowRightFormat)
            objSheet.write(intRowIndex, 24, dictOrdrSysD["SAP_QTY_PKG_APPD_SUM_DIR"], objRowRightFormat)
            objSheet.write(intRowIndex, 25, dictOrdrSysD["SAP_QTY_PKG_APPD_SUM"], objRowRightFormat)
            objSheet.write(intRowIndex, 26, dictOrdrSysD["SAP_QTY_PKG_APPD_SUM_DIF"], objRowRightFormat)
            objSheet.write(intRowIndex, 27, dictOrdrSysD["SHIP_QTY_PKG_DIF_SUM"], objRowRightFormat)
            objSheet.write(intRowIndex, 28, dictOrdrSysD["SHIP_QTY_PKG_DEV_SUM"], objRowRightFormat)
            objSheet.write(intRowIndex, 29, dictOrdrSysD["SHIP_QTY_PKG_ACT_SUM"], objRowRightFormat)
            objSheet.write(intRowIndex, 30, dictOrdrSysD["SHIP_QTY_PKG_ACT_SUM_DIF"], objRowRightFormat)
            objSheet.write(intRowIndex, 31, dictOrdrSysD["TRAS_RETURN_PHASE_NM"], objRowCenterFormat)
            objSheet.write(intRowIndex, 32, dictOrdrSysD["TRAS_RETURN_RMK"], objRowLeftFormat)
            intRowIndex += 1
                    
        objSheet = objBook.add_worksheet("开单明细-" + strSystemOrdrYM)
        objSheet.set_default_row(20)   
    
        objSheet.set_column(0, 0, 10)
        objSheet.set_column(1, 1, 10)
        objSheet.set_column(2, 2, 10)
        objSheet.set_column(3, 3, 32)
        objSheet.set_column(4, 4, 20)
        objSheet.set_column(5, 5, 15)
        objSheet.set_column(6, 6, 15)
        objSheet.set_column(7, 7, 12)
        objSheet.set_column(8, 8, 10)
        objSheet.set_column(9, 9, 15)
        objSheet.set_column(10, 10, 10)
        objSheet.set_column(11, 11, 15)
        objSheet.set_column(12, 12, 10)
        objSheet.set_column(13, 13, 15)
        objSheet.set_column(14, 14, 10)
        objSheet.set_column(15, 15, 10)
        objSheet.set_column(16, 16, 10)
        objSheet.set_column(17, 17, 10)
        objSheet.set_column(18, 18, 7)
        objSheet.set_column(19, 19, 7)
        objSheet.set_column(20, 20, 40)
        objSheet.set_column(21, 21, 12)
        objSheet.set_column(22, 22, 12)
        objSheet.set_column(23, 23, 10)
        objSheet.set_column(24, 24, 10)
        objSheet.set_column(25, 25, 20)
        objSheet.set_column(26, 26, 40)
        objSheet.set_column(27, 27, 17)
        objSheet.set_column(28, 28, 17)
        objSheet.set_column(29, 29, 17)
        objSheet.set_column(30, 30, 17)
        objSheet.set_column(31, 31, 20)
        objSheet.set_column(32, 32, 40)
        objSheet.set_column(33, 33, 7)
        objSheet.set_column(34, 34, 7)
        objSheet.set_column(35, 35, 10)
        objSheet.set_column(36, 36, 10)
        objSheet.set_column(37, 37, 10)
        objSheet.set_column(38, 38, 10)
        objSheet.set_column(39, 39, 15)
        objSheet.set_column(40, 40, 15)
        objSheet.set_column(41, 41, 10)
        objSheet.set_column(42, 42, 10)
        objSheet.set_column(43, 43, 15)
        objSheet.set_column(44, 44, 15)
        objSheet.set_column(45, 45, 15)

        intRowIndex = 0

        objSheet.write(intRowIndex, 0, "系统编号", objColumnFormat)
        objSheet.write(intRowIndex, 1, "系统名称", objColumnFormat)
        objSheet.write(intRowIndex, 2, "订单日期", objColumnFormat) 
        objSheet.write(intRowIndex, 3, "订单唯一码", objColumnFormat)
        objSheet.write(intRowIndex, 4, "订单编号", objColumnFormat)
        objSheet.write(intRowIndex, 5, "SAP订单编号", objColumnFormat)
        objSheet.write(intRowIndex, 6, "订单开单日期", objColumnFormat)
        objSheet.write(intRowIndex, 7, "开单客户号", objColumnFormat)
        objSheet.write(intRowIndex, 8, "订单客户送货分公司", objColumnFormat)
        objSheet.write(intRowIndex, 9, "订单客户送货分公司名称", objColumnFormat)
        objSheet.write(intRowIndex, 10, "开单实际送货分公司", objColumnFormat)
        objSheet.write(intRowIndex, 11, "开单实际送货分公司名称", objColumnFormat)
        objSheet.write(intRowIndex, 12, "开单实际开单分公司", objColumnFormat) 
        objSheet.write(intRowIndex, 13, "开单实际开单分公司名称", objColumnFormat)
        objSheet.write(intRowIndex, 14, "分销渠道", objColumnFormat)
        objSheet.write(intRowIndex, 15, "产品组", objColumnFormat)
        objSheet.write(intRowIndex, 16, "交货日期", objColumnFormat)
        objSheet.write(intRowIndex, 17, "工厂代发货", objColumnFormat)
        objSheet.write(intRowIndex, 18, "行号", objColumnFormat)
        objSheet.write(intRowIndex, 19, "SAP行号", objColumnFormat)
        objSheet.write(intRowIndex, 20, "系统产品名称", objColumnFormat)
        objSheet.write(intRowIndex, 21, "产品大类编号", objColumnFormat)
        objSheet.write(intRowIndex, 22, "产品大类名称", objColumnFormat)
        objSheet.write(intRowIndex, 23, "PM线编号", objColumnFormat)
        objSheet.write(intRowIndex, 24, "PM线名称", objColumnFormat)
        objSheet.write(intRowIndex, 25, "物料编号", objColumnFormat)
        objSheet.write(intRowIndex, 26, "物料名称", objColumnFormat)
        objSheet.write(intRowIndex, 27, "开单产品大类编号", objColumnFormat)
        objSheet.write(intRowIndex, 28, "开单产品大类名称", objColumnFormat)
        objSheet.write(intRowIndex, 29, "开单PM线编号", objColumnFormat)
        objSheet.write(intRowIndex, 30, "开单PM线名称", objColumnFormat)
        objSheet.write(intRowIndex, 31, "开单物料编号", objColumnFormat)
        objSheet.write(intRowIndex, 32, "开单物料名称", objColumnFormat)
        objSheet.write(intRowIndex, 33, "仓别", objColumnFormat)
        objSheet.write(intRowIndex, 34, "直配仓", objColumnFormat)
        objSheet.write(intRowIndex, 35, "需求箱金额", objColumnFormat)
        objSheet.write(intRowIndex, 36, "需求箱数", objColumnFormat)
        objSheet.write(intRowIndex, 37, "开单箱金额", objColumnFormat)
        objSheet.write(intRowIndex, 38, "开单箱数", objColumnFormat)
        objSheet.write(intRowIndex, 39, "SAP开单箱金额", objColumnFormat)
        objSheet.write(intRowIndex, 40, "SAP开单箱数", objColumnFormat)
        objSheet.write(intRowIndex, 41, "审核箱金额", objColumnFormat)
        objSheet.write(intRowIndex, 42, "审核箱数", objColumnFormat)
        objSheet.write(intRowIndex, 43, "储运差异箱数", objColumnFormat)
        objSheet.write(intRowIndex, 44, "实际交货数量", objColumnFormat)
        objSheet.write(intRowIndex, 45, "客户实数箱数", objColumnFormat)

        intRowIndex += 1

        for dictOrdrTrasD in listOrdrTrasD:                
            objSheet.write(intRowIndex, 0, dictOrdrTrasD["KA_SYSTEM_CODE"], objRowCenterFormat)
            objSheet.write(intRowIndex, 1, dictOrdrTrasD["KA_SYSTEM_NM"], objRowCenterFormat)
            objSheet.write(intRowIndex, 2, dictOrdrTrasD["SYSTEM_ORDR_DATE"], objRowCenterFormat)
            objSheet.write(intRowIndex, 3, dictOrdrTrasD["ORDR_MAIN_ID"], objRowCenterFormat)
            objSheet.write(intRowIndex, 4, dictOrdrTrasD["SYSTEM_ORDR_NO"], objRowLeftFormat)
            objSheet.write(intRowIndex, 5, dictOrdrTrasD["SAP_ORDR_NO"], objRowCenterFormat)
            objSheet.write(intRowIndex, 6, dictOrdrTrasD["OPEN_ORDR_DATE"], objRowCenterFormat)
            objSheet.write(intRowIndex, 7, dictOrdrTrasD["CUST_ID"], objRowCenterFormat)
            objSheet.write(intRowIndex, 8, dictOrdrTrasD["SALES_COM_ID_DE_ORDR"], objRowCenterFormat)
            objSheet.write(intRowIndex, 9, dictOrdrTrasD["SALES_COM_ABR_DE_ORDR"], objRowCenterFormat)
            objSheet.write(intRowIndex, 10, dictOrdrTrasD["SALES_COM_ID_DE"], objRowCenterFormat)
            objSheet.write(intRowIndex, 11, dictOrdrTrasD["SALES_COM_ABR_DE"], objRowCenterFormat)
            objSheet.write(intRowIndex, 12, dictOrdrTrasD["SALES_COM_ID_BL"], objRowCenterFormat)
            objSheet.write(intRowIndex, 13, dictOrdrTrasD["SALES_COM_ABR_BL"], objRowCenterFormat)
            objSheet.write(intRowIndex, 14, dictOrdrTrasD["SALES_CHAN_ID"], objRowCenterFormat)
            objSheet.write(intRowIndex, 15, dictOrdrTrasD["PROD_DIV_ID"], objRowCenterFormat)
            objSheet.write(intRowIndex, 16, dictOrdrTrasD["SYSTEM_DEV_DATE"], objRowCenterFormat)
            objSheet.write(intRowIndex, 17, dictOrdrTrasD["IS_FACT_DEV"], objRowCenterFormat)
            objSheet.write(intRowIndex, 18, dictOrdrTrasD["ORDR_LINE_NUM"], objRowCenterFormat)
            objSheet.write(intRowIndex, 19, dictOrdrTrasD["SAP_LINE_NUM"], objRowCenterFormat)
            objSheet.write(intRowIndex, 20, dictOrdrTrasD["SYSTEM_ORDR_PROD_NM"], objRowLeftFormat)
            objSheet.write(intRowIndex, 21, dictOrdrTrasD["PROD_H1_ID_SYS"], objRowCenterFormat)
            objSheet.write(intRowIndex, 22, dictOrdrTrasD["PROD_H1_NM_SYS"], objRowCenterFormat)
            objSheet.write(intRowIndex, 23, dictOrdrTrasD["PROD_H2_ID_SYS"], objRowCenterFormat)
            objSheet.write(intRowIndex, 24, dictOrdrTrasD["PROD_H2_NM_SYS"], objRowCenterFormat)
            objSheet.write(intRowIndex, 25, dictOrdrTrasD["PROD_MATL_ID_SYS"], objRowCenterFormat)
            objSheet.write(intRowIndex, 26, dictOrdrTrasD["PROD_MATL_NM_SYS"], objRowLeftFormat)
            objSheet.write(intRowIndex, 27, dictOrdrTrasD["PROD_H1_ID_OPEN"], objRowCenterFormat)
            objSheet.write(intRowIndex, 28, dictOrdrTrasD["PROD_H1_NM_OPEN"], objRowCenterFormat)
            objSheet.write(intRowIndex, 29, dictOrdrTrasD["PROD_H2_ID_OPEN"], objRowCenterFormat)
            objSheet.write(intRowIndex, 30, dictOrdrTrasD["PROD_H2_NM_OPEN"], objRowCenterFormat)
            objSheet.write(intRowIndex, 31, dictOrdrTrasD["PROD_MATL_ID_OPEN"], objRowCenterFormat)
            objSheet.write(intRowIndex, 32, dictOrdrTrasD["PROD_MATL_NM_OPEN"], objRowLeftFormat)
            objSheet.write(intRowIndex, 33, dictOrdrTrasD["STORE_PLACE_CODE"], objRowCenterFormat)
            objSheet.write(intRowIndex, 34, dictOrdrTrasD["IS_STORE_PLACE_DIR"], objRowCenterFormat)
            objSheet.write(intRowIndex, 35, dictOrdrTrasD["PROD_AMT_PKG_SYS"], objRowRightFormat)
            objSheet.write(intRowIndex, 36, dictOrdrTrasD["PROD_QTY_PKG_SYS"], objRowRightFormat)
            objSheet.write(intRowIndex, 37, dictOrdrTrasD["PROD_AMT_PKG_OPEN"], objRowRightFormat)
            objSheet.write(intRowIndex, 38, dictOrdrTrasD["PROD_QTY_PKG_OPEN"], objRowRightFormat)
            objSheet.write(intRowIndex, 39, dictOrdrTrasD["SAP_AMT_PKG_OPEN"], objRowRightFormat)
            objSheet.write(intRowIndex, 40, dictOrdrTrasD["SAP_QTY_PKG_OPEN"], objRowRightFormat)
            objSheet.write(intRowIndex, 41, dictOrdrTrasD["SAP_AMT_PKG_APPD"], objRowRightFormat)
            objSheet.write(intRowIndex, 42, dictOrdrTrasD["SAP_QTY_PKG_APPD"], objRowRightFormat)
            objSheet.write(intRowIndex, 43, dictOrdrTrasD["SHIP_QTY_PKG_DIF"], objRowRightFormat)
            objSheet.write(intRowIndex, 44, dictOrdrTrasD["SHIP_QTY_PKG_DEV"], objRowRightFormat)
            objSheet.write(intRowIndex, 45, dictOrdrTrasD["SHIP_QTY_PKG_ACT"], objRowRightFormat)
            intRowIndex += 1

        objBook.close()
        return True

def execMailOrdrD(strLoggerName, strJobPathRES, strDataDate):
    strEDIConnection = "3DW-DWuser@tpe-centos7-maria10-dw"
    strEDIDB = "DMMDL"

    listSystemOrdrYM = getSystemOrdrYMList(strEDIConnection, strEDIDB, strDataDate)

    for dictSystemOrdrYM in listSystemOrdrYM:
        listOrdrSysD = getOrdrSysDList(strEDIConnection, strEDIDB, strDataDate, dictSystemOrdrYM["SYSTEM_ORDR_YM"])
        listOrdrTrasD = getOrdrTrasDList(strEDIConnection, strEDIDB, strDataDate, dictSystemOrdrYM["SYSTEM_ORDR_YM"])

        if execWriteWorkbook(strJobPathRES, dictSystemOrdrYM["SYSTEM_ORDR_YM"], listOrdrSysD, listOrdrTrasD) == True:
            strMessageSMTPServer = "tw-mail02.want-want.com"
            strMessageSMTPFrom = "Data.Center@want-want.com"

            strMessageSubject = "现渠自动化管理平台-订单清单及开单明细报表-" + dictSystemOrdrYM["SYSTEM_ORDR_YM"] + "-" + strDataDate
            strAttachFilePath = strJobPathRES.replace(".dat", "-" + dictSystemOrdrYM["SYSTEM_ORDR_YM"] + ".dat")
            strAttachFileName = "现渠自动化管理平台-订单清单及开单明细报表-" + dictSystemOrdrYM["SYSTEM_ORDR_YM"] + "-" + strDataDate + ".xlsx"

            arrayMessageSMTPTo = [ "hong_yueping@want-want.com", "Liu_Cui@want-want.com", "Han_Lei3@want-want.com", "Miao_Qi@want-want.com", "Zoe.Hsu@want-want.com" ]

            if (os.stat(strAttachFilePath).st_size/1024/1024)>7:
                strContent = "尊敬的长官：早上好！\n" + \
                    "敬请查阅：截止" + strDataDate[4:6] + "月" + strDataDate[-2:] + "日【" + "现渠自动化管理平台-订单清单及开单明细报表-" + dictSystemOrdrYM["SYSTEM_ORDR_YM"] + "】\n\n" + \
                    "注意！此档案有多个压缩包，请将压缩包置于同一位置后，在.zip压缩文档上点选二下執行解压缩，即可取得EXCEL文档。\n\n"

                strAttachDirPath = os.path.dirname(strAttachFilePath)
                strExcelFilePath = os.path.join(strAttachDirPath, strAttachFileName)
                strZipFileName = "现渠自动化管理平台-订单清单及开单明细报表-" + dictSystemOrdrYM["SYSTEM_ORDR_YM"] + "-" + strDataDate
                strZipFilePath = os.path.join(strAttachDirPath, strZipFileName)

                os.rename(strAttachFilePath, strExcelFilePath)

                strCommand = "zip -s 5m -j " + strZipFilePath + " " + strExcelFilePath
                tupleOutput = subprocess.Popen(strCommand, shell=True, stderr=subprocess.PIPE).communicate()
                strErrorOutput = tupleOutput[1].decode('utf-8')
                if strErrorOutput != "":
                    logger = logging.getLogger(strLoggerName)
                    logger.error(strErrorOutput)
                else:
                    for strFileName in os.listdir(strAttachDirPath):
                        if strFileName.startswith(strZipFileName) == True and strFileName.endswith(".xlsx") == False:
                            Message.sendSMTPMail(strMessageSMTPServer, strMessageSMTPFrom, arrayMessageSMTPTo, strMessageSubject, strContent, os.path.join(strAttachDirPath, strFileName), strFileName)

                os.rename(strExcelFilePath, strAttachFilePath)
            else:
                strContent = "尊敬的长官：早上好！\n" + \
                    "敬请查阅：截止" + strDataDate[4:6] + "月" + strDataDate[-2:] + "日【" + "现渠自动化管理平台-订单清单及开单明细报表-" + dictSystemOrdrYM["SYSTEM_ORDR_YM"] + "】\n\n"
                Message.sendSMTPMail(strMessageSMTPServer, strMessageSMTPFrom, arrayMessageSMTPTo, strMessageSubject, strContent, strAttachFilePath, strAttachFileName)
        else:
            return False

    return True

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

    execMailOrdrD(strLoggerName, strJobPathRES, strDataDate)

if __name__ == "__main__":
    main()
