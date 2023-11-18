import re
from datetime import datetime, timedelta
from fastapi import status
from decouple import config
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.schemas.schedule import ScheduleCreate, ScheduleUpdate
from app.controllers.schedule_controller import scheduleController
from app.models.schedule import Schedule
from datetime import date, time, datetime
from app.mediator.user_mediator import UserMediator
from app.schemas.user import UserCreate
from app.models.labroom import LabRoom
from app.schemas.labroom import LabRoomCreate, LabRoomUpdate
from app.mediator.user_mediator import UserMediator
from app.mediator.labroom_mediator import LabRoomMediator
from app.controllers.labroom_controller import LabRoomController

class ScheduleMediator:
    def __init__(self, db:Session):
        self.schedule_controller = scheduleController()
        self.db = db 
        self.user_mediator = UserMediator(db)
        self.labroom_mediator = LabRoomMediator(db)

    def validate_hour(self, hour:time):
        exist_schedule = self.schedule_controller.get_schedule_by_hour(hour)
        if exist_schedule: 
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Horario nao disponivel")
        if hour < "08:00:00" or hour > "18:00:00":
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Fora horario de funcionamento")
    
    def validate_date(self, date: date):
        exist_schedule = self.schedule_controller.get_schedule_by_date(date)
        if exist_schedule:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Data nao disponivel")
        if date.weekday() == 1 or date.weekday() == 7:
            
            
            
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Data nao disponivel")



