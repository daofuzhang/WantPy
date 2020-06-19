select {edino} as EDI_NO
     , id
     , ifnull(sap_order_no, '') as sap_order_no
     , ifnull(sap_posnr, -99999) as sap_posnr
     , ifnull(difference_box_num, -99999) as difference_box_num
     , ifnull(actual_deliver_box_num, -99999) as actual_deliver_box_num
     , ifnull(date_format(sap_harvest_date, '%Y%m%d'), '') as sap_harvest_date
     , ifnull(date_format(sap_return_receipt_date, '%Y%m%d'), '') as sap_return_receipt_date
     , ifnull(sap_shipment_num, '') as sap_shipment_num
     , ifnull(sap_shipment_name, '') as sap_shipment_name
     , ifnull(date_format(return_date, '%Y%m%d'), '') as return_date
     , ifnull(date_format(return_time, '%Y%m%d%H%i%s'), '') as return_time
     , ifnull(customer_received_box_num, -99999) as customer_received_box_num
     , ifnull(text_desc, '') as text_desc
     , ifnull(date_format(created, '%Y%m%d%H%i%s'), '') as created
from ka_wantwant_prod.ka_sap_shipping_return
where date_format(sap_return_receipt_date, '%Y%m%d')>='2019-09-17 00:00:00.0'
  and date_format(sap_return_receipt_date, '%Y%m%d')>=concat(date_format(date_add(str_to_date({datadate}, '%Y%m%d'), interval -3 month), '%Y%m'), '01')
  and date_format(sap_return_receipt_date, '%Y%m%d')<={datadate}
;