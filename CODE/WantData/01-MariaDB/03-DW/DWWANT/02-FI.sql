SET FOREIGN_KEY_CHECKS=0 ;

CREATE TABLE `FI_CUST_STMT`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`SALES_CREDIT_ID` VARCHAR(4) NOT NULL,
	`WANT_COM_ID` VARCHAR(4) NOT NULL,
	`SALES_OFF_ID` VARCHAR(4) NOT NULL,
	`CUST_ID` VARCHAR(15) NOT NULL,
	`TODAY_AMT` DECIMAL(21,4) NOT NULL,
	`BAL_BEGIN` DECIMAL(21,4) NOT NULL,
	`CUM_AMT` DECIMAL(21,4) NOT NULL,
	`SALES_AMT` DECIMAL(21,4) NOT NULL,
	`BAL_END` DECIMAL(21,4) NOT NULL,
	CONSTRAINT `PK_FI_CUST_STMT` PRIMARY KEY (`SALES_CREDIT_ID`,`WANT_COM_ID`,`SALES_OFF_ID`,`CUST_ID`)
)

;

CREATE TABLE `FI_CUST_SPEC`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`SPEC_NUM` VARCHAR(10) NOT NULL,
	`PROD_DIV_ID` VARCHAR(2) NOT NULL,
	`SALES_CHAN_ID` VARCHAR(2) NOT NULL,
	`SALES_COM_ID` VARCHAR(4) NOT NULL,
	`SALES_COM_CODE` VARCHAR(4) NOT NULL,
	`CUST_ID` VARCHAR(15) NOT NULL,
	`PROD_MATL_ID` VARCHAR(18) 	 NULL,
	`PROD_MATL_GRP1_ID` VARCHAR(3) 	 NULL,
	`SPEC_STATUS` VARCHAR(1) 	 NULL,
	`SPEC_AMT` DECIMAL(21,4) NOT NULL,
	CONSTRAINT `PK_FI_CUST_SPEC` PRIMARY KEY (`SPEC_NUM`,`SALES_COM_CODE`,`SALES_COM_ID`,`SALES_CHAN_ID`,`PROD_DIV_ID`,`CUST_ID`)
)

;

CREATE TABLE `FI_CUST_BAL`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`DATA_DATE` CHAR(8) NOT NULL,
	`FISC_PER` VARCHAR(7) NOT NULL,
	`FISC_VARNT` VARCHAR(2) NOT NULL,
	`FISC_DSB_ITEM` VARCHAR(4) NOT NULL,
	`AC_DOC_NUM` VARCHAR(10) NOT NULL,
	`AC_DOC_ITEM` VARCHAR(3) NOT NULL,
	`AC_DOC_TYPE` VARCHAR(2) NOT NULL,
	`AC_DOC_POST_YMD` VARCHAR(8) NOT NULL,
	`SALES_COM_CODE` VARCHAR(4) NOT NULL,
	`CUST_ID` VARCHAR(15) NOT NULL,
	`SALES_CREDIT_ID` VARCHAR(4) 	 NULL,
	`SALES_TRAS_CODE` VARCHAR(20) 	 NULL,
	`BAL_AMT` DECIMAL(21,4) NOT NULL,
	CONSTRAINT `PK_FI_CUST_BAL` PRIMARY KEY (`SALES_COM_CODE`,`CUST_ID`,`FISC_PER`,`FISC_VARNT`,`AC_DOC_NUM`,`AC_DOC_ITEM`,`FISC_DSB_ITEM`)
)

;

SET FOREIGN_KEY_CHECKS=1 ;
