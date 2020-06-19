SELECT '"' || {edino} || '"'
   || ',"' || CHANNEL_ID || '"'
   || ',"' || CHANNEL_NAME || '"'
   || ',"' || STATUS || '"'
   || ',"' || ERP_CHANNEL_ID || '"'
   || ',"' || ERP_CHANNEL_DESC || '"'
   || ',"' || ERP_PROD_GROUP_ID || '"'
   || ',"' || ERP_PROD_GROUP_DESC || '"'
   || ',"' || DIVISION_ID || '"'
   || ',"' || DIVISION_NAME || '"' AS CONTENT
FROM SALES.CHANNEL
;
