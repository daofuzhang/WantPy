SELECT '"' || {edino} || '"'
   || ',"' || SID || '"'
   || ',"' || SMALL_MARKET_ID || '"'
   || ',"' || CUSTOMER_ID || '"'
   || ',"' || CREATE_USER || '"'
   || ',"' || TO_CHAR(CREATE_DATE,'YYYYMMDD') || '"'
   || ',"' || UPDATE_USER || '"'
   || ',"' || TO_CHAR(UPDATE_DATE,'YYYYMMDD') || '"'
   || ',"' || CHANNEL_ID || '"'
   || ',"' || TYPE || '"'
   || ',"' || MARKET_ID || '"'
   || ',"' || TO_CHAR(START_DATE,'YYYYMMDD') || '"'
   || ',"' || TO_CHAR(END_DATE,'YYYYMMDD') || '"'
   || ',"' || IS_DELETE || '"' AS CONTENT
FROM SALES.CUSTOMER_SMALL_MARKET
;
