SET @DATA_DATE_KA='20190123' COLLATE utf8_unicode_ci;  /*現渠戰報資料日期*/

USE APDC;

----資料核對----
SELECT COUNT(1)
FROM APDC.MAN_KA_POS
WHERE DATA_DATE=@DATA_DATE_KA
;

----數值核對----
--TRG_AMT_MONTH:115472504.258004
SELECT SUM(TRG_AMT_MONTH)
FROM APDC.MAN_KA_POS
WHERE DATA_DATE=@DATA_DATE_KA
;

--POS_AMT_PAST_MONTH:96294495.133901
SELECT SUM(POS_AMT_PAST_MONTH)
FROM APDC.MAN_KA_POS
WHERE DATA_DATE=@DATA_DATE_KA
;

--POS_AMT_MONTH:101800479.117189
SELECT SUM(POS_AMT_MONTH)
FROM APDC.MAN_KA_POS
WHERE DATA_DATE=@DATA_DATE_KA
;

--SG_COUNT:2162
SELECT SUM(SG_COUNT)
FROM APDC.MAN_KA_POS
WHERE DATA_DATE=@DATA_DATE_KA
;

--TRG_REACH_RATE:14874.308736
SELECT SUM(TRG_REACH_RATE)
FROM APDC.MAN_KA_POS
WHERE DATA_DATE=@DATA_DATE_KA
;

--PAST_MONTH_GROWTH_RATE:15443.614033
SELECT SUM(PAST_MONTH_GROWTH_RATE)
FROM APDC.MAN_KA_POS
WHERE DATA_DATE=@DATA_DATE_KA
;

----分類、文字欄位 使用
----1.TRIM確認有沒有空白
----2.GROUP BY & ORDER BY 檢視一下有沒有名稱很接近的
----3.GROUP BY & COUNT(1)確認是否與原始資料相同

--KA_RGN_COORD

SELECT *
FROM APDC.MAN_KA_POS
WHERE TRIM(KA_RGN_COORD)<>KA_RGN_COORD 
;

SELECT KA_RGN_COORD, COUNT(1)
FROM APDC.MAN_KA_POS
WHERE DATA_DATE=@DATA_DATE_KA
GROUP BY KA_RGN_COORD
ORDER BY KA_RGN_COORD
;

--KA_COM_NM
SELECT *
FROM APDC.MAN_KA_POS
WHERE TRIM(KA_COM_NM)<>KA_COM_NM
;

SELECT KA_COM_NM ,COUNT(1)
FROM APDC.MAN_KA_POS
WHERE DATA_DATE=@DATA_DATE_KA
GROUP BY KA_COM_NM
ORDER BY KA_COM_NM
;

--KA_CHANNEL_NM
SELECT *
FROM APDC.MAN_KA_POS
WHERE TRIM(KA_CHANNEL_NM)<>KA_CHANNEL_NM
;

SELECT KA_CHANNEL_NM ,COUNT(1)
FROM APDC.MAN_KA_POS
WHERE DATA_DATE=@DATA_DATE_KA
GROUP BY KA_CHANNEL_NM
ORDER BY KA_CHANNEL_NM
;

--KA_SYS_NM
SELECT *
FROM APDC.MAN_KA_POS
WHERE TRIM(KA_SYS_NM)<>KA_SYS_NM
;

SELECT KA_SYS_NM ,COUNT(1)
FROM APDC.MAN_KA_POS
WHERE DATA_DATE=@DATA_DATE_KA
GROUP BY KA_SYS_NM
;

--KA_RC_ID
SELECT *
FROM APDC.MAN_KA_POS
WHERE TRIM(KA_RC_ID)<>KA_RC_ID
;

SELECT KA_RC_ID, COUNT(1) AS CN
FROM APDC.MAN_KA_POS
WHERE DATA_DATE=@DATA_DATE_KA
GROUP BY KA_RC_ID
;

SELECT *
FROM (SELECT KA_RC_ID, COUNT(1) AS CN
      FROM APDC.MAN_KA_POS
      WHERE DATA_DATE=@DATA_DATE_KA
      GROUP BY KA_RC_ID) A
WHERE CN>1
;

--STORE_NM
SELECT *
FROM APDC.MAN_KA_POS
WHERE TRIM(STORE_NM)<>STORE_NM
;

SELECT *
FROM (SELECT STORE_NM ,COUNT(1) AS CN
      FROM APDC.MAN_KA_POS
      WHERE DATA_DATE=@DATA_DATE_KA
      GROUP BY STORE_NM) A
WHERE A.CN>1
;

SELECT *
FROM APDC.MAN_KA_POS
WHERE STORE_NM='余姚店'
;

--PSYS_STORE_ID
SELECT *
FROM APDC.MAN_KA_POS
WHERE TRIM(PSYS_STORE_ID)<>PSYS_STORE_ID
;

SELECT *
FROM (SELECT PSYS_STORE_ID ,COUNT(1) AS CN
      FROM APDC.MAN_KA_POS
      WHERE DATA_DATE=@DATA_DATE_KA
      GROUP BY PSYS_STORE_ID) A
WHERE A.CN>1
;

--AREA_COORD
SELECT *
FROM APDC.MAN_KA_POS
WHERE TRIM(AREA_COORD)<>AREA_COORD
;

SELECT AREA_COORD, COUNT(1)
FROM APDC.MAN_KA_POS
WHERE DATA_DATE=@DATA_DATE_KA
GROUP BY AREA_COORD
ORDER BY AREA_COORD
;

--AREA_EXEC
SELECT *
FROM APDC.MAN_KA_POS
WHERE TRIM(AREA_EXEC)<>AREA_EXEC
;

SELECT AREA_EXEC, COUNT(1)
FROM APDC.MAN_KA_POS
WHERE DATA_DATE=@DATA_DATE_KA
GROUP BY AREA_EXEC
ORDER BY AREA_EXEC
;

--DECL_TYPE
SELECT *
FROM APDC.MAN_KA_POS
WHERE TRIM(DECL_TYPE)<>DECL_TYPE
;

SELECT DECL_TYPE, COUNT(1)
FROM APDC.MAN_KA_POS
WHERE DATA_DATE=@DATA_DATE_KA
GROUP BY DECL_TYPE
ORDER BY DECL_TYPE
;

SELECT DECL_TYPE ,COUNT(1)
FROM APDC.MAN_KA_POS
WHERE DATA_DATE=@DATA_DATE_KA AND PAST_MONTH_GROWTH_RATE<0
GROUP BY DECL_TYPE
ORDER BY DECL_TYPE
;















--SG_NM處理
--1.檢查欄位（中文字的長度是3）
--2.找出各種可能的分隔情形
--3.依各種分隔情形UPDATE

SELECT *
FROM APDC.MAN_KA_POS
WHERE DATA_DATE=@DATA_DATE_KA AND TRIM(SG_NM)<>SG_NM
;

UPDATE APDC.MAN_KA_POS SET
     SG_NM=TRIM(SG_NM)
WHERE DATA_DATE=@DATA_DATE_KA
;

SELECT SUBSTRING_INDEX(SG_NM,'/',1), SUBSTRING_INDEX(SG_NM,'/',-1), SG_NM
FROM APDC.MAN_KA_POS
WHERE DATA_DATE=@DATA_DATE_KA AND LOCATE('/', SG_NM)>0
;

SELECT SUBSTRING_INDEX(SG_NM,'、',1), SUBSTRING_INDEX(SG_NM,'、',-1), SG_NM
FROM APDC.MAN_KA_POS
WHERE DATA_DATE=@DATA_DATE_KA AND LOCATE('、', SG_NM)>0
;

SELECT SUBSTRING_INDEX(SG_NM,',',1), SUBSTRING_INDEX(SG_NM,',',-1), SG_NM
FROM APDC.MAN_KA_POS
WHERE DATA_DATE=@DATA_DATE_KA AND LOCATE(',', SG_NM)>0
;

SELECT SUBSTRING_INDEX(SG_NM,'／',1), SUBSTRING_INDEX(SG_NM,'／',-1), SG_NM
FROM APDC.MAN_KA_POS
WHERE DATA_DATE=@DATA_DATE_KA AND LOCATE('／', SG_NM)>0
;

--UPDATE ADD_SG1_NM, ADD_SG2_NM
UPDATE APDC.MAN_KA_POS SET
    ADD_SG1_NM=SG_NM 
WHERE DATA_DATE=@DATA_DATE_KA
  AND LOCATE('/', SG_NM)=0 AND LOCATE('、', SG_NM)=0 AND LOCATE(',', SG_NM)=0 AND LOCATE('／', SG_NM)=0
;

UPDATE APDC.MAN_KA_POS SET
    ADD_SG1_NM=SUBSTRING_INDEX(SG_NM,'/',1)
  , ADD_SG2_NM=SUBSTRING_INDEX(SG_NM,'/',-1)
WHERE DATA_DATE=@DATA_DATE_KA AND LOCATE('/', SG_NM)>0
;

UPDATE APDC.MAN_KA_POS SET
    ADD_SG1_NM=SUBSTRING_INDEX(SG_NM,'、',1)
  , ADD_SG2_NM=SUBSTRING_INDEX(SG_NM,'、',-1)
WHERE DATA_DATE=@DATA_DATE_KA AND LOCATE('、', SG_NM)>0
;

UPDATE APDC.MAN_KA_POS SET
    ADD_SG1_NM=SUBSTRING_INDEX(SG_NM,',',1)
  , ADD_SG2_NM=SUBSTRING_INDEX(SG_NM,',',-1)
WHERE DATA_DATE=@DATA_DATE_KA AND LOCATE(',', SG_NM)>0
;

UPDATE APDC.MAN_KA_POS SET
    ADD_SG1_NM=SUBSTRING_INDEX(SG_NM,'／',1)
  , ADD_SG2_NM=SUBSTRING_INDEX(SG_NM,'／',-1)
WHERE DATA_DATE=@DATA_DATE_KA AND LOCATE('／', SG_NM)>0
;

--ADD的欄位邏輯及UPDATE

--分公司系統邏輯
SELECT KA_RC_ID
     , (CASE WHEN KA_CHANNEL_NM='NKA' THEN KA_SYS_NM ELSE CONCAT(KA_COM_NM,KA_SYS_NM) END) AS ADD_KA_COM_SYS_NM
FROM APDC.MAN_KA_POS
WHERE DATA_DATE=@DATA_DATE_KA
;

UPDATE APDC.MAN_KA_POS SET
     ADD_KA_COM_SYS_NM=(CASE WHEN KA_CHANNEL_NM='NKA' THEN KA_SYS_NM ELSE CONCAT(KA_COM_NM,KA_SYS_NM) END)
WHERE DATA_DATE=@DATA_DATE_KA
;

SELECT ADD_KA_COM_SYS_NM, COUNT(1)
FROM APDC.MAN_KA_POS
WHERE DATA_DATE=@DATA_DATE_KA
GROUP BY ADD_KA_COM_SYS_NM
ORDER BY ADD_KA_COM_SYS_NM
;

--中心別邏輯
SELECT KA_RC_ID
     , (CASE WHEN ADD_KA_COM_SYS_NM IN ('农工商','麦德龙','苏州福兴祥','苏州永旺美思佰乐','欧尚','家乐福','南昌国光系统','南昌新华都','南昌百货大楼','南昌天虹','南宁南百佳年华','南宁冠超市','南宁步步高','南宁天和商贸','武汉武商','武汉永旺美思佰乐','武汉中商','武汉中百仓储','杭州联华华商','杭州浙北大厦','杭州物美','易初莲花','宁波联华华商','宁波路桥华联','宁波物美','大润发','上海华联吉买盛') THEN '1中心'
             WHEN ADD_KA_COM_SYS_NM IN ('郑州银座','郑州北京华联','郑州丹尼斯','郑州大商集团','贵阳贵州合力','贵阳北京华联','广州嘉荣','广州百佳','广州吉之岛','漯河固始华联','漯河西亚超市','深圳岁宝','深圳嘉荣','深圳百佳华','深圳百佳','深圳吉之岛','重庆新世纪','重庆重客隆','沃尔玛','成都百货大楼','北京物美','北京京客隆','北京北京华冠','世纪联华','人人乐') THEN '2中心'
             WHEN ADD_KA_COM_SYS_NM IN ('苏果','温州联华华商','温州物美','济南银座','济南潍坊百货','济南济南华联','济南寿光百货','济南福兴祥','济南家家悦','华润','乐购','福州新华都','南京福兴祥','青岛银座','青岛潍坊百货','青岛崂山百货','青岛寿光百货','青岛福兴祥','青岛家家悦','合肥合家福','石家庄保百广场','石家庄北国系统','永辉','太原华美超市','太原美特好','太原北京华联','太原介休吉隆斯','太原万家福','太原山姆士超市','天津唐山八方','天津物美','天津百货大楼','天津宁河家乐','天津大港迎宾','天津唐山陈氏') THEN '3中心'
             ELSE NULL
        END) AS ADD_KA_CTR_NM
FROM APDC.MAN_KA_POS
WHERE DATA_DATE=@DATA_DATE_KA
ORDER BY ADD_KA_CTR_NM
;

UPDATE APDC.MAN_KA_POS SET
     ADD_KA_CTR_NM=(CASE WHEN ADD_KA_COM_SYS_NM IN ('农工商','麦德龙','苏州福兴祥','苏州永旺美思佰乐','欧尚','家乐福','南昌国光系统','南昌新华都','南昌百货大楼','南昌天虹','南宁南百佳年华','南宁冠超市','南宁步步高','南宁天和商贸','武汉武商','武汉永旺美思佰乐','武汉中商','武汉中百仓储','杭州联华华商','杭州浙北大厦','杭州物美','易初莲花','宁波联华华商','宁波路桥华联','宁波物美','大润发','上海华联吉买盛') THEN '1中心'
                         WHEN ADD_KA_COM_SYS_NM IN ('郑州银座','郑州北京华联','郑州丹尼斯','郑州大商集团','贵阳贵州合力','贵阳北京华联','广州嘉荣','广州百佳','广州吉之岛','漯河固始华联','漯河西亚超市','深圳岁宝','深圳嘉荣','深圳百佳华','深圳百佳','深圳吉之岛','重庆新世纪','重庆重客隆','沃尔玛','成都百货大楼','北京物美','北京京客隆','北京北京华冠','世纪联华','人人乐') THEN '2中心'
                         WHEN ADD_KA_COM_SYS_NM IN ('苏果','温州联华华商','温州物美','济南银座','济南潍坊百货','济南济南华联','济南寿光百货','济南福兴祥','济南家家悦','华润','乐购','福州新华都','南京福兴祥','青岛银座','青岛潍坊百货','青岛崂山百货','青岛寿光百货','青岛福兴祥','青岛家家悦','合肥合家福','石家庄保百广场','石家庄北国系统','永辉','太原华美超市','太原美特好','太原北京华联','太原介休吉隆斯','太原万家福','太原山姆士超市','天津唐山八方','天津物美','天津百货大楼','天津宁河家乐','天津大港迎宾','天津唐山陈氏') THEN '3中心'
                         ELSE NULL
                    END)
WHERE DATA_DATE=@DATA_DATE_KA
;

SELECT ADD_KA_CTR_NM, COUNT(1)
FROM APDC.MAN_KA_POS
WHERE DATA_DATE=@DATA_DATE_KA
GROUP BY ADD_KA_CTR_NM
ORDER BY ADD_KA_CTR_NM
;

--業績表現分類邏輯
SELECT KA_RC_ID
     , (CASE WHEN TRG_REACH_RATE >= 1 THEN '1特优' 
             WHEN TRG_REACH_RATE < 1 AND (PAST_MONTH_GROWTH_RATE >= 0 OR PAST_MONTH_GROWTH_RATE IS NULL) THEN '2普通'
             WHEN PAST_MONTH_GROWTH_RATE < 0 THEN '3衰退'
             ELSE NULL
        END) AS ADD_POS_PERF_TYPE
FROM APDC.MAN_KA_POS
WHERE DATA_DATE=@DATA_DATE_KA
GROUP BY KA_RC_ID
;

UPDATE APDC.MAN_KA_POS SET
     ADD_POS_PERF_TYPE=(CASE WHEN TRG_REACH_RATE >= 1 THEN '1特优' 
                             WHEN TRG_REACH_RATE < 1 AND (PAST_MONTH_GROWTH_RATE >= 0 OR PAST_MONTH_GROWTH_RATE IS NULL) THEN '2普通'
                             WHEN PAST_MONTH_GROWTH_RATE < 0 THEN '3衰退'
                             ELSE NULL
                        END)
WHERE DATA_DATE=@DATA_DATE_KA
;

SELECT ADD_POS_PERF_TYPE, COUNT(1)
FROM APDC.MAN_KA_POS
WHERE DATA_DATE=@DATA_DATE_KA
GROUP BY ADD_POS_PERF_TYPE
ORDER BY ADD_POS_PERF_TYPE
;

--業績區間分群邏輯
SELECT KA_RC_ID
     , (CASE WHEN POS_AMT_MONTH<20000 THEN '1危险' 
             WHEN POS_AMT_MONTH<40000 AND POS_AMT_MONTH>=20000  THEN '2待加强'
             WHEN POS_AMT_MONTH<60000 AND POS_AMT_MONTH>=40000  THEN '3普通'
             WHEN POS_AMT_MONTH<100000 AND POS_AMT_MONTH>=60000  THEN '4高' 
             WHEN POS_AMT_MONTH>=100000  THEN '5超高'
             ELSE NULL
        END) AS ADD_POS_AMT_GROUP
FROM APDC.MAN_KA_POS
WHERE DATA_DATE=@DATA_DATE_KA
GROUP BY KA_RC_ID
;

UPDATE APDC.MAN_KA_POS SET
     ADD_POS_AMT_GROUP=(CASE WHEN POS_AMT_MONTH<20000 THEN '1危险' 
                             WHEN POS_AMT_MONTH<40000 AND POS_AMT_MONTH>=20000  THEN '2待加强'
                             WHEN POS_AMT_MONTH<60000 AND POS_AMT_MONTH>=40000  THEN '3普通'
                             WHEN POS_AMT_MONTH<100000 AND POS_AMT_MONTH>=60000  THEN '4高' 
                             WHEN POS_AMT_MONTH>=100000  THEN '5超高'
                             ELSE NULL
                        END)
WHERE DATA_DATE=@DATA_DATE_KA
;

SELECT ADD_POS_AMT_GROUP,COUNT(1)
FROM APDC.MAN_KA_POS
WHERE DATA_DATE=@DATA_DATE_KA
GROUP BY ADD_POS_AMT_GROUP
ORDER BY ADD_POS_AMT_GROUP
;

--目標達成率＆同期成長率

--UPDATE ADD_ZTRG_REACH_RATE
UPDATE APDC.MAN_KA_POS SET
     ADD_ZTRG_REACH_RATE=(POS_AMT_MONTH/TRG_AMT_MONTH)
WHERE DATA_DATE=@DATA_DATE_KA
;

--UPDATE ADD_ZPAST_MONTH_GROWTH_RATE
UPDATE APDC.MAN_KA_POS SET
     ADD_ZPAST_MONTH_GROWTH_RATE=(CASE WHEN (POS_AMT_PAST_MONTH IS NULL OR POS_AMT_PAST_MONTH=0) THEN NULL
                                       ELSE (POS_AMT_MONTH/POS_AMT_PAST_MONTH-1)
                                  END)
WHERE DATA_DATE=@DATA_DATE_KA
;

--排名

--ADD_RANK_GROWTH_RATE_ALL
SELECT @ROWNUM:=@ROWNUM+1 AS ROWNUM, Z.KA_RC_ID
FROM ( SELECT * 
       FROM APDC.MAN_KA_POS
       WHERE DATA_DATE=@DATA_DATE_KA) Z
JOIN (SELECT @ROWNUM:=0) X
ON 1=1
ORDER BY Z.PAST_MONTH_GROWTH_RATE DESC
;

USE APDC;
UPDATE APDC.MAN_KA_POS A
JOIN (SELECT @ROWNUM:=@ROWNUM+1 AS ROWNUM, Z.KA_RC_ID
      FROM ( SELECT * 
             FROM APDC.MAN_KA_POS
             WHERE DATA_DATE=@DATA_DATE_KA) Z
      JOIN (SELECT @ROWNUM:=0) X
      ON 1=1
      ORDER BY Z.PAST_MONTH_GROWTH_RATE DESC) B
ON A.KA_RC_ID=B.KA_RC_ID
SET A.ADD_RANK_GROWTH_RATE_ALL=B.ROWNUM
WHERE A.DATA_DATE=@DATA_DATE_KA
;

SELECT ADD_RANK_GROWTH_RATE_ALL
FROM APDC.MAN_KA_POS
WHERE DATA_DATE=@DATA_DATE_KA
ORDER BY ADD_RANK_GROWTH_RATE_ALL
;

--ADD_RANK_GROWTH_RATE_COM
SELECT KA_RC_ID, KA_COM_NM, PAST_MONTH_GROWTH_RATE
     , RANK() OVER (PARTITION BY KA_COM_NM ORDER BY PAST_MONTH_GROWTH_RATE DESC) AS ADD_RANK_GROWTH_RATE_COM
FROM APDC.MAN_KA_POS
;

UPDATE APDC.MAN_KA_POS F
JOIN (SELECT @ROWNUM:=(CASE WHEN @ROWGROUP<>KA_COM_NM THEN 1 ELSE @ROWNUM+1 END) AS ROWNUM
           , @ROWGROUP:=KA_COM_NM AS ROWGROUP
           , A.KA_RC_ID
      FROM (SELECT *
            FROM APDC.MAN_KA_POS
            WHERE DATA_DATE=@DATA_DATE_KA) A
      JOIN (SELECT @ROWGROUP:='' COLLATE UTF8_UNICODE_CI, @ROWNUM:=0) Z
      ON 1=1
      ORDER BY A.KA_COM_NM, PAST_MONTH_GROWTH_RATE DESC) X
ON F.KA_RC_ID=X.KA_RC_ID
SET F.ADD_RANK_GROWTH_RATE_COM=X.ROWNUM
WHERE F.DATA_DATE=@DATA_DATE_KA
;

--ADD_RANK_REACH_RATE_ALL
SELECT KA_RC_ID ,TRG_REACH_RATE , RANK() OVER (ORDER BY TRG_REACH_RATE DESC) AS ADD_RANK_REACH_RATE_ALL
FROM APDC.MAN_KA_POS
;

UPDATE APDC.MAN_KA_POS A
JOIN (SELECT @ROWNUM:=@ROWNUM+1 AS ROWNUM, Z.KA_RC_ID
      FROM ( SELECT * 
             FROM APDC.MAN_KA_POS
             WHERE DATA_DATE=@DATA_DATE_KA) Z
      JOIN (SELECT @ROWNUM:=0) X
      ON 1=1
      ORDER BY Z.TRG_REACH_RATE DESC) B
ON A.KA_RC_ID=B.KA_RC_ID
SET A.ADD_RANK_REACH_RATE_ALL=B.ROWNUM
WHERE A.DATA_DATE=@DATA_DATE_KA
;

--ADD_RANK_REACH_RATE_COM
SELECT KA_RC_ID , KA_COM_NM, TRG_REACH_RATE
     , RANK() OVER (PARTITION BY KA_COM_NM ORDER BY TRG_REACH_RATE DESC) AS ADD_RANK_REACH_RATE_COM
FROM APDC.MAN_KA_POS
;

UPDATE APDC.MAN_KA_POS F
JOIN (SELECT @ROWNUM:=(CASE WHEN @ROWGROUP<>KA_COM_NM THEN 1 ELSE @ROWNUM+1 END) AS ROWNUM
           , @ROWGROUP:=KA_COM_NM AS ROWGROUP
           , A.KA_RC_ID
      FROM (SELECT *
            FROM APDC.MAN_KA_POS
            WHERE DATA_DATE=@DATA_DATE_KA) A
      JOIN (SELECT @ROWGROUP:='' COLLATE UTF8_UNICODE_CI, @ROWNUM:=0) Z
      ON 1=1
      ORDER BY A.KA_COM_NM, TRG_REACH_RATE DESC) X
ON F.KA_RC_ID=X.KA_RC_ID
SET F.ADD_RANK_REACH_RATE_COM=X.ROWNUM
WHERE F.DATA_DATE=@DATA_DATE_KA
;