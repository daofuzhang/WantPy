DROP FUNCTION IF EXISTS RAWWANT.FN_GET_ALPHANUMERIC_INDEX;

CREATE FUNCTION RAWWANT.FN_GET_ALPHANUMERIC_INDEX(VAR_COL VARCHAR(200)) RETURNS INT
BEGIN
    DECLARE VAR_INDEX INT;
    DECLARE VAR_TEMP INT;

    SET VAR_INDEX = 0;

    IF VAR_COL IS NOT NULL AND CHAR_LENGTH(VAR_COL)>0 THEN
        VAR_WHILE : WHILE VAR_INDEX<CHAR_LENGTH(VAR_COL) DO
            SET VAR_INDEX = VAR_INDEX + 1;

            SET VAR_TEMP = ASCII(SUBSTRING(VAR_COL, VAR_INDEX, 1));
            IF (VAR_TEMP<48) OR (VAR_TEMP>57 AND VAR_TEMP<65) OR (VAR_TEMP>90 AND VAR_TEMP<97) OR (VAR_TEMP>122) THEN
                SET VAR_INDEX = VAR_INDEX - 1;
                LEAVE VAR_WHILE;
            END IF;

        END WHILE;
    END IF;

    RETURN VAR_INDEX;
END