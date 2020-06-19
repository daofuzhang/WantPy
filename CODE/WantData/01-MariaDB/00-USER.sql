--RAW
CREATE USER 'RAWdbo'@'localhost';
CREATE USER 'RAWdbo'@'%';

CREATE USER 'RAWuser'@'localhost';
CREATE USER 'RAWuser'@'%';

CREATE USER 'RAWreader'@'localhost';
CREATE USER 'RAWreader'@'%';

GRANT FILE ON *.* TO 'RAWdbo'@'localhost';
GRANT FILE ON *.* TO 'RAWdbo'@'%';

GRANT ALL ON RAWEXT.* TO 'RAWdbo'@'localhost' IDENTIFIED BY '密碼';
GRANT ALL ON RAWEXT.* TO 'RAWdbo'@'%' IDENTIFIED BY '密碼';

GRANT SELECT,INSERT,UPDATE,DELETE ON RAWEXT.* TO 'RAWuser'@'localhost' IDENTIFIED BY '密碼';
GRANT SELECT,INSERT,UPDATE,DELETE ON RAWEXT.* TO 'RAWuser'@'%' IDENTIFIED BY '密碼';
GRANT EXECUTE ON RAWEXT.* TO 'RAWuser'@'localhost' IDENTIFIED BY '密碼';
GRANT EXECUTE ON RAWEXT.* TO 'RAWuser'@'%' IDENTIFIED BY '密碼';

GRANT SELECT ON RAWEXT.* TO 'RAWreader'@'localhost' IDENTIFIED BY '密碼';
GRANT SELECT ON RAWEXT.* TO 'RAWreader'@'%' IDENTIFIED BY '密碼';

GRANT ALL ON RAWWANT.* TO 'RAWdbo'@'localhost' IDENTIFIED BY '密碼';
GRANT ALL ON RAWWANT.* TO 'RAWdbo'@'%' IDENTIFIED BY '密碼';

GRANT SELECT,INSERT,UPDATE,DELETE ON RAWWANT.* TO 'RAWuser'@'localhost' IDENTIFIED BY '密碼';
GRANT SELECT,INSERT,UPDATE,DELETE ON RAWWANT.* TO 'RAWuser'@'%' IDENTIFIED BY '密碼';
GRANT EXECUTE ON RAWWANT.* TO 'RAWuser'@'localhost' IDENTIFIED BY '密碼';
GRANT EXECUTE ON RAWWANT.* TO 'RAWuser'@'%' IDENTIFIED BY '密碼';

GRANT SELECT ON RAWWANT.* TO 'RAWreader'@'localhost' IDENTIFIED BY '密碼';
GRANT SELECT ON RAWWANT.* TO 'RAWreader'@'%' IDENTIFIED BY '密碼';

FLUSH PRIVILEGES;

--DW
CREATE USER 'DWdbo'@'localhost';
CREATE USER 'DWdbo'@'%';

CREATE USER 'DWuser'@'localhost';
CREATE USER 'DWuser'@'%';

CREATE USER 'DWreader'@'localhost';
CREATE USER 'DWreader'@'%';

GRANT FILE ON *.* TO 'DWdbo'@'localhost';
GRANT FILE ON *.* TO 'DWdbo'@'%';

GRANT ALL ON RAWEXT.* TO 'DWdbo'@'localhost' IDENTIFIED BY '密碼';
GRANT ALL ON RAWEXT.* TO 'DWdbo'@'%' IDENTIFIED BY '密碼';

GRANT SELECT,INSERT,UPDATE,DELETE ON RAWEXT.* TO 'DWuser'@'localhost' IDENTIFIED BY '密碼';
GRANT SELECT,INSERT,UPDATE,DELETE ON RAWEXT.* TO 'DWuser'@'%' IDENTIFIED BY '密碼';
GRANT EXECUTE ON RAWEXT.* TO 'DWuser'@'localhost' IDENTIFIED BY '密碼';
GRANT EXECUTE ON RAWEXT.* TO 'DWuser'@'%' IDENTIFIED BY '密碼';

GRANT SELECT ON RAWEXT.* TO 'DWreader'@'localhost' IDENTIFIED BY '密碼';
GRANT SELECT ON RAWEXT.* TO 'DWreader'@'%' IDENTIFIED BY '密碼';

GRANT ALL ON RAWWANT.* TO 'DWdbo'@'localhost' IDENTIFIED BY '密碼';
GRANT ALL ON RAWWANT.* TO 'DWdbo'@'%' IDENTIFIED BY '密碼';

GRANT SELECT,INSERT,UPDATE,DELETE ON RAWWANT.* TO 'DWuser'@'localhost' IDENTIFIED BY '密碼';
GRANT SELECT,INSERT,UPDATE,DELETE ON RAWWANT.* TO 'DWuser'@'%' IDENTIFIED BY '密碼';
GRANT EXECUTE ON RAWWANT.* TO 'DWuser'@'localhost' IDENTIFIED BY '密碼';
GRANT EXECUTE ON RAWWANT.* TO 'DWuser'@'%' IDENTIFIED BY '密碼';

GRANT SELECT ON RAWWANT.* TO 'DWreader'@'localhost' IDENTIFIED BY '密碼';
GRANT SELECT ON RAWWANT.* TO 'DWreader'@'%' IDENTIFIED BY '密碼';

GRANT ALL ON DWEXT.* TO 'DWdbo'@'localhost' IDENTIFIED BY '密碼';
GRANT ALL ON DWEXT.* TO 'DWdbo'@'%' IDENTIFIED BY '密碼';

GRANT SELECT,INSERT,UPDATE,DELETE ON DWEXT.* TO 'DWuser'@'localhost' IDENTIFIED BY '密碼';
GRANT SELECT,INSERT,UPDATE,DELETE ON DWEXT.* TO 'DWuser'@'%' IDENTIFIED BY '密碼';
GRANT EXECUTE ON DWEXT.* TO 'DWuser'@'localhost' IDENTIFIED BY '密碼';
GRANT EXECUTE ON DWEXT.* TO 'DWuser'@'%' IDENTIFIED BY '密碼';

GRANT SELECT ON DWEXT.* TO 'DWreader'@'localhost' IDENTIFIED BY '密碼';
GRANT SELECT ON DWEXT.* TO 'DWreader'@'%' IDENTIFIED BY '密碼';

GRANT ALL ON DWWANT.* TO 'DWdbo'@'localhost' IDENTIFIED BY '密碼';
GRANT ALL ON DWWANT.* TO 'DWdbo'@'%' IDENTIFIED BY '密碼';

GRANT SELECT,INSERT,UPDATE,DELETE ON DWWANT.* TO 'DWuser'@'localhost' IDENTIFIED BY '密碼';
GRANT SELECT,INSERT,UPDATE,DELETE ON DWWANT.* TO 'DWuser'@'%' IDENTIFIED BY '密碼';
GRANT EXECUTE ON DWWANT.* TO 'DWuser'@'localhost' IDENTIFIED BY '密碼';
GRANT EXECUTE ON DWWANT.* TO 'DWuser'@'%' IDENTIFIED BY '密碼';

GRANT SELECT ON DWWANT.* TO 'DWreader'@'localhost' IDENTIFIED BY '密碼';
GRANT SELECT ON DWWANT.* TO 'DWreader'@'%' IDENTIFIED BY '密碼';

GRANT ALL ON DMMDL.* TO 'DWdbo'@'localhost' IDENTIFIED BY '密碼';
GRANT ALL ON DMMDL.* TO 'DWdbo'@'%' IDENTIFIED BY '密碼';

GRANT SELECT,INSERT,UPDATE,DELETE ON DMMDL.* TO 'DWuser'@'localhost' IDENTIFIED BY '密碼';
GRANT SELECT,INSERT,UPDATE,DELETE ON DMMDL.* TO 'DWuser'@'%' IDENTIFIED BY '密碼';
GRANT EXECUTE ON DMMDL.* TO 'DWuser'@'localhost' IDENTIFIED BY '密碼';
GRANT EXECUTE ON DMMDL.* TO 'DWuser'@'%' IDENTIFIED BY '密碼';

GRANT SELECT ON DMMDL.* TO 'DWreader'@'localhost' IDENTIFIED BY '密碼';
GRANT SELECT ON DMMDL.* TO 'DWreader'@'%' IDENTIFIED BY '密碼';

FLUSH PRIVILEGES;

--DM
CREATE USER 'DMdbo'@'localhost';
CREATE USER 'DMdbo'@'%';

CREATE USER 'DMuser'@'localhost';
CREATE USER 'DMuser'@'%';

CREATE USER 'DMreader'@'localhost';
CREATE USER 'DMreader'@'%';

GRANT FILE ON *.* TO 'DMdbo'@'localhost';
GRANT FILE ON *.* TO 'DMdbo'@'%';

GRANT ALL ON DMMDL.* TO 'DMdbo'@'localhost' IDENTIFIED BY '密碼';
GRANT ALL ON DMMDL.* TO 'DMdbo'@'%' IDENTIFIED BY '密碼';

GRANT SELECT,INSERT,UPDATE,DELETE ON DMMDL.* TO 'DMuser'@'localhost' IDENTIFIED BY '密碼';
GRANT SELECT,INSERT,UPDATE,DELETE ON DMMDL.* TO 'DMuser'@'%' IDENTIFIED BY '密碼';
GRANT EXECUTE ON DMMDL.* TO 'DMuser'@'localhost' IDENTIFIED BY '密碼';
GRANT EXECUTE ON DMMDL.* TO 'DMuser'@'%' IDENTIFIED BY '密碼';

GRANT SELECT ON DMMDL.* TO 'DMreader'@'localhost' IDENTIFIED BY '密碼';
GRANT SELECT ON DMMDL.* TO 'DMreader'@'%' IDENTIFIED BY '密碼';

GRANT ALL ON APWX.* TO 'DMdbo'@'localhost' IDENTIFIED BY '密碼';
GRANT ALL ON APWX.* TO 'DMdbo'@'%' IDENTIFIED BY '密碼';

GRANT SELECT,INSERT,UPDATE,DELETE ON APWX.* TO 'DMuser'@'localhost' IDENTIFIED BY '密碼';
GRANT SELECT,INSERT,UPDATE,DELETE ON APWX.* TO 'DMuser'@'%' IDENTIFIED BY '密碼';
GRANT EXECUTE ON APWX.* TO 'DMuser'@'localhost' IDENTIFIED BY '密碼';
GRANT EXECUTE ON APWX.* TO 'DMuser'@'%' IDENTIFIED BY '密碼';

GRANT SELECT ON APWX.* TO 'DMreader'@'localhost' IDENTIFIED BY '密碼';
GRANT SELECT ON APWX.* TO 'DMreader'@'%' IDENTIFIED BY '密碼';

GRANT ALL ON APDC.* TO 'DMdbo'@'localhost' IDENTIFIED BY '密碼';
GRANT ALL ON APDC.* TO 'DMdbo'@'%' IDENTIFIED BY '密碼';

GRANT SELECT,INSERT,UPDATE,DELETE ON APDC.* TO 'DMuser'@'localhost' IDENTIFIED BY '密碼';
GRANT SELECT,INSERT,UPDATE,DELETE ON APDC.* TO 'DMuser'@'%' IDENTIFIED BY '密碼';
GRANT EXECUTE ON APDC.* TO 'DMuser'@'localhost' IDENTIFIED BY '密碼';
GRANT EXECUTE ON APDC.* TO 'DMuser'@'%' IDENTIFIED BY '密碼';

GRANT SELECT ON APDC.* TO 'DMreader'@'localhost' IDENTIFIED BY '密碼';
GRANT SELECT ON APDC.* TO 'DMreader'@'%' IDENTIFIED BY '密碼';

FLUSH PRIVILEGES;

--AP1
CREATE USER 'APdbo'@'localhost';
CREATE USER 'APdbo'@'%';

CREATE USER 'APuser'@'localhost';
CREATE USER 'APuser'@'%';

CREATE USER 'APreader'@'localhost';
CREATE USER 'APreader'@'%';

GRANT FILE ON *.* TO 'APdbo'@'localhost';
GRANT FILE ON *.* TO 'APdbo'@'%';

GRANT ALL ON APWANT.* TO 'APdbo'@'localhost' IDENTIFIED BY '密碼';
GRANT ALL ON APWANT.* TO 'APdbo'@'%' IDENTIFIED BY '密碼';

GRANT SELECT,INSERT,UPDATE,DELETE ON APWANT.* TO 'APuser'@'localhost' IDENTIFIED BY '密碼';
GRANT SELECT,INSERT,UPDATE,DELETE ON APWANT.* TO 'APuser'@'%' IDENTIFIED BY '密碼';
GRANT EXECUTE ON APWANT.* TO 'APuser'@'localhost' IDENTIFIED BY '密碼';
GRANT EXECUTE ON APWANT.* TO 'APuser'@'%' IDENTIFIED BY '密碼';

GRANT SELECT ON APWANT.* TO 'APreader'@'localhost' IDENTIFIED BY '密碼';
GRANT SELECT ON APWANT.* TO 'APreader'@'%' IDENTIFIED BY '密碼';

GRANT ALL ON APDC.* TO 'APdbo'@'localhost' IDENTIFIED BY '密碼';
GRANT ALL ON APDC.* TO 'APdbo'@'%' IDENTIFIED BY '密碼';

GRANT SELECT,INSERT,UPDATE,DELETE ON APDC.* TO 'APuser'@'localhost' IDENTIFIED BY '密碼';
GRANT SELECT,INSERT,UPDATE,DELETE ON APDC.* TO 'APuser'@'%' IDENTIFIED BY '密碼';
GRANT EXECUTE ON APDC.* TO 'APuser'@'localhost' IDENTIFIED BY '密碼';
GRANT EXECUTE ON APDC.* TO 'APuser'@'%' IDENTIFIED BY '密碼';

GRANT SELECT ON APDC.* TO 'APreader'@'localhost' IDENTIFIED BY '密碼';
GRANT SELECT ON APDC.* TO 'APreader'@'%' IDENTIFIED BY '密碼';

GRANT ALL ON APWX.* TO 'APdbo'@'localhost' IDENTIFIED BY '密碼';
GRANT ALL ON APWX.* TO 'APdbo'@'%' IDENTIFIED BY '密碼';

GRANT SELECT,INSERT,UPDATE,DELETE ON APWX.* TO 'APuser'@'localhost' IDENTIFIED BY '密碼';
GRANT SELECT,INSERT,UPDATE,DELETE ON APWX.* TO 'APuser'@'%' IDENTIFIED BY '密碼';
GRANT EXECUTE ON APWX.* TO 'APuser'@'localhost' IDENTIFIED BY '密碼';
GRANT EXECUTE ON APWX.* TO 'APuser'@'%' IDENTIFIED BY '密碼';

GRANT SELECT ON APWX.* TO 'APreader'@'localhost' IDENTIFIED BY '密碼';
GRANT SELECT ON APWX.* TO 'APreader'@'%' IDENTIFIED BY '密碼';

FLUSH PRIVILEGES;
