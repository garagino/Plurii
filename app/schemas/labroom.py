from pydantic import BaseModel


class LabRoom(BaseModel):
    name: str
    description: str
    is_active: bool = True