import os
import sys
import logging
import subprocess
import xlsxwriter
import datetime
from Utility import Common
from Utility import Message
from Entity import DBEntity
from Entity import MariaEntity
from EDI import EDIEntity

def getWorkDayT(strEDIConnection, strEDIDB, strDataDate, strTODAY):
    strSQL = "SELECT WORKDAY_YM, WORKDAY_YMD, WORKDAY_YN " + \
             "FROM DWWANT.CM_WORKDAY " + \
             "WHERE {WORKDAY_YMD}; "

    dictMariaParameter = {
        "WORKDAY_YMD": MariaEntity.MariaParameter(strOperator="=", objValue=strTODAY, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listWorkDayT = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listWorkDayT

def getStoreMatlMSystemList(strEDIConnection, strEDIDB, strDataDate):
    strSQL = "SELECT KA_SYSTEM_CODE, MAX(KA_SYSTEM_NM) AS KA_SYSTEM_NM " + \
             "     , CONCAT(MAX(KA_SYSTEM_CODE), '-', MAX(KA_STORE_CODE)) AS STORE_CODE " + \
             "     , MAX(POS_YM) AS POS_YM " + \
             "FROM DMMDL.DC0024_STORE_MATL_M " + \
             "WHERE {DATA_DATE} " + \
             "GROUP BY KA_SYSTEM_CODE " + \
             "ORDER BY KA_SYSTEM_CODE; "

    dictMariaParameter = {
        "DATA_DATE": MariaEntity.MariaParameter(strOperator="=", objValue=strDataDate, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listStoreMatlMSystem = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listStoreMatlMSystem

def getStoreMatlMList(strEDIConnection, strEDIDB, strDataDate):
    strSQL = "SELECT KA_SYSTEM_CODE, KA_SYSTEM_NM " + \
             "     , CONCAT(KA_SYSTEM_CODE, '-', KA_STORE_CODE) AS STORE_CODE, KA_STORE_NM " + \
             "     , SALES_COM_ABR_SA, SALES_COM_ABR_WH " + \
             "     , PROD_H1_NM, PROD_H2_NM, PROD_MATL_ID, PROD_MATL_NM " + \
             "     , CONCAT(LEFT(POS_YM,4), '/', RIGHT(POS_YM,2)) AS POS_YM " + \
             "     , POS_QTY_PCS_D, POS_QTY_PKG_D, POS_AMT_D " + \
             "     , POS_QTY_PCS_M, POS_QTY_PKG_M, POS_AMT_M " + \
             "FROM DMMDL.DC0024_STORE_MATL_M " + \
             "WHERE {DATA_DATE} " + \
             "ORDER BY KA_SYSTEM_CODE, STORE_CODE; "

    dictMariaParameter = {
        "DATA_DATE": MariaEntity.MariaParameter(strOperator="=", objValue=strDataDate, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listStoreMatlM = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listStoreMatlM

def getStoreMList(strEDIConnection, strEDIDB, strDataDate):
    strSQL = "SELECT KA_SYSTEM_CODE, KA_SYSTEM_NM " + \
             "     , CONCAT(KA_SYSTEM_CODE, '-', KA_STORE_CODE) AS STORE_CODE, KA_STORE_NM " + \
             "     , SALES_COM_ABR_SA, SALES_COM_ABR_WH " + \
             "     , CONCAT(LEFT(POS_YM,4), '/', RIGHT(POS_YM,2)) AS POS_YM " + \
             "     , POS_QTY_PCS_D, POS_QTY_PKG_D, POS_AMT_D " + \
             "     , POS_QTY_PCS_M, POS_QTY_PKG_M, POS_AMT_M " + \
             "FROM DMMDL.DC0024_STORE_M " + \
             "WHERE {DATA_DATE} " + \
             "ORDER BY KA_SYSTEM_CODE, STORE_CODE; "

    dictMariaParameter = {
        "DATA_DATE": MariaEntity.MariaParameter(strOperator="=", objValue=strDataDate, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listStoreM = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listStoreM

def execWriteWorkbook(strJobPathRES, listStoreMatlMSystem, listStoreMatlM, listStoreM):
    if len(listStoreMatlMSystem) == 0 or len(listStoreMatlM) == 0 or len(listStoreM) == 0:
        return False
    else:
        objBook = None
        strKA_SYSTEM_CODE = None
        intStoreRowIndex=0
        intStoreMatlRowIndex = 0
        intlistStoreMCounter = 0

        for dictStoreMatlM in listStoreMatlM:
            if dictStoreMatlM["KA_SYSTEM_CODE"] != strKA_SYSTEM_CODE:
                strKA_SYSTEM_CODE = dictStoreMatlM["KA_SYSTEM_CODE"]

                if objBook != None:
                    objBook.close()

                objBook = xlsxwriter.Workbook(strJobPathRES.replace(".dat", "-" + dictStoreMatlM["KA_SYSTEM_CODE"] + ".dat"))

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

                if intlistStoreMCounter < len(listStoreM):
                    if strKA_SYSTEM_CODE == listStoreM[intlistStoreMCounter]["KA_SYSTEM_CODE"]:
                        objSheet1 = objBook.add_worksheet("門店" + listStoreM[intlistStoreMCounter]["KA_SYSTEM_CODE"] + listStoreM[intlistStoreMCounter]["KA_SYSTEM_NM"])
                        objSheet1.set_default_row(20) 
                        objSheet1.set_column(0, 0, 8)
                        objSheet1.set_column(1, 1, 10)
                        objSheet1.set_column(2, 2, 15)
                        objSheet1.set_column(3, 3, 30)
                        objSheet1.set_column(4, 4, 10)
                        objSheet1.set_column(5, 5, 10)
                        objSheet1.set_column(6, 6, 10)
                        objSheet1.set_column(7, 7, 17)
                        objSheet1.set_column(8, 8, 17)
                        objSheet1.set_column(9, 9, 17)
                        objSheet1.set_column(10, 10, 17)
                        objSheet1.set_column(11, 11, 17)
                        objSheet1.set_column(12, 12, 17)
                        intStoreRowIndex = 0
                        objSheet1.write(intStoreRowIndex, 0, "系统代号", objColumnFormat)
                        objSheet1.write(intStoreRowIndex, 1, "系统名称", objColumnFormat)
                        objSheet1.write(intStoreRowIndex, 2, "门店编号", objColumnFormat) 
                        objSheet1.write(intStoreRowIndex, 3, "门店名称", objColumnFormat)
                        objSheet1.write(intStoreRowIndex, 4, "业绩拆分地", objColumnFormat)
                        objSheet1.write(intStoreRowIndex, 5, "大仓所在地", objColumnFormat)
                        objSheet1.write(intStoreRowIndex, 6, "销售月份", objColumnFormat)
                        objSheet1.write(intStoreRowIndex, 7, "销售数量-日结算", objColumnFormat)
                        objSheet1.write(intStoreRowIndex, 8, "销售件数-日结算", objColumnFormat)
                        objSheet1.write(intStoreRowIndex, 9, "销售金额-日结算", objColumnFormat)
                        objSheet1.write(intStoreRowIndex, 10, "销售数量-月结算", objColumnFormat)
                        objSheet1.write(intStoreRowIndex, 11, "销售件数-月结算", objColumnFormat)
                        objSheet1.write(intStoreRowIndex, 12, "销售金额-月结算", objColumnFormat)
                        intStoreRowIndex += 1

                        while intlistStoreMCounter < len(listStoreM):
                            if strKA_SYSTEM_CODE == listStoreM[intlistStoreMCounter]["KA_SYSTEM_CODE"]:
                                objSheet1.write(intStoreRowIndex, 0, listStoreM[intlistStoreMCounter]["KA_SYSTEM_CODE"], objRowCenterFormat)
                                objSheet1.write(intStoreRowIndex, 1, listStoreM[intlistStoreMCounter]["KA_SYSTEM_NM"], objRowCenterFormat)
                                objSheet1.write(intStoreRowIndex, 2, listStoreM[intlistStoreMCounter]["STORE_CODE"], objRowCenterFormat)
                                objSheet1.write(intStoreRowIndex, 3, listStoreM[intlistStoreMCounter]["KA_STORE_NM"], objRowLeftFormat)
                                objSheet1.write(intStoreRowIndex, 4, listStoreM[intlistStoreMCounter]["SALES_COM_ABR_SA"], objRowCenterFormat)
                                objSheet1.write(intStoreRowIndex, 5, listStoreM[intlistStoreMCounter]["SALES_COM_ABR_WH"], objRowCenterFormat)
                                objSheet1.write(intStoreRowIndex, 6, listStoreM[intlistStoreMCounter]["POS_YM"], objRowCenterFormat)
                                objSheet1.write(intStoreRowIndex, 7, listStoreM[intlistStoreMCounter]["POS_QTY_PCS_D"], objRowRightFormat)
                                objSheet1.write(intStoreRowIndex, 8, listStoreM[intlistStoreMCounter]["POS_QTY_PKG_D"], objRowRightFormat)
                                objSheet1.write(intStoreRowIndex, 9, listStoreM[intlistStoreMCounter]["POS_AMT_D"], objRowRightFormat)
                                objSheet1.write(intStoreRowIndex, 10, listStoreM[intlistStoreMCounter]["POS_QTY_PCS_M"], objRowRightFormat)
                                objSheet1.write(intStoreRowIndex, 11, listStoreM[intlistStoreMCounter]["POS_QTY_PKG_M"], objRowRightFormat)
                                objSheet1.write(intStoreRowIndex, 12, listStoreM[intlistStoreMCounter]["POS_AMT_M"], objRowRightFormat)
                                intlistStoreMCounter += 1
                                intStoreRowIndex += 1
                            else:
                                break

                objSheet2 = objBook.add_worksheet("品項" + dictStoreMatlM["KA_SYSTEM_CODE"] + dictStoreMatlM["KA_SYSTEM_NM"])
                objSheet2.set_default_row(20) 
                objSheet2.set_column(0, 0, 8)
                objSheet2.set_column(1, 1, 10)
                objSheet2.set_column(2, 2, 15)
                objSheet2.set_column(3, 3, 30)
                objSheet2.set_column(4, 4, 10)
                objSheet2.set_column(5, 5, 10)
                objSheet2.set_column(6, 6, 10)
                objSheet2.set_column(7, 7, 10)
                objSheet2.set_column(8, 8, 20)
                objSheet2.set_column(9, 9, 40)
                objSheet2.set_column(10, 10, 12)
                objSheet2.set_column(11, 11, 17)
                objSheet2.set_column(12, 12, 17)
                objSheet2.set_column(13, 13, 17)
                objSheet2.set_column(14, 14, 17)
                objSheet2.set_column(15, 15, 17)
                objSheet2.set_column(15, 15, 17)
                objSheet2.set_column(16, 16, 17)
                intStoreMatlRowIndex = 0
                objSheet2.write(intStoreMatlRowIndex, 0, "系统代号", objColumnFormat)
                objSheet2.write(intStoreMatlRowIndex, 1, "系统名称", objColumnFormat)
                objSheet2.write(intStoreMatlRowIndex, 2, "门店编号", objColumnFormat) 
                objSheet2.write(intStoreMatlRowIndex, 3, "门店名称", objColumnFormat)
                objSheet2.write(intStoreMatlRowIndex, 4, "业绩拆分地", objColumnFormat)
                objSheet2.write(intStoreMatlRowIndex, 5, "大仓所在地", objColumnFormat)
                objSheet2.write(intStoreMatlRowIndex, 6, "产品大类", objColumnFormat)
                objSheet2.write(intStoreMatlRowIndex, 7, "PM线", objColumnFormat)
                objSheet2.write(intStoreMatlRowIndex, 8, "物料编号", objColumnFormat)
                objSheet2.write(intStoreMatlRowIndex, 9, "物料名称", objColumnFormat) 
                objSheet2.write(intStoreMatlRowIndex, 10, "销售月份", objColumnFormat)
                objSheet2.write(intStoreMatlRowIndex, 11, "销售数量-日结算", objColumnFormat)
                objSheet2.write(intStoreMatlRowIndex, 12, "销售件数-日结算", objColumnFormat)
                objSheet2.write(intStoreMatlRowIndex, 13, "销售金额-日结算", objColumnFormat)
                objSheet2.write(intStoreMatlRowIndex, 14, "销售数量-月结算", objColumnFormat)
                objSheet2.write(intStoreMatlRowIndex, 15, "销售件数-月结算", objColumnFormat)
                objSheet2.write(intStoreMatlRowIndex, 16, "销售金额-月结算", objColumnFormat)
                intStoreMatlRowIndex += 1


            objSheet2.write(intStoreMatlRowIndex, 0, dictStoreMatlM["KA_SYSTEM_CODE"], objRowCenterFormat)
            objSheet2.write(intStoreMatlRowIndex, 1, dictStoreMatlM["KA_SYSTEM_NM"], objRowCenterFormat)
            objSheet2.write(intStoreMatlRowIndex, 2, dictStoreMatlM["STORE_CODE"], objRowCenterFormat)
            objSheet2.write(intStoreMatlRowIndex, 3, dictStoreMatlM["KA_STORE_NM"], objRowLeftFormat)
            objSheet2.write(intStoreMatlRowIndex, 4, dictStoreMatlM["SALES_COM_ABR_SA"], objRowCenterFormat)
            objSheet2.write(intStoreMatlRowIndex, 5, dictStoreMatlM["SALES_COM_ABR_WH"], objRowCenterFormat)
            objSheet2.write(intStoreMatlRowIndex, 6, dictStoreMatlM["PROD_H1_NM"], objRowCenterFormat)
            objSheet2.write(intStoreMatlRowIndex, 7, dictStoreMatlM["PROD_H2_NM"], objRowCenterFormat)
            objSheet2.write(intStoreMatlRowIndex, 8, dictStoreMatlM["PROD_MATL_ID"], objRowCenterFormat)
            objSheet2.write(intStoreMatlRowIndex, 9, dictStoreMatlM["PROD_MATL_NM"], objRowLeftFormat)
            objSheet2.write(intStoreMatlRowIndex, 10, dictStoreMatlM["POS_YM"], objRowCenterFormat)
            objSheet2.write(intStoreMatlRowIndex, 11, dictStoreMatlM["POS_QTY_PCS_D"], objRowRightFormat)
            objSheet2.write(intStoreMatlRowIndex, 12, dictStoreMatlM["POS_QTY_PKG_D"], objRowRightFormat)
            objSheet2.write(intStoreMatlRowIndex, 13, dictStoreMatlM["POS_AMT_D"], objRowRightFormat)
            objSheet2.write(intStoreMatlRowIndex, 14, dictStoreMatlM["POS_QTY_PCS_M"], objRowRightFormat)
            objSheet2.write(intStoreMatlRowIndex, 15, dictStoreMatlM["POS_QTY_PKG_M"], objRowRightFormat)
            objSheet2.write(intStoreMatlRowIndex, 16, dictStoreMatlM["POS_AMT_M"], objRowRightFormat)
            intStoreMatlRowIndex += 1
        
        if objBook != None:
            objBook.close()

        return True

def execMailStoreMatlM(strLoggerName, strJobPathRES, strDataDate):
    strEDIConnection = "3DW-DWuser@tpe-centos7-maria10-dw"
    strEDIDB = "DMMDL"
    
    today = datetime.date.today()
    strTODAY = str(today.year) + ("0" + str(today.month))[-2:] + ("0" + str(today.day))[-2:]

    listWorkDayT = getWorkDayT(strEDIConnection, strEDIDB, strDataDate, strTODAY)
    
    if len(listWorkDayT) == 1:
        if listWorkDayT[0]["WORKDAY_YN"] == "Y" and today.day<12:
            listStoreMatlMSystem = getStoreMatlMSystemList(strEDIConnection, strEDIDB, strDataDate)
            listStoreMatlM = getStoreMatlMList(strEDIConnection, strEDIDB, strDataDate)
            listStoreM = getStoreMList(strEDIConnection, strEDIDB, strDataDate)

            if execWriteWorkbook(strJobPathRES, listStoreMatlMSystem, listStoreMatlM, listStoreM) == True:
                strMessageSMTPServer = "tw-mail02.want-want.com"
                strMessageSMTPFrom = "Data.Center@want-want.com"

                for dictStoreMatlMSystem in listStoreMatlMSystem:
                    strMessageSubject = dictStoreMatlMSystem["KA_SYSTEM_NM"] + "-现渠自动化管理平台-门店品项销售数据-"+ dictStoreMatlMSystem["POS_YM"] +"月结算报表-" + strDataDate
                    strAttachFilePath = strJobPathRES.replace(".dat", "-" + dictStoreMatlMSystem["KA_SYSTEM_CODE"] + ".dat")
                    strAttachFileName = dictStoreMatlMSystem["KA_SYSTEM_NM"] + "-现渠自动化管理平台-门店品项销售数据-"+ dictStoreMatlMSystem["POS_YM"] +"月结算报表-" + strDataDate + ".xlsx"

                    if dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "H002":
                        #  量贩 H002 大润发 : 朱晓菁
                        arrayMessageSMTPTo = [ "Zhu_XiaoJing2@want-want.com", "Zoe.Hsu@want-want.com" ]
                    elif dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "H005":
                        #  量贩 H005 麦德龙 : 朱晓菁
                        arrayMessageSMTPTo = [ "Zhu_XiaoJing2@want-want.com", "Zoe.Hsu@want-want.com" ]
                    elif dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "H007":
                        #  标超 H007 人人乐 : 杨露露
                        arrayMessageSMTPTo = [ "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
                    elif dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "H009":
                        #  标超 H009 世纪联华 : 朱晓菁
                        arrayMessageSMTPTo = [ "Zhu_XiaoJing2@want-want.com", "Zoe.Hsu@want-want.com" ]
                    elif dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "H010":
                        #  量贩 H010 沃尔玛 : 张懿晴
                        arrayMessageSMTPTo = [ "Zhang_YiQing@want-want.com", "Zoe.Hsu@want-want.com" ]
                    elif dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "H011":
                        #  标超 H011 物美 : 杨露露
                        arrayMessageSMTPTo = [ "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
                    elif dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "H013":
                        #  量贩 H013 易初莲花 : 许曣
                        arrayMessageSMTPTo = [ "Xu_Yao@want-want.com", "Zoe.Hsu@want-want.com" ]
                    elif dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "H016":
                        #  标超 H016 丹尼斯 : 杨露露
                        arrayMessageSMTPTo = [ "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
                    elif dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "H017":
                        #  标超 H017 天虹 : 杨露露
                        arrayMessageSMTPTo = [ "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
                    elif dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "H018":
                        #  标超 H018 华润万家 : 张懿晴
                        arrayMessageSMTPTo = [ "Zhang_YiQing@want-want.com", "Zoe.Hsu@want-want.com" ]
                    elif dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "H021":
                        #  标超 H021 美特好 : 杨露露
                        arrayMessageSMTPTo = [ "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
                    elif dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "H042":
                        #  标超 H042 百佳华 : 杨露露
                        arrayMessageSMTPTo = [ "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
                    elif dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "H060":
                        #  标超 H060 北国系统 : 杨露露
                        arrayMessageSMTPTo = [ "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
                    elif dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "S001":
                        #  标超 S001 农工商 : 张懿晴
                        arrayMessageSMTPTo = [ "Zhang_YiQing@want-want.com", "Zoe.Hsu@want-want.com" ]
                    elif dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "S004":
                        #  标超 S004 上海联华 : 朱晓菁
                        arrayMessageSMTPTo = [ "Zhu_XiaoJing2@want-want.com", "Zoe.Hsu@want-want.com" ]
                    elif dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "S006":
                        #  标超 S006 苏果 : 朱晓菁
                        arrayMessageSMTPTo = [ "Zhu_XiaoJing2@want-want.com", "Zoe.Hsu@want-want.com" ]
                    elif dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "S009":
                        #  便利 S009 中百便民 : 杨露露
                        arrayMessageSMTPTo = [ "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
                    elif dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "S010":
                        #  标超 S010 中百仓储 : 杨露露
                        arrayMessageSMTPTo = [ "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
                    elif dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "S011":
                        #  标超 S011 中商 : 杨露露
                        arrayMessageSMTPTo = [ "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
                    elif dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "S014":
                        #  标超 S014 永辉 : 许曣
                        arrayMessageSMTPTo = [ "Xu_Yao@want-want.com", "Zoe.Hsu@want-want.com" ]
                    elif dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "S018":
                        #  标超 S018 武商 : 杨露露
                        arrayMessageSMTPTo = [ "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
                    elif dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "S020":
                        #  标超 S020 威海糖酒 : 杨露露
                        arrayMessageSMTPTo = [ "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
                    elif dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "S026":
                        #  标超 S026 新世纪 : 杨露露
                        arrayMessageSMTPTo = [ "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
                    elif dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "S030":
                        #  便利 S030 红旗连锁 : 杨露露
                        arrayMessageSMTPTo = [ "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
                    elif dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "S031":
                        #  标超 S031 银座 : 杨露露
                        arrayMessageSMTPTo = [ "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
                    elif dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "S044":
                        #  标超 S044 北京华冠 : 杨露露
                        arrayMessageSMTPTo = [ "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
                    elif dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "S052":
                        #  标超 S052 步步高 : 杨露露
                        arrayMessageSMTPTo = [ "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
                    elif dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "S063":
                        #  标超 S063 新华都 : 杨露露
                        arrayMessageSMTPTo = [ "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
                    elif dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "S110":
                        #  标超 S110 联华华商 : 杨露露
                        arrayMessageSMTPTo = [ "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
                    elif dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "S151":
                        #  标超 S151 华联系统 : 杨露露
                        arrayMessageSMTPTo = [ "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
                    elif dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "S219":
                        #  标超 S219 介休吉隆斯 : 杨露露
                        arrayMessageSMTPTo = [ "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
                    elif dictStoreMatlMSystem["KA_SYSTEM_CODE"] == "S284":
                        #  标超 S284 重客隆 : 
                        arrayMessageSMTPTo = [ "Zoe.Hsu@want-want.com" ]
                    else:
                        arrayMessageSMTPTo = [ "Zoe.Hsu@want-want.com" ]

                    if (os.stat(strAttachFilePath).st_size/1024/1024)>7:
                        strContent = "尊敬的长官：早上好！\n" + \
                            "敬请查阅：截止" + strDataDate + "为止，" + "【" + dictStoreMatlMSystem["KA_SYSTEM_NM"] + "-门店品项销售数据-" + dictStoreMatlMSystem["POS_YM"] + "月结算报表】\n\n" + \
                            "注意！此档案有多个压缩包，请将压缩包置于同一位置后，在.zip压缩文档上点选二下執行解压缩，即可取得EXCEL文档。\n\n"

                        strAttachDirPath = os.path.dirname(strAttachFilePath)
                        strExcelFilePath = os.path.join(strAttachDirPath, strAttachFileName)
                        strZipFileName = dictStoreMatlMSystem["KA_SYSTEM_NM"] + "-现渠自动化管理平台-门店品项销售数据-"+ dictStoreMatlMSystem["POS_YM"] +"月结算报表-" + strDataDate
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
                            "敬请查阅：截止" + strDataDate + "为止，" + "【" + dictStoreMatlMSystem["KA_SYSTEM_NM"] + "-门店品项销售数据-" + dictStoreMatlMSystem["POS_YM"] + "月结算报表】\n\n"

                        Message.sendSMTPMail(strMessageSMTPServer, strMessageSMTPFrom, arrayMessageSMTPTo, strMessageSubject, strContent, strAttachFilePath, strAttachFileName)
            
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

    execMailStoreMatlM(strLoggerName, strJobPathRES, strDataDate)

if __name__ == "__main__":
    main()
