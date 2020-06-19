SELECT '"' || {edino} || '"'
   || ',"' || SID || '"'
   || ',"' || NVL(MARKET_RELATION_ID, -99999) || '"'
   || ',"' || MARKET_TYPE || '"'
   || ',"' || MARKET_ID || '"'
   || ',"' || MARKET_NAME || '"'
   || ',"' || SMALL_MARKET_ID || '"'
   || ',"' || SMALL_MARKET_NAME || '"' AS CONTENT
FROM SALES.CUS_SALES_MARKET_REL
;
