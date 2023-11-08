from re import U
from urllib import response
from pydantic import BaseModel, EmailStr, validator
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
    user_function: FunctionEnum
    user_role: FunctionRole
    


class UserBase(UserCreate):
    response: Optional[str] = "User created successfully"

    class Config:
        orm_mode = True
        
        
class UserUpdate(UserCreate):
    pass