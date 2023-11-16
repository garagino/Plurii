from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


class UserController:
    def create_user(self, db: Session, user: User):
        db_user = User()
        db_user.username = user.username
        db_user.email = user.email
        db_user.password = user.password
        db_user.user_function = user.user_function
        db_user.user_role = user.user_role
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user


    def get_user_by_username(self, db: Session, username: str):
        try:
            data = db.query(User).filter(User.username == username).first()
            return data
        except NoResultFound:
            return None
        except Exception as e:
            raise e

    def get_user_by_email(self, db: Session, email: str):
        return db.query(User).filter(User.email == email).first()
    
    def get_user_by_id(self, db: Session, id: int):
        return db.query(User).filter(User.id == id).first()

    def get_users(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(User).offset(skip).limit(limit).all()

    def update_user(self, db: Session, user_email: str, user: UserUpdate):
        db_user = db.query(User).filter(User.email == user_email).first()
        if db_user:
            for key, value in user.dict(exclude_unset=True).items():
                setattr(db_user, key, value)
            db.commit()
            db.refresh(db_user)
        return db_user

    def delete_user(self, db: Session, user_email: str):
        db_user = db.query(User).filter(User.email == user_email).first()
        db.delete(db_user)
        db.commit()
        return db_user
    
    