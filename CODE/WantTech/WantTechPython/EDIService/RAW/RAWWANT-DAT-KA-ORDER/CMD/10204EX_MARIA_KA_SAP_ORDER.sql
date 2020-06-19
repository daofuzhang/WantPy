select {edino} as EDI_NO
     , id
     , ifnull(order_create_number, -99999) as order_create_number
     , ifnull(open_no, '') as open_no
     , ifnull(check_no, '') as check_no
     , ifnull(order_main_id, '') as order_main_id
     , ifnull(order_no, '') as order_no
     , ifnull(store_code, '') as store_code
     , ifnull(store_name, '') as store_name
     , ifnull(deliver_address_code, '') as deliver_address_code
     , ifnull(deliver_address_desc, '') as deliver_address_desc
     , ifnull(judge_field, '') as judge_field
     , ifnull(sap_cust_code, '') as sap_cust_code
     , ifnull(ka_deliver_comp_code, '') as ka_deliver_comp_code
     , ifnull(ka_deliver_comp_name, '') as ka_deliver_comp_name
     , ifnull(ka_bill_comp_code, '') as ka_bill_comp_code
     , ifnull(ka_bill_comp_name, '') as ka_bill_comp_name
     , ifnull(ka_bill_ditch_code, '') as ka_bill_ditch_code
     , ifnull(ka_bill_prod_code, '') as ka_bill_prod_code
     , ifnull(date_format(deliver_date, '%Y%m%d'), '') as deliver_date
     , ifnull(sap_bill_deliver_code, '') as sap_bill_deliver_code
     , ifnull(sap_bill_deliver_name, '') as sap_bill_deliver_name
     , ifnull(is_fact_dev, '') as is_fact_dev
     , ifnull(date_format(open_order_date, '%Y%m%d'), '') as open_order_date
     , ifnull(sap_order_no, '') as sap_order_no
     , ifnull(sap_return_desc, '') as sap_return_desc
     , ifnull(date_format(return_time, '%Y%m%d%H%i%s'), '') as return_time
     , ifnull(order_status, -99999) as order_status
     , ifnull(status, -99999) as status
     , ifnull(request_desc, '') as request_desc
     , ifnull(date_format(created_time, '%Y%m%d%H%i%s'), '') as created_time
     , ifnull(created_by, '') as created_by
     , ifnull(created_by_name, '') as created_by_name
     , ifnull(date_format(updated_time, '%Y%m%d%H%i%s'), '') as updated_time
     , ifnull(updated_by, '') as updated_by
     , ifnull(updated_by_name, '') as updated_by_name
from ka_wantwant_prod.ka_sap_order
where status=1
  and substring(open_no, 2, 8)>='2019-09-17 00:00:00.0'
  and substring(open_no, 2, 8)>=concat(date_format(date_add(str_to_date({datadate}, '%Y%m%d'), interval -3 month), '%Y%m'), '01')
  and substring(open_no, 2, 8)<={datadate}
;