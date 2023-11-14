from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.labroom import LabRoomCreate, LabRoomUpdate
from app.schemas.user import UserCreate, UserUpdate
from app.mediator.labroom_mediator import LabRoomMediator
from app.mediator.user_mediator import UserMediator
from app.schemas.response import LabRoomCreateResponse
from app.database import get_db
from pydantic import ValidationError
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/labrooms/", response_model=LabRoomCreateResponse)
def create_labroom_route(labroom: LabRoomCreate, db: Session = Depends(get_db)):
    try:
        UserMediator(db)._create_labroom(labroom)
        response_data = {"response": "Labroom created successfully"}
        return LabRoomCreateResponse(**response_data)
    except ValidationError as e:
        return JSONResponse(status_code=422, content={"detail": str(e.errors())})
    
@router.get("/labrooms/")
def read_labrooms (skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    labrooms = LabRoomMediator(db)._get_users(skip=skip, limit=limit)
    return labrooms

# @router.get("/users/username/{username}") 
# Não sei pra que serve ai não fiz 

@router.put("/labrooms/{labroomd_id}")
def update_user_route(labroom_id: int, labroom: LabRoomUpdate, db: Session = Depends(get_db)):
    db_labroom = LabRoomMediator(db)._edit_labroom(labroom_id,labroom) 
    return db_labroom