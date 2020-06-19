DROP PROCEDURE IF EXISTS APDC.SP_DAT_30111_DC0021_RPT0103_DIVISIONC;

CREATE PROCEDURE APDC.SP_DAT_30111_DC0021_RPT0103_DIVISIONC (
    VAR_EDI_DATE CHAR(8), VAR_EDI_TIME CHAR(9), VAR_DATA_DATE CHAR(8)
  , OUT VAR_SP_RESULT CHAR(1)
)
BEGIN   

    SET @FY1_04=APDC.FN_GET_FY_YM(VAR_DATA_DATE, 1) COLLATE utf8_unicode_ci;
    SET @FY1_05=APDC.FN_GET_FY_YM(VAR_DATA_DATE, 2) COLLATE utf8_unicode_ci;
    SET @FY1_06=APDC.FN_GET_FY_YM(VAR_DATA_DATE, 3) COLLATE utf8_unicode_ci;
    SET @FY1_07=APDC.FN_GET_FY_YM(VAR_DATA_DATE, 4) COLLATE utf8_unicode_ci;
    SET @FY1_08=APDC.FN_GET_FY_YM(VAR_DATA_DATE, 5) COLLATE utf8_unicode_ci;
    SET @FY1_09=APDC.FN_GET_FY_YM(VAR_DATA_DATE, 6) COLLATE utf8_unicode_ci;
    SET @FY1_10=APDC.FN_GET_FY_YM(VAR_DATA_DATE, 7) COLLATE utf8_unicode_ci;
    SET @FY1_11=APDC.FN_GET_FY_YM(VAR_DATA_DATE, 8) COLLATE utf8_unicode_ci;
    SET @FY1_12=APDC.FN_GET_FY_YM(VAR_DATA_DATE, 9) COLLATE utf8_unicode_ci;
    SET @FY_01=APDC.FN_GET_FY_YM(VAR_DATA_DATE, 10) COLLATE utf8_unicode_ci;
    SET @FY_02=APDC.FN_GET_FY_YM(VAR_DATA_DATE, 11) COLLATE utf8_unicode_ci;
    SET @FY_03=APDC.FN_GET_FY_YM(VAR_DATA_DATE, 12) COLLATE utf8_unicode_ci;
    SET @DIVISION_ID_MILK='乳飲ID' COLLATE utf8_unicode_ci;
    SET @DIVISION_ID_LEIS='休閒ID' COLLATE utf8_unicode_ci;
    SET @DIVISIOND_ID_ONE='一中心ID' COLLATE utf8_unicode_ci;
    SET @DIVISIOND_ID_TWO='二中心ID' COLLATE utf8_unicode_ci;

    --INSERT1
    INSERT INTO APDC.DC0021_RPT0103_DIVISIONC
    SELECT VAR_DATA_DATE AS DATA_DATE 
         , VAR_DATA_DATE AS RPT_YMD
         , 0 AS WORK_DAY
         , 0 AS WORK_TOTAL_DAY
         , 0 AS WORK_RATIO
         , '乳飲休閒ID' AS DIVISIONC_ID
         , '乳飲休閒NM' AS DIVISIONC_NM
         , SUM(CASE WHEN @FY1_04=SUBSTRING(RPT_YMD,1 ,6) THEN SALES_AMT ELSE 0 END) AS FY1_SALES_AMT01
         , SUM(CASE WHEN @FY1_05=SUBSTRING(RPT_YMD,1 ,6) THEN SALES_AMT ELSE 0 END) AS FY1_SALES_AMT02
         , SUM(CASE WHEN @FY1_06=SUBSTRING(RPT_YMD,1 ,6) THEN SALES_AMT ELSE 0 END) AS FY1_SALES_AMT03
         , SUM(CASE WHEN @FY1_07=SUBSTRING(RPT_YMD,1 ,6) THEN SALES_AMT ELSE 0 END) AS FY1_SALES_AMT04
         , SUM(CASE WHEN @FY1_08=SUBSTRING(RPT_YMD,1 ,6) THEN SALES_AMT ELSE 0 END) AS FY1_SALES_AMT05
         , SUM(CASE WHEN @FY1_09=SUBSTRING(RPT_YMD,1 ,6) THEN SALES_AMT ELSE 0 END) AS FY1_SALES_AMT06
         , SUM(CASE WHEN @FY1_10=SUBSTRING(RPT_YMD,1 ,6) THEN SALES_AMT ELSE 0 END) AS FY1_SALES_AMT07
         , SUM(CASE WHEN @FY1_11=SUBSTRING(RPT_YMD,1 ,6) THEN SALES_AMT ELSE 0 END) AS FY1_SALES_AMT08
         , SUM(CASE WHEN @FY1_12=SUBSTRING(RPT_YMD,1 ,6) THEN SALES_AMT ELSE 0 END) AS FY1_SALES_AMT09
         , SUM(CASE WHEN (@FY_01, @FY_02) IN SUBSTRING(RPT_YMD,1 ,6) THEN SALES_AMT ELSE 0 END) AS FY_SALES_AMT1011
         , SUM(CASE WHEN @FY_03=SUBSTRING(RPT_YMD,1 ,6) THEN SALES_AMT ELSE 0 END) AS FY_SALES_AMT12
         , 0 AS MKT_SHARE
         , SUM(SALES_AMT_PAST_MONTH) AS SALES_AMT_PAST_MONTH_MKLS
         , ROUND(SUM(SALES_AMT_PAST_MONTH)/1000,0) AS SALES_AMT_PAST_MONTH_MKLS_V
         , SUM(BILLING) AS SALES_AMT_REACH_MKLS
         , ROUND(SUM(BILLING)/1000,0) AS SALES_AMT_REACH_MKLS_V
         , 0 AS SALES_PAST_REACH_RATE_MKLS
         , 0 AS SALES_PAST_REACH_RATE_MKLS_V
         , NULL AS SALES_PAST_REACH_RATE_MKLS_F
         , 0 AS MKT_SHARE_REACH_RATE
    FROM DMMDL.DC0021_SALES_DIST_PROD_DATE_CUM
    WHERE DATA_DATE=VAR_DATA_DATE AND RPT_YMD=VAR_DATA_DATE AND DIVISION_ID IN (@DIVISION_ID_MILK, @DIVISION_ID_LEIS)
    ;

    --UPDATE2
    --標準進度
    UPDATE APDC.DC0021_RPT0103_DIVISIONC A
    JOIN(SELECT WORK_DAY
              , WORK_TOTAL_DAY
              , ROUND(WORK_RATIO,3) AS WORK_RATIO
         FROM DMMDL.DC0021_WORK_RATIO_CUM
         WHERE DATA_DATE=VAR_DATA_DATE AND RPT_YMD=VAR_DATA_DATE) B
    ON A.DATA_DATE=B.DATA_DATE AND A.RPT_YMD=B.RPT_YMD
    SET A.WORK_DAY=B.WORK_DAY
      , A.WORK_TOTAL_DAY=B.WORK_TOTAL_DAY
      , A.WORK_RATIO=B.WORK_RATIO
    WHERE A.DATA_DATE=VAR_DATA_DATE AND A.RPT_YMD=VAR_DATA_DATE
    ;

    --UPDATE3
    --應有市場占比應有市場達成率
    UPDATE APDC.DC0021_RPT0103_DIVISIONC A
    JOIN(SELECT ROUND(DIVISION_MKT_SHARE,5) AS MKT_SHARE
              , ROUND(MKT_SHARE_REACH_RATE_MKLS,3) AS MKT_SHARE_REACH_RATE
          FROM DMMDL.DC0021_MKT_SHARE_REACH_RATE_DIVISIOND_CUM
          WHERE DATA_DATE=VAR_DATA_DATE AND RPT_YMD=VAR_DATA_DATE AND DIVISIOND_ID IN (@DIVISIOND_ID_ONE, @DIVISIOND_ID_TWO))B
    ON A.DATA_DATE=B.DATA_DATE AND A.RPT_YMD=B.RPT_YMD
    SET A.MKT_SHARE=B.MKT_SHARE
      , A.MKT_SHARE_REACH_RATE=B.MKT_SHARE_REACH_RATE
    WHERE A.DATA_DATE=VAR_DATA_DATE AND A.RPT_YMD=VAR_DATA_DATE
    ;
    
    --UPDATE4
    --SALES_PAST_REACH_RATE_MKLS 乳飲休閒事業部同期達成率
    UPDATE APDC.DC0021_RPT0103_DIVISIONC A
    JOIN(SELECT DIVISIONC_ID
              , ROUND(SALES_AMT_REACH_MKLS/SALES_AMT_PAST_MONTH_MKLS,3) AS SALES_PAST_REACH_RATE_MKLS
              , (CASE WHEN ROUND(SALES_AMT_REACH_MKLS/SALES_AMT_PAST_MONTH_MKLS,3)<0 THEN 0.00 ELSE ROUND(SALES_AMT_REACH_MKLS/SALES_AMT_PAST_MONTH_MKLS,3) END) AS SALES_PAST_REACH_RATE_MKLS_V
              , (CASE WHEN ROUND(SALES_AMT_REACH_MKLS/SALES_AMT_PAST_MONTH_MKLS,3)<WORK_RATIO THEN 'A'
                      WHEN SALES_AMT_PAST_MONTH_MKLS<=0 THEN 'B' ELSE NULL END) AS SALES_PAST_REACH_RATE_MKLS_F
         FROM APDC.DC0021_RPT0103_DIVISIONC
         WHERE DATA_DATE=VAR_DATA_DATE AND RPT_YMD=VAR_DATA_DATE
         GROUP BY DIVISIONC_ID) B
    ON A.DATA_DATE=B.DATA_DATE AND A.RPT_YMD=B.RPT_YMD AND A.DIVISIONC_ID=B.DIVISIONC_ID
    SET A.SALES_PAST_REACH_RATE_MKLS=B.SALES_PAST_REACH_RATE_MKLS
        A.SALES_PAST_REACH_RATE_MKLS_V=B.SALES_PAST_REACH_RATE_MKLS_V
        A.SALES_PAST_REACH_RATE_MKLS_F=B.SALES_PAST_REACH_RATE_MKLS_F
    WHERE A.DATA_DATE=VAR_DATA_DATE AND A.RPT_YMD=VAR_DATA_DATE
    ;




   

    SET VAR_SP_RESULT='Y';
    COMMIT;
END
;