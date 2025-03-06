from fastapi import FastAPI

from database import engine
import models
from routers import admin, auth, todo

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(admin.router)
app.include_router(auth.router)
app.include_router(todo.router)
