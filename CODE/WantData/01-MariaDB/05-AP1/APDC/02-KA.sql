/* ---------------------------------------------------- */
/*  Generated by Enterprise Architect Version 12.0 		*/
/*  Created On : 19-�|��-2019 �U�� 04:01:02 				*/
/*  DBMS       : MySql 						*/
/* ---------------------------------------------------- */

SET FOREIGN_KEY_CHECKS=0 ;

/* Create Tables */

CREATE TABLE `KA_SYS_PER`
(
	`SYS_ID` VARCHAR(4) NOT NULL,
	`SYS_NM` VARCHAR(20) NOT NULL,
	`COM_ID` VARCHAR(4) NOT NULL,
	`COM_NM` VARCHAR(20) NOT NULL,
	`EMP_ID` VARCHAR(8) NOT NULL,
	`EMP_NM` VARCHAR(20) NOT NULL,
	`EMP_ROLE` VARCHAR(2) NOT NULL,
	CONSTRAINT `PK_KA_SYS_PER` PRIMARY KEY (`SYS_ID`,`COM_ID`,`EMP_ID`,`EMP_ROLE`)
)

;

CREATE TABLE `KA_SYS_PER_NEW`
(
	`DATA_DATE` VARCHAR(8) NOT NULL,
	`SYS_ID` VARCHAR(4) NOT NULL,
	`SYS_NM` VARCHAR(50) NOT NULL,
	`COM_ID` VARCHAR(20) NOT NULL,
	`COM_NM` VARCHAR(4) NOT NULL,
	`EMP_ID` VARCHAR(20) NOT NULL,
	`EMP_NM` VARCHAR(8) NOT NULL,
	`EMP_ROLE` VARCHAR(2) NOT NULL,
	CONSTRAINT `PK_KA_SYS_PER_NEW` PRIMARY KEY (`SYS_ID`,`COM_ID`,`EMP_ID`,`EMP_ROLE`)
)

;

SET FOREIGN_KEY_CHECKS=1 ;