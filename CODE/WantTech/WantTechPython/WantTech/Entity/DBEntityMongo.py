from Utility import Security

def getMongoConnectionString(strConnection, strDB):
    strPassword = ""
    strReturn = ""

    if strConnection == "2RAW-RAWreader@tpe-centos7-mongo3-01":
        strPassword = "92FZ0EwMn02zLEAUXTRPLdwwJ+25DzzUV91Tj3OWX0Y="
        if strDB == "RAWEXT":
            strReturn = "mongodb://RAWreader:%s@10.231.8.167:27017/RAWEXT"
        elif strDB == "RAWWANT":
            strReturn = "mongodb://RAWreader:%s@10.231.8.167:27017/RAWWANT"

    elif strConnection == "2RAW-RAWuser@tpe-centos7-mongo3-01":
        strPassword = "AgRXR7EO+7UAYnBRwcQHv93b/LkQRaJjpmNDDWRHgRw="
        if strDB == "RAWEXT":
            strReturn = "mongodb://RAWuser:%s@10.231.8.167:27017/RAWEXT"
        elif strDB == "RAWWANT":
            strReturn = "mongodb://RAWuser:%s@10.231.8.167:27017/RAWWANT"

    elif strConnection == "3DW-DWreader@tpe-centos7-mongo3-01":
        strPassword = "RQILQOqcUwzQiFFxHDIFuMLE8zlQzo8K4YtL94mtOYw="
        if strDB == "DWEXT":
            strReturn = "mongodb://DWreader:%s@10.231.8.167:27017/DWEXT"
        elif strDB == "DWWANT":
            strReturn = "mongodb://DWreader:%s@10.231.8.167:27017/DWWANT"

    elif strConnection == "3DW-DWuser@tpe-centos7-mongo3-01":
        strPassword = "NqmeL8YJNtmKue8dYCvng8QXHYCx1BZkxOP+7z2HsT0="
        if strDB == "DWEXT":
            strReturn = "mongodb://DWuser:%s@10.231.8.167:27017/DWEXT"
        elif strDB == "DWWANT":
            strReturn = "mongodb://DWuser:%s@10.231.8.167:27017/DWWANT"

    elif strConnection == "5AP1-APreader@tpe-centos7-mongo3-01":
        strPassword = "JQqopkvSibwlnni6sDa5mN3Q1yL8FcM0MqrZPtm2sjw="
        if strDB == "APWANT":
            strReturn = "mongodb://APreader:%s@10.231.8.167:27017/APWANT"
        elif strDB == "APWX":
            strReturn = "mongodb://APreader:%s@10.231.8.167:27017/APWX"

    elif strConnection == "5AP1-APuser@tpe-centos7-mongo3-01":
        strPassword = "kel4uis6gFBGvkA0bXSlBQO518hPJ3/jII2ZIFJ5MOE="
        if strDB == "APWANT":
            strReturn = "mongodb://APuser:%s@10.231.8.167:27017/APWANT"
        elif strDB == "APWX":
            strReturn = "mongodb://APuser:%s@10.231.8.167:27017/APWX"

    return (strReturn % Security.decrypt(strPassword))
