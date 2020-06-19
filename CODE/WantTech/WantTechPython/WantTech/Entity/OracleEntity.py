from enum import Enum

class EnumOracleParameterType(Enum):
    Object = 0
    Char = 1
    Number = 3

class OracleParameter:
    strOperator = None
    objValue = None
    enumType = EnumOracleParameterType.Object
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

            if self.enumType == EnumOracleParameterType.Object:
                strSQLCommand = strValue
            elif self.enumType == EnumOracleParameterType.Char:
                if self.strOperator == None:
                    strSQLCommand = "'" + strValue + "'"
                else:
                    strSQLCommand = self.strKey + self.strOperator + "'" + strValue + "'"
            elif self.enumType == EnumOracleParameterType.Number:
                if self.strOperator == None:
                    strSQLCommand = strValue
                else:
                    strSQLCommand = self.strKey + self.strOperator + strValue

        return strSQLCommand
