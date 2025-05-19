import requests
import pytest

Base_URL = 'https://ru.yougile.com/api-v2/'
api_key = "ваш API ключ"

@pytest.fixture
def headers():
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

@pytest.fixture
def create_project(headers):
    data = {
        "title": "Новый проект",
        "users": {}
    }
    resp = requests.post(Base_URL + 'projects', headers=headers, json=data)
    return resp.json()["id"]  # Возвращаем ID созданного проекта

def test_create_project_positive(headers):
    data = {
        "title": "New test project",
        "users": {}
    }
    resp = requests.post(Base_URL + 'projects', headers=headers, json=data)
    assert resp.status_code == 201
    # Удаляем созданный проект
    project_id = resp.json()["id"]
    requests.delete(f'{Base_URL}projects/{project_id}', headers=headers)

def test_create_project_negative(headers):
    data = {
        "title": "",
        "users": {}
    }
    resp = requests.post(Base_URL + 'projects', headers=headers, json=data)
    assert resp.status_code == 400

def test_update_project_positive(headers, create_project):
    project_id = create_project
    data = {"title": "Update test title"}
    resp = requests.put(f'{Base_URL}projects/{project_id}',
                       headers=headers, json=data)
    assert resp.status_code == 200

def test_update_project_negative(headers):
    project_id = "non_existent_project_id"
    data = {"title": "Update test title"}
    resp = requests.put(f'{Base_URL}projects/{project_id}',
                       headers=headers, json=data)
    assert resp.status_code == 404

def test_get_project_positive(headers, create_project):
    project_id = create_project
    resp = requests.get(f'{Base_URL}projects/{project_id}', headers=headers)
    assert resp.status_code == 200

def test_get_project_negative(headers):
    project_id = "non_existent_project_id"
    resp = requests.get(f'{Base_URL}projects/{project_id}', headers=headers)
    assert resp.status_code == 404