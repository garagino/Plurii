import re
from datetime import datetime, timedelta
from fastapi import status
from decouple import config
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.mediator.user_mediator import UserMediator
from app.schemas.user import UserCreate
from app.models.labroom import LabRoom
from app.schemas.labroom import LabRoomCreate, LabRoomUpdate
from app.mediator.user_mediator import UserMediator
from app.controllers.labroom_controller import LabRoomController

class LabRoomMediator:
    
    def __init__(self, db: Session):
        self.labroom_controller = LabRoomController()
        self.db = db
        self.user_mediator = UserMediator(db)

    #Verifica a partir da id,se function é == admin
    def _validate_adm_function(self, email: str):
        exist_user = self.user_mediator.get_user_by_email(email)
        
        
        if exist_user.user_function != "admin":
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Credential denied for actual user")

    
    def _create_labroom(self, labroom: LabRoomCreate, email: str):

        self._validate_adm_function(email)

        db_labroom= LabRoom(**labroom.dict())
        
        self.labroom_controller.create_labroom(self.db, db_labroom)


    def _get_labroom_by_name(self, name: str):
        return self.labroom_controller.get_room_by_name(self.db,name)
    
    def _get_labrooms(self, skip: int = 0, limit: int = 100):
        return self.labroom_controller.get_labrooms(self.db, skip=skip, limit=limit)
    
    def get_labroom_by_id(self, id: int):
        return self.labroom_controller.get_labroom(self.db, id)
    

    def _edit_labroom(self, user: UserCreate, labroom_id: int, labroom: LabRoomUpdate):
        
        db_labroom = self.labroom_controller.get_labroom(self.db, labroom_id)

        self._validate_adm_function(user.email)
        
        if db_labroom is None:
            raise HTTPException(status_code=404, detail="Labroom not found")
        
        #senti como se tivesse faltando os campos
             
        self.labroom_controller.update_labroom(self.db, labroom_id, labroom)

    def _delete_labroom (self, user: UserCreate, labroom_id:int):

        db_labroom = self.labroom_controller.get_labroom_by_id(self.db, labroom_id)

        self._validate_adm_function(user.id)
        
        if db_labroom is None:
            raise HTTPException(status_code=404, detail="Labroom not found")
        
        self.user_controller.delete_labroom(self.db, labroom_id)