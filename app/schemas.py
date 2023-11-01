from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    is_active: bool = True 
    
    
class UserAuth(User):
    password: str 
    
class LabRoom(BaseModel):
    name: str
    description: str
    is_active: bool = True
    
    
class Student(User):
    is_monitor: bool = True


class Professor(User):
    discipline: str