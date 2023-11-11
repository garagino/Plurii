from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from app.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, unique=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(50), unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    user_function = Column(String(50), default="user")
    user_role = Column(String(50), default="student")