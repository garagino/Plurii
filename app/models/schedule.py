from sqlalchemy import Boolean, Column, Integer, String, Date, Time, ForeignKey, DateTime
from app.database import Base
from user import User
from labroom import LabRoom

class Schedule(Base):
    __tablename__ = "schedule"
    id = Column(Integer, primary_key=True, unique=True, index=True)
    idRoom = Column(Integer, ForeignKey(LabRoom.id))
    idUser = Column(Integer, ForeignKey(User.id))
    scheduleDate = Column(Date, default =True)
    scheduleHour = Column(Time, default =True)
    infAdicional = Column(String(50))
    approvalDateHour = Column(DateTime, default =True)
    approvalStatus = Column(String(20), default="Disponivel")
    idApproval = Column(Integer, ForeignKey(User.id))
    approvalNotes = Column(String)
