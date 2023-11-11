import re
from datetime import datetime, timedelta
from fastapi import status
from decouple import config
from sqlalchemy.orm import Session
import jwt
from fastapi import HTTPException
from app.schemas.user import UserCreate
from app.models.labroom import LabRoom
from app.schemas.labroom import LabRoomCreate
from app.controllers.user_controller import UserController
from app.controllers.labroom_controller import LabRoomController

class LabRoomMediator:
    
    def __init__(self, db: Session):
        self.labroom_controller = LabRoomController()
        self.user_controller = UserController()
        self.db = db

    #Verifica a partir da id,se function é == admin
    def _validate_adm_function(self, id:int):
        existe_user = self.user_controller.get_user_by_id(self.db, id)
        
        if existe_user.function != "admin":
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Credential denied for actual user")

    
    def _create_labroom(self, user:UserCreate, labroom: LabRoomCreate):

        self._validate_adm_function(user.id)

        db_labroom= LabRoom(**labroom.dict())
        
        self.labroom_controller.create_labroom(self.db, db_labroom)

    #falta os get do labroom

    # falta udpdate do labroom

    # falta o delete do labroom