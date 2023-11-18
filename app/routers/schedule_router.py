from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.schedule import ScheduleCreate, ScheduleUpdate
from app.mediator.schedule_mediator import ScheduleMediator
from app.schemas.response import ScheduleCreateResponse
from app.database import get_db
from pydantic import ValidationError
from fastapi.responses import JSONResponse
from app.depends import auth_wrapper

router = APIRouter()

@router.post("/schedules/", response_model=ScheduleCreateResponse)
def create_schedule_route(schedule: ScheduleCreate, db: Session = Depends(get_db), email = Depends(auth_wrapper)):
    try:
        ScheduleMediator(db).create_schedule(schedule)
        response_data = {"response": "Schedule created successfully"}
        return ScheduleCreateResponse(**response_data)
    except ValidationError as e:
        return JSONResponse(status_code=422, content={"detail": str(e.errors())})
    
    
@router.put("/schedules/{schedule_id}")
def update_schedule_route(schedule_id: int, schedule: ScheduleUpdate, db: Session = Depends(get_db)):
    db_schedule = ScheduleMediator(db).update_schedule(db,schedule, schedule_id)
    return HTTPException(status_code=200, detail={'msg': "Schedule updated successfully", "schedule": db_schedule})