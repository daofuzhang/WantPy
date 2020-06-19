SELECT '"' || {edino} || '"'
   || ',"' || ID || '"'
   || ',"' || REPLACE(NAME,'"','\"') || '"'
   || ',"' || REPLACE(OWNER,'"','\"') || '"'
   || ',"' || SHORT_NAME || '"'
   || ',"' || DESCRIPTION || '"'
   || ',"' || STATUS || '"'
   || ',"' || BRANCH_ID || '"'
   || ',"' || ID_FRIEND || '"'
   || ',"' || THIRD_ID || '"' AS CONTENT
FROM SALES.CUSTOMER
;
