/* ---------------------------------------------------- */
/*  Generated by Enterprise Architect Version 12.0 		*/
/*  Created On : 12-�Q�@��-2018 �W�� 12:25:18 				*/
/*  DBMS       : MySql 						*/
/* ---------------------------------------------------- */

SET FOREIGN_KEY_CHECKS=0 ;

/* Create Tables */

CREATE TABLE `IWANT_SALES_EMP_POSITION_ORG_VIEW`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`EMP_ID` VARCHAR(8) NOT NULL,
	`EMP_NAME` VARCHAR(80) NOT NULL,
	`POS_ID` VARCHAR(8) NOT NULL,
	`POS_NAME` VARCHAR(120) NOT NULL,
	`POS_TYPE_ID` VARCHAR(3) NOT NULL,
	`POS_TYPE_NAME` VARCHAR(40) NOT NULL,
	`COMPANY_ID` VARCHAR(4) NOT NULL,
	`COMPANY_NAME` VARCHAR(250) NOT NULL,
	`BRANCH_ID` VARCHAR(50) NOT NULL,
	`BRANCH_NAME` VARCHAR(360) NOT NULL,
	`DIRECTOR_EMP_ID` VARCHAR(8) NOT NULL,
	`DIRECTOR_EMP_NAME` VARCHAR(80) NOT NULL,
	`DIRECTOR_POS_ID` VARCHAR(8) NOT NULL,
	`DIRECTOR_POS_NAME` VARCHAR(120) NOT NULL,
	`DIRECTOR_POS_TYPE_ID` VARCHAR(3) NOT NULL,
	`DIRECTOR_POS_TYPE_NAME` VARCHAR(40) NOT NULL,
	`POS_PROPERTY_ID` VARCHAR(4) NOT NULL,
	`CHANNEL_ID` VARCHAR(4) NOT NULL,
	`CHANNEL_NAME` VARCHAR(50) NOT NULL,
	`AREA_ID` VARCHAR(50) NOT NULL,
	`AREA_NAME` VARCHAR(300) NOT NULL,
	`MASTER_POS` VARCHAR(1) NOT NULL,
	`EMP_GENDER` VARCHAR(1) NOT NULL,
	`EMP_ONBOARD_DATE1` VARCHAR(8) NOT NULL
)

;

SET FOREIGN_KEY_CHECKS=1 ;