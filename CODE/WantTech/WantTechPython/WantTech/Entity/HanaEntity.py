from enum import Enum

class EnumHanaParameterType(Enum):
    Object = 0
    Char = 1
    Integer = 2
    Decimal = 3
    Double = 31

class HanaParameter:
    strOperator = None
    objValue = None
    enumType = EnumHanaParameterType.Object
    strKey = None

    def __init__(self, objValue, enumType, strOperator=None):
        self.strOperator = strOperator
        self.objValue = objValue
        self.enumType = enumType

    def setParameterKey(self, strKey):
        self.strKey = strKey
        return True

    def getSQLCommand(self):
        strSQLCommand = ""
        strValue = ""

        if self.objValue == None:
            if self.strOperator == "<>":
                strSQLCommand = "\"" + self.strKey + "\" IS NOT NULL"
            elif self.strOperator == "=":
                strSQLCommand = "\"" + self.strKey + "\" IS NULL"
            else:
                strSQLCommand = "NULL"
        elif isinstance(self.objValue, list) and self.strOperator == "IN":
            strSQLCommand = "\"" + self.strKey + "\" IN " + "('" +"','".join(self.objValue) + "')"
        else:
            strValue = str(self.objValue).replace("'", "''")

            if self.enumType == EnumHanaParameterType.Object:
                strSQLCommand = strValue
            elif self.enumType == EnumHanaParameterType.Char:
                if self.strOperator == None:
                    strSQLCommand = "'" + strValue + "'"
                else:
                    strSQLCommand = "\"" + self.strKey + "\"" + self.strOperator + "'" + strValue + "'"
            elif self.enumType == EnumHanaParameterType.Integer or self.enumType == EnumHanaParameterType.Decimal or self.enumType == EnumHanaParameterType.Double:
                if self.strOperator == None:
                    strSQLCommand = strValue
                else:
                    strSQLCommand = "\"" + self.strKey + "\"" + self.strOperator + strValue

        return strSQLCommand
