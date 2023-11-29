from pydantic import BaseModel
from datetime import datetime, date, time
from enum import Enum
from typing import Optional


class ScheduleEnum(str, Enum):
    EM_APROVACAO = "em aprovacao"
    DISPONIVEL =  "disponivel"
    
    APROVADO = "aprovado"
    CANCELADO = "cancelado pelo usuario"
    NAO_AUTORIZADO = "nao autorizado"

class ScheduleCreate(BaseModel):
    idRoom: Optional[int]
    idUser: Optional[int]
    scheduleDateTime: Optional[datetime] = datetime.now()
    infAdicional: Optional[str]
    approvalStatus: Optional[ScheduleEnum] = ScheduleEnum.EM_APROVACAO


class ScheduleUpdate(ScheduleCreate):
    approvalDateHour: Optional[datetime] = datetime.now()
    idApproval: Optional[int] = None
    approvalNotes: Optional[str]
