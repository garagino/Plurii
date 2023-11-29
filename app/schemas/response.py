from pydantic import BaseModel



class UserCreateResponse(BaseModel):
    response: str

class LabRoomCreateResponse(BaseModel):
    response: str
    
    
class ScheduleCreateResponse(BaseModel):
    response: str