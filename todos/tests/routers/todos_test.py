import os
import sys

from fastapi import status

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from main import app
from models import Todo
from routers.todo import get_current_user, get_db
from tests.utils import *


app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user


def test_read_all_authenticated(test_todo):
    response = client.get("/todo")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
        {
            "id": 1,
            "title": "Learn to code!",
            "description": "Need to learn everyday!",
            "priority": 5,
            "complete": False,
            "owner_id": 1,
        }
    ]


def test_read_one_authenticated(test_todo):
    response = client.get("/todo/todo/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "id": 1,
        "title": "Learn to code!",
        "description": "Need to learn everyday!",
        "priority": 5,
        "complete": False,
        "owner_id": 1,
    }


def test_read_one_authenticated_not_found(test_todo):
    response = client.get("/todo/todo/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Todo with id 999 not found"}


def test_create_todo(test_todo):
    request_data = {
        "title": "New todo!",
        "description": "New todo description",
        "priority": 5,
        "complete": False,
    }

    response = client.post("/todo/todo", json=request_data)
    assert response.status_code == status.HTTP_201_CREATED

    db = TestingSessionLocal()
    model = db.query(Todo).filter(Todo.id == 2).first()
    assert model.title == request_data.get("title")
    assert model.description == request_data.get("description")
    assert model.priority == request_data.get("priority")
    assert model.complete == request_data.get("complete")


def test_update_todo(test_todo):
    request_data = {
        "title": "Change the title",
        "description": "Need top learn everyday!",
        "priority": 5,
        "complete": False,
    }

    response = client.put("/todo/todo/1", json=request_data)
    assert response.status_code == status.HTTP_204_NO_CONTENT

    db = TestingSessionLocal()
    model = db.query(Todo).filter(Todo.id == 1).first()
    assert model.title == request_data.get("title")
    assert model.description == request_data.get("description")
    assert model.priority == request_data.get("priority")
    assert model.complete == request_data.get("complete")


def test_update_todo_not_found():
    request_data = {
        "title": "Change the title",
        "description": "Need top learn everyday!",
        "priority": 5,
        "complete": False,
    }

    response = client.put("/todo/todo/999", json=request_data)
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Todo with id 999 not found"}


def test_delete_todo(test_todo):
    response = client.delete("/todo/todo/1")
    assert response.status_code == status.HTTP_204_NO_CONTENT

    db = TestingSessionLocal()
    model = db.query(Todo).filter(Todo.id == 1).first()
    assert model == None


def test_delete_todo_not_found():
    response = client.delete("/todo/todo/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() == {"detail": "Todo with id 999 not found"}
