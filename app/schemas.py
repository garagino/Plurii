from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    password: str
    is_active: bool = True
    is_superuser: bool = False