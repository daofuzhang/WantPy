SELECT '"' || {edino} || '"'
   || ',"' || SID || '"'
   || ',"' || CUSTOMER_SMALL_MARKET_ID || '"'
   || ',"' || PROD_LINE_ID || '"'
   || ',"' || PROD_LINE_NAME || '"'
   || ',"' || STATUS || '"'
   || ',"' || CREATE_USER || '"'
   || ',"' || TO_CHAR(CREATE_DATE,'YYYYMMDD') || '"'
   || ',"' || UPDATE_USER || '"'
   || ',"' || TO_CHAR(UPDATE_DATE,'YYYYMMDD') || '"' AS CONTENT
FROM SALES.CUS_SMALL_MARKET_PROD_LINE
;
