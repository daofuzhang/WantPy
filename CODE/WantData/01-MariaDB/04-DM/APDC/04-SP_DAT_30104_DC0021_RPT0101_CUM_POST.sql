DROP PROCEDURE IF EXISTS APDC.SP_DAT_30104_DC0021_RPT0101_CUM_POST;

CREATE PROCEDURE APDC.SP_DAT_30104_DC0021_RPT0101_DIVISIONC (
    VAR_EDI_DATE CHAR(8), VAR_EDI_TIME CHAR(9), VAR_DATA_DATE CHAR(8)
  , OUT VAR_SP_RESULT CHAR(1)
)
BEGIN
    
    SET @DIVISION_ID_MILK='乳飲' COLLATE utf8_unicode_ci;
    SET @DIVISION_ID_LEIS='休閒' COLLATE utf8_unicode_ci;
    SET @DIVISION_ID_BEV1S='飲一南' COLLATE utf8_unicode_ci;
    SET @DIVISION_ID_BEV1N='飲一北' COLLATE utf8_unicode_ci;
    SET @DIVISION_ID_WL='旺禮' COLLATE utf8_unicode_ci;

    --DC0021_SALES_DIST_PROD_DATE_CUM-日業績金額-累積
    --INSERT1
    INSERT INTO APDC.DC0021_RPT0101_CUM_POST A
    SELECT VAR_DATA_DATE AS DATA_DATE
         , VAR_DATA_DATE AS RPT_YMD
         , DISTRICT15_ID AS ITEM_ID
         , 'DISTRICT15_NM' AS ITEM_NM
         , SUM(SALES_AMT) AS CUM_SALES_AMT_POST
    FROM DMMDL.DC0021_SALES_DIST_PROD_DATE_CUM
    WHERE DATA_DATE=VAR_DATA_DATE AND RPT_YMD=VAR_DATA_DATE AND DIVISION_ID IN (@DIVISION_ID_MILK, @DIVISION_ID_LEIS)
    GROUP BY DISTRICT15_ID
    ;

    --INSERT2
    INSERT INTO APDC.DC0021_RPT0101_CUM_POST A
    SELECT VAR_DATA_DATE AS DATA_DATE
         , VAR_DATA_DATE AS RPT_YMD
         , DIVISIOND_ID AS ITEM_ID
         , 'DIVISIOND_NM'AS ITEM_NM
         , SUM(SALES_AMT) AS CUM_SALES_AMT_POST
    FROM DMMDL.DC0021_SALES_DIST_PROD_DATE_CUM
    WHERE DATA_DATE=VAR_DATA_DATE AND RPT_YMD=VAR_DATA_DATE AND DIVISION_ID IN (@DIVISION_ID_BEV1S, @DIVISION_ID_BEV1N, @DIVISION_ID_WL)
    GROUP BY DIVISIOND_ID
    ;

    --INSERT3
    INSERT INTO APDC.DC0021_RPT0101_CUM_POST A
    SELECT VAR_DATA_DATE AS DATA_DATE
         , VAR_DATA_DATE AS RPT_YMD
         , DIVISION_ID AS ITEM_ID
         , 'DIVISION_NM' AS ITEM_NM
         , SUM(SALES_AMT) AS CUM_SALES_AMT_POST
    FROM DMMDL.DC0021_SALES_DIST_PROD_DATE_CUM
    WHERE DATA_DATE=VAR_DATA_DATE AND RPT_YMD=VAR_DATA_DATE AND DIVISION_ID NOT IN (@DIVISION_ID_MILK, @DIVISION_ID_LEIS, @DIVISION_ID_BEV1S, @DIVISION_ID_BEV1N, @DIVISION_ID_WL)
    GROUP BY DIVISION_ID
    ;


    SET VAR_SP_RESULT= 'Y';
    COMMIT;
END
;