SELECT {edino} AS EDI_NO
     , "SALESORG", "LANGU"
     , REPLACE(REPLACE("TXTLG", CHAR(13), ''), CHAR(10), '') AS "TXTLG"
FROM "SAPBHP"."/BI0/TSALESORG"
;