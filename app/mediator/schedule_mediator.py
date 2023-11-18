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

    def validate_datetime(self, datetime_param:datetime, room_id:int = None):
        exist_schedule = self.schedule_controller.get_schedule_by_datetime(self.db,datetime_param, room_id)
        if exist_schedule: 
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Horario nao disponivel")
        if datetime_param.time() < time(8, 0) or datetime_param.time() > time(18, 0):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Fora horario de funcionamento")
        if datetime_param.date() < date.today():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Data invalida")
        if datetime_param.date() == date.today() and datetime_param.time() < datetime.now().time():
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Horario invalido")
        if datetime_param.weekday() == 5 or datetime_param.weekday() == 6:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Fora horario de funcionamento")
    
        
        
    def create_schedule(self, schedule:ScheduleCreate):
        self.validate_datetime(schedule.scheduleDateTime, schedule.idRoom)
        return self.schedule_controller.create_schedule(self.db, schedule)



    def update_schedule(self, db: Session, schedule_update: ScheduleUpdate, id_schedule: int):
        return self.schedule_controller.update_schedule_parameter(db, id_schedule, schedule_update)