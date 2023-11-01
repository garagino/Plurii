from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from .database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(50), unique=True, index=True)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    

class UserAuth(User):
    __tablename__ = "user_auths"
    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    password = Column(String(50))
    

class LabRoom(Base):
    __tablename__ = "lab_rooms"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)
    description = Column(String(50))
    is_active = Column(Boolean, default=True)
    in_use = Column(Boolean, default=False)
    last_used = Column(DateTime)
    
    
class Student(User):
    __tablename__ = "students"
    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    is_monitor = Column(Boolean, default=False)
    
class Professor(User):
    __tablename__ = "professors"
    id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    discipline = Column(String(50))