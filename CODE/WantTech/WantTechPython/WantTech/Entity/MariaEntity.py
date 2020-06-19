from enum import Enum

class EnumMariaParameterType(Enum):
    Object = 0
    Char = 1
    Int = 2
    Numeric = 3
    DateTime = 4

class MariaParameter:
    strOperator = None
    objValue = None
    enumType = EnumMariaParameterType.Object
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
                strSQLCommand = self.strKey + " IS NOT NULL"
            elif self.strOperator == "=":
                strSQLCommand = self.strKey + " IS NULL"
            else:
                strSQLCommand = "NULL"
        elif isinstance(self.objValue, list) and self.strOperator == "IN":
            strSQLCommand = self.strKey + " IN " + "('" +"','".join(self.objValue) + "')"
        else:
            strValue = str(self.objValue).replace("'", "''")

            if self.enumType == EnumMariaParameterType.Object:
                strSQLCommand = strValue
            elif self.enumType == EnumMariaParameterType.Char or self.enumType == EnumMariaParameterType.DateTime:
                if self.strOperator == None:
                    strSQLCommand = "'" + strValue + "'"
                else:
                    strSQLCommand = self.strKey + self.strOperator + "'" + strValue + "'"
            elif self.enumType == EnumMariaParameterType.Int or self.enumType == EnumMariaParameterType.Numeric:
                if self.strOperator == None:
                    strSQLCommand = strValue
                else:
                    strSQLCommand = self.strKey + self.strOperator + strValue

        return strSQLCommand
