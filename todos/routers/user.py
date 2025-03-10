from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from passlib.context import CryptContext
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from starlette import status

from .auth import get_current_user
from database import SessionLocal
from models import User

router = APIRouter(prefix="/user", tags=["user"])


class UserVerification(BaseModel):
    password: str
    new_password: str = Field(min_length=6)


class UserPhone(BaseModel):
    new_phone: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.get("/", status_code=status.HTTP_200_OK)
async def get_user(user: user_dependency, db: db_dependency):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication failed",
        )

    user_model = db.query(User).filter(User.id == user.get("id")).first()

    return user_model


@router.put("/password", status_code=status.HTTP_204_NO_CONTENT)
async def change_password(
    user: user_dependency,
    db: db_dependency,
    user_verification: UserVerification,
):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication failed",
        )

    user_model = db.query(User).filter(User.id == user.get("id")).first()

    if not bcrypt_context.verify(
        user_verification.password, user_model.hashed_password
    ):
        raise HTTPException(status_code=401, detail="Incorrect password")

    user_model.hashed_password = bcrypt_context.hash(
        user_verification.new_password
    )

    db.add(user_model)
    db.commit()


@router.put("/phone-number", status_code=status.HTTP_204_NO_CONTENT)
async def change_phone_number(
    user: user_dependency, db: db_dependency, user_phone: UserPhone
):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication failed",
        )

    user_model = db.query(User).filter(User.id == user.get("id")).first()

    user_model.phone_number = user_phone.new_phone

    db.add(user_model)
    db.commit()
