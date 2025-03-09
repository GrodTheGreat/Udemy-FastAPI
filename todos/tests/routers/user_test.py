import os
import sys

from fastapi import status

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from main import app
from routers.user import get_current_user, get_db
from tests.utils import *

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_return_user(test_user):
    response = client.get("/user")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["username"] == "codingwithrobytest"
    assert response.json()["email"] == "codingwithrobytest@email.com"
    assert response.json()["first_name"] == "Eric"
    assert response.json()["last_name"] == "Roby"
    assert response.json()["role"] == "admin"
    assert response.json()["phone_number"] == "(111) 111-1111"


def test_change_password_success(test_user):
    response = client.put(
        "user/password",
        json={"password": "testpassword", "new_password": "newpassword"},
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_change_password_invalid_current_password(test_user):
    response = client.put(
        "user/password",
        json={"password": "badpassword", "new_password": "newpassword"},
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {"detail": "Incorrect password"}


def test_change_phone_number_success(test_user):
    response = client.put("/user/phone-number", json={"new_phone": "(555) 555-5555"})
    assert response.status_code == status.HTTP_204_NO_CONTENT
