SELECT EDI_NO
, EMPLOYEE, DATETO, RECORDMODE
, BIC_ZORG_03, BIC_ZORG_04, BIC_ZORG_05, BIC_ZORG_06, BIC_ZORG_07, BIC_ZORG_08, BIC_ZORG_09
, BIC_ZORG_03_T, BIC_ZORG_04_T, BIC_ZORG_05_T, BIC_ZORG_06_T, BIC_ZORG_07_T, BIC_ZORG_08_T, BIC_ZORG_09_T
, REPLACE(EE_SNAME,' ','') AS EE_SNAME, PERS_AREA, BIC_ZPERS_A_N
, PERS_SAREA, BIC_ZPERSSA_N, ENTRYDATE
, BIC_ZORGUNIT, BIC_ZORG_T
, HRPOSITION, BIC_ZHRPOS_N
, BIC_ZPOS_ATTR, BIC_ZPOS_A_N
, BIC_ZHRIC189, BIC_ZHRIC205
, BIC_ZHRIC206, BIC_ZHRIC208, BIC_ZHRIC207
, JOB, BIC_ZJOB_N
, BIC_ZSGRADE, BIC_ZGRADE_N
, GENDER, BIC_ZHRIC209
, BIC_ZHRIK029
FROM RAWWANT.BW_SAPBHP_BIC_AZHR_O7100