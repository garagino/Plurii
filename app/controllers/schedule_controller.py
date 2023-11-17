from sqlalchemy.orm import Session
from app.models.schedule import Schedule
from app.schemas.schedule import ScheduleUpdate
from app.mediator.labroom_mediator import LabRoomMediator
from datetime import date, time, datetime

class scheduleController:
    def create_schedule(self, db:Session, schedule:Schedule):
        db_schedule = Schedule()
        db_schedule.idUser = schedule.idUser
        db_schedule.idRoom = schedule.idRoom
        db_schedule.scheduleDate = schedule.scheduleDate
        db_schedule.scheduleHour = schedule.scheduleHour
        db_schedule.infAdicional = schedule.infAdicional
        db_schedule.approvalDateHour = schedule.approvalDateHour
        db_schedule.idApproval = schedule.idApproval
        db_schedule.approvalStatus = schedule.approvalStatus
        db_schedule.approvalNotes = schedule.approvalNotes

        db.add(db_schedule)
        db.commit()
        db.refresh(db_schedule)
        return db_schedule
    
    def get_schedule_by_room(self, db:Session, room_id:int):
        return db.query(Schedule).filter(Schedule.idRoom == room_id).all()

    def get_schedule_by_user(self, db:Session, user_id:int):
        return db.query(Schedule).filter(Schedule.idUser == user_id).all()
    
    def get_schedule_by_date(self, db:Session, date: date):
        return db.query(Schedule).filter(Schedule.scheduleDate == date).all()
    
    def get_schedule_by_hour(self, db:Session, hour: time):
        return db.query(Schedule).filter(Schedule.scheduleHour == hour).all()
    
    def update_schedule(self, db:Session, schedule:ScheduleUpdate, id_schedule: int):
        db_schedule = db.query(Schedule).filter(Schedule.id == id_schedule).first()
        for key, value in schedule.dict(exclude_unset=True).items():
            setattr(db_schedule, key, value)
        
        db.commit()
        db.refresh(db_schedule)
        return db_schedule
    
    



