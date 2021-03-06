DROP PROCEDURE IF EXISTS DWWANT.SP_DC0024_ORDER_30101_TRAS;

CREATE PROCEDURE DWWANT.SP_DC0024_ORDER_30101_TRAS (
    VAR_EDI_NO CHAR(12), VAR_DATA_DATE CHAR(8), OUT VAR_SP_RESULT CHAR(1)
)
BEGIN
    DECLARE VAR_DATE_MIN CHAR(8);

    SET VAR_DATE_MIN = CONCAT(DATE_FORMAT(DATE_ADD(STR_TO_DATE(VAR_DATA_DATE, '%Y%m%d'), INTERVAL -3 MONTH), '%Y%m'), '01');

    INSERT INTO DMMDL.DC0024_ORDR_TRAS_D
    SELECT VAR_EDI_NO AS EDI_NO, VAR_DATA_DATE AS DATA_DATE
         , S.KA_SYSTEM_CODE
         , DWWANT.FN_GET_CM_KA_SYSTEM_NM(S.KA_SYSTEM_CODE) AS KA_SYSTEM_NM
         , S.SYSTEM_ORDR_DATE
         , S.ORDR_MAIN_ID
         , S.SYSTEM_ORDR_NO
         , S.SAP_ORDR_NO
         , S.OPEN_ORDR_DATE
         , S.CUST_ID
         , S.SALES_COM_ID_DE_ORDR
         , DWWANT.FN_GET_ORG_SALES_COM_ABR(S.SALES_COM_ID_DE_ORDR) AS SALES_COM_ABR_DE_ORDR
         , S.SALES_COM_ID_DE
         , DWWANT.FN_GET_ORG_SALES_COM_ABR(S.SALES_COM_ID_DE) AS SALES_COM_ABR_DE
         , S.SALES_COM_ID_BL
         , DWWANT.FN_GET_ORG_SALES_COM_ABR(S.SALES_COM_ID_BL) AS SALES_COM_ABR_BL
         , S.SALES_CHAN_ID
         , S.PROD_DIV_ID
         , LEFT(S.SYSTEM_DEV_TIME, 8) AS SYSTEM_DEV_DATE
         , S.IS_FACT_DEV
          
         , S.ORDR_LINE_NUM
         , S.SAP_LINE_NUM
         , S.SYSTEM_ORDR_PROD_NM
         , (SELECT PROD_H1_ID from DWWANT.PROD_MATL WHERE PROD_MATL_ID=S.PROD_MATL_ID_SYS) AS PROD_H1_ID_SYS
         , DWWANT.FN_GET_PROD_HIER_NM((SELECT PROD_H1_ID from DWWANT.PROD_MATL WHERE PROD_MATL_ID=S.PROD_MATL_ID_SYS)) AS PROD_H1_NM_SYS
         , (SELECT PROD_H2_ID from DWWANT.PROD_MATL WHERE PROD_MATL_ID=S.PROD_MATL_ID_SYS) AS PROD_H2_ID_SYS
         , DWWANT.FN_GET_PROD_HIER_NM((SELECT PROD_H2_ID from DWWANT.PROD_MATL WHERE PROD_MATL_ID=S.PROD_MATL_ID_SYS)) AS PROD_H2_NM_SYS
         , S.PROD_MATL_ID_SYS
         , DWWANT.FN_GET_PROD_MATL_NM(S.PROD_MATL_ID_SYS) AS PROD_MATL_NM_SYS

         , (SELECT PROD_H1_ID from DWWANT.PROD_MATL WHERE PROD_MATL_ID=S.PROD_MATL_ID_OPEN) AS PROD_H1_ID_OPEN
         , DWWANT.FN_GET_PROD_HIER_NM((SELECT PROD_H1_ID from DWWANT.PROD_MATL WHERE PROD_MATL_ID=S.PROD_MATL_ID_OPEN)) AS PROD_H1_NM_OPEN
         , (SELECT PROD_H2_ID from DWWANT.PROD_MATL WHERE PROD_MATL_ID=S.PROD_MATL_ID_OPEN) AS PROD_H2_ID_OPEN
         , DWWANT.FN_GET_PROD_HIER_NM((SELECT PROD_H2_ID from DWWANT.PROD_MATL WHERE PROD_MATL_ID=S.PROD_MATL_ID_OPEN)) AS PROD_H2_NM_OPEN
         , S.PROD_MATL_ID_OPEN
         , DWWANT.FN_GET_PROD_MATL_NM(S.PROD_MATL_ID_OPEN) AS PROD_MATL_NM_OPEN
          
         , S.STORE_PLACE_CODE
         , S.IS_STORE_PLACE_DIR
          
         , S.PROD_AMT_PKG_SYS
         , S.PROD_QTY_PKG_SYS
         , S.PROD_AMT_PKG_OPEN
         , S.PROD_QTY_PKG_OPEN
         , S.SAP_AMT_PKG_OPEN
         , S.SAP_QTY_PKG_OPEN
         , S.SAP_AMT_PKG_APPD
         , S.SAP_QTY_PKG_APPD
         , S.SHIP_QTY_PKG_DIF
         , S.SHIP_QTY_PKG_DEV
         , S.SHIP_QTY_PKG_ACT
    FROM DWWANT.TRAS_KA_ORDR S
    WHERE S.KA_SYSTEM_CODE IN ('C005','C010','H001','H002','H005','H007','H009','H010','H011','H013',
                               'H016','H017','H018','H021','H042','H060','S004','S006','S009','S010',
                               'S011','S014','S018','S020','S026','S030','S031','S044','S052','S063',
                               'S110','S151','S219')
      AND S.SYSTEM_ORDR_DATE>=VAR_DATE_MIN AND S.SYSTEM_ORDR_DATE<=VAR_DATA_DATE
    ORDER BY S.KA_SYSTEM_CODE, S.SYSTEM_ORDR_DATE, S.SYSTEM_ORDR_NO, S.ORDR_LINE_NUM
    ;

    SET VAR_SP_RESULT='Y';
    COMMIT;
END
;