SELECT DISTINCT EDI_NO
     , RIGHT(CONCAT('00000000',REPLACE(TRIM(USER_ID),'.0','')),8) AS USER_ID
     , (CASE WHEN LEFT(TRIM(CUSTOMER_ID), 2)='00' THEN CONCAT('00000', TRIM(CUSTOMER_ID)) ELSE TRIM(CUSTOMER_ID) END) AS CUSTOMER_ID
     , CREDIT_ID
     , START_TIME, END_TIME
     , '' AS COMPANY_ID
     , '' AS PROD_GROUP_ID
     , '' AS THIRD_CITY_ID
     , CREATE_DATE, CREATE_USER, UPDATE_DATE, UPDATE_USER
     , STATUS
     , POS_TYPE_ID, TRIM(POS_TYPE_NAME) AS POS_TYPE_NAME
     , MARKET_RELATION_ID
     , '' AS POS_NAME
     , EMP_COMPANY_ID
     , (CASE WHEN ASCII(EMP_BRANCH_ID)=32 THEN '' ELSE EMP_BRANCH_ID END) AS EMP_BRANCH_ID
FROM (SELECT A.*
      FROM RAWWANT.IWANT_SALES_CUSTOMER_SALES A
      JOIN (SELECT USER_ID, CUSTOMER_ID, CREDIT_ID, START_TIME, END_TIME
                 , CREATE_DATE, CREATE_USER, UPDATE_DATE, UPDATE_USER
                 , STATUS, POS_TYPE_ID
            FROM (SELECT USER_ID, CUSTOMER_ID, CREDIT_ID, START_TIME, END_TIME
                       , CREATE_DATE, CREATE_USER, UPDATE_DATE, UPDATE_USER
                       , STATUS, POS_TYPE_ID
                       , COUNT(DISTINCT MARKET_RELATION_ID) AS CN
                  FROM RAWWANT.IWANT_SALES_CUSTOMER_SALES
                  WHERE TRIM(USER_ID)<>'#N/A' AND INSTR(TRIM(CUSTOMER_ID),'.')=0
                  GROUP BY USER_ID, CUSTOMER_ID, CREDIT_ID, START_TIME, END_TIME
                         , CREATE_DATE, CREATE_USER, UPDATE_DATE, UPDATE_USER
                         , STATUS, POS_TYPE_ID) A
            WHERE CN=1) B
      ON A.USER_ID=B.USER_ID AND A.CUSTOMER_ID=B.CUSTOMER_ID AND A.CREDIT_ID=B.CREDIT_ID AND A.START_TIME=B.START_TIME AND A.END_TIME=B.END_TIME AND
         A.CREATE_DATE=B.CREATE_DATE AND A.CREATE_USER=B.CREATE_USER AND A.UPDATE_DATE=B.UPDATE_DATE AND A.UPDATE_USER=B.UPDATE_USER AND 
         A.STATUS=B.STATUS AND A.POS_TYPE_ID=B.POS_TYPE_ID
      WHERE TRIM(A.USER_ID)<>'#N/A' AND INSTR(TRIM(A.CUSTOMER_ID),'.')=0

      UNION ALL

      SELECT A.*
      FROM RAWWANT.IWANT_SALES_CUSTOMER_SALES A
      JOIN (SELECT USER_ID, CUSTOMER_ID, CREDIT_ID, START_TIME, END_TIME
                 , CREATE_DATE, CREATE_USER, UPDATE_DATE, UPDATE_USER
                 , STATUS, POS_TYPE_ID
            FROM (SELECT USER_ID, CUSTOMER_ID, CREDIT_ID, START_TIME, END_TIME
                       , CREATE_DATE, CREATE_USER, UPDATE_DATE, UPDATE_USER
                       , STATUS, POS_TYPE_ID
                       , COUNT(DISTINCT MARKET_RELATION_ID) AS CN
                  FROM RAWWANT.IWANT_SALES_CUSTOMER_SALES
                  WHERE TRIM(USER_ID)<>'#N/A' AND INSTR(TRIM(CUSTOMER_ID),'.')=0
                  GROUP BY USER_ID, CUSTOMER_ID, CREDIT_ID, START_TIME, END_TIME
                         , CREATE_DATE, CREATE_USER, UPDATE_DATE, UPDATE_USER
                         , STATUS, POS_TYPE_ID) A
            WHERE CN>1) B
      ON A.USER_ID=B.USER_ID AND A.CUSTOMER_ID=B.CUSTOMER_ID AND A.CREDIT_ID=B.CREDIT_ID AND A.START_TIME=B.START_TIME AND A.END_TIME=B.END_TIME AND
         A.CREATE_DATE=B.CREATE_DATE AND A.CREATE_USER=B.CREATE_USER AND A.UPDATE_DATE=B.UPDATE_DATE AND A.UPDATE_USER=B.UPDATE_USER AND 
         A.STATUS=B.STATUS AND A.POS_TYPE_ID=B.POS_TYPE_ID
      WHERE TRIM(A.USER_ID)<>'#N/A' AND INSTR(TRIM(A.CUSTOMER_ID),'.')=0
        AND MARKET_RELATION_ID>-99999) Z
;