SELECT EDI_NO
     , PROD_HIER, LANGU
     , TRIM(TXTLG) AS TXTLG
FROM RAWWANT.BW_SAPBHP_BI0_TPROD_HIER
WHERE LANGU='1'
;