import os

from fastapi import FastAPI, Request, status
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from database import engine
from models import Base
from routers import admin, auth, todo, user

app = FastAPI()

Base.metadata.create_all(bind=engine)


app.mount(
    "/static",
    StaticFiles(directory=os.path.join(os.path.dirname(__file__), "static")),
    name="static",
)


@app.get("/")
def index(request: Request):
    return RedirectResponse(url="/todo/todo-page", status_code=status.HTTP_302_FOUND)


@app.get("/healthy")
def health_check():
    return {"status": "healthy"}


app.include_router(admin.router)
app.include_router(auth.router)
app.include_router(todo.router)
app.include_router(user.router)
