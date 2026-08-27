import pytest
import uuid
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
    return YougileProjectClient(base_url=BASE_URL, token=TOKEN)


@pytest.fixture
def temp_project(api_client):
    unique_title = f"Test Project {uuid.uuid4().hex[:6]}"
    response = api_client.create_project(title=unique_title)
    assert response.status_code == 201, "Не удалось создать временный проект для теста"
    project_id = response.json().get("id")

    yield project_id

    api_client.update_project(project_id, deleted=True)


def test_create_project_positive(api_client):
    project_title = f"Autotest Project {uuid.uuid4().hex[:6]}"
    response = api_client.create_project(title=project_title)

    assert response.status_code == 201
    res_data = response.json()
    assert "id" in res_data
    #assert res_data.get("title") == project_title


def test_get_project_positive(api_client, temp_project):
    response = api_client.get_project(temp_project)

    assert response.status_code == 200
    res_data = response.json()
    assert res_data.get("id") == temp_project


def test_update_project_positive(api_client, temp_project):
    new_title = f"Updated Title {uuid.uuid4().hex[:6]}"
    response = api_client.update_project(temp_project, title=new_title)

    assert response.status_code == 200

    get_response = api_client.get_project(temp_project)
    assert get_response.json().get("title") == new_title


def test_create_project_negative_missing_title(api_client):
    response = api_client.create_project(title="")

    assert response.status_code == 400


def test_get_project_negative_not_found(api_client):
    non_existent_id = "00000000-0000-0000-0000-000000000000"
    response = api_client.get_project(non_existent_id)

    assert response.status_code == 404


def test_update_project_negative_invalid_id(api_client):
    invalid_id = "invalid-id-format"
    response = api_client.update_project(invalid_id, title="New Title")

    assert response.status_code in [400, 404]