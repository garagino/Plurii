from pydantic import BaseModel
from enum import Enum

class FunctionEnum(str, Enum):
    ADMIN = "admin"
    USER = "user"

class UserBase(BaseModel):
    username: str
    email: str
    is_active: bool = True
    user_function: FunctionEnum

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True