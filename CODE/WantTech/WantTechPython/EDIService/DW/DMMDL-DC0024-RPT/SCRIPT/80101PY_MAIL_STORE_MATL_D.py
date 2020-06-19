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

def getStoreMatlDSystemList(strEDIConnection, strEDIDB, strDataDate):
    strSQL = "SELECT KA_SYSTEM_CODE, MAX(KA_SYSTEM_NM) AS KA_SYSTEM_NM, MAX(POS_INV_DATE) AS POS_INV_DATE " + \
             "FROM DMMDL.DC0024_STORE_MATL_D " + \
             "WHERE {DATA_DATE} " + \
             "GROUP BY KA_SYSTEM_CODE " + \
             "ORDER BY KA_SYSTEM_CODE; "

    dictMariaParameter = {
        "DATA_DATE": MariaEntity.MariaParameter(strOperator="=", objValue=strDataDate, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listStoreMatlDSystem = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listStoreMatlDSystem

def getStoreMatlDList(strEDIConnection, strEDIDB, strDataDate):
    strSQL = "SELECT KA_SYSTEM_CODE, KA_SYSTEM_NM " + \
             "     , CONCAT(KA_SYSTEM_CODE, '-', KA_STORE_WH_CODE) AS KA_STORE_WH_CODE, KA_STORE_WH_NM, STORE_WH_TYPE_NM " + \
             "     , SALES_COM_ABR_SA, SALES_COM_ABR_WH " + \
             "     , PROD_H1_NM, PROD_H2_NM, PROD_MATL_ID, PROD_MATL_NM " + \
             "     , POS_INV_DATE, POS_QTY_PCS, POS_QTY_PKG, POS_AMT, INV_QTY_PCS, INV_QTY_PKG " + \
             "FROM DMMDL.DC0024_STORE_MATL_D " + \
             "WHERE {DATA_DATE} " + \
             "ORDER BY KA_SYSTEM_CODE, KA_STORE_WH_CODE, PROD_H1_ID, PROD_H2_ID, PROD_MATL_ID; "

    dictMariaParameter = {
        "DATA_DATE": MariaEntity.MariaParameter(strOperator="=", objValue=strDataDate, enumType=MariaEntity.EnumMariaParameterType.Char),
    }
    strSQL = DBEntity.getMariaSQLCommand(strSQL, dictMariaParameter)

    listStoreMatlD = DBEntity.getMariaDataList(strEDIConnection, strEDIDB, strSQL)
    return listStoreMatlD

def execWriteWorkbook(strJobPathRES, listStoreMatlD):
    if len(listStoreMatlD) == 0:
        return False
    else:
        objBook = None
        strKA_SYSTEM_CODE = None
        intRowIndex = 0

        for dictStoreMatlD in listStoreMatlD:
            if dictStoreMatlD["KA_SYSTEM_CODE"] != strKA_SYSTEM_CODE:
                strKA_SYSTEM_CODE = dictStoreMatlD["KA_SYSTEM_CODE"]

                if objBook != None:
                    objBook.close()
                
                objBook = xlsxwriter.Workbook(strJobPathRES.replace(".dat", "-" + dictStoreMatlD["KA_SYSTEM_CODE"] + ".dat"))

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
            
                objSheet = objBook.add_worksheet(dictStoreMatlD["KA_SYSTEM_CODE"] + dictStoreMatlD["KA_SYSTEM_NM"])

                objSheet.set_default_row(20)   
            
                objSheet.set_column(0, 0, 8)
                objSheet.set_column(1, 1, 10)
                objSheet.set_column(2, 2, 15)
                objSheet.set_column(3, 3, 30)
                objSheet.set_column(4, 4, 10)
                objSheet.set_column(5, 5, 10)
                objSheet.set_column(6, 6, 10)
                objSheet.set_column(7, 7, 10)
                objSheet.set_column(8, 8, 10)
                objSheet.set_column(9, 9, 20)
                objSheet.set_column(10, 10, 40)
                objSheet.set_column(11, 11, 12)
                objSheet.set_column(12, 12, 10)
                objSheet.set_column(13, 13, 10)
                objSheet.set_column(14, 14, 10)
                objSheet.set_column(15, 15, 10)
                objSheet.set_column(16, 16, 10)

                intRowIndex = 0
            
                objSheet.write(intRowIndex, 0, "系统代号", objColumnFormat)
                objSheet.write(intRowIndex, 1, "系统名称", objColumnFormat)
                objSheet.write(intRowIndex, 2, "门店编号", objColumnFormat) 
                objSheet.write(intRowIndex, 3, "门店名称", objColumnFormat)
                objSheet.write(intRowIndex, 4, "门店大仓别", objColumnFormat)
                objSheet.write(intRowIndex, 5, "业绩拆分地", objColumnFormat)
                objSheet.write(intRowIndex, 6, "大仓所在地", objColumnFormat)
                objSheet.write(intRowIndex, 7, "产品大类", objColumnFormat)
                objSheet.write(intRowIndex, 8, "PM线", objColumnFormat)
                objSheet.write(intRowIndex, 9, "物料编号", objColumnFormat)
                objSheet.write(intRowIndex, 10, "物料名称", objColumnFormat) 
                objSheet.write(intRowIndex, 11, "销售库存日期", objColumnFormat)
                objSheet.write(intRowIndex, 12, "销售数量", objColumnFormat)
                objSheet.write(intRowIndex, 13, "销售件数", objColumnFormat)
                objSheet.write(intRowIndex, 14, "销售金额", objColumnFormat)
                objSheet.write(intRowIndex, 15, "库存数量", objColumnFormat)
                objSheet.write(intRowIndex, 16, "库存件数", objColumnFormat)
                intRowIndex += 1
            
            objSheet.write(intRowIndex, 0, dictStoreMatlD["KA_SYSTEM_CODE"], objRowCenterFormat)
            objSheet.write(intRowIndex, 1, dictStoreMatlD["KA_SYSTEM_NM"], objRowCenterFormat)
            objSheet.write(intRowIndex, 2, dictStoreMatlD["KA_STORE_WH_CODE"], objRowCenterFormat)
            objSheet.write(intRowIndex, 3, dictStoreMatlD["KA_STORE_WH_NM"], objRowLeftFormat)
            objSheet.write(intRowIndex, 4, dictStoreMatlD["STORE_WH_TYPE_NM"], objRowCenterFormat)
            objSheet.write(intRowIndex, 5, dictStoreMatlD["SALES_COM_ABR_SA"], objRowCenterFormat)
            objSheet.write(intRowIndex, 6, dictStoreMatlD["SALES_COM_ABR_WH"], objRowCenterFormat)
            objSheet.write(intRowIndex, 7, dictStoreMatlD["PROD_H1_NM"], objRowCenterFormat)
            objSheet.write(intRowIndex, 8, dictStoreMatlD["PROD_H2_NM"], objRowCenterFormat)
            objSheet.write(intRowIndex, 9, dictStoreMatlD["PROD_MATL_ID"], objRowCenterFormat)
            objSheet.write(intRowIndex, 10, dictStoreMatlD["PROD_MATL_NM"], objRowLeftFormat)
            objSheet.write(intRowIndex, 11, Common.formatDateString(dictStoreMatlD["POS_INV_DATE"]), objRowCenterFormat)
            objSheet.write(intRowIndex, 12, dictStoreMatlD["POS_QTY_PCS"], objRowRightFormat)
            objSheet.write(intRowIndex, 13, dictStoreMatlD["POS_QTY_PKG"], objRowRightFormat)
            objSheet.write(intRowIndex, 14, dictStoreMatlD["POS_AMT"], objRowRightFormat)
            objSheet.write(intRowIndex, 15, dictStoreMatlD["INV_QTY_PCS"], objRowRightFormat)
            objSheet.write(intRowIndex, 16, dictStoreMatlD["INV_QTY_PKG"], objRowRightFormat)
            intRowIndex += 1
                    
        objBook.close()
        return True

def execMailStoreMatlD(strLoggerName, strJobPathRES, strDataDate):
    strEDIConnection = "3DW-DWuser@tpe-centos7-maria10-dw"
    strEDIDB = "DMMDL"

    listStoreMatlD = getStoreMatlDList(strEDIConnection, strEDIDB, strDataDate)
    listStoreMatlDSystem = getStoreMatlDSystemList(strEDIConnection, strEDIDB, strDataDate)

    if execWriteWorkbook(strJobPathRES, listStoreMatlD) == True:
        strMessageSMTPServer = "tw-mail02.want-want.com"
        strMessageSMTPFrom = "Data.Center@want-want.com"

        for dictStoreMatlDSystem in listStoreMatlDSystem:
            strMessageSubject = dictStoreMatlDSystem["KA_SYSTEM_NM"] + "-现渠自动化管理平台-门店品项销售库存数据-日结算报表-" + dictStoreMatlDSystem["POS_INV_DATE"]
            strAttachFilePath = strJobPathRES.replace(".dat", "-" + dictStoreMatlDSystem["KA_SYSTEM_CODE"] + ".dat")
            strAttachFileName = dictStoreMatlDSystem["KA_SYSTEM_NM"] + "-现渠自动化管理平台-门店品项销售库存数据-日结算报表-" + dictStoreMatlDSystem["POS_INV_DATE"] + ".xlsx"

            if dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "H002":
                #  量贩 H002 大润发 : 成骏 / 郭丹丹 / 朱晓菁
                arrayMessageSMTPTo = [ "Cheng_Jun2@want-want.com", "Guo_DanDan@want-want.com", "Zhu_XiaoJing2@want-want.com", "Zoe.Hsu@want-want.com" ]
            elif dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "H005":
                #  量贩 H005 麦德龙 : 左晓云 / 成骏 / 崔建辉 / 朱晓菁
                arrayMessageSMTPTo = [ "Zuo_XiaoYun2@want-want.com", "Cheng_Jun2@want-want.com", "Cui_JianHui@want-want.com", "Zhu_XiaoJing2@want-want.com", "Zoe.Hsu@want-want.com" ]
            elif dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "H007":
                #  标超 H007 人人乐 : 郭鹏 / 宋涛 / 杨露露
                arrayMessageSMTPTo = [ "Guo_Peng@want-want.com", "Song_Tao2@want-want.com", "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
            elif dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "H009":
                #  标超 H009 世纪联华 : 郭鹏 / 成骏 / 宋涛 / 朱晓菁
                arrayMessageSMTPTo = [ "Guo_Peng@want-want.com", "Cheng_Jun2@want-want.com", "Song_Tao2@want-want.com", "Zhu_XiaoJing2@want-want.com", "Zoe.Hsu@want-want.com" ]
            elif dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "H010":
                #  量贩 H010 沃尔玛 : 郭鹏 / 王勇 / 成骏 / 张懿晴
                arrayMessageSMTPTo = [ "Guo_Peng@want-want.com", "Wang_Yong@want-want.com", "Cheng_Jun2@want-want.com", "Zhang_YiQing@want-want.com", "Zoe.Hsu@want-want.com" ]
            elif dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "H011":
                #  标超 H011 物美 : 陈寿明 / 胡雪斌 / 黄华 / 王珑 / 鲍冠杰 / 杨露露     
                arrayMessageSMTPTo = [ "chen_shouming@want-want.com", "hu_xuebin@want-want.com", "Huang_Hua@want-want.com", "Wang_Long2@want-want.com", "Bao_GuanJie@want-want.com", "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
            elif dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "H013":
                #  量贩 H013 易初莲花 : 左晓云 / 成骏 / 崔建辉 / 许曣
                arrayMessageSMTPTo = [ "Zuo_XiaoYun2@want-want.com", "Cheng_Jun2@want-want.com", "Cui_JianHui@want-want.com", "Xu_Yao@want-want.com", "Zoe.Hsu@want-want.com" ]
            elif dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "H016":
                #  标超 H016 丹尼斯 : 黄艳丽 / 杨露露
                arrayMessageSMTPTo = [ "huang_yanli2@want-want.com", "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
            elif dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "H017":
                #  标超 H017 天虹 : 王从阳 / 章丽萍 / 张健 / 何丽琴 / 杨露露
                arrayMessageSMTPTo = [ "wang_chongyang@want-want.com", "Zhang_LiPing2@want-want.com", "Zhang_Jian7@want-want.com", "he_liqin@want-want.com", "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
            elif dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "H018":
                #  标超 H018 华润万家 : 郭鹏 / 高贺 / 成骏 / 张懿晴
                arrayMessageSMTPTo = [ "Guo_Peng@want-want.com", "Gao_He@want-want.com", "Cheng_Jun2@want-want.com", "Zhang_YiQing@want-want.com", "Zoe.Hsu@want-want.com" ]
            elif dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "H021":
                #  标超 H021 美特好 : 杨文卿 / 杨露露
                arrayMessageSMTPTo = [ "yang_wenqing@want-want.com", "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
            elif dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "H042":
                #  标超 H042 百佳华 : 王从阳 / 雷艳红 / 何丽琴 / 杨露露
                arrayMessageSMTPTo = [ "wang_chongyang@want-want.com", "lei_yanhong@want-want.com", "he_liqin@want-want.com", "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
            elif dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "H060":
                #  标超 H060 北国系统 : 艾贵银 / 杨露露
                arrayMessageSMTPTo = [ "ai_guiyin@want-want.com", "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
            elif dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "S001":
                #  标超 S001 农工商 : 郭鹏 / 成骏 / 张懿晴
                arrayMessageSMTPTo = [ "Guo_Peng@want-want.com", "Cheng_Jun2@want-want.com", "Zhang_YiQing@want-want.com", "Zoe.Hsu@want-want.com" ]
            elif dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "S004":
                #  标超 S004 上海联华 : 郭鹏 / 成骏 / 宋涛 / 朱晓菁
                arrayMessageSMTPTo = [ "Guo_Peng@want-want.com", "Cheng_Jun2@want-want.com", "Song_Tao2@want-want.com", "Zhu_XiaoJing2@want-want.com", "Zoe.Hsu@want-want.com" ]
            elif dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "S006":
                #  标超 S006 苏果 : 杨斯竣 / 成骏 / 朱晓菁
                arrayMessageSMTPTo = [ "Yang_SiJun@want-want.com", "Cheng_Jun2@want-want.com", "Zhu_XiaoJing2@want-want.com", "Zoe.Hsu@want-want.com" ]
            elif dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "S009":
                #  便利 S009 中百便民 : 王宁 / 杨露露
                arrayMessageSMTPTo = [ "wang_ning2@want-want.com", "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
            elif dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "S010":
                #  标超 S010 中百仓储 : 王宁 / 杨露露
                arrayMessageSMTPTo = [ "wang_ning2@want-want.com", "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
            elif dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "S011":
                #  标超 S011 中商 : 王宁 / 杨露露
                arrayMessageSMTPTo = [ "wang_ning2@want-want.com", "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
            elif dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "S014":
                #  标超 S014 永辉 : 徐俊 / 张利霞 / 成骏 / 许曣
                arrayMessageSMTPTo = [ "Xu_Jun6@want-want.com", "Zhang_LiXia@want-want.com", "Cheng_Jun2@want-want.com", "Xu_Yao@want-want.com", "Zoe.Hsu@want-want.com" ]
            elif dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "S018":
                #  标超 S018 武商 : 王宁 / 杨露露
                arrayMessageSMTPTo = [ "wang_ning2@want-want.com", "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
            elif dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "S020":
                #  标超 S020 威海糖酒 : 陈寿明 / 徐瑞虎 / 杨露露
                arrayMessageSMTPTo = [ "chen_shouming@want-want.com", "Xu_Ruihu@want-want.com", "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
            elif dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "S026":
                #  标超 S026 新世纪 : 刘爱民 / 杨露露
                arrayMessageSMTPTo = [ "Liu_AiMin@want-want.com", "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
            elif dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "S030":
                #  便利 S030 红旗连锁 : 向君 / 杨露露
                arrayMessageSMTPTo = [ "xiang_jun@want-want.com", "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
            elif dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "S031":
                #  标超 S031 银座 : 陈寿明 / 黄艳丽 / 徐瑞虎 / 王冰冰 / 杨露露
                arrayMessageSMTPTo = [ "chen_shouming@want-want.com", "huang_yanli2@want-want.com", "Xu_Ruihu@want-want.com", "wang_bingbing@want-want.com", "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
            elif dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "S044":
                #  标超 S044 北京华冠 : 陈寿明 / 杨露露
                arrayMessageSMTPTo = [ "chen_shouming@want-want.com", "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
            elif dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "S052":
                #  标超 S052 步步高 : 张健 / 杨露露
                arrayMessageSMTPTo = [ "Zhang_Jian7@want-want.com", "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
            elif dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "S063":
                #  标超 S063 新华都 : 朱巧燕 / 杨露露
                arrayMessageSMTPTo = [ "zhu_qiaoyan@want-want.com", "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
            elif dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "S110":
                #  标超 S110 联华华商 : 胡雪斌 / 鲍冠杰 / 杨露露
                arrayMessageSMTPTo = [ "hu_xuebin@want-want.com", "Bao_GuanJie@want-want.com", "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
            elif dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "S151":
                #  标超 S151 华联系统 : 王冰冰 / 杨露露
                arrayMessageSMTPTo = [ "wang_bingbing@want-want.com", "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
            elif dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "S219":
                #  标超 S219 介休吉隆斯 : 杨文卿 / 杨露露
                arrayMessageSMTPTo = [ "yang_wenqing@want-want.com", "Yang_LuLu@want-want.com", "Zoe.Hsu@want-want.com" ]
            elif dictStoreMatlDSystem["KA_SYSTEM_CODE"] == "S284":
                #  标超 S284 重客隆 : 刘爱民
                arrayMessageSMTPTo = [ "Liu_AiMin@want-want.com", "Zoe.Hsu@want-want.com" ]
            else:
                arrayMessageSMTPTo = [ "Zoe.Hsu@want-want.com" ]

            if (os.stat(strAttachFilePath).st_size/1024/1024)>7:
                strContent = "尊敬的长官：早上好！\n" + \
                    "敬请查阅：截止" + dictStoreMatlDSystem["POS_INV_DATE"][4:6] + "月" + dictStoreMatlDSystem["POS_INV_DATE"][-2:] + "日【" + dictStoreMatlDSystem["KA_SYSTEM_NM"] + "-门店品项销售库存数据-日结算报表】\n\n" + \
                    "注意！此档案有多个压缩包，请将压缩包置于同一位置后，在.zip压缩文档上点选二下執行解压缩，即可取得EXCEL文档。\n\n"

                strAttachDirPath = os.path.dirname(strAttachFilePath)
                strExcelFilePath = os.path.join(strAttachDirPath, strAttachFileName)
                strZipFileName = dictStoreMatlDSystem["KA_SYSTEM_NM"] + "-现渠自动化管理平台-门店品项销售库存数据-日结算报表-" + dictStoreMatlDSystem["POS_INV_DATE"]
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
                    "敬请查阅：截止" + dictStoreMatlDSystem["POS_INV_DATE"][4:6] + "月" + dictStoreMatlDSystem["POS_INV_DATE"][-2:] + "日【" + dictStoreMatlDSystem["KA_SYSTEM_NM"] + "-门店品项销售库存数据-日结算报表】\n\n"
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

    execMailStoreMatlD(strLoggerName, strJobPathRES, strDataDate)

if __name__ == "__main__":
    main()
