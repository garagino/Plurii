from sqlalchemy import Boolean, Column, Integer, String, Date, Time, ForeignKey, DateTime
from app.database import Base
from app.models.user import User
from app.models.labroom import LabRoom
from datetime import datetime

class Schedule(Base):
    __tablename__ = "schedule"
    id = Column(Integer, primary_key=True, unique=True, index=True)
    idRoom = Column(Integer, ForeignKey(LabRoom.id))
    idUser = Column(Integer, ForeignKey(User.id))
    scheduleDateTime = Column(DateTime, default=datetime.utcnow)
    infAdicional = Column(String(50), nullable=True)
    approvalDateHour = Column(DateTime, nullable=True)
    approvalStatus = Column(String(20), default="Disponivel")
    idApproval = Column(Integer, ForeignKey(User.id), nullable=True)
    approvalNotes = Column(String, nullable=True)

