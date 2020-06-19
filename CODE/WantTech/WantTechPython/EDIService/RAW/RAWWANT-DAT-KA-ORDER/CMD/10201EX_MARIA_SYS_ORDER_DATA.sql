select {edino} as EDI_NO
     , id
     , ifnull(order_main_id, '') as order_main_id
     , ifnull(raw_id, -99999) as raw_id
     , ifnull(client_id, -99999) as client_id
     , ifnull(date_format(means_date, '%Y%m%d'), '') as means_date
     , ifnull(date_format(means_time, '%Y%m%d%H%i%s'), '') as means_time
     , ifnull(choose, '') as choose
     , ifnull(sys_code, '') as sys_code
     , ifnull(sys_name, '') as sys_name
     , ifnull(sys_account, '') as sys_account
     , ifnull(sys_other_info, '') as sys_other_info
     , ifnull(is_means, '') as is_means
     , ifnull(store_code, '') as store_code
     , ifnull(store_name, '') as store_name
     , ifnull(deliver_address_code, '') as deliver_address_code
     , ifnull(deliver_address_desc, '') as deliver_address_desc
     , ifnull(judge_field, '') as judge_field
     , ifnull(sap_cust_code, '') as sap_cust_code
     , ifnull(sap_cust_name, '') as sap_cust_name
     , ifnull(ka_deliver_comp_code, '') as ka_deliver_comp_code
     , ifnull(ka_deliver_comp_name, '') as ka_deliver_comp_name
     , ifnull(ka_bill_comp_code, '') as ka_bill_comp_code
     , ifnull(ka_bill_comp_name, '') as ka_bill_comp_name
     , ifnull(ka_bill_ditch_code, '') as ka_bill_ditch_code
     , ifnull(ka_bill_prod_code, '') as ka_bill_prod_code
     , ifnull(sap_bill_deliver_code, '') as sap_bill_deliver_code
     , ifnull(sap_bill_deliver_name, '') as sap_bill_deliver_name
     , ifnull(order_division, '') as order_division
     , ifnull(good_age, -99999) as good_age
     , ifnull(sap_text, '') as sap_text
     , ifnull(order_no, '') as order_no
     , ifnull(date_format(order_date, '%Y%m%d%H%i%s'), '') as order_date
     , ifnull(date_format(deliver_date, '%Y%m%d%H%i%s'), '') as deliver_date
     , ifnull(date_format(deliver_time, '%Y%m%d%H%i%s'), '') as deliver_time
     , ifnull(supplier_code, '') as supplier_code
     , ifnull(supplier_name, '') as supplier_name
     , ifnull(order_num, -99999) as order_num
     , ifnull(prod_type_code, '') as prod_type_code
     , ifnull(prod_type_name, '') as prod_type_name
     , ifnull(bar_code, '') as bar_code
     , ifnull(sale_prod_code, '') as sale_prod_code
     , ifnull(ka_materiel_code, '') as ka_materiel_code
     , ifnull(ka_materiel_name, '') as ka_materiel_name
     , ifnull(ka_materiel_ean, '') as ka_materiel_ean
     , ifnull(shelf_life_num, -99999) as shelf_life_num
     , ifnull(is_buy_term, '') as is_buy_term
     , ifnull(allow_data, -99999) as allow_data
     , ifnull(prod_code, '') as prod_code
     , ifnull(prod_name, '') as prod_name
     , ifnull(prod_spec, '') as prod_spec
     , ifnull(min_prod_unit, '') as min_prod_unit
     , ifnull(min_unit_box_num, -99999) as min_unit_box_num
     , ifnull(min_unit_price, -99999) as min_unit_price
     , ifnull(min_unit_order_num, -99999) as min_unit_order_num
     , ifnull(sap_box_price, -99999) as sap_box_price
     , ifnull(sap_order_num, -99999) as sap_order_num
     , ifnull(date_format(created, '%Y%m%d%H%i%s'), '') as created
     , ifnull(created_by, '') as created_by
     , ifnull(date_format(updated, '%Y%m%d%H%i%s'), '') as updated
     , ifnull(updated_by, '') as updated_by
     , ifnull(status, -99999) as status
     , ifnull(match_status, -9) as match_status
     , ifnull(repeat_match_flag, -9) as repeat_match_flag
     , ifnull(send_code_status, -9) as send_code_status
     , ifnull(order_source, '') as order_source
     , ifnull(residual_box_reason, '') as residual_box_reason
     , ifnull(ka_materiel_code_replace, '') as ka_materiel_code_replace
     , ifnull(ka_materiel_name_replace, '') as ka_materiel_name_replace
     , ifnull(is_replace, -99999) as is_replace
     , ifnull(open_box_num, -99999) as open_box_num
     , ifnull(surplus_box_num, -99999) as surplus_box_num
     , ifnull(order_stage, '') as order_stage
     , ifnull(order_header_error, '') as order_header_error
     , ifnull(order_item_error, '') as order_item_error
     , ifnull(is_invalid, '') as is_invalid
     , ifnull(order_invalid_reason, '') as order_invalid_reason
     , ifnull(is_auto_check, -9) as is_auto_check
     , ifnull(dms_min_unit_box_num, '') as dms_min_unit_box_num
     , ifnull(date_format(dms_update_time, '%Y%m%d%H%i%s'), '') as dms_update_time
     , ifnull(is_open_item, -9) as is_open_item
     , ifnull(sap_box_price_spcial, -99999) as sap_box_price_spcial
from ka_wantwant_prod.sys_order_data
where upper(choose)='Y'
  and order_date>='2019-09-17 00:00:00.0'
  and order_date>=concat(date_format(date_add(str_to_date({datadate}, '%Y%m%d'), interval -3 month), '%Y-%m'), '-01 00:00:00.0')
  and order_date<=concat(date_format(str_to_date({datadate}, '%Y%m%d'), '%Y-%m-%d'), ' 00:00:00.0')
;