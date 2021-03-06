DROP FUNCTION IF EXISTS DWWANT.FN_GET_ORG_HR_OFF_NM;

CREATE FUNCTION DWWANT.FN_GET_ORG_HR_OFF_NM(VAR_HR_OFF_ID VARCHAR(8)) RETURNS VARCHAR(60)
BEGIN
    DECLARE VAR_HR_OFF_NM VARCHAR(60);

    SELECT HR_OFF_NM INTO VAR_HR_OFF_NM 
    FROM DWWANT.ORG_HR_OFF
    WHERE HR_OFF_ID=VAR_HR_OFF_ID;

    RETURN VAR_HR_OFF_NM;
END
