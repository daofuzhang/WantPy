select {edino} as EDI_NO
     , id
     , ifnull(sys_code, '') as sys_code
     , ifnull(store_code, '') as store_code
     , ifnull(store_name, '') as store_name
     , ifnull(deliver_address_code, '') as deliver_address_code
     , ifnull(deliver_address_desc, '') as deliver_address_desc
     , ifnull(judge_field, '') as judge_field
     , ifnull(check_no, '') as check_no
     , ifnull(order_no, '') as order_no
     , ifnull(order_main_id, '') as order_main_id
     , ifnull(cust_code, '') as cust_code
     , ifnull(deliver_comp_code, '') as deliver_comp_code
     , ifnull(bill_comp_code, '') as bill_comp_code
     , ifnull(bill_ditch_code, '') as bill_ditch_code
     , ifnull(bill_prod_code, '') as bill_prod_code
     , ifnull(bill_deliver_code, '') as bill_deliver_code
     , ifnull(date_format(open_order_date, '%Y%m%d'), '') as open_order_date
     , ifnull(is_factdev, '') as is_factdev
     , ifnull(check_user, -99999) as check_user
     , ifnull(date_format(check_date, '%Y%m%d'), '') as check_date
     , ifnull(date_format(check_time , '%H%i%s'), '') as check_time
     , ifnull(type, -99999) as type
     , ifnull(is_over, '') as is_over
     , ifnull(date_format(result_date, '%Y%m%d'), '') as result_date
     , ifnull(date_format(result_time, '%H%i%s'), '') as result_time
     , ifnull(check_status, -99999) as check_status
     , ifnull(check_result, '') as check_result
     , ifnull(status, -99999) as status
     , ifnull(date_format(create_time, '%Y%m%d%H%i%s'), '') as create_time
     , ifnull(create_by, -99999) as create_by
     , ifnull(create_by_name, '') as create_by_name
from ka_wantwant_prod.ka_order_check_result
where substring(check_no, 2, 8)>='2019-09-17 00:00:00.0'
  and substring(check_no, 2, 8)>=concat(date_format(date_add(str_to_date({datadate}, '%Y%m%d'), interval -3 month), '%Y%m'), '01')
  and substring(check_no, 2, 8)<={datadate}
;