from pydantic import BaseModel


class LabRoomCreate(BaseModel):
    name: str
    capacity: str
    description: str
    in_use: bool
    is_active: bool = True

class LabRoomUpdate(LabRoomCreate):
    pass