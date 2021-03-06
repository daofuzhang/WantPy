DROP FUNCTION IF EXISTS DWWANT.FN_GET_WEEK_NUM;

CREATE FUNCTION DWWANT.FN_GET_WEEK_NUM(VAR_DATE CHAR(8)) RETURNS CHAR(6)
BEGIN
    DECLARE VAR_LAST_YEAR CHAR(4);

    IF WEEK(VAR_DATE, 5)=0 THEN
        SET VAR_LAST_YEAR = CONVERT(CONVERT(LEFT(VAR_DATE, 4), INT) - 1, CHAR);

        RETURN CONCAT(VAR_LAST_YEAR, RIGHT(CONCAT('0', CONVERT(WEEK(CONCAT(VAR_LAST_YEAR, '1231'), 5), CHAR)), 2));
    ELSE
        RETURN CONCAT(LEFT(VAR_DATE, 4), RIGHT(CONCAT('0', CONVERT(WEEK(VAR_DATE, 5), CHAR)), 2));
    END IF;
END
