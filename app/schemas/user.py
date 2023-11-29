from re import U
from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum


class FunctionEnum(str, Enum):
    USER = "user"
    ADMIN = "admin"
    
    
class FunctionRole(str, Enum):
    STUDENT = "student"
    TEACHER = "teacher"
    MONITOR = "monitor"


class UserAuth(BaseModel):
    email: EmailStr
    password: str


class UserCreate(UserAuth):
    username: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    user_function: FunctionEnum = FunctionEnum.USER
    user_role: FunctionRole = FunctionRole.STUDENT
        
class UserUpdate(UserCreate):
    pass