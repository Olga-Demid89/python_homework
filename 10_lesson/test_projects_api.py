import pytest
import uuid
import allure
from api_client import YougileProjectClient
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("YOUGILE_TOKEN")
if not TOKEN:
    raise RuntimeError("Не задана переменная окружения YOUGILE_TOKEN")

BASE_URL = "https://ru.yougile.com"


@pytest.fixture(scope="session")
def api_client():
    """Создаёт клиент API для сессии тестов."""
    return YougileProjectClient(base_url=BASE_URL, token=TOKEN)


@pytest.fixture
def temp_project(api_client):
    """
    Создаёт временный проект и удаляет его после теста (soft-delete через deleted=True).
    """
    unique_title = f"Test Project {uuid.uuid4().hex[:6]}"
    with allure.step("Создание временного проекта"):
        response = api_client.create_project(title=unique_title)
        assert response.status_code == 201, "Не удалось создать временный проект для теста"
        project_id = response.json().get("id")
        assert project_id, "В ответе отсутствует id проекта"

    yield project_id

    with allure.step("Удаление временного проекта (deleted=True)"):
        api_client.update_project(project_id, deleted=True)


@allure.feature("Projects API")
@allure.title("Успешное создание проекта")
@allure.description("Проверяет, что проект успешно создаётся и возвращает статус 201 и id.")
@allure.severity(allure.severity_level.NORMAL)
def test_create_project_positive(api_client):
    project_title = f"Autotest Project {uuid.uuid4().hex[:6]}"

    with allure.step(f"Отправляем запрос на создание проекта с названием '{project_title}'"):
        response = api_client.create_project(title=project_title)

    with allure.step("Проверяем статус-код 201"):
        assert response.status_code == 201

    with allure.step("Проверяем, что в ответе есть поле id"):
        res_data = response.json()
        assert "id" in res_data
        # assert res_data.get("title") == project_title  # можно раскомментировать при необходимости


@allure.feature("Projects API")
@allure.title("Получение существующего проекта")
@allure.description("Проверяет получение проекта по id и соответствие id в ответе.")
@allure.severity(allure.severity_level.NORMAL)
def test_get_project_positive(api_client, temp_project):
    with allure.step(f"Отправляем GET-запрос для проекта id={temp_project}"):
        response = api_client.get_project(temp_project)

    with allure.step("Проверяем статус-код 200"):
        assert response.status_code == 200

    with allure.step("Проверяем соответствие id в ответе"):
        res_data = response.json()
        assert res_data.get("id") == temp_project


@allure.feature("Projects API")
@allure.title("Обновление проекта (смена названия)")
@allure.description("Проверяет обновление названия проекта и его чтение после обновления.")
@allure.severity(allure.severity_level.NORMAL)
def test_update_project_positive(api_client, temp_project):
    new_title = f"Updated Title {uuid.uuid4().hex[:6]}"

    with allure.step(f"Обновляем проект {temp_project}, устанавливаем новое название '{new_title}'"):
        response = api_client.update_project(temp_project, title=new_title)

    with allure.step("Проверяем статус-код 200 при обновлении"):
        assert response.status_code == 200

    with allure.step(f"Получаем проект {temp_project} для проверки обновлённого названия"):
        get_response = api_client.get_project(temp_project)

    with allure.step("Проверяем, что название в ответе совпадает с новым"):
        assert get_response.json().get("title") == new_title


@allure.feature("Projects API")
@allure.title("Создание проекта с пустым названием (негатив)")
@allure.description("Проверяет, что API отклоняет создание проекта с пустым title и возвращает 400.")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_project_negative_missing_title(api_client):
    with allure.step("Отправляем запрос на создание проекта с пустым title"):
        response = api_client.create_project(title="")

    with allure.step("Ожидаем статус-код 400 (ошибка валидации)"):
        assert response.status_code == 400


@allure.feature("Projects API")
@allure.title("Получение несуществующего проекта (негатив)")
@allure.description("Проверяет, что получение несуществующего проекта возвращает 404.")
@allure.severity(allure.severity_level.NORMAL)
def test_get_project_negative_not_found(api_client):
    non_existent_id = "00000000-0000-0000-0000-000000000000"

    with allure.step(f"Отправляем GET для несуществующего id={non_existent_id}"):
        response = api_client.get_project(non_existent_id)

    with allure.step("Ожидаем статус-код 404"):
        assert response.status_code == 404


@allure.feature("Projects API")
@allure.title("Обновление с некорректным id (негатив)")
@allure.description("Проверяет обработку некорректного формата id при обновлении проекта.")
@allure.severity(allure.severity_level.NORMAL)
def test_update_project_negative_invalid_id(api_client):
    invalid_id = "invalid-id-format"
    new_title = "New Title"

    with allure.step(f"Пытаемся обновить проект с некорректным id={invalid_id}"):
        response = api_client.update_project(invalid_id, title=new_title)

    with allure.step("Ожидаем статус-код 400 или 404 в зависимости от реализации API"):
        assert response.status_code in [400, 404]