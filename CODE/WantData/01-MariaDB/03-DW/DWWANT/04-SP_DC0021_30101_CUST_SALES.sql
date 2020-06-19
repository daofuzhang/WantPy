DROP PROCEDURE IF EXISTS DWWANT.SP_DC0021_30101_CUST_SALES;

CREATE PROCEDURE DWWANT.SP_DC0021_30101_CUST_SALES (
    VAR_EDI_NO CHAR(12), VAR_DATA_DATE CHAR(8), OUT VAR_SP_RESULT CHAR(1)
)
BEGIN
    DECLARE VAR_RPT_YM CHAR(6);
    DECLARE VAR_RPT_YM_LAST CHAR(6);
    DECLARE VAR_WORKDAYS INT;
    DECLARE VAR_WORKDAY_TOTAL INT;

    SET VAR_RPT_YM = SUBSTR(VAR_DATA_DATE, 1, 6);
    SET VAR_RPT_YM_LAST = SUBSTR(DWWANT.FN_GET_DATE(DATE_ADD(CONVERT(VAR_DATA_DATE, DATE), INTERVAL -1 YEAR)), 1, 6);

    SET VAR_WORKDAYS = 0;
    SET VAR_WORKDAY_TOTAL = 1;

    SELECT WORKDAYS, WORKDAY_TOTAL INTO VAR_WORKDAYS, VAR_WORKDAY_TOTAL
    FROM DWWANT.CM_WORKDAY
    WHERE WORKDAY_YMD=VAR_DATA_DATE
    ;

    INSERT INTO DMMDL.DC0021_CUST_SALES
    SELECT VAR_EDI_NO AS EDI_NO, VAR_DATA_DATE AS DATA_DATE
         , VAR_RPT_YM AS RPT_YM
         , A.WANT_CHAN_ID, W.WANT_CHAN_NM
         , A.WANT_COM_ID, C.WANT_COM_NM
         , IFNULL(A.PROD_H1_ID, 'NULL') AS PROD_H1_ID, H1.PROD_H_NM AS PROD_H1_NM
         , IFNULL(A.PROD_H2_ID, 'NULL') AS PROD_H2_ID, H2.PROD_H_NM AS PROD_H2_NM
         , IFNULL(A.PROD_H3_ID, 'NULL') AS PROD_H3_ID, H3.PROD_H_NM AS PROD_H3_NM
         , A.POSTED_AMT_LAST_ALL
         , A.POSTED_AMT_LAST_ALL*VAR_WORKDAYS/VAR_WORKDAY_TOTAL AS POSTED_AMT_LAST
         , A.POSTED_AMT_THIS
         , A.POSTING_AMT
         , NULL AS BU01_ID, NULL AS BU01_NM
    FROM (SELECT S.WANT_CHAN_ID, S.WANT_COM_ID, P.PROD_H1_ID, P.PROD_H2_ID, P.PROD_H3_ID
               , SUM(CASE WHEN S.POSTED_YM=VAR_RPT_YM_LAST THEN S.POSTED_AMT ELSE 0 END) AS POSTED_AMT_LAST_ALL
               , SUM(CASE WHEN S.POSTED_YM=VAR_RPT_YM THEN S.POSTED_AMT ELSE 0 END) AS POSTED_AMT_THIS
               , SUM(CASE WHEN S.POSTED_YM=VAR_RPT_YM THEN S.POSTING_AMT ELSE 0 END) AS POSTING_AMT
          FROM DWWANT.TRAS_CUST_SALES S
          LEFT JOIN DWWANT.PROD_MATL P ON S.PROD_MATL_ID=P.PROD_MATL_ID
          WHERE S.POSTED_YM IN (VAR_RPT_YM_LAST, VAR_RPT_YM)
          GROUP BY S.WANT_CHAN_ID, S.WANT_COM_ID, P.PROD_H1_ID, P.PROD_H2_ID, P.PROD_H3_ID) A
    LEFT JOIN DWWANT.ORG_WANT_CHAN W ON A.WANT_CHAN_ID=W.WANT_CHAN_ID
    LEFT JOIN DWWANT.ORG_WANT_COM C ON A.WANT_COM_ID=C.WANT_COM_ID
    LEFT JOIN DWWANT.PROD_HIER H1 ON A.PROD_H1_ID=H1.PROD_H_ID
    LEFT JOIN DWWANT.PROD_HIER H2 ON A.PROD_H2_ID=H2.PROD_H_ID
    LEFT JOIN DWWANT.PROD_HIER H3 ON A.PROD_H3_ID=H3.PROD_H_ID
    WHERE A.POSTED_AMT_LAST_ALL<>0 OR A.POSTED_AMT_THIS<>0 OR A.POSTING_AMT<>0
    ;

    UPDATE DMMDL.DC0021_CUST_SALES SET
        BU01_ID=(CASE WHEN WANT_CHAN_ID IN ('WW0052','WW0053','WW0047') AND PROD_H2_ID<>'D11M01' AND WANT_COM_ID IN ('W10','W12','W31','W32','WX5','WX6','WXI') THEN 'BU01'
                      WHEN WANT_CHAN_ID IN ('WW0052','WW0053','WW0047') AND PROD_H2_ID<>'D11M01' AND WANT_COM_ID IN ('W11','W13','W14','W46','WX1','WXC') THEN 'BU02'
                      WHEN WANT_CHAN_ID IN ('WW0052','WW0053','WW0047') AND PROD_H2_ID<>'D11M01' AND WANT_COM_ID IN ('W27','W28','W29','W77','WXD','WXE','WXG') THEN 'BU03'
                      WHEN WANT_CHAN_ID IN ('WW0052','WW0053','WW0047') AND PROD_H2_ID<>'D11M01' AND WANT_COM_ID IN ('W34','W55','WX2','WXF') THEN 'BU04'
                      WHEN WANT_CHAN_ID IN ('WW0052','WW0053','WW0047') AND PROD_H2_ID<>'D11M01' AND WANT_COM_ID IN ('W18','W49','W50','W75','WX8','WX9','WXA','WXB') THEN 'BU05'
                      WHEN WANT_CHAN_ID IN ('WW0052','WW0053','WW0047') AND PROD_H2_ID<>'D11M01' AND WANT_COM_ID IN ('W19','W20','W21','W22','W23','W24','W76','WX3') THEN 'BU06'
                      WHEN WANT_CHAN_ID IN ('WW0052','WW0053','WW0047') AND PROD_H2_ID<>'D11M01' AND WANT_COM_ID IN ('W35','W36','W37','W38','WX4','WXH') THEN 'BU07'
                      WHEN WANT_CHAN_ID IN ('WW0052','WW0053','WW0047') AND PROD_H2_ID<>'D11M01' AND WANT_COM_ID IN ('W25','W39','W40','W44','W78','WX7') THEN 'BU08'
                      WHEN WANT_CHAN_ID='WW0048' AND PROD_H2_ID<>'D11M01' THEN 'BU09'
                      WHEN WANT_CHAN_ID='WW0021' AND PROD_H2_ID<>'D11M01' THEN 'BU10'
                      WHEN WANT_CHAN_ID='WW0016' AND PROD_H2_ID<>'D11M01' THEN 'BU11'
                      WHEN WANT_CHAN_ID='WW0030' AND PROD_H2_ID<>'D11M01' THEN 'BU12'
                      WHEN WANT_CHAN_ID='WW0024' AND PROD_H2_ID<>'D11M01' THEN 'BU13'
                      WHEN WANT_CHAN_ID NOT IN ('WW0001','WW0002','WW0026','WW0049') AND PROD_H2_ID='D11M01' THEN 'BU14'
                      WHEN WANT_CHAN_ID='WW0050' AND PROD_H2_ID<>'D11M01' THEN 'BU15'
                      WHEN WANT_CHAN_ID='WW0043' AND PROD_H2_ID<>'D11M01' THEN 'BU16'
                      WHEN WANT_CHAN_ID='WW0054' AND PROD_H2_ID<>'D11M01' THEN 'BU17'
                      WHEN WANT_CHAN_ID='WW0041' AND PROD_H2_ID<>'D11M01' THEN 'BU18'
                      WHEN WANT_CHAN_ID='WW0044' AND PROD_H2_ID<>'D11M01' THEN 'BU19'
                      WHEN WANT_CHAN_ID IN ('WW0001','WW0002') THEN 'BU20'
                      WHEN WANT_CHAN_ID IN ('WW0026','WW0049') THEN 'BU21'
                      WHEN WANT_CHAN_ID='WW9999' THEN 'BU99'
                      ELSE 'NULL'
                 END)
    WHERE DATA_DATE=VAR_DATA_DATE
    ;
    
    UPDATE DMMDL.DC0021_CUST_SALES SET
        BU01_NM=DMMDL.FN_GET_CM_CODE_NM('0001', BU01_ID)
    WHERE DATA_DATE=VAR_DATA_DATE
    ;

    SET VAR_SP_RESULT='Y';
    COMMIT;
END
;