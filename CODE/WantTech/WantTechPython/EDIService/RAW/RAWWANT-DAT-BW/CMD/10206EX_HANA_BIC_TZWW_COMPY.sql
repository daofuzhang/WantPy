SELECT {edino} AS EDI_NO
     , "/BIC/ZWW_COMPY"
     , REPLACE(REPLACE("TXTSH", CHAR(13), ''), CHAR(10), '') AS "TXTSH"
FROM "SAPBHP"."/BIC/TZWW_COMPY"
;