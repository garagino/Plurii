from datetime import datetime, timedelta
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from app.models.user import User
from app.models.labroom import LabRoom
from app.models.schedule import Schedule
from app.routers import user_router
from app.routers import labroom_router, schedule_router
from .database import engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


User.metadata.create_all(bind=engine)
LabRoom.metadata.create_all(bind=engine)
Schedule.metadata.create_all(bind=engine)



app.include_router(user_router.router, prefix="", tags=["users"])
app.include_router(labroom_router.router, prefix="", tags=["labrooms"])
app.include_router(schedule_router.router, prefix="", tags=["schedules"])