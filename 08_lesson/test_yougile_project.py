import pytest
from YouGileApi import YouGileAPI
from config import *

api = YouGileAPI(api_url, my_headers)
api_negative = YouGileAPI(api_url, not_valid_headers)


@pytest.mark.parametrize("title",
                         ["Проект",
                          "Project",
                          "Проект number 1"])
def test_add_project_positive(title):
    project = api.create_project(title, users_info)
    assert project.status_code == 201
    new_id = project.json()["id"]
    new_project = api.get_project(new_id)
    assert new_project.status_code == 200
    assert new_project.json()["title"] == title
    api.delete_project(new_id)


def test_add_project_not_valid_title():
    project = api.create_project("", users_info)
    assert project.status_code == 400
    assert project.json()["error"] == "Bad Request"


def test_add_project_not_valid_token():
    project = api_negative.create_project("", users_info)
    assert project.status_code == 401
    assert project.json()["error"] == "Unauthorized"



#метод гет
# Позитивный тест на получение существующего проекта
def test_get_existing_project_positive():
    # Сначала создаем новый проект
    created_project = api.create_project("Тестовый Проект", users_info)
    assert created_project.status_code == 201
    new_id = created_project.json()["id"]

    # Затем запрашиваем этот проект
    retrieved_project = api.get_project(new_id)

    # Проверка наличия проекта и правильности возвращенных данных
    assert retrieved_project.status_code == 200
    assert retrieved_project.json()["title"] == "Тестовый Проект"

    # Убираем созданный проект
    api.delete_project(new_id)


# Негативный тест на получение несуществующего проекта
def test_get_nonexistent_project_negative():
    non_existent_id = "00000000-0000-0000-0000-000000000000"
    response = api.get_project(non_existent_id)
    assert response.status_code == 404


#метод пут

def test_update_project_positive(setup_project):
    project_id = setup_project
    new_title = "Новое название проекта"
    response = api.update_project(project_id, new_title)
    assert response.status_code == 200
    updated_project = api.get_project(project_id)
    assert updated_project.json()["title"] == new_title

def test_update_project_invalid_data(setup_project):
    project_id = setup_project
    response = api.update_project(project_id, "")
    assert response.status_code == 400