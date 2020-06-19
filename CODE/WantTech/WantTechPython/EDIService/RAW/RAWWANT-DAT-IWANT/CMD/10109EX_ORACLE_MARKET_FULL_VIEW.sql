SELECT '"' || {edino} || '"'
   || ',"' || COMPANY_ID || '"'
   || ',"' || COMPANY_NAME || '"'
   || ',"' || BRANCH_ID || '"'
   || ',"' || BRANCH_NAME || '"'
   || ',"' || MARKET_ID || '"'
   || ',"' || MARKET_NAME || '"'
   || ',"' || THIRD_ID || '"'
   || ',"' || THIRD_NAME || '"' AS CONTENT
FROM SALES.MARKET_FULL_VIEW
;
