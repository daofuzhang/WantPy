DROP FUNCTION IF EXISTS DWWANT.FN_GET_DATETIME;

CREATE FUNCTION DWWANT.FN_GET_DATETIME(VAR_DATETIME DATETIME) RETURNS CHAR(14)
BEGIN
    RETURN DATE_FORMAT(VAR_DATETIME, '%Y%m%d%h%i%s');
END