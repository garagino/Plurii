from pydantic import BaseModel
from datetime import datetime, date, time
from enum import Enum
from typing import Optional

class ScheduleEnum(str, Enum):
    DISPONIVEL =  "disponivel"
    EM_APROVACAO = "em aprovacao"
    APROVADO = "aprovado"
    CANCELADO = "cancelado pelo usuario"
    NAO_AUTORIZADO = "nao autorizado"

class ScheduleCreate(BaseModel):
    idRoom: Optional[int]
    idUser: Optional[int]
    scheduleDateTime: Optional[datetime] 
    infAdicional: Optional[str]
    approvalDateHour: Optional[datetime] 
    approvalStatus: Optional[ScheduleEnum]
    idApproval: Optional[int] = None
    approvalNotes: Optional[str]

class ScheduleUpdate(ScheduleCreate):
    pass

