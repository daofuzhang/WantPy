DROP PROCEDURE IF EXISTS APDC.SP_DAT_30108_DC0021_RPT0102_TOTAL;

CREATE PROCEDURE APDC.SP_DAT_30108_DC0021_RPT0102_TOTAL (
    VAR_EDI_DATE CHAR(8), VAR_EDI_TIME CHAR(9), VAR_DATA_DATE CHAR(8)
  , OUT VAR_SP_RESULT CHAR(1)
)
BEGIN
    
    SET @DIVISION_ID_MILK='乳飲' COLLATE utf8_unicode_ci;
    SET @DIVISION_ID_LEIS='休閒' COLLATE utf8_unicode_ci;
    SET @DIVISION_ID_BEV1N='飲一北' COLLATE utf8_unicode_ci;
    SET @DIVISION_ID_BEV1S='飲一南' COLLATE utf8_unicode_ci;
    SET @DIVISION_ID_BEV2='飲二' COLLATE utf8_unicode_ci;
    SET @DIVISION_ID_ICE='冰品' COLLATE utf8_unicode_ci;
    SET @DIVISION_ID_MAT='母嬰' COLLATE utf8_unicode_ci;
    SET @DIVISION_ID_CDCN='冷鏈' COLLATE utf8_unicode_ci;
    SET @DIVISION_ID_BULK='開心散裝' COLLATE utf8_unicode_ci;
    SET @DIVISIOND_ID_WL='旺禮個體' COLLATE utf8_unicode_ci;
    SET @DIVISIOND_ID_WLALL='旺禮禮包' COLLATE utf8_unicode_ci;
    SET @DIVISION_ID_KA='現渠' COLLATE utf8_unicode_ci;
    SET @DIVISION_ID_EC='電子商務' COLLATE utf8_unicode_ci;

    --INSERT1
    --SALES_AMT_REACH_D1 達成截至D1
    --SALES_AMT_PAST_MONTH全月同期
    --PAST_PROG_REACH_RATE 全月同期達成率
    --SALES_AMT_REACH_D1_V 達成截至D1(畫面數值)
    --SALES_AMT_PAST_MONTH_V 全月同期(畫面數值)
    --SALES_PAST_REACH_RATE 各事業部同期達成率
    INSERT INTO APDC.DC0021_RPT0102_TOTAL
    SELECT VAR_DATA_DATE AS DATA_DATE 
         , VAR_DATA_DATE AS RPT_YMD
         , 0 AS WORK_DAY
         , 0 AS WORK_TOTAL_DAY
         , 0 AS WORK_RATIO
         , 0 AS MKT_SHARE
         , 0 AS POPU
         , 0 AS POPU_V
         , SUM(BILLING) AS SALES_AMT_REACH_D1
         , ROUND(SUM(BILLING)/1000,0) AS SALES_AMT_REACH_D1_V
         , SUM(SALES_AMT_PAST_MONTH) AS SALES_AMT_PAST_MONTH
         , ROUND(SUM(SALES_AMT_PAST_MONTH)/1000,0) AS SALES_AMT_PAST_MONTH_V
         , ROUND(SUM(BILLING)/SUM(SALES_AMT_PAST_MONTH),3) AS PAST_PROG_REACH_RATE
         , 0 AS FCST_AMT
         , 0 AS FCST_AMT_V
         , 0 AS FCST_REACH_RATE
         , 0 AS MKT_SHARE_REACH_RATE
         , (CASE WHEN DIVISION_ID IN (@DIVISION_ID_MILK, @DIVISION_ID_LEIS) THEN ROUND(SUM(BILLING)/SUM(SALES_AMT_PAST_MONTH),3) ELSE 0 END) AS SALES_PAST_REACH_RATE_MKLS
         , (CASE WHEN DIVISION_ID=@DIVISION_ID_BEV1S THEN ROUND(SUM(BILLING)/SUM(SALES_AMT_PAST_MONTH),3) ELSE 0 END) AS SALES_PAST_REACH_RATE_BEV1S
         , (CASE WHEN DIVISION_ID=@DIVISION_ID_BEV1N THEN ROUND(SUM(BILLING)/SUM(SALES_AMT_PAST_MONTH),3) ELSE 0 END) AS SALES_PAST_REACH_RATE_BEV1N
         , (CASE WHEN DIVISION_ID=@DIVISION_ID_BEV2 THEN SUM(SALES_AMT_PAST_MONTH) ELSE 0 END) AS SALES_AMT_PAST_MONTH_BEV2
         , (CASE WHEN DIVISION_ID=@DIVISION_ID_BEV2 THEN ROUND(SUM(BILLING)/SUM(SALES_AMT_PAST_MONTH),3) ELSE 0 END) AS SALES_PAST_REACH_RATE_BEV2
         , NULL AS SALES_PAST_REACH_RATE_BEV2_F
         , (CASE WHEN DIVISION_ID=@DIVISION_ID_ICE THEN ROUND(SUM(BILLING)/SUM(SALES_AMT_PAST_MONTH),3) ELSE 0 END) AS SALES_PAST_REACH_RATE_ICE
         , (CASE WHEN DIVISION_ID=@DIVISION_ID_BULK THEN ROUND(SUM(BILLING)/SUM(SALES_AMT_PAST_MONTH),3) ELSE 0 END) AS SALES_PAST_REACH_RATE_BULK
         , (CASE WHEN DIVISION_ID=@DIVISION_ID_MAT THEN ROUND(SUM(BILLING)/SUM(SALES_AMT_PAST_MONTH),3) ELSE 0 END) AS SALES_PAST_REACH_RATE_MAT
         , (CASE WHEN DIVISION_ID=@DIVISION_ID_CDCN THEN ROUND(SUM(BILLING)/SUM(SALES_AMT_PAST_MONTH),3) ELSE 0 END) AS SALES_PAST_REACH_RATE_CDCN
         , (CASE WHEN DIVISION_ID=@DIVISIOND_ID_WLALL THEN ROUND(SUM(BILLING)/SUM(SALES_AMT_PAST_MONTH),3) ELSE 0 END) AS SALES_PAST_REACH_RATE_WLALL
         , (CASE WHEN DIVISION_ID=@DIVISIOND_ID_WL THEN ROUND(SUM(BILLING)/SUM(SALES_AMT_PAST_MONTH),3) ELSE 0 END) AS SALES_PAST_REACH_RATE_WL
         , (CASE WHEN DIVISION_ID=@DIVISION_ID_KA THEN ROUND(SUM(BILLING)/SUM(SALES_AMT_PAST_MONTH),3) ELSE 0 END) AS SALES_PAST_REACH_RATE_KA
         , (CASE WHEN DIVISION_ID=@DIVISION_ID_EC THEN ROUND(SUM(BILLING)/SUM(SALES_AMT_PAST_MONTH),3) ELSE 0 END) AS SALES_PAST_REACH_RATE_EC
    FROM DMMDL.DC0021_SALES_DIST_PROD_DATE_CUM
    WHERE DATA_DATE=VAR_DATA_DATE AND RPT_YMD=VAR_DATA_DATE
    ;

    --UPDATE2
    --WORK_RATIO 標準進度
    UPDATE APDC.DC0021_RPT0102_TOTAL A
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
    --MKT_SHARE 應有市場占比
    --MKT_SHARE_REACH_RATE 應有市場達成率
    UPDATE APDC.DC0021_RPT0102_TOTAL A
    JOIN(SELECT ROUND(DIVISION_MKT_SHARE,5) AS MKT_SHARE
              , ROUND(MKT_SHARE_REACH_RATE,3) AS MKT_SHARE_REACH_RATE
         FROM DMMDL.DC0021_MKT_SHARE_REACH_RATE_DIVISION_CUM
         WHERE DATA_DATE=VAR_DATA_DATE AND RPT_YMD=VAR_DATA_DATE) B
    ON A.DATA_DATE=B.DATA_DATE AND A.RPT_YMD=B.RPT_YMD
    SET A.MKT_SHARE=B.MKT_SHARE
      , A.MKT_SHARE_REACH_RATE=B.MKT_SHARE_REACH_RATE
    WHERE A.DATA_DATE=VAR_DATA_DATE AND A.RPT_YMD=VAR_DATA_DATE
    ;

    --UPDATE4
    --人口數(萬)
    UPDATE APDC.DC0021_RPT0102_TOTAL A
    JOIN(SELECT SUM(POPU) AS POPU
              , ROUND(SUM(POPU)/10000,0) AS POPU_V
         FROM DMMDL.DC0021_POPU_COM
         WHERE DATA_DATE=VAR_DATA_DATE AND RPT_YMD=VAR_DATA_DATE) B
    ON A.DATA_DATE=B.DATA_DATE AND A.RPT_YMD=B.RPT_YMD
    SET A.POPU=B.POPU
      , A.POPU_V=B.POPU_V
    WHERE A.DATA_DATE=VAR_DATA_DATE AND A.RPT_YMD=VAR_DATA_DATE
    ;
    
    --UPDATE5
    --FCST_AMT 全月預估
    --FCST_AMT_V 全月預估(畫面數值)
    UPDATE APDC.DC0021_RPT0102_TOTAL A
    JOIN(SELECT SUM(FCST_AMT) AS FCST_AMT
              , ROUND(SUM(FCST_AMT)/1000,0) AS FCST_AMT_V
         FROM DMMDL.DC0021_FCST_AMT_CUM
         WHERE DATA_DATE=VAR_DATA_DATE AND RPT_YMD=VAR_DATA_DATE) B
    ON A.DATA_DATE=B.DATA_DATE AND A.RPT_YMD=B.RPT_YMD
    SET A.FCST_AMT=B.FCST_AMT
      , A.FCST_AMT_V=B.FCST_AMT_V
    WHERE A.DATA_DATE=VAR_DATA_DATE AND A.RPT_YMD=VAR_DATA_DATE
    ;

    --UPDATE6
    --FCST_REACH_RATE 預估達成率
    UPDATE APDC.DC0021_RPT0102_TOTAL A
    JOIN(SELECT (CASE WHEN SALES_AMT_PAST_MONTH_BEV2<0 THEN 'A' ELSE NULL END) AS SALES_PAST_REACH_RATE_BEV2_F
              , ROUND(SALES_AMT_REACH_D1/FCST_AMT,3) AS FCST_REACH_RATE
         FROM APDC.DC0021_RPT0102_TOTAL
         WHERE DATA_DATE=VAR_DATA_DATE AND RPT_YMD=VAR_DATA_DATE) B
    ON A.DATA_DATE=B.DATA_DATE AND A.RPT_YMD=B.RPT_YMD
    SET A.SALES_PAST_REACH_RATE_BEV2_F=B.SALES_PAST_REACH_RATE_BEV2_F
      , A.FCST_REACH_RATE=B.FCST_REACH_RATE
    WHERE A.DATA_DATE=VAR_DATA_DATE AND A.RPT_YMD=VAR_DATA_DATE
    ;
   
       
    
    SET VAR_SP_RESULT='Y';
    COMMIT;
END
;