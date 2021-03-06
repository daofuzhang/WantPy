/* ---------------------------------------------------- */
/*  Generated by Enterprise Architect Version 12.0 		*/
/*  Created On : 13-�|��-2018 �W�� 10:04:12 				*/
/*  DBMS       : MySql 						*/
/* ---------------------------------------------------- */

SET FOREIGN_KEY_CHECKS=0 ;

/* Create Tables */

CREATE TABLE `DIST2_STOCK`
(
	`EDI_DATE` CHAR(8) NOT NULL,
	`EDI_TIME` CHAR(9) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`RPT_YM` CHAR(6) NOT NULL,
	`CHANNEL_GROUP_ID` VARCHAR(10) NOT NULL,
	`CHANNEL_GROUP_NM` NVARCHAR(21) NOT NULL,
	`CHANNEL_DISTRICT_ID` VARCHAR(4) NOT NULL,
	`CHANNEL_DISTRICT_NM` NVARCHAR(12) NOT NULL,
	`BRANCH_ID` VARCHAR(4) NOT NULL,
	`BRANCH_NM` NVARCHAR(51) NOT NULL,
	`OFFICE_ID` VARCHAR(4) NOT NULL,
	`OFFICE_NM` NVARCHAR(36) NOT NULL,
	`DIST_ID` VARCHAR(10) NOT NULL,
	`DIST_NM` NVARCHAR(90) NOT NULL,
	`STOCK_AMT` NUMERIC(22,8) NOT NULL,
	`SALES_AMT_90DAYS` NUMERIC(22,6) NOT NULL,
	`INVENTORY_TURNOVER_DAYS` INT NOT NULL,
	`STOCK_ABNORMAL_AMT` NUMERIC(22,8) NOT NULL,
	`STOCK_ABNORMAL_RATE` NUMERIC(22,8) NOT NULL,
	`SALES_AMT_MONTH` NUMERIC(22,6) NOT NULL,
	`STOCK_SALES_RATE` NUMERIC(22,6) NOT NULL,
	CONSTRAINT `PK_DIST2_STOCK` PRIMARY KEY (`DATA_DATE`,`RPT_YM`,`CHANNEL_GROUP_ID`,`CHANNEL_DISTRICT_ID`,`BRANCH_ID`,`OFFICE_ID`,`DIST_ID`)
)

;

CREATE TABLE `DIST2_STATUS`
(
	`EDI_DATE` CHAR(8) NOT NULL,
	`EDI_TIME` CHAR(9) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`RPT_YM` CHAR(6) NOT NULL,
	`CHANNEL_GROUP_ID` VARCHAR(10) NOT NULL,
	`CHANNEL_GROUP_NM` NVARCHAR(21) NOT NULL,
	`CHANNEL_DISTRICT_ID` VARCHAR(4) NOT NULL,
	`CHANNEL_DISTRICT_NM` NVARCHAR(12) NOT NULL,
	`BRANCH_ID` VARCHAR(4) NOT NULL,
	`BRANCH_NM` NVARCHAR(51) NOT NULL,
	`OFFICE_ID` VARCHAR(4) NOT NULL,
	`OFFICE_NM` NVARCHAR(36) NOT NULL,
	`DIST_ID` VARCHAR(10) NOT NULL,
	`DIST_NM` NVARCHAR(90) NOT NULL,
	`DIST_STATUS_ID` VARCHAR(10) NOT NULL,
	`DIST_STATUS_NM` NVARCHAR(50) NOT NULL,
	`SALES_AMT_MONTH` NUMERIC(22,6) NOT NULL,
	`SALES_AMT_PAST_MONTH` NUMERIC(22,6) NOT NULL,
	`SALES_AMT_GROWTH_RATE` NUMERIC(22,6) NOT NULL,
	`IS_CURRENT_MONTH_DEAL` CHAR(1) NOT NULL,
	CONSTRAINT `PK_DIST2_STATUS` PRIMARY KEY (`DATA_DATE`,`RPT_YM`,`CHANNEL_GROUP_ID`,`CHANNEL_DISTRICT_ID`,`BRANCH_ID`,`OFFICE_ID`,`DIST_ID`)
)

;

CREATE TABLE `DIST2_SCORES`
(
	`EDI_DATE` CHAR(8) NOT NULL,
	`EDI_TIME` CHAR(9) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`RPT_YM` CHAR(6) NOT NULL,
	`CHANNEL_GROUP_ID` VARCHAR(10) NOT NULL,
	`CHANNEL_GROUP_NM` NVARCHAR(21) NOT NULL,
	`CHANNEL_DISTRICT_ID` VARCHAR(4) NOT NULL,
	`CHANNEL_DISTRICT_NM` NVARCHAR(12) NOT NULL,
	`BRANCH_ID` VARCHAR(4) NOT NULL,
	`BRANCH_NM` NVARCHAR(51) NOT NULL,
	`OFFICE_ID` VARCHAR(4) NOT NULL,
	`OFFICE_NM` NVARCHAR(36) NOT NULL,
	`DIST_ID` VARCHAR(10) NOT NULL,
	`DIST_NM` NVARCHAR(90) NOT NULL,
	`SALES_AMT_MONTH` NUMERIC(22,6) NOT NULL,
	`SALES_AMT_MONTH_MAX` NUMERIC(22,6) NOT NULL,
	`SALES_AMT_MONTH_SCORES` NUMERIC(22,6) NOT NULL,
	CONSTRAINT `PK_DIST2_SCORES` PRIMARY KEY (`DATA_DATE`,`RPT_YM`,`CHANNEL_GROUP_ID`,`CHANNEL_DISTRICT_ID`,`BRANCH_ID`,`OFFICE_ID`,`DIST_ID`)
)

;

CREATE TABLE `DIST2_SALES_MONTH`
(
	`EDI_DATE` CHAR(8) NOT NULL,
	`EDI_TIME` CHAR(9) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`RPT_YM` CHAR(6) NOT NULL,
	`SALES_YM` CHAR(6) NOT NULL,
	`CHANNEL_GROUP_ID` VARCHAR(10) NOT NULL,
	`CHANNEL_GROUP_NM` NVARCHAR(21) NOT NULL,
	`CHANNEL_DISTRICT_ID` VARCHAR(4) NOT NULL,
	`CHANNEL_DISTRICT_NM` NVARCHAR(12) NOT NULL,
	`BRANCH_ID` VARCHAR(4) NOT NULL,
	`BRANCH_NM` NVARCHAR(51) NOT NULL,
	`OFFICE_ID` VARCHAR(4) NOT NULL,
	`OFFICE_NM` NVARCHAR(36) NOT NULL,
	`DIST_ID` VARCHAR(10) NOT NULL,
	`DIST_NM` NVARCHAR(90) NOT NULL,
	`SALES_AMT_MONTH` NUMERIC(22,6) NOT NULL,
	`SALES_AMT_PAST_MONTH` NUMERIC(22,6) NOT NULL,
	`SALES_AMT_MONTH_EXCLRET` NUMERIC(22,6) NOT NULL,
	`SALES_AMT_PAST_MONTH_EXCLRET` NUMERIC(22,6) NOT NULL,
	CONSTRAINT `PK_DIST2_SALES_MONTH` PRIMARY KEY (`DATA_DATE`,`RPT_YM`,`SALES_YM`,`CHANNEL_GROUP_ID`,`CHANNEL_DISTRICT_ID`,`BRANCH_ID`,`OFFICE_ID`,`DIST_ID`)
)

;

CREATE TABLE `DIST2_INDEX_AVG_SCORES`
(
	`EDI_DATE` CHAR(8) NOT NULL,
	`EDI_TIME` CHAR(9) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`RPT_YM` CHAR(6) NOT NULL,
	`CHANNEL_GROUP_ID` VARCHAR(10) NOT NULL,
	`CHANNEL_GROUP_NM` NVARCHAR(21) NOT NULL,
	`CHANNEL_DISTRICT_ID` VARCHAR(4) NOT NULL,
	`CHANNEL_DISTRICT_NM` NVARCHAR(12) NOT NULL,
	`AVG_SALES_AMT_MONTH_SCORES` NUMERIC(22,6) NOT NULL,
	`AVG_SALES_AMT_GROWTH_RATE_SCORES` NUMERIC(22,6) NOT NULL,
	`AVG_FORECAST_REACH_RATE_SCORES` NUMERIC(22,6) NOT NULL,
	`AVG_PAY_REACH_RATE_SCORES` NUMERIC(22,6) NOT NULL,
	`AVG_BILLING_BAL_SCORES` NUMERIC(22,6) NOT NULL,
	`AVG_INVENTORY_TURNOVER_DAYS_SCORES` NUMERIC(22,6) NOT NULL,
	`AVG_STOCK_ABNORMAL_RATE_SCORES` NUMERIC(22,6) NOT NULL,
	`AVG_STOCK_SALES_RATE_SCORES` NUMERIC(22,6) NOT NULL,
	`AVG_TERM_TRA_STABILITY_SCORES` NUMERIC(22,6) NOT NULL,
	`AVG_RELY_RATE_SCORES` NUMERIC(22,6) NOT NULL,
	`AVG_TERM_COVERAGE_SCORES` NUMERIC(22,6) NOT NULL,
	`AVG_BACK_CONV_RATE_SCORES` NUMERIC(22,6) NOT NULL,
	CONSTRAINT `PK_DIST2_INDEX_AVG_SCORES` PRIMARY KEY (`DATA_DATE`,`RPT_YM`,`CHANNEL_GROUP_ID`,`CHANNEL_DISTRICT_ID`)
)

;

CREATE TABLE `DIST2_EVAL_OFFICE`
(
	`EDI_DATE` CHAR(8) NOT NULL,
	`EDI_TIME` CHAR(9) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`RPT_YM` CHAR(6) NOT NULL,
	`CHANNEL_GROUP_ID` VARCHAR(10) NOT NULL,
	`CHANNEL_GROUP_NM` NVARCHAR(21) NOT NULL,
	`CHANNEL_DISTRICT_ID` VARCHAR(4) NOT NULL,
	`CHANNEL_DISTRICT_NM` NVARCHAR(12) NOT NULL,
	`BRANCH_ID` VARCHAR(4) NOT NULL,
	`BRANCH_NM` NVARCHAR(51) NOT NULL,
	`OFFICE_ID` VARCHAR(4) NOT NULL,
	`OFFICE_NM` NVARCHAR(36) NOT NULL,
	`DIST_TOTAL_COUNT` INT NOT NULL,
	`DIST_TOP_COUNT` INT NOT NULL,
	`DIST_GOLDEN_COUNT` INT NOT NULL,
	`DIST_POTENTIAL_COUNT` INT NOT NULL,
	`DIST_RELY_COUNT` INT NOT NULL,
	`DIST_STABLE_COUNT` INT NOT NULL,
	`DIST_MARKET_COUNT` INT NOT NULL,
	`DIST_EFFICIENCY_COUNT` INT NOT NULL,
	`DIST_ACCURATE_COUNT` INT NOT NULL,
	`DIST_COOPERATE_COUNT` INT NOT NULL,
	`DIST_OTHER_COUNT` INT NOT NULL,
	`DIST_WARNING_COUNT` INT NOT NULL,
	CONSTRAINT `PK_DIST2_EVAL_OFFICE` PRIMARY KEY (`DATA_DATE`,`RPT_YM`,`CHANNEL_GROUP_ID`,`CHANNEL_DISTRICT_ID`,`BRANCH_ID`,`OFFICE_ID`)
)

;

CREATE TABLE `DIST2_EVAL`
(
	`EDI_DATE` CHAR(8) NOT NULL,
	`EDI_TIME` CHAR(9) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`RPT_YM` CHAR(6) NOT NULL,
	`CHANNEL_GROUP_ID` VARCHAR(10) NOT NULL,
	`CHANNEL_GROUP_NM` NVARCHAR(21) NOT NULL,
	`CHANNEL_DISTRICT_ID` VARCHAR(4) NOT NULL,
	`CHANNEL_DISTRICT_NM` NVARCHAR(12) NOT NULL,
	`BRANCH_ID` VARCHAR(4) NOT NULL,
	`BRANCH_NM` NVARCHAR(51) NOT NULL,
	`OFFICE_ID` VARCHAR(4) NOT NULL,
	`OFFICE_NM` NVARCHAR(36) NOT NULL,
	`DIST_ID` VARCHAR(10) NOT NULL,
	`DIST_NM` NVARCHAR(90) NOT NULL,
	`DIST_STATUS_ID` VARCHAR(10) NOT NULL,
	`DIST_STATUS_NM` NVARCHAR(50) NOT NULL,
	`DIST_TYPE_ID` VARCHAR(10) NOT NULL,
	`DIST_TYPE_NM` NVARCHAR(50) NOT NULL,
	`TOTAL_SCORES` NUMERIC(22,6) NOT NULL,
	`SALES_AMT_MONTH` NUMERIC(22,6) NOT NULL,
	`SALES_AMT_MONTH_MAX` NUMERIC(22,6) NOT NULL,
	`SALES_AMT_MONTH_SCORES` NUMERIC(22,6) NOT NULL,
	`SALES_AMT_MONTH_SCORES_WEIGHT` NUMERIC(22,6) NOT NULL,
	`SALES_AMT_PAST_MONTH` NUMERIC(22,6) NOT NULL,
	`SALES_AMT_GROWTH_RATE` NUMERIC(22,6) NOT NULL,
	`SALES_AMT_GROWTH_RATE_SCORES` NUMERIC(22,6) NOT NULL,
	`SALES_AMT_GROWTH_RATE_SCORES_WEIGHT` NUMERIC(22,6) NOT NULL,
	`BALLING_MONTH` NUMERIC(22,6) NOT NULL,
	`FORECAST_AMT` NUMERIC(22,6) NOT NULL,
	`FORECAST_REACH_RATE` NUMERIC(22,6) NOT NULL,
	`FORECAST_REACH_RATE_SCORES` NUMERIC(22,6) NOT NULL,
	`FORECAST_REACH_RATE_SCORES_WEIGHT` NUMERIC(22,6) NOT NULL,
	`PAY_AMT` NUMERIC(22,6) NOT NULL,
	`PAY_REACH_RATE` NUMERIC(22,6) NOT NULL,
	`PAY_REACH_RATE_SCORES` NUMERIC(22,6) NOT NULL,
	`PAY_REACH_RATE_SCORES_WEIGHT` NUMERIC(22,6) NOT NULL,
	`BILLING_BAL` NUMERIC(22,6) NOT NULL,
	`BILLING_BAL_MAX` NUMERIC(22,6) NOT NULL,
	`BILLING_BAL_SCORES` NUMERIC(22,6) NOT NULL,
	`BILLING_BAL_SCORES_WEIGHT` NUMERIC(22,6) NOT NULL,
	`STOCK_AMT` NUMERIC(22,8) NOT NULL,
	`SALES_AMT_90DAYS` NUMERIC(22,6) NOT NULL,
	`INVENTORY_TURNOVER_DAYS` INT NOT NULL,
	`INVENTORY_TURNOVER_DAYS_SCORES` NUMERIC(22,6) NOT NULL,
	`INVENTORY_TURNOVER_DAYS_SCORES_WEIGHT` NUMERIC(22,6) NOT NULL,
	`STOCK_ABNORMAL_AMT` NUMERIC(22,8) NOT NULL,
	`STOCK_ABNORMAL_RATE` NUMERIC(22,8) NOT NULL,
	`STOCK_ABNORMAL_RATE_SCORES` NUMERIC(22,6) NOT NULL,
	`STOCK_ABNORMAL_RATE_SCORES_WEIGHT` NUMERIC(22,6) NOT NULL,
	`STOCK_SALES_RATE` NUMERIC(22,2) NOT NULL,
	`STOCK_SALES_RATE_SCORES` NUMERIC(22,6) NOT NULL,
	`STOCK_SALES_RATE_SCORES_WEIGHT` NUMERIC(22,6) NOT NULL,
	`TWO_MONTH_TERM_COUNT` INT NOT NULL,
	`LAST_MONTH_TERM_COUNT` INT NOT NULL,
	`TERM_TRA_STABILITY` NUMERIC(22,6) NOT NULL,
	`TERM_TRA_STABILITY_SCORES` NUMERIC(22,6) NOT NULL,
	`TERM_TRA_STABILITY_SCORES_WEIGHT` NUMERIC(22,6) NOT NULL,
	`ORDR_TERM_AMT` NUMERIC(22,6) NOT NULL,
	`RELY_RATE` NUMERIC(22,6) NOT NULL,
	`RELY_RATE_SCORES` NUMERIC(22,6) NOT NULL,
	`RELY_RATE_SCORES_WEIGHT` NUMERIC(22,6) NOT NULL,
	`CURRENT_MONTH_TERM_COUNT` INT NOT NULL,
	`TERM_COUNT` INT NOT NULL,
	`TERM_COVERAGE` NUMERIC(22,6) NOT NULL,
	`TERM_COVERAGE_SCORES` NUMERIC(22,6) NOT NULL,
	`TERM_COVERAGE_SCORES_WEIGHT` NUMERIC(22,6) NOT NULL,
	`ORDR_TERM_BACK_AMT` NUMERIC(22,6) NOT NULL,
	`BACK_CONV_RATE` NUMERIC(22,6) NOT NULL,
	`BACK_CONV_RATE_SCORES` NUMERIC(22,6) NOT NULL,
	`BACK_CONV_RATE_SCORES_WEIGHT` NUMERIC(22,6) NOT NULL,
	CONSTRAINT `PK_DIST2_EVAL` PRIMARY KEY (`DATA_DATE`,`RPT_YM`,`CHANNEL_GROUP_ID`,`CHANNEL_DISTRICT_ID`,`BRANCH_ID`,`OFFICE_ID`,`DIST_ID`)
)

;

CREATE TABLE `DIST2_EMP_MARKET`
(
	`EDI_DATE` CHAR(8) NOT NULL,
	`EDI_TIME` CHAR(9) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`RPT_YM` CHAR(6) NOT NULL,
	`CHANNEL_GROUP_ID` VARCHAR(10) NOT NULL,
	`CHANNEL_GROUP_NM` NVARCHAR(21) NOT NULL,
	`CHANNEL_DISTRICT_ID` VARCHAR(4) NOT NULL,
	`CHANNEL_DISTRICT_NM` NVARCHAR(12) NOT NULL,
	`BRANCH_ID` VARCHAR(4) NOT NULL,
	`BRANCH_NM` NVARCHAR(51) NOT NULL,
	`OFFICE_ID` VARCHAR(4) NOT NULL,
	`OFFICE_NM` NVARCHAR(36) NOT NULL,
	`DIST_ID` VARCHAR(10) NOT NULL,
	`DIST_NM` NVARCHAR(90) NOT NULL,
	`TWO_MONTH_TERM_COUNT` INT NOT NULL,
	`LAST_MONTH_TERM_COUNT` INT NOT NULL,
	`TERM_TRA_STABILITY` NUMERIC(22,6) NOT NULL,
	`ORDR_TERM_AMT` NUMERIC(22,6) NOT NULL,
	`SALES_AMT_MONTH` NUMERIC(22,6) NOT NULL,
	`RELY_RATE` NUMERIC(22,6) NOT NULL,
	`CURRENT_MONTH_TERM_COUNT` INT NOT NULL,
	`TERM_COUNT` INT NOT NULL,
	`TERM_COVERAGE` NUMERIC(22,6) NOT NULL,
	`ORDR_TERM_BACK_AMT` NUMERIC(22,6) NOT NULL,
	`BACK_CONV_RATE` NUMERIC(22,6) NOT NULL,
	CONSTRAINT `PK_DIST2_EMP_MARKET` PRIMARY KEY (`DATA_DATE`,`RPT_YM`,`CHANNEL_GROUP_ID`,`CHANNEL_DISTRICT_ID`,`BRANCH_ID`,`OFFICE_ID`,`DIST_ID`)
)

;

CREATE TABLE `DIST2_BAL_REACH`
(
	`EDI_DATE` CHAR(8) NOT NULL,
	`EDI_TIME` CHAR(9) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`RPT_YM` CHAR(6) NOT NULL,
	`CHANNEL_GROUP_ID` VARCHAR(10) NOT NULL,
	`CHANNEL_GROUP_NM` NVARCHAR(21) NOT NULL,
	`CHANNEL_DISTRICT_ID` VARCHAR(4) NOT NULL,
	`CHANNEL_DISTRICT_NM` NVARCHAR(12) NOT NULL,
	`BRANCH_ID` VARCHAR(4) NOT NULL,
	`BRANCH_NM` NVARCHAR(51) NOT NULL,
	`OFFICE_ID` VARCHAR(4) NOT NULL,
	`OFFICE_NM` NVARCHAR(36) NOT NULL,
	`DIST_ID` VARCHAR(10) NOT NULL,
	`DIST_NM` NVARCHAR(90) NOT NULL,
	`BILLING_MONTH` NUMERIC(22,6) NOT NULL,
	`FORECAST_AMT` NUMERIC(22,6) NOT NULL,
	`FORECAST_REACH_RATE` NUMERIC(22,6) NOT NULL,
	`PAY_AMT` NUMERIC(22,6) NOT NULL,
	`PAY_REACH_RATE` NUMERIC(22,6) NOT NULL,
	`BILLING_BAL` NUMERIC(22,6) NOT NULL,
	`BILLING_BAL_MAX` NUMERIC(22,6) NOT NULL,
	`BILLING_BAL_SCORES` NUMERIC(22,6) NOT NULL,
	CONSTRAINT `PK_DIST2_BAL_REACH` PRIMARY KEY (`DATA_DATE`,`RPT_YM`,`CHANNEL_GROUP_ID`,`CHANNEL_DISTRICT_ID`,`BRANCH_ID`,`OFFICE_ID`,`DIST_ID`)
)

;

SET FOREIGN_KEY_CHECKS=1 ;
