DROP PROCEDURE IF EXISTS DWWANT.SP_KA_30202_KA_W;

CREATE PROCEDURE DWWANT.SP_KA_30202_KA_W (
    VAR_EDI_NO CHAR(12), VAR_DATA_DATE CHAR(8), OUT VAR_SP_RESULT CHAR(1)
)
BEGIN
    DECLARE VAR_POS_DATE_MIN CHAR(8);
    DECLARE VAR_POS_DATE_MAX CHAR(8);
    DECLARE VAR_WEEK_FIRST_DATE CHAR(8);
    DECLARE VAR_WEEK_LAST_DATE CHAR(8);

    SELECT POS_DATE_MIN, POS_DATE_MAX INTO VAR_POS_DATE_MIN, VAR_POS_DATE_MAX
    FROM DWWANT.EDI_FLOW_DWWANT_KA
    WHERE EDI_NO=VAR_EDI_NO;

    SET VAR_WEEK_FIRST_DATE = DWWANT.FN_GET_WEEK_FIRST_DATE(VAR_POS_DATE_MIN);
    SET VAR_WEEK_LAST_DATE = DWWANT.FN_GET_WEEK_LAST_DATE(VAR_POS_DATE_MAX);

    INSERT INTO DWWANT.TRAS_KA_POS_MATL_W
    SELECT VAR_EDI_NO AS EDI_NO, VAR_DATA_DATE AS DATA_DATE
         , K.KA_SYSTEM_CODE
         , K.KA_STORE_CODE, MAX(K.KA_STORE_NM) AS KA_STORE_NM
         , MIN(K.SALES_COM_ID_SA) AS SALES_COM_ID_SA
         , MIN(K.SALES_COM_ID_WH) AS SALES_COM_ID_WH
         , MIN(K.SALES_COM_ID_DE) AS SALES_COM_ID_DE
         , K.PROD_MATL_ID
         , K.POS_WEEK_NUM
         , MIN(K.POS_WEEK_FIRST_DATE) AS POS_WEEK_FIRST_DATE
         , MAX(K.POS_WEEK_LAST_DATE) AS POS_WEEK_LAST_DATE
         , SUM(K.POS_QTY_PCS) AS POS_QTY_PCS
         , SUM(K.POS_QTY_PKG) AS POS_QTY_PKG
         , SUM(K.POS_AMT) AS POS_AMT
    FROM (SELECT EDI_NO, DATA_DATE
               , KA_SYSTEM_CODE
               , KA_STORE_CODE, KA_STORE_NM
               , SALES_COM_ID_SA, SALES_COM_ID_WH, SALES_COM_ID_DE
               , PROD_MATL_ID
               , DWWANT.FN_GET_WEEK_NUM(POS_DATE) AS POS_WEEK_NUM
               , DWWANT.FN_GET_WEEK_FIRST_DATE(POS_DATE) AS POS_WEEK_FIRST_DATE
               , DWWANT.FN_GET_WEEK_LAST_DATE(POS_DATE) AS POS_WEEK_LAST_DATE
               , IFNULL(POS_QTY_PCS, 0) AS POS_QTY_PCS
               , IFNULL(POS_QTY_PKG, 0) AS POS_QTY_PKG
               , IFNULL(POS_AMT, 0) AS POS_AMT
          FROM DWWANT.TRAS_KA_POS
          WHERE POS_DATE>=VAR_WEEK_FIRST_DATE AND POS_DATE<=VAR_WEEK_LAST_DATE
            AND POS_STATUS='0' AND POS_TYPE='S' AND POS_SETTLE_TYPE='D'
            AND (IFNULL(POS_QTY_PCS, 0)<>0 OR IFNULL(POS_AMT, 0)<>0)) K
    GROUP BY K.KA_SYSTEM_CODE, K.KA_STORE_CODE, K.PROD_MATL_ID, K.POS_WEEK_NUM
    ;

    SET VAR_SP_RESULT='Y';
    COMMIT;
END
;