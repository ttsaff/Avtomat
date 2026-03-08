import requests

class YougileClient:
    """
    Минимальный API-клиент для Yougile.
    Ожидается, что base_url — это базовый URL API (может содержать '/api-v2').
    Примеры:
      - "https://ru.yougile.com"
      - "https://yougile.com/api-v2"
    Клиент корректно формирует конечные URL.
    """
    def __init__(self, base_url: str, token: str, timeout: int = 30):
        self.base_url = base_url.rstrip('/')  # удаляем завершающий слэш
        self.token = token
        self.timeout = timeout
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    def _projects_url(self):
        # Если base_url уже включает api-v2, то получится ".../api-v2/projects"
        return f"{self.base_url}/projects"

    def _project_item_url(self, project_id: str):
        return f"{self._projects_url()}/{project_id}"

    def create_project(self, payload: dict) -> requests.Response:
        url = self._projects_url()
        return requests.post(url, json=payload, headers=self.headers, timeout=self.timeout)

    def get_project(self, project_id: str) -> requests.Response:
        url = self._project_item_url(project_id)
        return requests.get(url, headers=self.headers, timeout=self.timeout)

    def update_project(self, project_id: str, payload: dict) -> requests.Response:
        url = self._project_item_url(project_id)
        return requests.put(url, json=payload, headers=self.headers, timeout=self.timeout)