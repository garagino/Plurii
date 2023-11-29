from pydantic import BaseModel


class LabRoomCreate(BaseModel):
    name: str
    capacity: int
    description: str
    in_use: bool = False
    is_active: bool = True

class LabRoomUpdate(LabRoomCreate):
    pass