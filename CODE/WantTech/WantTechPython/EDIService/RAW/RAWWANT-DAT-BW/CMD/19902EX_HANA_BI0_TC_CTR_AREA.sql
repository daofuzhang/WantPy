SELECT {edino} AS EDI_NO
     , "C_CTR_AREA", "LANGU"
     , REPLACE(REPLACE("TXTMD", CHAR(13), ''), CHAR(10), '') AS "TXTMD"
     , REPLACE(REPLACE("TXTLG", CHAR(13), ''), CHAR(10), '') AS "TXTLG"
FROM "SAPBHP"."/BI0/TC_CTR_AREA"
;