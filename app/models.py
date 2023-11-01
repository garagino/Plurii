from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(50), unique=True, index=True)
    password = Column(String(50))
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    

class LabRoom(Base):
    __tablename__ = "lab_rooms"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)
    description = Column(String(50))
    is_active = Column(Boolean, default=True)
    in_use = Column(Boolean, default=False)
    last_used = Column(DateTime)