SELECT '"' || {edino} || '"'
   || ',"' || ID || '"'
   || ',"' || NAME || '"' 
   || ',"' || MARKET_ID || '"'
   || ',"' || BRANCH_ID || '"'   AS CONTENT
FROM SALES.THIRD_CITY
;