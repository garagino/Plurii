from fastapi import FastAPI
from app import models
from .database import engine
from fastapi.middleware.cors import CORSMiddleware
from app.config import db



models.Base.metadata.create_all(bind=engine)


origins= [
    "http://localhost:3000"
]

def init_app():
    db.init()

    app = FastAPI(
        title= "Garagino App",
        description= "Login Page",
        version= "1"
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    @app.on_event("startup")
    async def starup():
        await db.create_all()
    
    @app.on_event("shutdown")
    async def shutdown():
        await db.close()

    return app

app = init_app()




@app.get("/")
def root():
    return {"message": "Welcome to FastAPI with SQLAlchemy"}