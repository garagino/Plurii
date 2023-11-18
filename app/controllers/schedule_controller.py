from sqlalchemy.orm import Session
from app.models.schedule import Schedule
from app.schemas.schedule import ScheduleUpdate
from app.mediator.labroom_mediator import LabRoomMediator
from datetime import date, time, datetime

class scheduleController:
    def create_schedule(self, db:Session, schedule:Schedule):
        db_schedule = Schedule(**schedule.dict())
        db.add(db_schedule)
        db.commit()
        db.refresh(db_schedule)
        return db_schedule
    
    def get_schedule_by_room(self, db:Session, room_id:int):
        return db.query(Schedule).filter(Schedule.idRoom == room_id).all()

    def get_schedule_by_user(self, db:Session, user_id:int):
        return db.query(Schedule).filter(Schedule.idUser == user_id).all()
    
    def get_schedule_by_datetime(self, db:Session, datetime_param: datetime, room_id:int = None):
        if room_id is None:
            return db.query(Schedule).filter(Schedule.scheduleDateTime == datetime_param).all()
        else:
            return db.query(Schedule).filter(Schedule.scheduleDateTime == datetime_param, Schedule.idRoom == room_id).all()
        
    def get_schedule_by_id(self, db:Session, id_schedule:int):
        return db.query(Schedule).filter(Schedule.id == id_schedule).first()
    
    def update_schedule_parameter(self, db: Session, id_schedule: int, schedule_update: ScheduleUpdate):
        db_schedule = db.query(Schedule).filter(Schedule.id == id_schedule).first()

        if db_schedule:
            for key, value in schedule_update.dict(exclude_unset=True).items():
                setattr(db_schedule, key, value)

            db.commit()
            db.refresh(db_schedule)
        return db_schedule
    
    



