SELECT EDI_NO
     , (CASE WHEN LEFT(TRIM(ID), 2)='00' THEN CONCAT('00000', TRIM(ID)) ELSE TRIM(ID) END) AS ID
     , TRIM(NAME) AS NAME
     , TRIM(OWNER) AS OWNER
     , TRIM(SHORT_NAME) AS SHORT_NAME
     , TRIM(DESCRIPTION) AS DESCRIPTION
     , STATUS
     , BRANCH_ID
     , ID_FRIEND
     , (CASE WHEN RAWWANT.FN_IS_ALPHANUMERIC(THIRD_ID)='Y' THEN THIRD_ID ELSE '' END) AS THIRD_ID
FROM RAWWANT.IWANT_SALES_CUSTOMER
;