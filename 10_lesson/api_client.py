import requests
from typing import Optional, Dict, Any


class YougileProjectClient:

    def __init__(self, base_url: str, token: str) -> None:
        """
        Инициализирует клиент.

        :param base_url: базовый URL API (например, 'https://ru.yougile.com')
        :param token: токен авторизации (Bearer)
        """
        self.base_url = base_url
        self.headers: Dict[str, str] = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(self, title: str, users: Optional[Dict[str, Any]] = None) -> requests.Response:
        """
        Создаёт проект.

        :param title: название проекта (обязательно, непустое)
        :param users: словарь с пользователями (опционально)
        :return: объект ответа requests.Response
        """
        url = f"{self.base_url}/api-v2/projects"
        payload: Dict[str, Any] = {"title": title}
        if users:
            payload["users"] = users
        return requests.post(url, json=payload, headers=self.headers)

    def get_project(self, project_id: str) -> requests.Response:
        """
        Получает данные проекта по ID.

        :param project_id: идентификатор проекта (UUID)
        :return: объект ответа requests.Response
        """
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        return requests.get(url, headers=self.headers)

    def update_project(
        self,
        project_id: str,
        title: Optional[str] = None,
        deleted: Optional[bool] = None
    ) -> requests.Response:
        """
        Обновляет проект (можно менять title и флаг deleted).

        :param project_id: идентификатор проекта
        :param title: новое название (если передано)
        :param deleted: флаг удаления (если передан)
        :return: объект ответа requests.Response
        """
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        payload: Dict[str, Any] = {}
        if title is not None:
            payload["title"] = title
        if deleted is not None:
            payload["deleted"] = deleted
        return requests.put(url, json=payload, headers=self.headers)
