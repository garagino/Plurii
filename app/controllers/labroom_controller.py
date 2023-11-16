from sqlalchemy.orm import Session
from app.models.labroom import LabRoom


class LabRoomController:

    def create_labroom(self, db: Session, room: LabRoom):
        db_room = LabRoom()
        db_room.name = room.name
        db_room.description = room.description
        db_room.is_active = room.is_active
        db_room.in_use = room.in_use
        db_room.capacity = room.capacity
        db.add(db_room)
        db.commit()
        db.refresh(db_room)
        return db_room

    def get_labroom(self,db: Session, room_id: int):
        return db.query(LabRoom).filter(LabRoom.id == room_id).first()

    def get_room_by_name(self,db: Session, name: str):
        return db.query(LabRoom).filter(LabRoom.name == name).first()

    def get_labrooms(self,db: Session, skip: int = 0, limit: int = 100):
        return db.query(LabRoom).offset(skip).limit(limit).all()

    def update_labroom(self, db: Session, room: LabRoom):
        db_room = db.query(LabRoom).filter(LabRoom.id == room.id).first()
        db_room.name = room.name
        db_room.description = room.description
        db.commit()
        db.refresh(db_room)
        return db_room

    def delete_labroom(self, db: Session, room_id: int):
        db_room = db.query(LabRoom).filter(LabRoom.id == room_id).first()
        db.delete(db_room)
        db.commit()
        return db_room