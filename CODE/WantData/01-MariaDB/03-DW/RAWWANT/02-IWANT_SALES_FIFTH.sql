SET FOREIGN_KEY_CHECKS=0 ;

CREATE TABLE `IWANT_SALES_FIFTH_CITY`
(
	`EDI_NO` CHAR(12) NOT NULL,
	`SID` VARCHAR(38) NOT NULL,
	`FIFTH_LV_ID` VARCHAR(20) NOT NULL,
	`NAME` VARCHAR(100) NOT NULL,
	`FORTH_SID` VARCHAR(38) NOT NULL,
	`STATUS` CHAR(1) NOT NULL,
	CONSTRAINT `PK_IWANT_SALES_FIFTH_CITY` PRIMARY KEY (`SID`)
)

;

SET FOREIGN_KEY_CHECKS=1 ;