DROP FUNCTION IF EXISTS DWWANT.FN_GET_CM_CODE_NM;

CREATE FUNCTION DWWANT.FN_GET_CM_CODE_NM(VAR_CODE_KIND VARCHAR(10), VAR_CODE_ID VARCHAR(10)) RETURNS VARCHAR(150)
BEGIN
    DECLARE VAR_CODE_NM VARCHAR(150);

    SELECT CODE_NM INTO VAR_CODE_NM
    FROM DWWANT.CM_CODE 
    WHERE CODE_KIND=VAR_CODE_KIND AND CODE_ID=VAR_CODE_ID;

    RETURN VAR_CODE_NM;
END
