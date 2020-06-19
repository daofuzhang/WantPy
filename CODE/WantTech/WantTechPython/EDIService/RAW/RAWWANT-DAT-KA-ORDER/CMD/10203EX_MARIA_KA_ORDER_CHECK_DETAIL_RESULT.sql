select {edino} as EDI_NO
     , d.id
     , ifnull(d.order_main_id, '') as order_main_id
     , ifnull(d.check_no, '') as check_no
     , ifnull(d.order_num, '') as order_num
     , ifnull(d.materiel_code, '') as materiel_code
     , ifnull(d.materiel_name, '') as materiel_name
     , ifnull(date_format(d.allow_date, '%Y%m%d'), '') as allow_date
     , ifnull(d.sap_order_num, -99999) as sap_order_num
     , ifnull(d.sap_box_price, -99999) as sap_box_price
     , ifnull(d.sap_box_price_old, -99999) as sap_box_price_old
     , ifnull(d.materiel_code_replace, '') as materiel_code_replace
     , ifnull(d.materiel_name_replace, '') as materiel_name_replace
     , ifnull(d.is_buy_term, '') as is_buy_term
     , ifnull(d.result, '') as result
     , ifnull(d.distro_result, '') as distro_result
     , ifnull(d.status, -99999) as status
from ka_wantwant_prod.ka_order_check_result m
join ka_wantwant_prod.ka_order_check_detail_result d
on m.check_no=d.check_no
where substring(m.check_no, 2, 8)>='2019-09-17 00:00:00.0'
  and substring(m.check_no, 2, 8)>=concat(date_format(date_add(str_to_date({datadate}, '%Y%m%d'), interval -3 month), '%Y%m'), '01')
  and substring(m.check_no, 2, 8)<={datadate}
;