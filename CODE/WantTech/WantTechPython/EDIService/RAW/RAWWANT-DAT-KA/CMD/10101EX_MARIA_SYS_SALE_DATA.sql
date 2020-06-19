select {edino} as EDI_NO
     , id
     , date_format(means_date, '%Y%m%d') as means_date
     , date_format(means_time, '%H%i%s') as means_time
     , ifnull(choose, '') as choose
     , ifnull(sys_code, '') as sys_code
     , ifnull(sys_name, '') as sys_name
     , ifnull(sale_division, '') as sale_division
     , ifnull(serial_num, '') as serial_num
     , ifnull(is_means, '') as is_means
     , ifnull(store_code, '') as store_code
     , ifnull(store_name, '') as store_name
     , ifnull(ka_store_code, '') as ka_store_code
     , ifnull(sale_prod_code, '') as sale_prod_code
     , ifnull(ka_materiel_code, '') as ka_materiel_code
     , ifnull(prod_name, '') as prod_name
     , ifnull(prod_spec, '') as prod_spec
     , ifnull(min_prod_unit, '') as min_prod_unit
     , date_format(sale_date, '%Y%m%d') as sale_date
     , ifnull(day_sale_num, -99999) as day_sale_num
     , ifnull(day_sale_price, -99999) as day_sale_price
     , date_format(created, '%Y%m%d%H%i%s') as created
     , ifnull(created_by, '') as created_by
     , date_format(updated, '%Y%m%d%H%i%s') as updated
     , ifnull(updated_by, '') as updated_by
     , status
     , ifnull(prod_type_code, '') as prod_type_code
     , ifnull(prod_type_name, '') as prod_type_name
     , ifnull(material_name, '') as material_name
     , ifnull(shelf_life_num, '') as shelf_life_num
     , ifnull(ww_store_name, '') as ww_store_name
     , ifnull(sys_account, '') as sys_account
     , ifnull(sys_other_info, '') as sys_other_info
     , dms_data_sale_id
     , client_id
     , ifnull(code_warehouse_plot, '') as code_warehouse_plot
     , ifnull(code_split_ground, '') as code_split_ground
     , end_month_flag
     , ifnull(name_warehouse_plot, '') as name_warehouse_plot
     , ifnull(name_split_ground, '') as name_split_ground
     , ifnull(pm_code, '') as pm_code
     , ifnull(pm_name, '') as pm_name
     , ifnull(terminal_code, '') as terminal_code
     , ifnull(sale_box_num, -99999) as sale_box_num
     , match_status
     , repeat_match_flag
     , ifnull(ww_delivery_branch_office_code, '') as ww_delivery_branch_office_code
     , ifnull(ww_delivery_branch_office_name, '') as ww_delivery_branch_office_name
from ka_wantwant_prod.sys_sale_data
where sale_date>='2019-06-01 00:00:00.0' 
  and ((end_month_flag=0 and sale_date>=concat(date_format(date_add(str_to_date({datadate}, '%Y%m%d'), interval -10 day), '%Y-%m-%d'), ' 00:00:00.0') and sale_date<=concat(date_format(str_to_date({datadate}, '%Y%m%d'), '%Y-%m-%d'), ' 00:00:00.0')) or 
       (end_month_flag=1 and date_format(sale_date, '%Y-%m')=date_format(date_add(str_to_date({datadate}, '%Y%m%d'), interval -10 day), '%Y-%m')))
;