/* ---------------------------------------------------- */
/*  Generated by Enterprise Architect Version 12.0 		*/
/*  Created On : 24-�|��-2018 �W�� 10:54:37 				*/
/*  DBMS       : MySql 						*/
/* ---------------------------------------------------- */

SET FOREIGN_KEY_CHECKS=0 ;

/* Create Tables */

CREATE TABLE `SRC_PROD_SKU`
(
	`EDI_DATE` CHAR(8) NOT NULL,
	`EDI_TIME` CHAR(9) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`PROD_SKU_ID` VARCHAR(18) NOT NULL,
	`PROD_SKU_NM` NVARCHAR(88) NOT NULL,
	`PROD_PORTFOLIO_ID` VARCHAR(4) NOT NULL,
	`PROD_PORTFOLIO_NM` NVARCHAR(36) NOT NULL,
	`PROD_LEVEL1_ID` VARCHAR(4) NOT NULL,
	`PROD_LEVEL1_NM` NVARCHAR(20) NOT NULL,
	`PROD_LEVEL2_ID` VARCHAR(6) NOT NULL,
	`PROD_LEVEL2_NM` NVARCHAR(23) NOT NULL,
	`PROD_LEVEL3_ID` VARCHAR(9) NOT NULL,
	`PROD_LEVEL3_NM` NVARCHAR(36) NOT NULL,
	`PROD_LEVEL4_ID` VARCHAR(12) NOT NULL,
	`PROD_LEVEL4_NM` NVARCHAR(53) NOT NULL,
	`PROD_LEVEL5_ID` VARCHAR(15) NOT NULL,
	`PROD_LEVEL5_NM` NVARCHAR(63) NOT NULL,
	`PROD_NP_ID` VARCHAR(10) NOT NULL,
	`PROD_NP_NM` NVARCHAR(15) NOT NULL,
	CONSTRAINT `PK_SRC_PROD_SKU` PRIMARY KEY (`DATA_DATE`,`PROD_SKU_ID`)
)

;

CREATE TABLE `SRC_PROD`
(
	`PROD_LEVEL1_ID` VARCHAR(4) NOT NULL,
	`PROD_LEVEL3_ID` VARCHAR(9) NOT NULL,
	`UPD_USER_ID` VARCHAR(8) NOT NULL,
	`UPD_DT` DATETIME(0) NOT NULL,
	CONSTRAINT `PK_SRC_PROD` PRIMARY KEY (`PROD_LEVEL3_ID`)
)

;

CREATE TABLE `SRC_ORG_REL`
(
	`EDI_DATE` CHAR(8) NOT NULL,
	`EDI_TIME` CHAR(9) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`CHANNEL_GROUP_ID` VARCHAR(10) NOT NULL,
	`CHANNEL_GROUP_NM` NVARCHAR(21) NOT NULL,
	`CHANNEL_DISTRICT_ID` VARCHAR(4) NOT NULL,
	`CHANNEL_DISTRICT_NM` NVARCHAR(12) NOT NULL,
	`CHANNEL_DISTRICT8_ID` VARCHAR(4) NOT NULL,
	`CHANNEL_DISTRICT8_NM` NVARCHAR(9) NOT NULL,
	`DISTRICT_ID` VARCHAR(4) NOT NULL,
	`DISTRICT_NM` NVARCHAR(12) NOT NULL,
	`BRANCH_ID` VARCHAR(4) NOT NULL,
	`BRANCH_NM` NVARCHAR(51) NOT NULL,
	`AREA_ID` VARCHAR(4) NOT NULL,
	`AREA_NM` NVARCHAR(13) NOT NULL,
	`OFFICE_TYPE` VARCHAR(10) NOT NULL,
	`OFFICE_TYPE_NM` NVARCHAR(21) NOT NULL,
	`OFFICE_ID` VARCHAR(4) NOT NULL,
	`OFFICE_NM` NVARCHAR(36) NOT NULL,
	`STD_MARKET_ID` VARCHAR(6) NOT NULL,
	`STD_MARKET_NM` NVARCHAR(45) NOT NULL,
	`STD_MARKET_SMALL_ID` VARCHAR(10) NOT NULL,
	`STD_MARKET_SMALL_NM` NVARCHAR(46) NOT NULL,
	`SSR_MARKET_SHARE_RATE` NUMERIC(22,10) NOT NULL,
	`STD_MARKET_SMALL_POPU` INT NOT NULL,
	`SORT_ORDER` VARCHAR(25) NOT NULL,
	CONSTRAINT `PK_SRC_ORG_REL` PRIMARY KEY (`DATA_DATE`,`DISTRICT_ID`,`BRANCH_ID`,`AREA_ID`,`OFFICE_ID`,`STD_MARKET_ID`,`STD_MARKET_SMALL_ID`)
)

;

CREATE TABLE `SRC_ORG_REGION_BRANCH`
(
	`EDI_DATE` CHAR(8) NOT NULL,
	`EDI_TIME` CHAR(9) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`REGION_ID` VARCHAR(4) NOT NULL,
	`REGION_NM` NVARCHAR(24) NOT NULL,
	`BRANCH_ID` VARCHAR(4) NOT NULL,
	`BRANCH_NM` NVARCHAR(51) NOT NULL,
	`SORT_ORDER` VARCHAR(3) NOT NULL,
	CONSTRAINT `PK_SRC_ORG_REGION_BRANCH` PRIMARY KEY (`DATA_DATE`,`BRANCH_ID`)
)

;

CREATE TABLE `SRC_ORG_PROD`
(
	`EDI_DATE` CHAR(8) NOT NULL,
	`EDI_TIME` CHAR(9) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`PROD_GROUP_ID` VARCHAR(10) NOT NULL,
	`PROD_GROUP_NM` NVARCHAR(50) NOT NULL,
	`PROD_GROUPD_ID` VARCHAR(10) NOT NULL,
	`PROD_GROUPD_NM` NVARCHAR(50) NOT NULL,
	`PROD_LEVEL1_ID` VARCHAR(4) NOT NULL,
	`PROD_LEVEL1_NM` NVARCHAR(20) NOT NULL,
	`PROD_LEVEL3_ID` VARCHAR(9) NOT NULL,
	`PROD_LEVEL3_NM` NVARCHAR(36) NOT NULL,
	`PROD_PORTFOLIO_ID` VARCHAR(4) NOT NULL,
	`PROD_PORTFOLIO_NM` NVARCHAR(36) NOT NULL,
	`OFFICE_ID` VARCHAR(4) NOT NULL,
	`OFFICE_NM` NVARCHAR(36) NOT NULL,
	`SORT_ORDER` VARCHAR(15) NOT NULL,
	CONSTRAINT `PK_SRC_ORG_PROD` PRIMARY KEY (`DATA_DATE`,`PROD_LEVEL3_ID`,`OFFICE_ID`)
)

;

CREATE TABLE `SRC_CHANNEL`
(
	`PROD_GROUP_ID` VARCHAR(10) NOT NULL,
	`PROD_GROUPD_ID` VARCHAR(10) NOT NULL,
	`CHANNEL_DISTRICT8_ID` VARCHAR(4) NOT NULL,
	`BRANCH_ID` VARCHAR(4) NOT NULL,
	`OFFICE_ID` VARCHAR(4) NOT NULL,
	`UPD_USER_ID` VARCHAR(8) NOT NULL,
	`UPD_DT` DATETIME(0) NOT NULL,
	CONSTRAINT `PK_SRC_CHANNEL` PRIMARY KEY (`PROD_GROUP_ID`,`OFFICE_ID`,`PROD_GROUPD_ID`)
)

;

SET FOREIGN_KEY_CHECKS=1 ;