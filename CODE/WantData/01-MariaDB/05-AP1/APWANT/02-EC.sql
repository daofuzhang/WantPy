/* ---------------------------------------------------- */
/*  Generated by Enterprise Architect Version 12.0 		*/
/*  Created On : 25-�E��-2017 �U�� 01:34:36 				*/
/*  DBMS       : MySql 						*/
/* ---------------------------------------------------- */

SET FOREIGN_KEY_CHECKS=0 ;

/* Create Tables */

CREATE TABLE `EC_PROD`
(
	`MODEL_ID` CHAR(18) NOT NULL,
	`CRAWL_DATE` CHAR(8) NOT NULL,
	`EC_SHOP_ID` VARCHAR(10) NOT NULL,
	`PROD_LEVEL1_ID` VARCHAR(4) NOT NULL,
	`URL` VARCHAR(200) NOT NULL,
	`PROD_NM` NVARCHAR(70) NOT NULL,
	`PROD_BRAND` NVARCHAR(30) NOT NULL,
	`PROD_PRICE` NUMERIC(10,2) 	 NULL,
	`PROD_NORM` VARCHAR(20) 	 NULL,
	`PROD_PACKAGE` NVARCHAR(30) NOT NULL,
	`PROD_FLAVOR` NVARCHAR(50) NOT NULL,
	`PROD_CMNT_CN` INT 	 NULL,
	`PROD_GOOD_RATE` NUMERIC(10,2) 	 NULL,
	`PROD_SELLER` NVARCHAR(50) 	 NULL,
	`PROD_MADE_PLACE` NVARCHAR(10) NOT NULL,
	CONSTRAINT `PK_EC_PROD` PRIMARY KEY (`MODEL_ID`,`CRAWL_DATE`,`EC_SHOP_ID`,`PROD_LEVEL1_ID`,`URL`)
)

;

CREATE TABLE `EC_INDICA_WANT`
(
	`MODEL_ID` CHAR(18) NOT NULL,
	`CRAWL_DATE` CHAR(8) NOT NULL,
	`EC_INDICA_WANT` NUMERIC(14,6) NOT NULL,
	CONSTRAINT `PK_EC_INDICA_WANT` PRIMARY KEY (`MODEL_ID`,`CRAWL_DATE`)
)

;

CREATE TABLE `EC_INDICA_PROD_FACTOR`
(
	`MODEL_ID` CHAR(18) NOT NULL,
	`CRAWL_DATE` CHAR(8) NOT NULL,
	`PROD_LEVEL1_ID` VARCHAR(4) NOT NULL,
	`PROD_BRAND` NVARCHAR(30) NOT NULL,
	`RROD_BRAND_PRICE_HIGH` NUMERIC(10,2) 	 NULL,
	`PROD_BRAND_PRICE_LOW` NUMERIC(10,2) 	 NULL,
	`PROD_BRAND_PRICE_AVG` NUMERIC(10,2) 	 NULL,
	`PROD_BRAND_PROD_CN` INT NOT NULL,
	`PROD_BRAND_CMNT_GOOD` INT 	 NULL,
	`PROD_BRAND_CMNT_FAIR` INT 	 NULL,
	`PROD_BRAND_CMNT_BAD` INT 	 NULL,
	`PROD_BRAND_STAR_ONE` INT 	 NULL,
	`PROD_BRAND_STAR_TWO` INT 	 NULL,
	`PROD_BRAND_STAR_THREE` INT 	 NULL,
	`PROD_BRAND_STAR_FOUR` INT 	 NULL,
	`PROD_BRAND_STAR_FIVE` INT 	 NULL,
	`PROD_BRAND_STAR_ALL` INT 	 NULL,
	CONSTRAINT `PK_EC_INDICA_PROD_FACTOR` PRIMARY KEY (`CRAWL_DATE`,`PROD_LEVEL1_ID`,`PROD_BRAND`,`MODEL_ID`)
)

;

CREATE TABLE `EC_CMNT_TEXT_EMON`
(
	`MODEL_ID` CHAR(18) NOT NULL,
	`TRAIN_NUM` CHAR(11) NOT NULL,
	`CRAWL_DATE` CHAR(8) NOT NULL,
	`PROD_LEVEL1_ID` VARCHAR(4) NOT NULL,
	`PROD_BRAND` NVARCHAR(30) NOT NULL,
	`CMNT_ID` VARCHAR(30) NOT NULL,
	`POST_DATE` CHAR(8) NOT NULL,
	`TEXT` NVARCHAR(100) NOT NULL,
	`RATIO` NUMERIC(7,6) NOT NULL,
	`EMON_MARK_ID` VARCHAR(10) 	 NULL,
	CONSTRAINT `PK_EC_CMNT_TEXT_EMON` PRIMARY KEY (`MODEL_ID`,`TRAIN_NUM`,`PROD_LEVEL1_ID`,`CMNT_ID`,`POST_DATE`,`TEXT`)
)

;

SET FOREIGN_KEY_CHECKS=1 ;
