SELECT {edino} AS EDI_NO
     , "/BIC/ZWWCHAN"
     , REPLACE(REPLACE("TXTSH", CHAR(13), ''), CHAR(10), '') AS "TXTSH"
FROM "SAPBHP"."/BIC/TZWWCHAN"
;