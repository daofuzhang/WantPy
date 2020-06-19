SELECT {edino} AS EDI_NO
     , "FISCYEAR", "FISCVARNT", "BILL_NUM", "BILL_ITEM"
     , "CALMONTH", "CALDAY", "SUBTOTAL_1", "ITEM_CATEG", "CUST_SALES"
     , "DIVISION", "MATERIAL", "DISTR_CHAN", "SALESORG"
     , "COMP_CODE", "/BIC/ZCUS_WWID", "CUSTOMER"
FROM "SAPBHP"."/BIC/AZSD_O2100"
WHERE "CALMONTH">=SUBSTR({datadate},1,6)-200
;