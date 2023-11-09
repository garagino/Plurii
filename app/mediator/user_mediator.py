import re
from datetime import datetime, timedelta
from wsgiref import validate
from fastapi import status
from decouple import config
from sqlalchemy.orm import Session
import jwt
from passlib.context import CryptContext
from fastapi import HTTPException
from app.models.user import User
from app.schemas.user import UserAuth, UserCreate, UserUpdate
from app.controllers.user_controller import UserController


class UserMediator:
    
    def __init__(self, db: Session):
        self.user_controller = UserController()
        self.db = db
        self.pwd_context = CryptContext(schemes=['sha256_crypt'])
        self.secret_key = config("SECRET_KEY")
        self.algorithm = config("ALGORITHM")
        
    
    def _validate_email(self, email: str):
        existe_user = self.user_controller.get_user_by_email(self.db, email)
        if existe_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
        
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid email address")

    
    
    def _validate_username(self, username: str):
        if len(username) < 3:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username must be at least 3 characters")
        
        if len(username) > 50:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username must be less than 50 characters")
        
        if not re.match(r"^[a-zA-ZÀ-ÖØ-öø-ÿ]+$", username):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username must contain only letters")
        
        
    def _validate_password(self, password: str):
        if len(password) < 8:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password must be at least 8 characters")
        
        if len(password) > 50:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password must be less than 50 characters")
        
        if not any(char.isdigit() for char in password):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password must contain at least one number")
                
        if not any(char.isupper() for char in password):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password must contain at least one uppercase letter")
        
        if not any(char in "!@#$%&*()-+?_=,<>/;:[]{}" for char in password):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Password must contain at least one special character")
        
    
    
    def _create_user(self, user: UserCreate):

        self._validate_email(user.email)
        self._validate_password(user.password)
        
        
        
        user.password = self.pwd_context.hash(user.password)
        
        db_user = User(**user.dict())
        
        self.user_controller.create_user(self.db, db_user)
        
    def _get_user_by_username(self, username: str):
        return self.user_controller.get_user_by_username(self.db, username)
    
    def _get_users(self, skip: int = 0, limit: int = 100):
        return self.user_controller.get_users(self.db, skip=skip, limit=limit)
    
    def get_user_by_email(self, email: str):
        return self.user_controller.get_user_by_email(self.db, email)
    
    
    def _edit_user(self, user_email: str, user: UserUpdate):
        
        db_user = self.user_controller.get_user_by_email(self.db, user_email)
        
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        if db_user.username != user.username:
            self._validate_username(user.username)
        
        if db_user.password != user.password:
            self._validate_password(user.password)
            user.password = self.pwd_context.hash(user.password)
        

        self.user_controller.update_user(self.db, user_email, user)
        
        
        
    
    
    def _delete_user(self, user_email: str):
        
        db_user = self.user_controller.get_user_by_email(self.db, user_email)
        
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        self.user_controller.delete_user(self.db, user_email)
        
        
    def user_login(self, user: UserAuth):
        
        db_user = self.user_controller.get_user_by_email(self.db, user.email)
        
        if db_user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        if not self.pwd_context.verify(user.password, db_user.password):
            raise HTTPException(status_code=401, detail="Incorrect password or email")
        
        access_token_expires = timedelta(minutes=30)
        access_token = jwt.encode(
            {"exp": datetime.utcnow() + access_token_expires, "sub": db_user.email},
            self.secret_key,
            algorithm=None
        )
        
        return {"access_token": access_token, "username": db_user.username, "access": db_user.user_function}
    
    
    def verify_token(self, access_token):
        
        try:
            payload = jwt.decode(access_token, self.secret_key, algorithms=[self.algorithm])
            email: str = payload.get("sub")
            if email is None:
                raise HTTPException(status_code=401, detail="Could not validate credentials")
            
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Signature has expired")
        
        except jwt.InvalidTokenError as e:
            raise HTTPException(status_code=401, detail="Invalid token")
        
        