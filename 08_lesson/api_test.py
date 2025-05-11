import requests
import pytest

Base_URL = 'https://ru.yougile.com/api-v2/'
api_key = "My_api"  # заменить на мой API ключ


@pytest.fixture
def create_project():
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data = {
        "title": "Новый проект",  # Название проекта
        "users": {}
        }
    resp = requests.post(Base_URL + 'projects', headers=headers, json=data)
    assert resp.status_code == 201


def test_create_project_positive():
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data = {
        "title": "New test project",
        "users": {}
    }
    resp = requests.post(Base_URL + 'projects', headers=headers, json=data)
    assert resp.status_code == 201


def test_create_project_negative():
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data = {
        "title": "",
        "users": {}
    }
    resp = requests.post(Base_URL + 'projects', headers=headers, json=data)
    assert resp.status_code == 201


def test_update_project_positive():
    created_project = api.create_project("Тестовый Проект", users_info)
    project_id = created_project.json()["id"]
    new_title = "Новое название проекта"
    response = api.update_project(project_id, new_title)
    assert response.status_code == 200
    updated_project = api.get_project(project_id)
    assert updated_project.json()["title"] == new_title

def test_update_project_invalid_data():
    created_project = api.create_project("Тестовый Проект", users_info)
    project_id = created_project.json()["id"]
    response = api.update_project(project_id, "")
    assert response.status_code == 400



def test_get_project_positive(create_project):
    project_id = create_project
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    resp = requests.get(f'{Base_URL} + projects/{project_id}', headers=headers)
    assert resp.status_code == 200


def test_get_project_negative():
    project_id = "non_existent_project_id"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    resp = requests.get(f'{Base_URL} + projects/{project_id}', headers=headers)
    assert resp.status_code == 404