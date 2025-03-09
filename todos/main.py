from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from database import engine
from models import Base
from routers import admin, auth, todo, user

app = FastAPI()

Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="./templates")


@app.get("/")
def test(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/healthy")
def health_check():
    return {"status": "healthy"}


app.include_router(admin.router)
app.include_router(auth.router)
app.include_router(todo.router)
app.include_router(user.router)
