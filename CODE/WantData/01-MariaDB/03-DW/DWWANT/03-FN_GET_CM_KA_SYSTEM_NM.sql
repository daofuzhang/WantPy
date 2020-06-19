DROP FUNCTION IF EXISTS DWWANT.FN_GET_CM_KA_SYSTEM_NM;

CREATE FUNCTION DWWANT.FN_GET_CM_KA_SYSTEM_NM(VAR_KA_SYSTEM_CODE VARCHAR(10)) RETURNS VARCHAR(60)
BEGIN
    DECLARE VAR_KA_SYSTEM_NM VARCHAR(60);

    SELECT KA_SYSTEM_NM INTO VAR_KA_SYSTEM_NM 
    FROM DWWANT.CM_KA_SYSTEM
    WHERE KA_SYSTEM_CODE=VAR_KA_SYSTEM_CODE;

    RETURN VAR_KA_SYSTEM_NM;
END
