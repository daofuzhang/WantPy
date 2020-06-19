SET FOREIGN_KEY_CHECKS=0 ;

CREATE TABLE `ORG_WANT_COM`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`WANT_COM_ID` VARCHAR(4) NOT NULL,
	`WANT_COM_NM` VARCHAR(60) 	 NULL,
	CONSTRAINT `PK_ORG_WANT_COM` PRIMARY KEY (`WANT_COM_ID`)
)

;

CREATE TABLE `ORG_WANT_CHAN_PROD`
(
	`WANT_CHAN_ID` VARCHAR(10) NOT NULL,
	`SALES_CHAN_ID` VARCHAR(2) NOT NULL,
	`PROD_DIV_ID` VARCHAR(2) NOT NULL,
	`UPD_USER_ID` VARCHAR(50) NOT NULL,
	`UPD_DT` DATETIME(0) NOT NULL,
	CONSTRAINT `PK_ORG_WANT_CHAN_PROD` PRIMARY KEY (`WANT_CHAN_ID`,`SALES_CHAN_ID`,`PROD_DIV_ID`)
)

;

CREATE TABLE `ORG_WANT_CHAN`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`WANT_CHAN_ID` VARCHAR(10) NOT NULL,
	`WANT_CHAN_NM` VARCHAR(60) 	 NULL,
	CONSTRAINT `PK_ORG_WANT_CHAN` PRIMARY KEY (`WANT_CHAN_ID`)
)

;

CREATE TABLE `ORG_SALES_OFF`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`SALES_OFF_ID` VARCHAR(4) NOT NULL,
	`SALES_OFF_NM` VARCHAR(60) 	 NULL,
	`SALES_OFF_TYPE` CHAR(1) 	 NULL,
	CONSTRAINT `PK_ORG_SALES_OFF` PRIMARY KEY (`SALES_OFF_ID`)
)

;

CREATE TABLE `ORG_SALES_COM`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`SALES_COM_ID` VARCHAR(4) NOT NULL,
	`SALES_COM_NM` VARCHAR(60) 	 NULL,
	`SALES_COM_ABR` VARCHAR(60) 	 NULL,
	CONSTRAINT `PK_ORG_SALES_COM` PRIMARY KEY (`SALES_COM_ID`)
)

;

CREATE TABLE `ORG_SALES_CHAN`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`SALES_CHAN_ID` VARCHAR(2) NOT NULL,
	`SALES_CHAN_NM` VARCHAR(60) 	 NULL,
	CONSTRAINT `PK_ORG_SALES_CHAN` PRIMARY KEY (`SALES_CHAN_ID`)
)

;

CREATE TABLE `ORG_IWANT_REGN`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`IWANT_REGN_ID` VARCHAR(3) NOT NULL,
	`IWANT_REGN_NM` VARCHAR(60) 	 NULL,
	`IWANT_COM_ID` VARCHAR(3) NOT NULL,
	`IWANT_REGN_TYP` CHAR(1) NOT NULL,
	CONSTRAINT `PK_ORG_IWANT_REGN` PRIMARY KEY (`IWANT_REGN_ID`)
)

;

CREATE TABLE `ORG_IWANT_OFF`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`IWANT_OFF_ID` VARCHAR(4) NOT NULL,
	`IWANT_OFF_NM` VARCHAR(60) NOT NULL,
	`IWANT_COM_ID` VARCHAR(3) NOT NULL,
	CONSTRAINT `PK_ORG_IWANT_OFF` PRIMARY KEY (`IWANT_OFF_ID`)
)

;

CREATE TABLE `ORG_IWANT_MARKET_SMALL`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`IWANT_MARKET_SMALL_ID` VARCHAR(9) NOT NULL,
	`IWANT_MARKET_SMALL_NM` VARCHAR(60) NOT NULL,
	`IWANT_MARKET_ID` VARCHAR(6) NOT NULL,
	CONSTRAINT `PK_ORG_IWANT_MARKET_SMALL` PRIMARY KEY (`IWANT_MARKET_SMALL_ID`)
)

;

CREATE TABLE `ORG_IWANT_MARKET`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`IWANT_MARKET_ID` VARCHAR(6) NOT NULL,
	`IWANT_MARKET_NM` VARCHAR(60) NOT NULL,
	`IWANT_OFF_ID` VARCHAR(4) NOT NULL,
	CONSTRAINT `PK_ORG_IWANT_MARKET` PRIMARY KEY (`IWANT_MARKET_ID`)
)

;

CREATE TABLE `ORG_IWANT_DIST`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`IWANT_DIST_ID` VARCHAR(3) NOT NULL,
	`IWANT_DIST_NM` VARCHAR(60) NOT NULL,
	CONSTRAINT `PK_ORG_IWANT_DIST` PRIMARY KEY (`IWANT_DIST_ID`)
)

;

CREATE TABLE `ORG_IWANT_COM`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`IWANT_COM_ID` VARCHAR(3) NOT NULL,
	`IWANT_COM_NM` VARCHAR(60) NOT NULL,
	`IWANT_DIST_ID` VARCHAR(3) 	 NULL,
	CONSTRAINT `PK_ORG_IWANT_COM` PRIMARY KEY (`IWANT_COM_ID`)
)

;

CREATE TABLE `ORG_IWANT_CHAN`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`IWANT_CHAN_ID` VARCHAR(4) NOT NULL,
	`IWANT_CHAN_NM` VARCHAR(60) NOT NULL,
	`IWANT_BU_ID` VARCHAR(4) 	 NULL,
	`SALES_CHAN_ID` VARCHAR(2) 	 NULL,
	`PROD_DIV_ID` VARCHAR(2) NOT NULL,
	CONSTRAINT `PK_ORG_IWANT_CHAN` PRIMARY KEY (`IWANT_CHAN_ID`)
)

;

CREATE TABLE `ORG_IWANT_BU`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`IWANT_BU_ID` VARCHAR(4) NOT NULL,
	`IWANT_BU_NM` VARCHAR(60) NOT NULL,
	CONSTRAINT `PK_ORG_IWANT_BU` PRIMARY KEY (`IWANT_BU_ID`)
)

;

CREATE TABLE `ORG_HR_OFF`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`HR_OFF_ID` VARCHAR(8) NOT NULL,
	`HR_OFF_NM` VARCHAR(60) 	 NULL,
	`HR_OFF_TYPE` CHAR(1) 	 NULL,
	CONSTRAINT `PK_ORG_HR_OFF` PRIMARY KEY (`HR_OFF_ID`)
)

;

CREATE TABLE `ORG_HR_COM`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`HR_COM_ID` VARCHAR(8) NOT NULL,
	`HR_COM_NM` VARCHAR(60) 	 NULL,
	CONSTRAINT `PK_ORG_HR_COM` PRIMARY KEY (`HR_COM_ID`)
)

;

CREATE TABLE `ORG_EMP_SALES_IWANT`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`EMP_ID` VARCHAR(8) NOT NULL,
	`IWANT_COM_ID` VARCHAR(3) NOT NULL,
	`IWANT_OFF_ID` VARCHAR(4) 	 NULL,
	`EMP_POS_PRIORITY` CHAR(1) NOT NULL,
	`EMP_POS_ID` VARCHAR(8) NOT NULL,
	`EMP_POS_TYPE` VARCHAR(3) 	 NULL,
	`ONBOARD_YMD1` CHAR(8) NOT NULL,
	CONSTRAINT `PK_ORG_EMP_SALES_IWANT` PRIMARY KEY (`EMP_ID`,`IWANT_COM_ID`,`EMP_POS_ID`)
)

;

CREATE TABLE `ORG_EMP_SALES_HR`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`EMP_ID` VARCHAR(8) NOT NULL,
	`HR_COM_ID` VARCHAR(8) NOT NULL,
	`HR_OFF_ID` VARCHAR(8) NOT NULL,
	`EMP_POS_PRIORITY` CHAR(1) NOT NULL,
	`EMP_POS_ID` VARCHAR(8) NOT NULL,
	`EMP_POS_TYPE` VARCHAR(3) NOT NULL,
	`EMP_POS_PROP_ID` VARCHAR(3) NOT NULL,
	`EMP_POS_FLAG` VARCHAR(2) 	 NULL,
	`EMP_POS_TITLE_ID` VARCHAR(8) NOT NULL,
	`EMP_POS_LEVEL_ID` VARCHAR(2) NOT NULL,
	`ONBOARD_YMD` CHAR(8) NOT NULL,
	`SENIORITY` DECIMAL(21,4) NOT NULL,
	CONSTRAINT `PK_ORG_EMP_SALES_HR` PRIMARY KEY (`EMP_ID`)
)

;

CREATE TABLE `ORG_EMP`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`EMP_ID` VARCHAR(8) NOT NULL,
	`EMP_NM` VARCHAR(60) NOT NULL,
	`EMP_GENDER` CHAR(1) 	 NULL,
	CONSTRAINT `PK_ORG_EMP` PRIMARY KEY (`EMP_ID`)
)

;

SET FOREIGN_KEY_CHECKS=1 ;
