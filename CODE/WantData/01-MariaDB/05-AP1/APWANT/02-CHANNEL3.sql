/* ---------------------------------------------------- */
/*  Generated by Enterprise Architect Version 12.0 		*/
/*  Created On : 24-�|��-2018 �W�� 09:18:16 				*/
/*  DBMS       : MySql 						*/
/* ---------------------------------------------------- */

SET FOREIGN_KEY_CHECKS=0 ;

/* Create Tables */

CREATE TABLE `CHANNEL3_PL3_INFO_SSR`
(
	`EDI_DATE` CHAR(8) NOT NULL,
	`EDI_TIME` CHAR(9) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`RPT_YM` CHAR(6) NOT NULL,
	`PROD_GROUP_ID` VARCHAR(10) NOT NULL,
	`PROD_GROUP_NM` NVARCHAR(50) NOT NULL,
	`PROD_GROUPD_ID` VARCHAR(10) NOT NULL,
	`PROD_GROUPD_NM` NVARCHAR(50) NOT NULL,
	`CHANNEL_DISTRICT8_ID` VARCHAR(4) NOT NULL,
	`CHANNEL_DISTRICT8_NM` NVARCHAR(9) NOT NULL,
	`BRANCH_ID` VARCHAR(4) NOT NULL,
	`BRANCH_NM` NVARCHAR(51) NOT NULL,
	`OFFICE_ID` VARCHAR(4) NOT NULL,
	`OFFICE_NM` NVARCHAR(36) NOT NULL,
	`STD_MARKET_ID` VARCHAR(6) NOT NULL,
	`STD_MARKET_NM` NVARCHAR(45) NOT NULL,
	`STD_MARKET_SMALL_ID` VARCHAR(10) NOT NULL,
	`STD_MARKET_SMALL_NM` NVARCHAR(46) NOT NULL,
	`PROD_LEVEL1_ID` VARCHAR(4) NOT NULL,
	`PROD_LEVEL1_NM` NVARCHAR(20) NOT NULL,
	`PROD_LEVEL3_ID` VARCHAR(9) NOT NULL,
	`PROD_LEVEL3_NM` NVARCHAR(36) NOT NULL,
	`SALES_AMT_MONTH` NUMERIC(22,6) NOT NULL,
	`REF_AMT` NUMERIC(22,6) NOT NULL,
	`REF_SALES_REACH_RATE` NUMERIC(22,6) NOT NULL,
	`SALES_ALLOW_DIST_COUNT` INT NOT NULL,
	`SALES_DIST_COUNT` INT NOT NULL,
	`NEW_DIST_COUNT` INT NOT NULL,
	`STD_MARKET_SMALL_POPU` INT NOT NULL,
	`SALES_EMP_COUNT` INT NOT NULL,
	`BACK_EMP_COUNT` INT NOT NULL,
	`TERM_COUNT` INT NOT NULL,
	CONSTRAINT `PK_CHANNEL3_PL3_INFO_SSR` PRIMARY KEY (`DATA_DATE`,`RPT_YM`,`PROD_GROUP_ID`,`PROD_GROUPD_ID`,`CHANNEL_DISTRICT8_ID`,`BRANCH_ID`,`OFFICE_ID`,`STD_MARKET_ID`,`STD_MARKET_SMALL_ID`,`PROD_LEVEL1_ID`,`PROD_LEVEL3_ID`)
)

;

CREATE TABLE `CHANNEL3_PL3_INFO_PROD`
(
	`EDI_DATE` CHAR(8) NOT NULL,
	`EDI_TIME` CHAR(9) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`RPT_YM` CHAR(6) NOT NULL,
	`PROD_GROUP_ID` VARCHAR(10) NOT NULL,
	`PROD_GROUP_NM` NVARCHAR(50) NOT NULL,
	`PROD_GROUPD_ID` VARCHAR(10) NOT NULL,
	`PROD_GROUPD_NM` NVARCHAR(50) NOT NULL,
	`PROD_LEVEL1_ID` VARCHAR(4) NOT NULL,
	`PROD_LEVEL1_NM` NVARCHAR(20) NOT NULL,
	`PROD_LEVEL3_ID` VARCHAR(9) NOT NULL,
	`PROD_LEVEL3_NM` NVARCHAR(36) NOT NULL,
	`SALES_AMT_MONTH` NUMERIC(22,6) NOT NULL,
	`REF_AMT` NUMERIC(22,6) NOT NULL,
	`REF_SALES_REACH_RATE` NUMERIC(22,6) NOT NULL,
	`FORECAST_AMT` NUMERIC(22,6) NOT NULL,
	`FORECAST_SALES_REACH_RATE` NUMERIC(22,6) NOT NULL,
	`SALES_ALLOW_DIST_COUNT` INT NOT NULL,
	`SALES_DIST_COUNT` INT NOT NULL,
	`NEW_DIST_COUNT` INT NOT NULL,
	`SALES_SSR_COUNT` INT NOT NULL,
	`SALES_DIST_SSR_COUNT` INT NOT NULL,
	`SSR_COUNT` INT NOT NULL,
	`SSR_SALES_COVERAGE` NUMERIC(22,6) NOT NULL,
	`SSR_DIST_COVERAGE` NUMERIC(22,6) NOT NULL,
	`STD_MARKET_SMALL_POPU` INT NOT NULL,
	`SALES_EMP_COUNT` INT NOT NULL,
	`BACK_EMP_COUNT` INT NOT NULL,
	`TERM_COUNT` INT NOT NULL,
	CONSTRAINT `PK_CHANNEL3_PL3_INFO_PROD` PRIMARY KEY (`DATA_DATE`,`RPT_YM`,`PROD_GROUP_ID`,`PROD_GROUPD_ID`,`PROD_LEVEL1_ID`,`PROD_LEVEL3_ID`)
)

;

CREATE TABLE `CHANNEL3_PL3_INFO_OFFICE`
(
	`EDI_DATE` CHAR(8) NOT NULL,
	`EDI_TIME` CHAR(9) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`RPT_YM` CHAR(6) NOT NULL,
	`PROD_GROUP_ID` VARCHAR(10) NOT NULL,
	`PROD_GROUP_NM` NVARCHAR(50) NOT NULL,
	`PROD_GROUPD_ID` VARCHAR(10) NOT NULL,
	`PROD_GROUPD_NM` NVARCHAR(50) NOT NULL,
	`CHANNEL_DISTRICT8_ID` VARCHAR(4) NOT NULL,
	`CHANNEL_DISTRICT8_NM` NVARCHAR(9) NOT NULL,
	`BRANCH_ID` VARCHAR(4) NOT NULL,
	`BRANCH_NM` NVARCHAR(51) NOT NULL,
	`OFFICE_ID` VARCHAR(4) NOT NULL,
	`OFFICE_NM` NVARCHAR(36) NOT NULL,
	`PROD_LEVEL1_ID` VARCHAR(4) NOT NULL,
	`PROD_LEVEL1_NM` NVARCHAR(20) NOT NULL,
	`PROD_LEVEL3_ID` VARCHAR(9) NOT NULL,
	`PROD_LEVEL3_NM` NVARCHAR(36) NOT NULL,
	`SALES_AMT_MONTH` NUMERIC(22,6) NOT NULL,
	`REF_AMT` NUMERIC(22,6) NOT NULL,
	`REF_SALES_REACH_RATE` NUMERIC(22,6) NOT NULL,
	`FORECAST_AMT` NUMERIC(22,6) NOT NULL,
	`FORECAST_SALES_REACH_RATE` NUMERIC(22,6) NOT NULL,
	`SALES_ALLOW_DIST_COUNT` INT NOT NULL,
	`SALES_DIST_COUNT` INT NOT NULL,
	`NEW_DIST_COUNT` INT NOT NULL,
	`SALES_SSR_COUNT` INT NOT NULL,
	`SALES_DIST_SSR_COUNT` INT NOT NULL,
	`SSR_COUNT` INT NOT NULL,
	`SSR_SALES_COVERAGE` NUMERIC(22,6) NOT NULL,
	`SSR_DIST_COVERAGE` NUMERIC(22,6) NOT NULL,
	`STD_MARKET_SMALL_POPU` INT NOT NULL,
	`SALES_EMP_COUNT` INT NOT NULL,
	`BACK_EMP_COUNT` INT NOT NULL,
	`TERM_COUNT` INT NOT NULL,
	CONSTRAINT `PK_CHANNEL3_PL3_INFO_OFFICE` PRIMARY KEY (`DATA_DATE`,`RPT_YM`,`PROD_GROUP_ID`,`PROD_GROUPD_ID`,`CHANNEL_DISTRICT8_ID`,`BRANCH_ID`,`OFFICE_ID`,`PROD_LEVEL1_ID`,`PROD_LEVEL3_ID`)
)

;

CREATE TABLE `CHANNEL3_PL3_INFO_BRANCH`
(
	`EDI_DATE` CHAR(8) NOT NULL,
	`EDI_TIME` CHAR(9) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`RPT_YM` CHAR(6) NOT NULL,
	`PROD_GROUP_ID` VARCHAR(10) NOT NULL,
	`PROD_GROUP_NM` NVARCHAR(50) NOT NULL,
	`PROD_GROUPD_ID` VARCHAR(10) NOT NULL,
	`PROD_GROUPD_NM` NVARCHAR(50) NOT NULL,
	`CHANNEL_DISTRICT8_ID` VARCHAR(4) NOT NULL,
	`CHANNEL_DISTRICT8_NM` NVARCHAR(9) NOT NULL,
	`BRANCH_ID` VARCHAR(4) NOT NULL,
	`BRANCH_NM` NVARCHAR(51) NOT NULL,
	`PROD_LEVEL1_ID` VARCHAR(4) NOT NULL,
	`PROD_LEVEL1_NM` NVARCHAR(20) NOT NULL,
	`PROD_LEVEL3_ID` VARCHAR(9) NOT NULL,
	`PROD_LEVEL3_NM` NVARCHAR(36) NOT NULL,
	`SALES_AMT_MONTH` NUMERIC(22,6) NOT NULL,
	`REF_AMT` NUMERIC(22,6) NOT NULL,
	`REF_SALES_REACH_RATE` NUMERIC(22,6) NOT NULL,
	`FORECAST_AMT` NUMERIC(22,6) NOT NULL,
	`FORECAST_SALES_REACH_RATE` NUMERIC(22,6) NOT NULL,
	`SALES_ALLOW_DIST_COUNT` INT NOT NULL,
	`SALES_DIST_COUNT` INT NOT NULL,
	`NEW_DIST_COUNT` INT NOT NULL,
	`SALES_SSR_COUNT` INT NOT NULL,
	`SALES_DIST_SSR_COUNT` INT NOT NULL,
	`SSR_COUNT` INT NOT NULL,
	`SSR_SALES_COVERAGE` NUMERIC(22,6) NOT NULL,
	`SSR_DIST_COVERAGE` NUMERIC(22,6) NOT NULL,
	`STD_MARKET_SMALL_POPU` INT NOT NULL,
	`SALES_EMP_COUNT` INT NOT NULL,
	`BACK_EMP_COUNT` INT NOT NULL,
	`TERM_COUNT` INT NOT NULL,
	CONSTRAINT `PK_CHANNEL3_PL3_INFO_BRANCH` PRIMARY KEY (`DATA_DATE`,`RPT_YM`,`PROD_GROUP_ID`,`PROD_GROUPD_ID`,`CHANNEL_DISTRICT8_ID`,`BRANCH_ID`,`PROD_LEVEL1_ID`,`PROD_LEVEL3_ID`)
)

;

CREATE TABLE `CHANNEL3_DIST_SALES_SSR`
(
	`EDI_DATE` CHAR(8) NOT NULL,
	`EDI_TIME` CHAR(9) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`RPT_YM` CHAR(10) NOT NULL,
	`SALES_YM` CHAR(6) NOT NULL,
	`PROD_GROUP_ID` VARCHAR(10) NOT NULL,
	`PROD_GROUP_NM` NVARCHAR(50) NOT NULL,
	`PROD_GROUPD_ID` VARCHAR(10) NOT NULL,
	`PROD_GROUPD_NM` NVARCHAR(50) NOT NULL,
	`CHANNEL_DISTRICT8_ID` VARCHAR(4) NOT NULL,
	`CHANNEL_DISTRICT8_NM` NVARCHAR(9) NOT NULL,
	`BRANCH_ID` VARCHAR(4) NOT NULL,
	`BRANCH_NM` NVARCHAR(51) NOT NULL,
	`OFFICE_ID` VARCHAR(4) NOT NULL,
	`OFFICE_NM` NVARCHAR(36) NOT NULL,
	`STD_MARKET_ID` VARCHAR(6) NOT NULL,
	`STD_MARKET_NM` NVARCHAR(45) NOT NULL,
	`STD_MARKET_SMALL_ID` VARCHAR(10) NOT NULL,
	`STD_MARKET_SMALL_NM` NVARCHAR(46) NOT NULL,
	`PROD_LEVEL1_ID` VARCHAR(4) NOT NULL,
	`PROD_LEVEL1_NM` NVARCHAR(20) NOT NULL,
	`PROD_LEVEL3_ID` VARCHAR(9) NOT NULL,
	`PROD_LEVEL3_NM` NVARCHAR(36) NOT NULL,
	`DIST_ID` VARCHAR(10) NOT NULL,
	`DIST_NM` NVARCHAR(90) NOT NULL,
	`SALES_AMT_MONTH` NUMERIC(22,6) NOT NULL,
	`SALES_AMT_MONTH_EXCLRET` NUMERIC(22,6) NOT NULL,
	`EMP_ID` VARCHAR(8) NOT NULL,
	`EMP_NM` NVARCHAR(20) NOT NULL,
	CONSTRAINT `PK_CHANNEL3_DIST_SALES_SSR` PRIMARY KEY (`DATA_DATE`,`RPT_YM`,`SALES_YM`,`PROD_GROUP_ID`,`PROD_GROUPD_ID`,`CHANNEL_DISTRICT8_ID`,`BRANCH_ID`,`OFFICE_ID`,`STD_MARKET_ID`,`STD_MARKET_SMALL_ID`,`PROD_LEVEL1_ID`,`PROD_LEVEL3_ID`,`DIST_ID`)
)

;

CREATE TABLE `CHANNEL3_DIST_INFO_SSR`
(
	`EDI_DATE` CHAR(8) NOT NULL,
	`EDI_TIME` CHAR(9) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`RPT_YM` CHAR(10) NOT NULL,
	`PROD_GROUP_ID` VARCHAR(10) NOT NULL,
	`PROD_GROUP_NM` NVARCHAR(50) NOT NULL,
	`PROD_GROUPD_ID` VARCHAR(10) NOT NULL,
	`PROD_GROUPD_NM` NVARCHAR(50) NOT NULL,
	`CHANNEL_DISTRICT8_ID` VARCHAR(4) NOT NULL,
	`CHANNEL_DISTRICT8_NM` NVARCHAR(9) NOT NULL,
	`BRANCH_ID` VARCHAR(4) NOT NULL,
	`BRANCH_NM` NVARCHAR(51) NOT NULL,
	`OFFICE_ID` VARCHAR(4) NOT NULL,
	`OFFICE_NM` NVARCHAR(36) NOT NULL,
	`STD_MARKET_ID` VARCHAR(6) NOT NULL,
	`STD_MARKET_NM` NVARCHAR(45) NOT NULL,
	`STD_MARKET_SMALL_ID` VARCHAR(10) NOT NULL,
	`STD_MARKET_SMALL_NM` NVARCHAR(46) NOT NULL,
	`PROD_LEVEL1_ID` VARCHAR(4) NOT NULL,
	`PROD_LEVEL1_NM` NVARCHAR(20) NOT NULL,
	`PROD_LEVEL3_ID` VARCHAR(9) NOT NULL,
	`PROD_LEVEL3_NM` NVARCHAR(36) NOT NULL,
	`DIST_ID` VARCHAR(10) NOT NULL,
	`DIST_NM` NVARCHAR(90) NOT NULL,
	`SALES_AMT_MONTH` NUMERIC(22,6) NOT NULL,
	`IS_SALES_DIST` CHAR(1) NOT NULL,
	`IS_NEW_DIST` CHAR(1) NOT NULL,
	`EMP_ID` VARCHAR(8) NOT NULL,
	`EMP_NM` NVARCHAR(20) NOT NULL,
	CONSTRAINT `PK_CHANNEL3_DIST_INFO_SSR` PRIMARY KEY (`DATA_DATE`,`RPT_YM`,`PROD_GROUP_ID`,`PROD_GROUPD_ID`,`CHANNEL_DISTRICT8_ID`,`BRANCH_ID`,`OFFICE_ID`,`STD_MARKET_ID`,`STD_MARKET_SMALL_ID`,`PROD_LEVEL1_ID`,`PROD_LEVEL3_ID`,`DIST_ID`)
)

;

CREATE TABLE `CHANNEL3_DIST_INFO_OFFICE`
(
	`EDI_DATE` CHAR(8) NOT NULL,
	`EDI_TIME` CHAR(9) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`RPT_YM` CHAR(10) NOT NULL,
	`PROD_GROUP_ID` VARCHAR(10) NOT NULL,
	`PROD_GROUP_NM` NVARCHAR(50) NOT NULL,
	`PROD_GROUPD_ID` VARCHAR(10) NOT NULL,
	`PROD_GROUPD_NM` NVARCHAR(50) NOT NULL,
	`CHANNEL_DISTRICT8_ID` VARCHAR(4) NOT NULL,
	`CHANNEL_DISTRICT8_NM` NVARCHAR(9) NOT NULL,
	`BRANCH_ID` VARCHAR(4) NOT NULL,
	`BRANCH_NM` NVARCHAR(51) NOT NULL,
	`OFFICE_ID` VARCHAR(4) NOT NULL,
	`OFFICE_NM` NVARCHAR(36) NOT NULL,
	`PROD_LEVEL1_ID` VARCHAR(4) NOT NULL,
	`PROD_LEVEL1_NM` NVARCHAR(20) NOT NULL,
	`PROD_LEVEL3_ID` VARCHAR(9) NOT NULL,
	`PROD_LEVEL3_NM` NVARCHAR(36) NOT NULL,
	`DIST_ID` VARCHAR(10) NOT NULL,
	`DIST_NM` NVARCHAR(90) NOT NULL,
	`SALES_AMT_MONTH` NUMERIC(22,6) NOT NULL,
	`IS_SALES_DIST` CHAR(1) NOT NULL,
	`IS_NEW_DIST` CHAR(1) NOT NULL,
	`EMP_ID` VARCHAR(8) NOT NULL,
	`EMP_NM` NVARCHAR(20) NOT NULL,
	CONSTRAINT `PK_CHANNEL3_DIST_INFO_OFFICE` PRIMARY KEY (`DATA_DATE`,`RPT_YM`,`PROD_GROUP_ID`,`PROD_GROUPD_ID`,`CHANNEL_DISTRICT8_ID`,`BRANCH_ID`,`OFFICE_ID`,`PROD_LEVEL1_ID`,`PROD_LEVEL3_ID`,`DIST_ID`)
)

;

SET FOREIGN_KEY_CHECKS=1 ;
