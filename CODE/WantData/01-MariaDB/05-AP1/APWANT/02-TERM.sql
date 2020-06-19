/* ---------------------------------------------------- */
/*  Generated by Enterprise Architect Version 12.0 		*/
/*  Created On : 27-�E��-2017 �W�� 11:48:20 				*/
/*  DBMS       : MySql 						*/
/* ---------------------------------------------------- */

SET FOREIGN_KEY_CHECKS=0 ;

/* Create Tables */

CREATE TABLE `TERM_TERM_DISTANCE`
(
	`MODEL_ID` CHAR(18) NOT NULL,
	`TERM_MAIN_ID` VARCHAR(10) NOT NULL,
	`TERM_ID` VARCHAR(10) NOT NULL,
	`TERM_TERM_DISTANCE` INT 	 NULL,
	CONSTRAINT `PK_TERM_TERM_DISTANCE` PRIMARY KEY (`MODEL_ID`,`TERM_MAIN_ID`,`TERM_ID`)
)

;

CREATE TABLE `TERM_DEVEL`
(
	`MODEL_ID` CHAR(18) NOT NULL,
	`BRANCH_ID` VARCHAR(4) 	 NULL,
	`OFFICE_ID` VARCHAR(4) 	 NULL,
	`STD_MARKET_ID` VARCHAR(6) 	 NULL,
	`STD_MARKET_SMALL_ID` VARCHAR(9) 	 NULL,
	`TERM_ID` VARCHAR(10) NOT NULL,
	`IS_ORDR` CHAR(1) 	 NULL,
	CONSTRAINT `PK_TERM_DEVEL` PRIMARY KEY (`MODEL_ID`,`TERM_ID`)
)

;

CREATE TABLE `TERM_CLUSTER_RESULT`
(
	`MODEL_ID` CHAR(18) NOT NULL,
	`TERM_ID` VARCHAR(10) NOT NULL,
	`TERM_LEVEL` VARCHAR(10) NOT NULL,
	`TERM_CLUSTER` VARCHAR(4) NOT NULL,
	`STD_MARKET_ID` VARCHAR(6) 	 NULL,
	`STD_MARKET_SMALL_ID` VARCHAR(9) 	 NULL,
	`TOTAL_BACK_AMT` NUMERIC(22,6) 	 NULL,
	`TOTAL_BACK_COUNT` NUMERIC(22,6) 	 NULL,
	`TOTAL_ACTUAL_EXP` NUMERIC(22,6) 	 NULL,
	`TOTAL_ACTUAL_COUNT` INT 	 NULL,
	`GAODE_KFC_COUNT` INT 	 NULL,
	`GAODE_MCDONALDS_COUNT` INT 	 NULL,
	`GAODE_STARBUCKS_COUNT` INT 	 NULL,
	`GAODE_MALL_COUNT` INT 	 NULL,
	`GAODE_CVS_COUNT` INT 	 NULL,
	`GAODE_MARKET_COUNT` INT 	 NULL,
	`GAODE_POST_COUNT` INT 	 NULL,
	`GAODE_LOGISTICS_COUNT` INT 	 NULL,
	`GAODE_ENT_COUNT` INT 	 NULL,
	`GAODE_HOSP_COUNT` INT 	 NULL,
	`GAODE_STARHTL_COUNT` INT 	 NULL,
	`GAODE_ECOHTL_COUNT` INT 	 NULL,
	`GAODE_VILLA_COUNT` INT 	 NULL,
	`GAODE_RESI_COUNT` INT 	 NULL,
	`GAODE_BEDU_COUNT` INT 	 NULL,
	`GAODE_HEDU_COUNT` INT 	 NULL,
	`GAODE_KINDG_COUNT` INT 	 NULL,
	`GAODE_TRAFF_COUNT` INT 	 NULL,
	`GAODE_PARKING_COUNT` INT 	 NULL,
	`GAODE_FCOM_COUNT` INT 	 NULL,
	`GAODE_FACTORY_COUNT` INT 	 NULL,
	`GAODE_GLOBALBANK_COUNT` INT 	 NULL,
	`GAODE_LOCALBANK_COUNT` INT 	 NULL,
	CONSTRAINT `PK_TERM_CLUSTER_RESULT` PRIMARY KEY (`MODEL_ID`,`TERM_ID`)
)

;

CREATE TABLE `TERM_CLUSTER_PROD_LEVEL3_NEW`
(
	`MODEL_ID` CHAR(18) NOT NULL,
	`PROD_LEVEL2_ID` VARCHAR(6) NOT NULL,
	`PROD_LEVEL3_ID` VARCHAR(9) NOT NULL,
	`IS_NEW` CHAR(1) NOT NULL,
	CONSTRAINT `TERM_CLUSTER_PROD_LEVEL3_NEW` PRIMARY KEY (`MODEL_ID`,`PROD_LEVEL3_ID`)
)

;

CREATE TABLE `TERM_CLUSTER_PROD_LEVEL2_FIT`
(
	`MODEL_ID` CHAR(18) NOT NULL,
	`STD_MARKET_ID` VARCHAR(6) NOT NULL,
	`TERM_CLUSTER` VARCHAR(4) NOT NULL,
	`PROD_LEVEL2_ID` VARCHAR(6) NOT NULL,
	`SALES_RATIO` NUMERIC(7,6) NOT NULL,
	`PROD_LEVEL2_FIT_DEGREE` NUMERIC(7,6) NOT NULL,
	`IS_PROD_LEVEL2_FIT` CHAR(1) NOT NULL,
	CONSTRAINT `PK_TERM_CLUSTER_PROD_LEVEL2_FIT` PRIMARY KEY (`MODEL_ID`,`STD_MARKET_ID`,`TERM_CLUSTER`,`PROD_LEVEL2_ID`)
)

;

SET FOREIGN_KEY_CHECKS=1 ;