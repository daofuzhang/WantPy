SELECT {edino} AS EDI_NO
     , "/BIC/ZCOOIC064", "LANGU"
     , REPLACE(REPLACE("TXTSH", CHAR(13), ''), CHAR(10), '') AS "TXTSH"
FROM "SAPBHP"."/BIC/TZCOOIC064"
;