import uuid
import pytest
from yougile_client import YougileClient

def _unique_title(prefix="test-project"):
    return f"{prefix}-{uuid.uuid4().hex[:8]}"

def _extract_project_dict(resp):
    """
    Попытка извлечь словарь проекта из ответа.
    Подстраиваемся под возможные варианты тела ответа.
    Если распознать не удалось — возвращаем None.
    """
    try:
        data = resp.json()
    except ValueError:
        return None

    if isinstance(data, dict):
        # Прямой вариант: { "id": ..., "title": ... } или только { "id": ... }
        if "id" in data:
            return data
        # Популярные обёртки
        for key in ("project", "data", "result"):
            if key in data and isinstance(data[key], dict) and "id" in data[key]:
                return data[key]
    return None

# ---------- POST /projects ------------
def test_create_project_positive(client):
    payload = {"title": _unique_title()}
    resp = client.create_project(payload)
    # Учитываем варианты возврата 200 или 201; важны успешный статус и наличие id
    assert 200 <= resp.status_code < 300, f"Ожидался успешный код, получили {resp.status_code}, тело: {resp.text}"
    proj = _extract_project_dict(resp)
    assert proj is not None and "id" in proj, f"Не удалось извлечь проект из о��вета: {resp.text}"
    project_id = str(proj["id"])

    # Подтверждаем через GET, так как create может возвращать только id
    get_resp = client.get_project(project_id)
    assert 200 <= get_resp.status_code < 300, f"GET failed: {get_resp.status_code} {get_resp.text}"
    got = _extract_project_dict(get_resp)
    assert got and str(got.get("id")) == project_id, f"GET вернул неожиданный проект: {get_resp.text}"
    assert got.get("title") == payload["title"], f"Ожидалось title={payload['title']}, получили: {got.get('title')}"

def test_create_project_negative_missing_title(client):
    # Отправляем payload без обязательного поля title
    payload = {}
    resp = client.create_project(payload)
    # Ожидаем ошибку клиента (4xx).
    assert 400 <= resp.status_code < 500, f"Ожидался 4xx для некорректного запроса, получили {resp.status_code}. Тело: {resp.text}"

# ---------- GET /projects/{id} ------------
def test_get_project_positive(client):
    # Сначала создаём проект, затем запрашиваем его
    title = _unique_title()
    create_resp = client.create_project({"title": title})
    assert 200 <= create_resp.status_code < 300, f"Create failed: {create_resp.status_code} {create_resp.text}"
    proj = _extract_project_dict(create_resp)
    assert proj and "id" in proj, "Не удалось получить id созданного проекта"
    project_id = str(proj["id"])
    get_resp = client.get_project(project_id)
    assert 200 <= get_resp.status_code < 300, f"GET failed: {get_resp.status_code} {get_resp.text}"
    got = _extract_project_dict(get_resp)
    assert got and str(got.get("id")) == project_id, f"GET вернул неожиданный проект: {get_resp.text}"
    assert got.get("title") == title, f"Ожидалось title={title}, получили: {got.get('title')}"

def test_get_project_negative_not_found(client):
    # Используем явно несуществующий id.
    fake_id = "00000000-0000-0000-0000-000000000000"
    resp = client.get_project(fake_id)
    # Ожидаем 404 или другое 4xx (not found)
    assert 400 <= resp.status_code < 500, f"Ожидался 4xx для несуществующего проекта, получили {resp.status_code}. Тело: {resp.text}"

# ---------- PUT /projects/{id} ------------
def test_update_project_positive(client):
    # Создаём проект
    original_title = _unique_title()
    create_resp = client.create_project({"title": original_title})
    assert 200 <= create_resp.status_code < 300, f"Create failed: {create_resp.status_code} {create_resp.text}"
    proj = _extract_project_dict(create_resp)
    assert proj and "id" in proj, "Не удалось получить id созданного проекта"
    project_id = str(proj["id"])

    # Обновляем title
    new_title = _unique_title("updated")
    update_payload = {"title": new_title}
    update_resp = client.update_project(project_id, update_payload)
    assert 200 <= update_resp.status_code < 300, f"Update failed: {update_resp.status_code} {update_resp.text}"

    # Подтверждаем через GET (update может возвращать только id)
    get_resp = client.get_project(project_id)
    assert 200 <= get_resp.status_code < 300, f"GET after update failed: {get_resp.status_code} {get_resp.text}"
    got = _extract_project_dict(get_resp)
    assert got, "Не удалось извлечь проект после обновления"
    assert got.get("title") == new_title, f"Ожидалось title={new_title} после обновления, получили: {got.get('title')}"

def test_update_project_negative_not_found(client):
    fake_id = "00000000-0000-0000-0000-000000000000"
    update_payload = {"title": _unique_title("should-not-exist")}
    resp = client.update_project(fake_id, update_payload)
    # Для обновления несуществующего ресурса ожидаем 4xx (обычно 404)
    assert 400 <= resp.status_code < 500, f"Ожидался 4xx для update несуществующего id, получили {resp.status_code}. Тело: {resp.text}"