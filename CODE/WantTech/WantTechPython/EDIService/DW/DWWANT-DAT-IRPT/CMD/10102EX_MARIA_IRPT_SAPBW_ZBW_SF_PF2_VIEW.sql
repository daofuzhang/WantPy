SELECT EDI_NO
     , CHANNEL_ID, SALES_CHANNEL
     , PROD_GROUP
     , COMPANY_ID, AREA_ID
     , YEARMONTH
     , PROD_ID
     , SF_QUANTITY, SF_AMOUNT, NEXT_SF_QTY, NEXT_SF_AMOUNT
FROM RAWWANT.IRPT_SAPBW_ZBW_SF_PF2_VIEW
;