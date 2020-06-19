/* ---------------------------------------------------- */
/*  Generated by Enterprise Architect Version 12.0 		*/
/*  Created On : 15-�Q�@��-2018 �W�� 09:22:13 				*/
/*  DBMS       : MySql 						*/
/* ---------------------------------------------------- */

SET FOREIGN_KEY_CHECKS=0 ;

/* Create Tables */

CREATE TABLE `BW_SAPBHP_BI0_TSALESORG`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`SALESORG` VARCHAR(4) NOT NULL,
	`LANGU` VARCHAR(1) NOT NULL,
	`TXTLG` VARCHAR(60) NOT NULL
)

;

CREATE TABLE `BW_SAPBHP_BI0_TSALES_OFF`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`SALES_OFF` VARCHAR(4) NOT NULL,
	`LANGU` VARCHAR(1) NOT NULL,
	`TXTSH` VARCHAR(20) NOT NULL
)

;

CREATE TABLE `BW_SAPBHP_BI0_TPROD_HIER`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`PROD_HIER` VARCHAR(60) NOT NULL,
	`LANGU` VARCHAR(1) NOT NULL,
	`TXTLG` VARCHAR(60) NOT NULL
)

;

CREATE TABLE `BW_SAPBHP_BI0_TMATERIAL`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`MATERIAL` VARCHAR(18) NOT NULL,
	`LANGU` VARCHAR(1) NOT NULL,
	`TXTMD` VARCHAR(40) NOT NULL
)

;

CREATE TABLE `BW_SAPBHP_BI0_TDIVISION`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DIVISION` VARCHAR(2) NOT NULL,
	`LANGU` VARCHAR(1) NOT NULL,
	`TXTSH` VARCHAR(20) NOT NULL
)

;

CREATE TABLE `BW_SAPBHP_BI0_TDISTR_CHAN`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DISTR_CHAN` VARCHAR(2) NOT NULL,
	`LANGU` VARCHAR(1) NOT NULL,
	`TXTSH` VARCHAR(20) NOT NULL
)

;

CREATE TABLE `BW_SAPBHP_BI0_TCUSTOMER`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`CUSTOMER` VARCHAR(15) NOT NULL,
	`TXTMD` VARCHAR(40) NOT NULL
)

;

CREATE TABLE `BW_SAPBHP_BI0_TC_CTR_AREA`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`C_CTR_AREA` VARCHAR(4) NOT NULL,
	`LANGU` VARCHAR(1) NOT NULL,
	`TXTMD` VARCHAR(40) NOT NULL,
	`TXTLG` VARCHAR(60) NOT NULL
)

;

CREATE TABLE `BW_SAPBHP_BI0_PMATERIAL`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`MATERIAL` VARCHAR(18) NOT NULL,
	`OBJVERS` VARCHAR(1) NOT NULL,
	`DIVISION` VARCHAR(2) NOT NULL,
	`MATL_TYPE` VARCHAR(4) NOT NULL,
	`PRODH1` VARCHAR(60) NOT NULL,
	`PRODH2` VARCHAR(60) NOT NULL,
	`PRODH3` VARCHAR(60) NOT NULL,
	`PRODH4` VARCHAR(60) NOT NULL,
	`PRODH5` VARCHAR(60) NOT NULL,
	`BIC_ZSD_PXXL` VARCHAR(5) NOT NULL,
	`BIC_ZCOOIC064` VARCHAR(6) NOT NULL
)

;

CREATE TABLE `BW_SAPBHP_BI0_PCUSTOMER`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`CUSTOMER` VARCHAR(15) NOT NULL,
	`OBJVERS` VARCHAR(1) NOT NULL,
	`ACCNT_GRP` VARCHAR(4) NOT NULL,
	`CUST_CLASS` VARCHAR(2) NOT NULL,
	`SALES_OFF` VARCHAR(4) NOT NULL,
	`BIC_ZWW_COMPY` VARCHAR(4) NOT NULL
)

;

CREATE TABLE `BW_SAPBHP_BI0_PCUST_SALES`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DIVISION` VARCHAR(2) NOT NULL,
	`DISTR_CHAN` VARCHAR(2) NOT NULL,
	`SALESORG` VARCHAR(4) NOT NULL,
	`CUST_SALES` VARCHAR(15) NOT NULL,
	`OBJVERS` VARCHAR(1) NOT NULL,
	`SALES_OFF` VARCHAR(4) NOT NULL,
	`BIC_ZWW_COMPY` VARCHAR(4) NOT NULL
)

;

CREATE TABLE `BW_SAPBHP_BI0_AFIAR_O0300`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`COMP_CODE` VARCHAR(4) NOT NULL,
	`DEBITOR` VARCHAR(15) NOT NULL,
	`FISCPER` VARCHAR(7) NOT NULL,
	`FISCVARNT` VARCHAR(2) NOT NULL,
	`AC_DOC_NO` VARCHAR(10) NOT NULL,
	`ITEM_NUM` VARCHAR(3) NOT NULL,
	`FI_DSBITEM` VARCHAR(4) NOT NULL,
	`BIC_ZCUST_OLD` VARCHAR(35) NOT NULL,
	`C_CTR_AREA` VARCHAR(4) NOT NULL,
	`AC_DOC_TYP` VARCHAR(2) NOT NULL,
	`PSTNG_DATE` VARCHAR(8) NOT NULL,
	`DEB_CRE_LC` DECIMAL(21,4) NOT NULL,
	`CUSTOMER` VARCHAR(15) NOT NULL,
	`BIC_ZTCODE` VARCHAR(20) NOT NULL
)

;

SET FOREIGN_KEY_CHECKS=1 ;