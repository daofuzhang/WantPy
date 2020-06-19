/* ---------------------------------------------------- */
/*  Generated by Enterprise Architect Version 12.0 		*/
/*  Created On : 19-�E��-2017 �U�� 06:30:37 				*/
/*  DBMS       : MySql 						*/
/* ---------------------------------------------------- */

SET FOREIGN_KEY_CHECKS=0 ;

/* Create Tables */

CREATE TABLE `SPDY_TYPE_GROUP_OPTIMIZED`
(
	`MODEL_ID` CHAR(18) NOT NULL,
	`BRANCH_ID` VARCHAR(4) NOT NULL,
	`OFFICE_ID` VARCHAR(4) NOT NULL,
	`STD_MARKET_ID` VARCHAR(6) NOT NULL,
	`TERM_TYPE` VARCHAR(4) NOT NULL,
	`PROD_LEVEL3_ID` VARCHAR(9) NOT NULL,
	`OPTIMIZED_SPDY_TYPE_GROUP` VARCHAR(10) NOT NULL,
	CONSTRAINT `PK_SPDY_TYPE_GROUP_OPTIMIZED` PRIMARY KEY (`MODEL_ID`,`STD_MARKET_ID`,`TERM_TYPE`,`PROD_LEVEL3_ID`)
)

;

CREATE TABLE `SPDY_OFFICE_PROD_EXP_PRED`
(
	`MODEL_ID` CHAR(18) NOT NULL,
	`BRANCH_ID` VARCHAR(4) NOT NULL,
	`OFFICE_ID` VARCHAR(4) NOT NULL,
	`PROD_LEVEL3_ID` VARCHAR(9) NOT NULL,
	`PRED_SPDY_YM` CHAR(6) NOT NULL,
	`SPDY_EXP_RATIO` DECIMAL(5,4) NOT NULL,
	`SPDY_EXP` NUMERIC(22,6) NOT NULL,
	CONSTRAINT `PK_SPDY_OFFICE_PROD_EXP_PRED` PRIMARY KEY (`MODEL_ID`,`OFFICE_ID`,`PROD_LEVEL3_ID`,`PRED_SPDY_YM`)
)

;

CREATE TABLE `SPDY_OFFICE_PROD_EXP_ACTUAL`
(
	`MODEL_ID` CHAR(18) NOT NULL,
	`BRANCH_ID` VARCHAR(4) NOT NULL,
	`OFFICE_ID` VARCHAR(4) NOT NULL,
	`PROD_LEVEL3_ID` VARCHAR(9) NOT NULL,
	`SPDY_YM` CHAR(6) NOT NULL,
	`TOTAL_SPDY_EXP` NUMERIC(22,6) NOT NULL,
	CONSTRAINT `PK_SPDY_OFFICE_PROD_EXP_ACTUAL` PRIMARY KEY (`MODEL_ID`,`OFFICE_ID`,`PROD_LEVEL3_ID`,`SPDY_YM`)
)

;

CREATE TABLE `SPDY_OFFICE_EXP_PRED`
(
	`MODEL_ID` CHAR(18) NOT NULL,
	`BRANCH_ID` VARCHAR(4) NOT NULL,
	`OFFICE_ID` VARCHAR(4) NOT NULL,
	`PRED_SPDY_YM` CHAR(6) NOT NULL,
	`SPDY_EXP_RATIO` DECIMAL(5,4) NOT NULL,
	`SPDY_EXP` NUMERIC(22,6) NOT NULL,
	CONSTRAINT `PK_SPDY_OFFICE_EXP_PRED` PRIMARY KEY (`MODEL_ID`,`OFFICE_ID`,`PRED_SPDY_YM`)
)

;

CREATE TABLE `SPDY_OFFICE_EXP_ACTUAL`
(
	`MODEL_ID` CHAR(18) NOT NULL,
	`BRANCH_ID` VARCHAR(4) NOT NULL,
	`OFFICE_ID` VARCHAR(4) NOT NULL,
	`SPDY_YM` CHAR(6) NOT NULL,
	`TOTAL_SPDY_EXP` NUMERIC(22,6) NOT NULL,
	CONSTRAINT `PK_SPDY_OFFICE_EXP_ACTUAL` PRIMARY KEY (`MODEL_ID`,`OFFICE_ID`,`SPDY_YM`)
)

;

SET FOREIGN_KEY_CHECKS=1 ;