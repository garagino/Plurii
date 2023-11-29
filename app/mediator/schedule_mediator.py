import re
from datetime import datetime
from fastapi import status
from decouple import config
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.schemas.schedule import ScheduleCreate, ScheduleUpdate
from app.controllers.schedule_controller import scheduleController
from datetime import date, time, datetime
from app.mediator.user_mediator import UserMediator
from app.mediator.user_mediator import UserMediator
from app.mediator.labroom_mediator import LabRoomMediator

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
    
    
    
    def get_schedule_by_room(self, room_id:int):
        exist_schedule = self.schedule_controller.get_schedule_by_room(self.db, room_id)
        exist_room = self.labroom_mediator.get_labroom_by_id(room_id)
        if not exist_room:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Sala nao encontrada")
        if not exist_schedule: 
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Nao existem agendamentos para esta sala")
        
        
        
    def get_schedule_by_user(self, email:str):
        user_id = self.user_mediator.get_user_by_email(email).id
        exist_user = self.user_mediator.get_user_by_id(user_id)
        exist_schedule = self.schedule_controller.get_schedule_by_user(self.db, user_id)
        if not exist_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario nao encontrado")
        if not exist_schedule: 
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Nao existem agendamentos para este usuario")
        return exist_schedule
    
    def update_schedule_status(self,  schedule_id: int, schedule_update: ScheduleUpdate, db: Session, email: str):
        db_schedule = self.schedule_controller.get_schedule_by_id(db, schedule_id)
        is_adm_user = self.user_mediator.get_user_by_email(email).user_function
        if is_adm_user != "admin":
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario nao autorizado")
        else:
            id_admin = self.user_mediator.get_user_by_email(email).id
        if not db_schedule:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Agendamento nao encontrado")
        
        return self.schedule_controller.update_schedule_status(db, schedule_id, schedule_update, id_admin)