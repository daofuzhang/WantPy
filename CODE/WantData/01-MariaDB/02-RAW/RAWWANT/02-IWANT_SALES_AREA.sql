SET FOREIGN_KEY_CHECKS=0 ;

CREATE TABLE `IWANT_SALES_AREA`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`ID` VARCHAR(10) NOT NULL,
	`NAME` VARCHAR(50) NOT NULL,
	`COMPANY_ID` VARCHAR(50) NOT NULL,
	`STATUS` CHAR(1) NOT NULL
)

;

SET FOREIGN_KEY_CHECKS=1 ;