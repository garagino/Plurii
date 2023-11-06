from fastapi import FastAPI
from app.models.user import User
from app.models.labroom import LabRoom
from app.routers import user_router
from .database import engine

app = FastAPI()


User.metadata.create_all(bind=engine)
LabRoom.metadata.create_all(bind=engine)


app.include_router(user_router.router, prefix="/api/v1", tags=["users"])