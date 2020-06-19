select {edino} as EDI_NO
     , id
     , ifnull(sap_order_no, '') as sap_order_no
     , ifnull(order_main_id, '') as order_main_id
     , ifnull(audit_status, -99999) as audit_status
     , ifnull(date_format(sap_open_order_date, '%Y%m%d'), '') as sap_open_order_date
     , ifnull(sap_delivery_branch, '') as sap_delivery_branch
     , ifnull(sap_is_check, '') as sap_is_check
     , ifnull(sap_check_num, '') as sap_check_num
     , ifnull(status, -99999) as status
     , ifnull(sap_audit_name, '') as sap_audit_name
     , ifnull(date_format(return_date, '%Y%m%d%H%i%s'), '') as return_date
     , ifnull(date_format(return_time, '%Y%m%d%H%i%s'), '') as return_time
from ka_wantwant_prod.ka_sap_pin_check
where status=1
  and date_format(sap_open_order_date, '%Y%m%d')>='2019-09-17 00:00:00.0'
  and date_format(sap_open_order_date, '%Y%m%d')>=concat(date_format(date_add(str_to_date({datadate}, '%Y%m%d'), interval -3 month), '%Y%m'), '01')
  and date_format(sap_open_order_date, '%Y%m%d')<={datadate}
;