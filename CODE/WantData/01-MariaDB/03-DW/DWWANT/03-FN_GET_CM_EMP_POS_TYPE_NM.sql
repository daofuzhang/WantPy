DROP FUNCTION IF EXISTS DWWANT.FN_GET_CM_EMP_POS_TYPE_NM;

CREATE FUNCTION DWWANT.FN_GET_CM_EMP_POS_TYPE_NM(VAR_EMP_POS_TYPE VARCHAR(3)) RETURNS VARCHAR(60)
BEGIN
    DECLARE VAR_EMP_POS_TYPE_NM VARCHAR(60);

    SELECT EMP_POS_TYPE_NM INTO VAR_EMP_POS_TYPE_NM 
    FROM DWWANT.CM_EMP_POS_TYPE
    WHERE EMP_POS_TYPE=VAR_EMP_POS_TYPE;

    RETURN VAR_EMP_POS_TYPE_NM;
END
