SET FOREIGN_KEY_CHECKS=0 ;

CREATE TABLE `DC0024_WEEK_NUM`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`WEEK_NUM` CHAR(6) NOT NULL,
	`WEEK_FIRST_DATE` CHAR(8) NOT NULL,
	`WEEK_LAST_DATE` CHAR(8) NOT NULL,
	CONSTRAINT `PK_DC0024_WEEK_NUM` PRIMARY KEY (`WEEK_NUM`)
)

;

CREATE TABLE `DC0024_STORE_MATL_M`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`KA_SYSTEM_CODE` VARCHAR(10) NOT NULL,
	`KA_SYSTEM_NM` VARCHAR(60) NOT NULL,
	`KA_STORE_CODE` VARCHAR(6) NOT NULL,
	`KA_STORE_NM` VARCHAR(150) 	 NULL,
	`SALES_COM_ID_SA` VARCHAR(4) 	 NULL,
	`SALES_COM_ABR_SA` VARCHAR(60) 	 NULL,
	`SALES_COM_ID_WH` VARCHAR(4) NOT NULL,
	`SALES_COM_ABR_WH` VARCHAR(60) 	 NULL,
	`SALES_COM_ID_DE` VARCHAR(4) NOT NULL,
	`SALES_COM_ABR_DE` VARCHAR(50) 	 NULL,
	`PROD_H1_ID` VARCHAR(20) NOT NULL,
	`PROD_H1_NM` VARCHAR(60) 	 NULL,
	`PROD_H2_ID` VARCHAR(20) 	 NULL,
	`PROD_H2_NM` VARCHAR(60) 	 NULL,
	`PROD_MATL_ID` VARCHAR(18) NOT NULL,
	`PROD_MATL_NM` VARCHAR(60) 	 NULL,
	`POS_YM` CHAR(6) NOT NULL,
	`POS_QTY_PCS_D` DECIMAL(21,4) NOT NULL,
	`POS_QTY_PKG_D` DECIMAL(21,4) NOT NULL,
	`POS_AMT_D` DECIMAL(21,4) NOT NULL,
	`POS_QTY_PCS_M` DECIMAL(21,4) NOT NULL,
	`POS_QTY_PKG_M` DECIMAL(21,4) NOT NULL,
	`POS_AMT_M` DECIMAL(21,4) NOT NULL,
	CONSTRAINT `PK_DC0024_STORE_MATL_M` PRIMARY KEY (`KA_SYSTEM_CODE`,`KA_STORE_CODE`,`PROD_MATL_ID`)
)

;

CREATE TABLE `DC0024_STORE_MATL_D`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`KA_SYSTEM_CODE` VARCHAR(10) NOT NULL,
	`KA_SYSTEM_NM` VARCHAR(60) NOT NULL,
	`KA_STORE_WH_CODE` VARCHAR(6) NOT NULL,
	`KA_STORE_WH_NM` VARCHAR(150) 	 NULL,
	`STORE_WH_TYPE` VARCHAR(10) NOT NULL,
	`STORE_WH_TYPE_NM` VARCHAR(150) 	 NULL,
	`SALES_COM_ID_SA` VARCHAR(4) 	 NULL,
	`SALES_COM_ABR_SA` VARCHAR(60) 	 NULL,
	`SALES_COM_ID_WH` VARCHAR(4) NOT NULL,
	`SALES_COM_ABR_WH` VARCHAR(60) 	 NULL,
	`SALES_COM_ID_DE` VARCHAR(4) NOT NULL,
	`SALES_COM_ABR_DE` VARCHAR(50) 	 NULL,
	`PROD_H1_ID` VARCHAR(20) NOT NULL,
	`PROD_H1_NM` VARCHAR(60) 	 NULL,
	`PROD_H2_ID` VARCHAR(20) 	 NULL,
	`PROD_H2_NM` VARCHAR(60) 	 NULL,
	`PROD_MATL_ID` VARCHAR(18) NOT NULL,
	`PROD_MATL_NM` VARCHAR(60) 	 NULL,
	`POS_INV_DATE` CHAR(8) NOT NULL,
	`POS_QTY_PCS` DECIMAL(21,4) NOT NULL,
	`POS_QTY_PKG` DECIMAL(21,4) NOT NULL,
	`POS_AMT` DECIMAL(21,4) NOT NULL,
	`INV_QTY_PCS` DECIMAL(21,4) NOT NULL,
	`INV_QTY_PKG` DECIMAL(21,4) NOT NULL,
	CONSTRAINT `PK_DC0024_STORE_MATL_D` PRIMARY KEY (`KA_SYSTEM_CODE`,`KA_STORE_WH_CODE`,`PROD_MATL_ID`)
)

;

CREATE TABLE `DC0024_STORE_M`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`KA_SYSTEM_CODE` VARCHAR(10) NOT NULL,
	`KA_SYSTEM_NM` VARCHAR(60) NOT NULL,
	`KA_STORE_CODE` VARCHAR(6) NOT NULL,
	`KA_STORE_NM` VARCHAR(150) 	 NULL,
	`SALES_COM_ID_SA` VARCHAR(4) 	 NULL,
	`SALES_COM_ABR_SA` VARCHAR(60) 	 NULL,
	`SALES_COM_ID_WH` VARCHAR(4) NOT NULL,
	`SALES_COM_ABR_WH` VARCHAR(60) 	 NULL,
	`SALES_COM_ID_DE` VARCHAR(4) NOT NULL,
	`SALES_COM_ABR_DE` VARCHAR(50) 	 NULL,
	`POS_YM` CHAR(6) NOT NULL,
	`POS_QTY_PCS_D` DECIMAL(21,4) NOT NULL,
	`POS_QTY_PKG_D` DECIMAL(21,4) NOT NULL,
	`POS_AMT_D` DECIMAL(21,4) NOT NULL,
	`POS_QTY_PCS_M` DECIMAL(21,4) NOT NULL,
	`POS_QTY_PKG_M` DECIMAL(21,4) NOT NULL,
	`POS_AMT_M` DECIMAL(21,4) NOT NULL,
	CONSTRAINT `PK_DC0024_STORE_M` PRIMARY KEY (`KA_SYSTEM_CODE`,`KA_STORE_CODE`)
)

;

CREATE TABLE `DC0024_POS_RPT01_SYSTEM`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`KA_SYSTEM_CODE` VARCHAR(10) NOT NULL,
	`KA_SYSTEM_NM` VARCHAR(60) NOT NULL,
	`KA_SYSTEM_ACT` VARCHAR(10) NOT NULL,
	`KA_SYSTEM_ACT_NM` VARCHAR(150) NOT NULL,
	`POS_WEEK_NUM` CHAR(6) NOT NULL,
	`POS_QTY_PCS` DECIMAL(21,4) NOT NULL,
	`POS_QTY_PKG` DECIMAL(21,4) NOT NULL,
	`POS_AMT` DECIMAL(21,4) NOT NULL,
	`POS_SKU` INT NOT NULL,
	CONSTRAINT `PK_DC0024_POS_RPT01_SYSTEM` PRIMARY KEY (`KA_SYSTEM_CODE`,`POS_WEEK_NUM`)
)

;

CREATE TABLE `DC0024_POS_RPT01_STORE`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`KA_SYSTEM_CODE` VARCHAR(10) NOT NULL,
	`KA_SYSTEM_NM` VARCHAR(60) NOT NULL,
	`KA_SYSTEM_ACT` VARCHAR(10) NOT NULL,
	`KA_SYSTEM_ACT_NM` VARCHAR(150) NOT NULL,
	`POS_WEEK_NUM` CHAR(6) NOT NULL,
	`KA_STORE_CODE` VARCHAR(4) NOT NULL,
	`KA_STORE_NM` VARCHAR(50) NOT NULL,
	`SALES_COM_ID_SA` VARCHAR(4) NOT NULL,
	`SALES_COM_ABR_SA` VARCHAR(60) NOT NULL,
	`SALES_COM_ID_WH` VARCHAR(4) NOT NULL,
	`SALES_COM_ABR_WH` VARCHAR(60) NOT NULL,
	`POS_QTY_PCS` DECIMAL(21,4) NOT NULL,
	`POS_QTY_PKG` DECIMAL(21,4) NOT NULL,
	`POS_AMT` DECIMAL(21,4) NOT NULL,
	`POS_SKU` INT NOT NULL,
	CONSTRAINT `PK_DC0024_POS_RPT01_STORE` PRIMARY KEY (`KA_SYSTEM_CODE`,`POS_WEEK_NUM`,`KA_STORE_CODE`,`SALES_COM_ID_SA`,`SALES_COM_ID_WH`)
)

;

CREATE TABLE `DC0024_POS_RPT01_PRODH1`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`KA_SYSTEM_CODE` VARCHAR(10) NOT NULL,
	`KA_SYSTEM_NM` VARCHAR(60) NOT NULL,
	`KA_SYSTEM_ACT` VARCHAR(10) NOT NULL,
	`KA_SYSTEM_ACT_NM` VARCHAR(150) NOT NULL,
	`POS_WEEK_NUM` CHAR(6) NOT NULL,
	`PROD_H1_ID` VARCHAR(20) NOT NULL,
	`PROD_H1_NM` VARCHAR(60) NOT NULL,
	`SALES_COM_ID_SA` VARCHAR(4) NOT NULL,
	`SALES_COM_ABR_SA` VARCHAR(60) NOT NULL,
	`POS_QTY_PCS` DECIMAL(21,4) NOT NULL,
	`POS_QTY_PKG` DECIMAL(21,4) NOT NULL,
	`POS_AMT` DECIMAL(21,4) NOT NULL,
	`POS_SKU` INT NOT NULL,
	CONSTRAINT `PK_DC0024_POS_RPT01_PRODH1` PRIMARY KEY (`KA_SYSTEM_CODE`,`POS_WEEK_NUM`,`PROD_H1_ID`,`SALES_COM_ID_SA`)
)

;

CREATE TABLE `DC0024_POS_RPT01_COM`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`SALES_COM_ID_SA` VARCHAR(4) NOT NULL,
	`SALES_COM_ABR_SA` VARCHAR(60) NOT NULL,
	`POS_WEEK_NUM` CHAR(6) NOT NULL,
	`POS_QTY_PCS` DECIMAL(21,4) NOT NULL,
	`POS_QTY_PKG` DECIMAL(21,4) NOT NULL,
	`POS_AMT` DECIMAL(21,4) NOT NULL,
	`POS_SKU` INT NOT NULL,
	CONSTRAINT `PK_DC0024_POS_RPT01_COM` PRIMARY KEY (`SALES_COM_ID_SA`,`POS_WEEK_NUM`)
)

;

CREATE TABLE `DC0024_POS_RPT01`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`POS_DATE` CHAR(8) NOT NULL,
	CONSTRAINT `PK_DC0024_POS_RPT01` PRIMARY KEY (`DATA_DATE`)
)

;

CREATE TABLE `DC0024_ORDR_TRAS_D`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`KA_SYSTEM_CODE` VARCHAR(10) NOT NULL,
	`KA_SYSTEM_NM` VARCHAR(60) 	 NULL,
	`SYSTEM_ORDR_DATE` CHAR(8) NOT NULL,
	`ORDR_MAIN_ID` VARCHAR(40) NOT NULL,
	`SYSTEM_ORDR_NO` VARCHAR(64) NOT NULL,
	`SAP_ORDR_NO` VARCHAR(10) NOT NULL,
	`OPEN_ORDR_DATE` CHAR(8) NOT NULL,
	`CUST_ID` VARCHAR(15) NOT NULL,
	`SALES_COM_ID_DE_ORDR` VARCHAR(4) NOT NULL,
	`SALES_COM_ABR_DE_ORDR` VARCHAR(60) 	 NULL,
	`SALES_COM_ID_DE` VARCHAR(4) NOT NULL,
	`SALES_COM_ABR_DE` VARCHAR(60) 	 NULL,
	`SALES_COM_ID_BL` VARCHAR(4) NOT NULL,
	`SALES_COM_ABR_BL` VARCHAR(60) 	 NULL,
	`SALES_CHAN_ID` VARCHAR(2) NOT NULL,
	`PROD_DIV_ID` VARCHAR(2) NOT NULL,
	`SYSTEM_DEV_DATE` CHAR(8) 	 NULL,
	`IS_FACT_DEV` CHAR(1) NOT NULL,
	`ORDR_LINE_NUM` INT NOT NULL,
	`SAP_LINE_NUM` INT NOT NULL,
	`SYSTEM_ORDR_PROD_NM` VARCHAR(150) NOT NULL,
	`PROD_H1_ID_SYS` VARCHAR(20) 	 NULL,
	`PROD_H1_NM_SYS` VARCHAR(60) 	 NULL,
	`PROD_H2_ID_SYS` VARCHAR(20) 	 NULL,
	`PROD_H2_NM_SYS` VARCHAR(60) 	 NULL,
	`PROD_MATL_ID_SYS` VARCHAR(18) NOT NULL,
	`PROD_MATL_NM_SYS` VARCHAR(60) 	 NULL,
	`PROD_H1_ID_OPEN` VARCHAR(20) 	 NULL,
	`PROD_H1_NM_OPEN` VARCHAR(60) 	 NULL,
	`PROD_H2_ID_OPEN` VARCHAR(20) 	 NULL,
	`PROD_H2_NM_OPEN` VARCHAR(60) 	 NULL,
	`PROD_MATL_ID_OPEN` VARCHAR(18) NOT NULL,
	`PROD_MATL_NM_OPEN` VARCHAR(60) 	 NULL,
	`STORE_PLACE_CODE` VARCHAR(4) 	 NULL,
	`IS_STORE_PLACE_DIR` CHAR(1) NOT NULL,
	`PROD_AMT_PKG_SYS` DECIMAL(21,4) 	 NULL,
	`PROD_QTY_PKG_SYS` DECIMAL(21,4) 	 NULL,
	`PROD_AMT_PKG_OPEN` DECIMAL(21,4) NOT NULL,
	`PROD_QTY_PKG_OPEN` DECIMAL(21,4) NOT NULL,
	`SAP_AMT_PKG_OPEN` DECIMAL(21,4) NOT NULL,
	`SAP_QTY_PKG_OPEN` DECIMAL(21,4) NOT NULL,
	`SAP_AMT_PKG_APPD` DECIMAL(21,4) NOT NULL,
	`SAP_QTY_PKG_APPD` DECIMAL(21,4) NOT NULL,
	`SHIP_QTY_PKG_DIF` INT 	 NULL,
	`SHIP_QTY_PKG_DEV` INT 	 NULL,
	`SHIP_QTY_PKG_ACT` INT 	 NULL,
	CONSTRAINT `PK_DC0024_ORDR_TRAS_D` PRIMARY KEY (`SAP_ORDR_NO`,`SAP_LINE_NUM`)
)

;

CREATE TABLE `DC0024_ORDR_SYS_D`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`KA_SYSTEM_CODE` VARCHAR(10) NOT NULL,
	`KA_SYSTEM_NM` VARCHAR(60) 	 NULL,
	`SYSTEM_ORDR_DATE` CHAR(8) NOT NULL,
	`ORDR_MAIN_ID` VARCHAR(40) NOT NULL,
	`SYSTEM_ORDR_NO` VARCHAR(64) NOT NULL,
	`SALES_COM_ID_DE` VARCHAR(4) 	 NULL,
	`SALES_COM_ABR_DE` VARCHAR(60) 	 NULL,
	`SALES_COM_ID_BL` VARCHAR(4) 	 NULL,
	`SALES_COM_ABR_BL` VARCHAR(60) 	 NULL,
	`SALES_CHAN_ID` VARCHAR(2) 	 NULL,
	`PROD_DIV_ID` VARCHAR(2) 	 NULL,
	`CUST_ID` VARCHAR(15) 	 NULL,
	`SYSTEM_DEV_DATE` CHAR(8) 	 NULL,
	`ORDR_LINE_NUM` INT NOT NULL,
	`SYSTEM_ORDR_PROD_NM` VARCHAR(150) NOT NULL,
	`PROD_H1_ID` VARCHAR(20) 	 NULL,
	`PROD_H1_NM` VARCHAR(60) 	 NULL,
	`PROD_H2_ID` VARCHAR(20) 	 NULL,
	`PROD_H2_NM` VARCHAR(60) 	 NULL,
	`PROD_MATL_ID` VARCHAR(18) 	 NULL,
	`PROD_MATL_NM` VARCHAR(60) 	 NULL,
	`PROD_AMT_PKG` DECIMAL(21,4) 	 NULL,
	`TRAS_PROD_AMT_PKG` DECIMAL(21,4) 	 NULL,
	`PROD_QTY_PKG` DECIMAL(21,4) 	 NULL,
	`SAP_QTY_PKG_APPD_SUM_DIR` DECIMAL(21,4) 	 NULL,
	`SAP_QTY_PKG_APPD_SUM` DECIMAL(21,4) 	 NULL,
	`SAP_QTY_PKG_APPD_SUM_DIF` DECIMAL(21,4) 	 NULL,
	`SHIP_QTY_PKG_DIF_SUM` INT 	 NULL,
	`SHIP_QTY_PKG_DEV_SUM` INT 	 NULL,
	`SHIP_QTY_PKG_ACT_SUM` INT 	 NULL,
	`SHIP_QTY_PKG_ACT_SUM_DIF` DECIMAL(21,4) 	 NULL,
	`TRAS_RETURN_PHASE_NM` VARCHAR(150) 	 NULL,
	`TRAS_RETURN_RMK` VARCHAR(200) 	 NULL,
	CONSTRAINT `PK_DC0024_ORDR_SYS_D` PRIMARY KEY (`ORDR_MAIN_ID`,`ORDR_LINE_NUM`)
)

;

CREATE TABLE `DC0024_INVALID_RPT01_WH_COM_INV`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`KA_SYSTEM_CODE` VARCHAR(10) NOT NULL,
	`KA_SYSTEM_NM` VARCHAR(60) NOT NULL,
	`KA_WH_CODE` VARCHAR(6) NOT NULL,
	`KA_WH_NM` VARCHAR(150) 	 NULL,
	`SALES_COM_WH_CN` INT NOT NULL,
	`SALES_COM_DE_CN` INT NOT NULL,
	CONSTRAINT `PK_DC0024_INVALID_RPT01_WH_COM_INV` PRIMARY KEY (`KA_SYSTEM_CODE`,`KA_WH_CODE`)
)

;

CREATE TABLE `DC0024_INVALID_RPT01_STORE_POS`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`KA_SYSTEM_CODE` VARCHAR(10) NOT NULL,
	`KA_SYSTEM_NM` VARCHAR(60) NOT NULL,
	`SYSTEM_STORE_CODE` VARCHAR(10) NOT NULL,
	`SYSTEM_STORE_NM` VARCHAR(150) NOT NULL,
	`POS_DATE_MIN` CHAR(8) NOT NULL,
	`POS_DATE_MAX` CHAR(8) NOT NULL,
	CONSTRAINT `PK_DC0024_INVALID_RPT01_STORE_POS` PRIMARY KEY (`KA_SYSTEM_CODE`,`SYSTEM_STORE_CODE`,`SYSTEM_STORE_NM`)
)

;

CREATE TABLE `DC0024_INVALID_RPT01_STORE_INV`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`KA_SYSTEM_CODE` VARCHAR(10) NOT NULL,
	`KA_SYSTEM_NM` VARCHAR(60) NOT NULL,
	`SYSTEM_STORE_CODE` VARCHAR(10) NOT NULL,
	`SYSTEM_STORE_NM` VARCHAR(150) NOT NULL,
	`INV_DATE_MIN` CHAR(8) NOT NULL,
	`INV_DATE_MAX` CHAR(8) NOT NULL,
	CONSTRAINT `PK_DC0024_INVALID_RPT01_STORE_INV` PRIMARY KEY (`KA_SYSTEM_CODE`,`SYSTEM_STORE_CODE`,`SYSTEM_STORE_NM`)
)

;

CREATE TABLE `DC0024_INVALID_RPT01_STORE_COM_POS`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`KA_SYSTEM_CODE` VARCHAR(10) NOT NULL,
	`KA_SYSTEM_NM` VARCHAR(60) NOT NULL,
	`KA_STORE_CODE` VARCHAR(4) NOT NULL,
	`KA_STORE_NM` VARCHAR(150) 	 NULL,
	`SALES_COM_SA_CN` INT NOT NULL,
	`SALES_COM_WH_CN` INT NOT NULL,
	`SALES_COM_DE_CN` INT NOT NULL,
	CONSTRAINT `PK_DC0024_INVALID_RPT01_STORE_COM_POS` PRIMARY KEY (`KA_SYSTEM_CODE`,`KA_STORE_CODE`)
)

;

CREATE TABLE `DC0024_INVALID_RPT01_STORE_COM_INV`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`KA_SYSTEM_CODE` VARCHAR(10) NOT NULL,
	`KA_SYSTEM_NM` VARCHAR(60) NOT NULL,
	`KA_STORE_CODE` VARCHAR(4) NOT NULL,
	`KA_STORE_NM` VARCHAR(150) 	 NULL,
	`SALES_COM_SA_CN` INT NOT NULL,
	`SALES_COM_WH_CN` INT NOT NULL,
	`SALES_COM_DE_CN` INT NOT NULL,
	CONSTRAINT `PK_DC0024_INVALID_RPT01_STORE_COM_INV` PRIMARY KEY (`KA_SYSTEM_CODE`,`KA_STORE_CODE`)
)

;

CREATE TABLE `DC0024_INVALID_RPT01_PROD_POS`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`KA_SYSTEM_CODE` VARCHAR(10) NOT NULL,
	`KA_SYSTEM_NM` VARCHAR(60) NOT NULL,
	`SYSTEM_PROD_CODE` VARCHAR(20) NOT NULL,
	`SYSTEM_PROD_NM` VARCHAR(150) NOT NULL,
	`POS_DATE_MIN` CHAR(8) NOT NULL,
	`POS_DATE_MAX` CHAR(8) NOT NULL,
	CONSTRAINT `PK_DC0024_INVALID_RPT01_PROD_POS` PRIMARY KEY (`KA_SYSTEM_CODE`,`SYSTEM_PROD_CODE`,`SYSTEM_PROD_NM`)
)

;

CREATE TABLE `DC0024_INVALID_RPT01_PROD_INV`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`KA_SYSTEM_CODE` VARCHAR(10) NOT NULL,
	`KA_SYSTEM_NM` VARCHAR(60) NOT NULL,
	`SYSTEM_PROD_CODE` VARCHAR(20) NOT NULL,
	`SYSTEM_PROD_NM` VARCHAR(150) NOT NULL,
	`INV_DATE_MIN` CHAR(8) NOT NULL,
	`INV_DATE_MAX` CHAR(8) NOT NULL,
	CONSTRAINT `PK_DC0024_INVALID_RPT01_PROD_INV` PRIMARY KEY (`KA_SYSTEM_CODE`,`SYSTEM_PROD_CODE`,`SYSTEM_PROD_NM`)
)

;

CREATE TABLE `DC0024_INVALID_RPT01`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`POS_DATE_MIN` CHAR(8) NOT NULL,
	`POS_DATE_MAX` CHAR(8) NOT NULL,
	CONSTRAINT `PK_DC0024_INVALID_RPT01` PRIMARY KEY (`EDI_NO`)
)

;

SET FOREIGN_KEY_CHECKS=1 ;
