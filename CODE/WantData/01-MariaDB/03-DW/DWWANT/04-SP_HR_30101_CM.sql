DROP PROCEDURE IF EXISTS DWWANT.SP_HR_30101_CM;

CREATE PROCEDURE DWWANT.SP_HR_30101_CM (
    VAR_EDI_NO CHAR(12), VAR_DATA_DATE CHAR(8), OUT VAR_SP_RESULT CHAR(1)
)
BEGIN

    INSERT INTO DWWANT.CM_EMP_POS
    SELECT VAR_EDI_NO AS EDI_NO, VAR_DATA_DATE AS DATA_DATE
         , (CASE WHEN E.HRPOSITION=''   THEN 'NULL' ELSE E.HRPOSITION   END) AS EMP_POS_ID
         , (CASE WHEN E.BIC_ZHRPOS_N='' THEN  NULL  ELSE E.BIC_ZHRPOS_N END) AS EMP_POS_NM
    FROM (SELECT MAX(EDI_NO) AS EDI_NO
               , HRPOSITION, MAX(BIC_ZHRPOS_N) AS BIC_ZHRPOS_N
          FROM RAWWANT.BW_SAPBHP_BIC_AZHR_O7100
          WHERE HRPOSITION<>''
          GROUP BY HRPOSITION) E
    ORDER BY E.HRPOSITION
    ;

    INSERT INTO DWWANT.CM_EMP_POS_PROP
    SELECT VAR_EDI_NO AS EDI_NO, VAR_DATA_DATE AS DATA_DATE
         , (CASE WHEN E.BIC_ZPOS_ATTR='' THEN 'NULL' ELSE E.BIC_ZPOS_ATTR END) AS EMP_POS_PROP_ID
         , (CASE WHEN E.BIC_ZPOS_A_N=''  THEN  NULL  ELSE E.BIC_ZPOS_A_N  END) AS EMP_POS_PROP_NM
    FROM (SELECT MAX(EDI_NO) AS EDI_NO
               , BIC_ZPOS_ATTR, MAX(BIC_ZPOS_A_N) AS BIC_ZPOS_A_N
          FROM RAWWANT.BW_SAPBHP_BIC_AZHR_O7100
          WHERE BIC_ZPOS_ATTR<>''
          GROUP BY BIC_ZPOS_ATTR) E
    ORDER BY E.BIC_ZPOS_ATTR
    ;

    INSERT INTO DWWANT.CM_EMP_POS_TITLE
    SELECT VAR_EDI_NO AS EDI_NO, VAR_DATA_DATE AS DATA_DATE
         , (CASE WHEN E.JOB=''        THEN 'NULL' ELSE E.JOB        END) AS EMP_POS_TITLE_ID
         , (CASE WHEN E.BIC_ZJOB_N='' THEN  NULL  ELSE E.BIC_ZJOB_N END) AS EMP_POS_TITLE_NM
    FROM (SELECT MAX(EDI_NO) AS EDI_NO
               , JOB, MAX(BIC_ZJOB_N) AS BIC_ZJOB_N
          FROM RAWWANT.BW_SAPBHP_BIC_AZHR_O7100
          WHERE JOB<>''
          GROUP BY JOB) E
    ORDER BY E.JOB
    ;

    INSERT INTO DWWANT.CM_EMP_POS_LEVEL
    SELECT VAR_EDI_NO AS EDI_NO, VAR_DATA_DATE AS DATA_DATE
         , (CASE WHEN E.BIC_ZSGRADE=''  THEN 'NULL' ELSE E.BIC_ZSGRADE  END) AS EMP_POS_LEVEL_ID
         , (CASE WHEN E.BIC_ZGRADE_N='' THEN  NULL  ELSE E.BIC_ZGRADE_N END) AS EMP_POS_LEVEL_NM
    FROM (SELECT MAX(EDI_NO) AS EDI_NO
               , BIC_ZSGRADE, MAX(BIC_ZGRADE_N) AS BIC_ZGRADE_N
          FROM RAWWANT.BW_SAPBHP_BIC_AZHR_O7100
          WHERE BIC_ZSGRADE<>''
          GROUP BY BIC_ZSGRADE) E
    ORDER BY E.BIC_ZSGRADE
    ;

    SET VAR_SP_RESULT='Y';
    COMMIT;
END
;