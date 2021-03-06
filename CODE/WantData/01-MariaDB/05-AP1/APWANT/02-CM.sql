/* ---------------------------------------------------- */
/*  Generated by Enterprise Architect Version 12.0 		*/
/*  Created On : 09-�|��-2018 �U�� 08:28:49 				*/
/*  DBMS       : MySql 						*/
/* ---------------------------------------------------- */

SET FOREIGN_KEY_CHECKS=0 ;

/* Create Tables */

CREATE TABLE `CM_USER`
(
	`SYS_ID` VARCHAR(6) NOT NULL,
	`USER_ID` VARCHAR(8) NOT NULL,
	`USER_NM` NVARCHAR(50) NOT NULL,
	`USER_PWD` CHAR(64) NOT NULL,
	`IS_VALID` CHAR(1) NOT NULL,
	`UPD_USER_ID` VARCHAR(8) NOT NULL,
	`UPD_DT` DATETIME(0) NOT NULL,
	CONSTRAINT `PK_CM_USER` PRIMARY KEY (`USER_ID`,`SYS_ID`)
)

;

CREATE TABLE `CM_CODE`
(
	`SYS_ID` VARCHAR(6) NOT NULL,
	`CODE_KIND` VARCHAR(10) NOT NULL,
	`CODE_ID` VARCHAR(10) NOT NULL,
	`IS_SYSTEM` CHAR(1) NOT NULL,
	`SORT_ORDER` VARCHAR(6) 	 NULL,
	`REMARK` NVARCHAR(300) 	 NULL,
	`UPD_USER_ID` VARCHAR(8) NOT NULL,
	`UPD_DT` DATETIME(0) NOT NULL,
	CONSTRAINT `PK_CM_CODE` PRIMARY KEY (`CODE_KIND`,`CODE_ID`,`SYS_ID`)
)

;

SET FOREIGN_KEY_CHECKS=1 ;
