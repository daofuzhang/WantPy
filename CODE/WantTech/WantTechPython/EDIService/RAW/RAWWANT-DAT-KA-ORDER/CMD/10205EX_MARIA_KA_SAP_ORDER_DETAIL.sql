select {edino} as EDI_NO
     , d.id
     , ifnull(d.ka_sap_order_id, -99999) as ka_sap_order_id
     , ifnull(d.open_no, '') as open_no
     , ifnull(d.valid_no, '') as valid_no
     , ifnull(d.ka_materiel_code, '') as ka_materiel_code
     , ifnull(d.ka_materiel_name, '') as ka_materiel_name
     , ifnull(d.is_buy_term, '') as is_buy_term
     , ifnull(date_format(d.per_production_date, '%Y%m%d'), '') as per_production_date
     , ifnull(d.store_place, '') as store_place
     , ifnull(d.sap_box_old_price, -99999) as sap_box_old_price
     , ifnull(d.sap_box_new_price, -99999) as sap_box_new_price
     , ifnull(d.sap_order_num, -99999) as sap_order_num
     , ifnull(d.ka_total_box_num, -99999) as ka_total_box_num
     , ifnull(d.ka_materiel_code_replace, '') as ka_materiel_code_replace
     , ifnull(d.ka_materiel_name_replace, '') as ka_materiel_name_replace
     , ifnull(d.is_replace, -99999) as is_replace
     , ifnull(d.sap_posnr, -99999) as sap_posnr
     , ifnull(d.sap_per_price, -99999) as sap_per_price
     , ifnull(d.sap_order_create_num, -99999) as sap_order_create_num
     , ifnull(d.sap_return_desc, '') as sap_return_desc
     , ifnull(d.sap_audit_box_num, -99999) as sap_audit_box_num
     , ifnull(d.sap_audit_per_price, -99999) as sap_audit_per_price
     , ifnull(d.sap_reason_rejection, '') as sap_reason_rejection
     , ifnull(d.sap_delive_box_num, -99999) as sap_delive_box_num
     , ifnull(d.difference_box_num, -99999) as difference_box_num
from ka_wantwant_prod.ka_sap_order m
join ka_wantwant_prod.ka_sap_order_detail d
on m.id=d.ka_sap_order_id
where m.status=1
  and substring(m.open_no, 2, 8)>='2019-09-17 00:00:00.0'
  and substring(m.open_no, 2, 8)>=concat(date_format(date_add(str_to_date({datadate}, '%Y%m%d'), interval -3 month), '%Y%m'), '01')
  and substring(m.open_no, 2, 8)<={datadate}
;