DROP PROCEDURE IF EXISTS DWWANT.SP_DC0022_30101_EMP_SALES;

CREATE PROCEDURE DWWANT.SP_DC0022_30101_EMP_SALES (
    VAR_EDI_NO CHAR(12), VAR_DATA_DATE CHAR(8), OUT VAR_SP_RESULT CHAR(1)
)
BEGIN

    INSERT INTO DMMDL.DC0022_EMP_SALES
    SELECT VAR_EDI_NO AS EDI_NO, VAR_DATA_DATE AS DATA_DATE
         , H.EMP_ID, N.EMP_NM
         , N.EMP_GENDER, DWWANT.FN_GET_ORG_EMP_GENDER_NM(N.EMP_GENDER) AS EMP_GENDER_NM
         , H.ONBOARD_YMD, H.SENIORITY
         , H.HR_COM_ID, DWWANT.FN_GET_ORG_HR_COM_NM(H.HR_COM_ID) AS HR_COM_NM
         , H.HR_OFF_ID, DWWANT.FN_GET_ORG_HR_OFF_NM(H.HR_OFF_ID) AS HR_OFF_NM
         , H.EMP_POS_ID, DWWANT.FN_GET_CM_EMP_POS_NM(H.EMP_POS_ID) AS EMP_POS_NM
         , H.EMP_POS_PROP_ID, DWWANT.FN_GET_CM_EMP_POS_PROP_NM(H.EMP_POS_PROP_ID) AS EMP_POS_PROP_NM
         , H.EMP_POS_TYPE, DWWANT.FN_GET_CM_EMP_POS_TYPE_NM(H.EMP_POS_TYPE) AS EMP_POS_TYPE_NM
         , H.EMP_POS_TITLE_ID, DWWANT.FN_GET_CM_EMP_POS_TITLE_NM(H.EMP_POS_TITLE_ID) AS EMP_POS_TITLE_NM
         , H.EMP_POS_LEVEL_ID, DWWANT.FN_GET_CM_EMP_POS_LEVEL_NM(H.EMP_POS_LEVEL_ID) AS EMP_POS_LEVEL_NM
         , H.EMP_POS_FLAG
    FROM DWWANT.ORG_EMP_SALES_HR H
    LEFT JOIN DWWANT.ORG_EMP N ON H.EMP_ID=N.EMP_ID
    ;
    
    SET VAR_SP_RESULT='Y';
    COMMIT;
END
;