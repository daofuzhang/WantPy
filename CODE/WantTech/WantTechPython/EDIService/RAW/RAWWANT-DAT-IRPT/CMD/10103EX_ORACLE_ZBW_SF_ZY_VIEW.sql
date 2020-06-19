SELECT '"' || {edino} || '"'
   || ',"' || CHANNEL_ID || '"'
   || ',"' || SALES_CHANNEL || '"'
   || ',"' || PROD_GROUP || '"'
   || ',"' || COMPANY_ID || '"'
   || ',"' || SYS_ID || '"'
   || ',"' || THIRD_ID || '"'
   || ',"' || KEYACCOUNT_ID || '"'
   || ',"' || ERP_ID || '"'
   || ',"' || STORE_ID || '"'
   || ',"' || YEARMONTH || '"'
   || ',"' || PROD_ID || '"'
   || ',"' || NVL(SF_QUANTITY, -99999) || '"'
   || ',"' || NVL(SF_AMOUNT, -99999) || '"'
   || ',"' || NVL(NEXT_SF_QTY, -99999) || '"'
   || ',"' || NVL(NEXT_SF_AMOUNT, -99999) || '"' AS CONTENT
FROM SAPBW.ZBW_SF_ZY_VIEW
WHERE YEARMONTH>=TO_CHAR(ADD_MONTHS(TO_DATE({datadate},'YYYYMMDD'),-24),'YYYYMM')
;
