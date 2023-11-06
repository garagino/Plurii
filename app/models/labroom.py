from sqlalchemy import Boolean, Column, Integer, String, DateTime
from app.database import Base


class LabRoom(Base):
    __tablename__ = "lab_rooms"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)
    description = Column(String(50))
    is_active = Column(Boolean, default=True)
    in_use = Column(Boolean, default=False)
    last_used = Column(DateTime)