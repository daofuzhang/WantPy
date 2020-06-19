select {edino} as EDI_NO
     , d.id
     , ifnull(d.sap_pin_check_id, -99999) as sap_pin_check_id
     , ifnull(d.sap_order_no, '') as sap_order_no
     , ifnull(d.status, -99999) as status
     , ifnull(d.sap_posnr, -99999) as sap_posnr
     , ifnull(d.sap_per_price, -99999) as sap_per_price
     , ifnull(d.sap_order_create_num, -99999) as sap_order_create_num
     , ifnull(d.sap_app_new_price, -99999) as sap_app_new_price
     , ifnull(date_format(d.sap_promotion_season_date, '%Y%m%d'), '') as sap_promotion_season_date
     , ifnull(d.sap_is_check, '') as sap_is_check
     , ifnull(d.sap_reason_rejection, '') as sap_reason_rejection
     , ifnull(d.is_shipping, -99999) as is_shipping
     , ifnull(d.audit_status, -99999) as audit_status
from ka_wantwant_prod.ka_sap_pin_check m
join ka_wantwant_prod.ka_sap_pin_check_detail d
on m.id=d.sap_pin_check_id
where m.status=1
  and date_format(m.sap_open_order_date, '%Y%m%d')>='2019-09-17 00:00:00.0'
  and date_format(m.sap_open_order_date, '%Y%m%d')>=concat(date_format(date_add(str_to_date({datadate}, '%Y%m%d'), interval -3 month), '%Y%m'), '01')
  and date_format(m.sap_open_order_date, '%Y%m%d')<={datadate}
  and d.status=1
;