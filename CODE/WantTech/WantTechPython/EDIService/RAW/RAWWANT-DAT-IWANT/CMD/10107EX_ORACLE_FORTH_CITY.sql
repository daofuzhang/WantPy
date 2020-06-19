SELECT '"' || {edino} || '"'
   || ',"' || SID || '"'
   || ',"' || NAME || '"'
   || ',"' || THIRD_ID || '"'
   || ',"' || STATUS || '"'
   || ',"' || NVL(TOTAL_PEOPLE, -99999) || '"' AS CONTENT
FROM SALES.FORTH_CITY
;