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

#метод пут

    def test_add_project_positive(title):
        # Создаем проект
        project = api.create_project(title, users_info)

        # Проверяем успешность операции (код статуса 201 — Created)
        assert project.status_code == 201

        # Получаем ID нового проекта
        new_id = project.json()["id"]

        # Запрашиваем созданный проект
        new_project = api.get_project(new_id)

        # Проверяем наличие проекта и правильность названия
        assert new_project.status_code == 200
        assert new_project.json()["title"] == title

        # Удаляем проект
        api.delete_project(new_id)


# Негативный тест на попытку создать проект с пустым названием
def test_add_project_not_valid_title():
    # Пытаемся создать проект с пустым заголовком
    project = api.create_project("", users_info)

    # Ожидаем ошибку Bad Request (статус-код 400)
    assert project.status_code == 400
    assert project.json()["error"] == "Bad Request"


# Негативный тест на попытки создать проект с неверным токеном авторизации
def test_add_project_not_valid_token():
    # Используем объект API с некорректными заголовками (невалидный токен)
    project = api_negative.create_project("", users_info)

    # Ожидаем статус Unauthorized (401)
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
    # Пытаемся получить проект с заведомо несуществующим id
    non_existent_project = api.get_project(-1)

    # Ожидаем код Not Found (404)
    assert non_existent_project.status_code == 404
