/* ---------------------------------------------------- */
/*  Generated by Enterprise Architect Version 12.0 		*/
/*  Created On : 24-�|��-2018 �W�� 10:01:15 				*/
/*  DBMS       : MySql 						*/
/* ---------------------------------------------------- */

SET FOREIGN_KEY_CHECKS=0 ;

/* Create Tables */

CREATE TABLE `EMP3_TERM_STATUS_OFFICE`
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
	`EMP_ALMIGHTY_COUNT` INT NOT NULL,
	`EMP_IMPROVE_SERVICE_COUNT` INT NOT NULL,
	`EMP_IMPROVE_PROD_COUNT` INT NOT NULL,
	`EMP_IMPROVE_SALES_COUNT` INT NOT NULL,
	`EMP_WARNING_COUNT` INT NOT NULL,
	`EMP_COUNT` INT NOT NULL,
	`LAST_MONTH_EMP_ALMIGHTY_COUNT` INT NOT NULL,
	`LAST_MONTH_EMP_IMPROVE_SERVICE_COUNT` INT NOT NULL,
	`LAST_MONTH_EMP_IMPROVE_PROD_COUNT` INT NOT NULL,
	`LAST_MONTH_EMP_IMPROVE_SALES_COUNT` INT NOT NULL,
	`LAST_MONTH_EMP_WARNING_COUNT` INT NOT NULL,
	`LAST_MONTH_EMP_COUNT` INT NOT NULL,
	`DIFF_EMP_ALMIGHTY_COUNT` INT NOT NULL,
	`DIFF_EMP_IMPROVE_SERVICE_COUNT` INT NOT NULL,
	`DIFF_EMP_IMPROVE_PROD_COUNT` INT NOT NULL,
	`DIFF_EMP_IMPROVE_SALES_COUNT` INT NOT NULL,
	`DIFF_EMP_WARNING_COUNT` INT NOT NULL,
	CONSTRAINT `PK_EMP3_TERM_STATUS_OFFICE` PRIMARY KEY (`DATA_DATE`,`RPT_YM`,`PROD_GROUP_ID`,`PROD_GROUPD_ID`,`CHANNEL_DISTRICT8_ID`,`BRANCH_ID`,`OFFICE_ID`)
)

;

CREATE TABLE `EMP3_TERM_STATUS_DISTRICT8`
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
	`MAX_DISTRICT8_BACK_AMT` NUMERIC(22,6) NOT NULL,
	`MAX_DISTRICT8_PROD_LEVEL3_COUNT` INT NOT NULL,
	`DISTRICT8_BACK_AMT_RATIO` NUMERIC(22,6) NOT NULL,
	`DISTRICT8_TERM_STABLE_RATIO` NUMERIC(22,6) NOT NULL,
	`DISTRICT8_PROD_LEVEL3_RATIO` NUMERIC(22,6) NOT NULL,
	CONSTRAINT `PK_EMP3_TERM_STATUS_DISTRICT8` PRIMARY KEY (`DATA_DATE`,`RPT_YM`,`PROD_GROUP_ID`,`PROD_GROUPD_ID`,`CHANNEL_DISTRICT8_ID`)
)

;

CREATE TABLE `EMP3_TERM_STATUS`
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
	`EMP_ID` VARCHAR(8) NOT NULL,
	`EMP_NM` NVARCHAR(20) NOT NULL,
	`EMP_JOB_ID` VARCHAR(10) NOT NULL,
	`EMP_JOB_NM` NVARCHAR(150) NOT NULL,
	`EMP_ATTR_ID` VARCHAR(10) NOT NULL,
	`EMP_ATTR_NM` NVARCHAR(150) NOT NULL,
	`EMP_POST_ID` VARCHAR(10) NOT NULL,
	`EMP_POST_NM` NVARCHAR(150) NOT NULL,
	`TOTAL_BACK_AMT` NUMERIC(22,6) NOT NULL,
	`MAX_DISTRICT8_BACK_AMT` NUMERIC(22,6) NOT NULL,
	`BACK_AMT_RATIO` NUMERIC(22,6) NOT NULL,
	`DISTRICT8_BACK_AMT_RATIO` NUMERIC(22,6) NOT NULL,
	`IS_HIGH_DISTRICT8_BACK_AMT_RATIO` CHAR(1) NOT NULL,
	`TWO_MONTH_TERM_COUNT` INT NOT NULL,
	`LAST_MONTH_TERM_COUNT` INT NOT NULL,
	`TERM_STABLE_RATIO` NUMERIC(22,6) NOT NULL,
	`DISTRICT8_TERM_STABLE_RATIO` NUMERIC(22,6) NOT NULL,
	`IS_HIGH_DISTRICT8_TERM_STABLE_RATIO` CHAR(1) NOT NULL,
	`PROD_LEVEL3_COUNT` INT NOT NULL,
	`MAX_DISTRICT8_PROD_LEVEL3_COUNT` INT NOT NULL,
	`PROD_LEVEL3_RATIO` NUMERIC(22,6) NOT NULL,
	`DISTRICT8_PROD_LEVEL3_RATIO` NUMERIC(22,6) NOT NULL,
	`IS_HIGH_DISTRICT8_PROD_LEVEL3_RATIO` CHAR(1) NOT NULL,
	`EMP_TERM_TYPE_ID` VARCHAR(10) NOT NULL,
	`EMP_TERM_TYPE_NM` NVARCHAR(15) NOT NULL,
	CONSTRAINT `PK_EMP3_TERM_STATUS` PRIMARY KEY (`DATA_DATE`,`RPT_YM`,`PROD_GROUP_ID`,`PROD_GROUPD_ID`,`CHANNEL_DISTRICT8_ID`,`BRANCH_ID`,`OFFICE_ID`,`EMP_ID`)
)

;

CREATE TABLE `EMP3_LIST`
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
	`EMP_ID` VARCHAR(8) NOT NULL,
	`EMP_NM` NVARCHAR(20) NOT NULL,
	`EMP_JOB_ID` VARCHAR(10) NOT NULL,
	`EMP_JOB_NM` NVARCHAR(150) NOT NULL,
	`EMP_ATTR_ID` VARCHAR(10) NOT NULL,
	`EMP_ATTR_NM` NVARCHAR(150) NOT NULL,
	`EMP_POST_ID` VARCHAR(10) NOT NULL,
	`EMP_POST_NM` NVARCHAR(150) NOT NULL,
	`EMP_PERFORMANCE` VARCHAR(4) NOT NULL,
	CONSTRAINT `PK_EMP3_LIST` PRIMARY KEY (`DATA_DATE`,`RPT_YM`,`PROD_GROUP_ID`,`PROD_GROUPD_ID`,`CHANNEL_DISTRICT8_ID`,`BRANCH_ID`,`OFFICE_ID`,`EMP_ID`,`EMP_PERFORMANCE`)
)

;

CREATE TABLE `EMP3_DIST_STOCK`
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
	`DIST_ID` VARCHAR(10) NOT NULL,
	`DIST_NM` NVARCHAR(90) NOT NULL,
	`STOCK_AMT` NUMERIC(22,8) NOT NULL,
	`AVG_SALES_AMT_M3` NUMERIC(22,6) NOT NULL,
	`INVENTORY_TURNOVER_DAYS` INT NOT NULL,
	CONSTRAINT `PK_EMP3_DIST_STOCK` PRIMARY KEY (`DATA_DATE`,`RPT_YM`,`PROD_GROUP_ID`,`PROD_GROUPD_ID`,`CHANNEL_DISTRICT8_ID`,`BRANCH_ID`,`OFFICE_ID`,`DIST_ID`)
)

;

CREATE TABLE `EMP3_DIST_STATUS_OFFICE`
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
	`EMP_ALMIGHTY_COUNT` INT NOT NULL,
	`EMP_IMPROVE_STOCK_COUNT` INT NOT NULL,
	`EMP_IMPROVE_PROD_COUNT` INT NOT NULL,
	`EMP_IMPROVE_SALES_COUNT` INT NOT NULL,
	`EMP_WARNING_COUNT` INT NOT NULL,
	`EMP_COUNT` INT NOT NULL,
	`LAST_MONTH_EMP_ALMIGHTY_COUNT` INT NOT NULL,
	`LAST_MONTH_EMP_IMPROVE_STOCK_COUNT` INT NOT NULL,
	`LAST_MONTH_EMP_IMPROVE_PROD_COUNT` INT NOT NULL,
	`LAST_MONTH_EMP_IMPROVE_SALES_COUNT` INT NOT NULL,
	`LAST_MONTH_EMP_WARNING_COUNT` INT NOT NULL,
	`LAST_MONTH_EMP_COUNT` INT NOT NULL,
	`DIFF_EMP_ALMIGHTY_COUNT` INT NOT NULL,
	`DIFF_EMP_IMPROVE_STOCK_COUNT` INT NOT NULL,
	`DIFF_EMP_IMPROVE_PROD_COUNT` INT NOT NULL,
	`DIFF_EMP_IMPROVE_SALES_COUNT` INT NOT NULL,
	`DIFF_EMP_WARNING_COUNT` INT NOT NULL,
	CONSTRAINT `PK_EMP3_DIST_STATUS_OFFICE` PRIMARY KEY (`DATA_DATE`,`RPT_YM`,`PROD_GROUP_ID`,`PROD_GROUPD_ID`,`CHANNEL_DISTRICT8_ID`,`BRANCH_ID`,`OFFICE_ID`)
)

;

CREATE TABLE `EMP3_DIST_STATUS_DISTRICT8`
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
	`DISTRICT8_SALES_MARKET_CONTRIBUTION` NUMERIC(22,6) NOT NULL,
	`DISTRICT8_ALLOW_PL3_RATIO` NUMERIC(22,6) NOT NULL,
	`DISTRICT8_STOCK_PERFORMANCE` NUMERIC(22,6) NOT NULL,
	CONSTRAINT `PK_EMP3_DIST_STATUS_DISTRICT8` PRIMARY KEY (`DATA_DATE`,`RPT_YM`,`PROD_GROUP_ID`,`PROD_GROUPD_ID`,`CHANNEL_DISTRICT8_ID`)
)

;

CREATE TABLE `EMP3_DIST_STATUS`
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
	`EMP_ID` VARCHAR(8) NOT NULL,
	`EMP_NM` NVARCHAR(20) NOT NULL,
	`EMP_JOB_ID` VARCHAR(10) NOT NULL,
	`EMP_JOB_NM` NVARCHAR(150) NOT NULL,
	`EMP_ATTR_ID` VARCHAR(10) NOT NULL,
	`EMP_ATTR_NM` NVARCHAR(150) NOT NULL,
	`EMP_POST_ID` VARCHAR(10) NOT NULL,
	`EMP_POST_NM` NVARCHAR(150) NOT NULL,
	`SALES_AMT` NUMERIC(22,6) NOT NULL,
	`MARKET_CONTRIBUTION` NUMERIC(22,6) NOT NULL,
	`SALES_MARKET_CONTRIBUTION` NUMERIC(22,6) NOT NULL,
	`DISTRICT8_SALES_MARKET_CONTRIBUTION` NUMERIC(22,6) NOT NULL,
	`IS_HIGH_DISTRICT8_SALES_MARKET_CONTRIBUTION` CHAR(1) NOT NULL,
	`SALES_ALLOW_PL3_COUNT` INT NOT NULL,
	`ALLOW_PL3_COUNT` INT NOT NULL,
	`ALLOW_PL3_RATIO` NUMERIC(22,6) NOT NULL,
	`DISTRICT8_ALLOW_PL3_RATIO` NUMERIC(22,6) NOT NULL,
	`IS_HIGH_DISTRICT8_ALLOW_PL3_RATIO` CHAR(1) NOT NULL,
	`DIST_INVENTORY_TURNOVER_DAYS` INT NOT NULL,
	`STOCK_DIST_COUNT` INT NOT NULL,
	`INVENTORY_TURNOVER_DAYS` INT NOT NULL,
	`DISTRICT8_DIST_INVENTORY_TURNOVER_DAYS` INT NOT NULL,
	`STOCK_PERFORMANCE` NUMERIC(22,6) NOT NULL,
	`DISTRICT8_STOCK_PERFORMANCE` NUMERIC(22,6) NOT NULL,
	`IS_HIGH_DISTRICT8_STOCK_PERFORMANCE` CHAR(1) NOT NULL,
	`EMP_DIST_TYPE_ID` VARCHAR(10) NOT NULL,
	`EMP_DIST_TYPE_NM` NVARCHAR(15) NOT NULL,
	CONSTRAINT `PK_EMP3_DIST_STATUS` PRIMARY KEY (`DATA_DATE`,`RPT_YM`,`PROD_GROUP_ID`,`PROD_GROUPD_ID`,`CHANNEL_DISTRICT8_ID`,`BRANCH_ID`,`OFFICE_ID`,`EMP_ID`)
)

;

CREATE TABLE `EMP3_DIST_DETAIL`
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
	`EMP_ID` VARCHAR(8) NOT NULL,
	`EMP_NM` NVARCHAR(20) NOT NULL,
	`EMP_JOB_ID` VARCHAR(10) NOT NULL,
	`EMP_JOB_NM` NVARCHAR(150) NOT NULL,
	`EMP_ATTR_ID` VARCHAR(10) NOT NULL,
	`EMP_ATTR_NM` NVARCHAR(150) NOT NULL,
	`EMP_POST_ID` VARCHAR(10) NOT NULL,
	`EMP_POST_NM` NVARCHAR(150) NOT NULL,
	`DIST_ID` VARCHAR(10) NOT NULL,
	`DIST_NM` NVARCHAR(90) NOT NULL,
	`SALES_AMT` NUMERIC(22,6) NOT NULL,
	`SALES_ALLOW_PL3_COUNT` INT NOT NULL,
	`ALLOW_PL3_COUNT` INT NOT NULL,
	`STOCK_AMT` NUMERIC(22,8) NOT NULL,
	`AVG_SALES_AMT_M3` NUMERIC(22,6) NOT NULL,
	`INVENTORY_TURNOVER_DAYS` INT NOT NULL,
	CONSTRAINT `PK_EMP3_DIST_DETAIL` PRIMARY KEY (`DATA_DATE`,`RPT_YM`,`PROD_GROUP_ID`,`PROD_GROUPD_ID`,`CHANNEL_DISTRICT8_ID`,`BRANCH_ID`,`OFFICE_ID`,`EMP_ID`,`DIST_ID`)
)

;

SET FOREIGN_KEY_CHECKS=1 ;
