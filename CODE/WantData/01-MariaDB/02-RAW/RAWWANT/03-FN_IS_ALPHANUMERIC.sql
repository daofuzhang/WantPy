DROP FUNCTION IF EXISTS RAWWANT.FN_IS_ALPHANUMERIC;

CREATE FUNCTION RAWWANT.FN_IS_ALPHANUMERIC(VAR_COL VARCHAR(20)) RETURNS CHAR COLLATE UTF8_GENERAL_CI
BEGIN
    DECLARE VAR_IS_ALPHANUMERIC INT;
    SELECT VAR_COL REGEXP '^[A-Za-z0-9]+$' INTO VAR_IS_ALPHANUMERIC;
    IF VAR_IS_ALPHANUMERIC=0 THEN
        RETURN 'N';
    ELSE
        RETURN 'Y';
    END IF;
END