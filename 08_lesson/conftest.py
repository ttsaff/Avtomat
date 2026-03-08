import os
import pytest
from dotenv import load_dotenv

load_dotenv()

from yougile_client import YougileClient

@pytest.fixture(scope="session")
def base_url():
    # По умолчанию используем https://yougile.com/api-v2/, но можно переопределить через YOUGILE_BASE_URL
    return os.getenv("YOUGILE_BASE_URL", "https://yougile.com/api-v2/")

@pytest.fixture(scope="session")
def token():
    token = "МОЙ ТОКЕН!!!"

    if not token:
        # Если токен не задан, пропускаем тесты — безопаснее, чем хранить токен в коде.
        pytest.skip("YOUGILE_API_TOKEN не задан. Установите переменную окружения и повторите запуск.")
    return token

@pytest.fixture
def client(base_url, token):
    return YougileClient(base_url=base_url, token=token)