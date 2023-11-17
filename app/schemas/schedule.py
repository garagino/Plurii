from pydantic import BaseModel
from datetime import datetime, date, time
from enum import Enum

class ScheduleEnum(str, Enum):
    DISPONIVEL =  "disponivel"
    EM_APROVACAO = "em aprovacao"
    APROVADO = "aprovado"
    CANCELADO = "cancelado pelo usuario"
    NAO_AUTORIZADO = "nao autorizado"

class ScheduleCreate(BaseModel):
    idRoom: int
    idUser: int
    scheduleDate: date
    scheduleHour: time
    infAdicional: str
    approvalDateHour: datetime 
    approvalStatus: ScheduleEnum
    idApproval: int
    approvalNotes: str

class ScheduleUpdate(ScheduleCreate):
    pass

