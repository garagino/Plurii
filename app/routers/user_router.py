from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.depends import auth_wrapper
from app.schemas.user import UserCreate, UserUpdate, UserAuth
from app.mediator.user_mediator import UserMediator
from app.schemas.response import UserCreateResponse
from app.database import get_db
from pydantic import ValidationError
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/users/", response_model=UserCreateResponse)
def create_user_route(user: UserCreate, db: Session = Depends(get_db)):
    try:
        UserMediator(db)._create_user(user)
        response_data = {"response": "User created successfully"}
        return UserCreateResponse(**response_data)
    except ValidationError as e:
        return JSONResponse(status_code=422, content={"detail": str(e.errors())})


@router.get("/users/")
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = UserMediator(db)._get_users(skip=skip, limit=limit)
    return users

@router.get("/users/username/{username}")
def read_user_by_username(username: str, db: Session = Depends(get_db)):
    db_user = UserMediator(db)._get_user_by_username(username=username)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/users/email/")
def read_user_logged(db: Session = Depends(get_db), email = Depends(auth_wrapper)):
    db_user = UserMediator(db).get_user_by_email(email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.put("/users/{user_id}")
def update_user_route(user_email: str, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = UserMediator(db)._edit_user(user_email, user)
    return db_user

@router.delete("/users/{user_id}")
def delete_user_route(user_email: str, db: Session = Depends(get_db)):
    db_user = UserMediator(db)._delete_user(user_email=user_email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post("/login/")
def login_user_route(user: UserAuth, db: Session = Depends(get_db)):
    db_user = UserMediator(db).user_login(user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    raise HTTPException(status_code=200, detail={'msg': "User logged in successfully", "token": db_user})