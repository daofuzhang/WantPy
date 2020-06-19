from enum import Enum

class EnumEDIStatusID(Enum):
    W = 0
    B = 1
    F = 2

class EnumEDIResultID(Enum):
    S = 0
    F = 1
    C = 2

class EnumFlowResult(Enum):
    Null = 0
    Success = 1
    Failure = 2
    Cancel = 3

class EnumJobResult(Enum):
    Null = 0
    Success = 1
    Failure = 2
    Cancel = 3

class EnumScheduleFrequency(Enum):
    Continuity = 1
    Daily = 2
    Monthly = 4

class EnumJobType(Enum):
    EDITrigNextFlow = 0
    HanaDBExport = 11
    OracleDBExport = 21
    MariaDBExport = 31
    MariaDBImport = 32
    MariaDBExecuteProcedures = 33
    PythonExecute = 99

class EnumJobDBImportUseRES(Enum):
    Y = 0
    N = 1
