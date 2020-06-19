SELECT D.EDI_NO
     , D.ID
     , D.SAP_PIN_CHECK_ID
     , D.SAP_ORDER_NO
     , D.STATUS
     , D.SAP_POSNR
     , D.SAP_PER_PRICE
     , D.SAP_ORDER_CREATE_NUM
     , D.SAP_APP_NEW_PRICE
     , D.SAP_PROMOTION_SEASON_DATE
     , D.SAP_IS_CHECK
     , D.SAP_REASON_REJECTION
     , D.IS_SHIPPING
     , D.AUDIT_STATUS
FROM RAWWANT.KA_WANTWANT_KA_SAP_PIN_CHECK M
JOIN RAWWANT.KA_WANTWANT_KA_SAP_PIN_CHECK_DETAIL D
ON M.ID=D.SAP_PIN_CHECK_ID
;