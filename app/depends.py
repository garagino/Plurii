from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi import Security, Depends
from app.mediator.user_mediator import UserMediator
from app.database import get_db
from sqlalchemy.orm import Session


def auth_wrapper(auth: HTTPAuthorizationCredentials = Security(HTTPBearer()), db: Session = Depends(get_db)):
    user_mediator = UserMediator(db)
    return user_mediator.verify_token(auth.credentials)

