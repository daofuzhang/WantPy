SELECT EDI_NO
     , (CASE WHEN ID LIKE '0000%' THEN SUBSTR(ID, 5) 
             ELSE ID           
        END)
     , REPLACE(NAME, (CASE WHEN ID LIKE '0000%' THEN SUBSTR(ID, 5)      
                           ELSE ID 
                      END), '')  
    , MARKET_ID
    , BRANCH_ID
FROM RAWWANT.IWANT_SALES_THIRD_CITY
;