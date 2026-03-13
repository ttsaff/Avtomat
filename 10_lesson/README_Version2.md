# UI Tests with Selenium + Allure

Этот репозиторий содержит:
- Page objects для примеров (SauceDemo и slow calculator).
- Пример тестов с разметкой для Allure (в `tests/`).
- Инструкции по запуску тестов и генерации Allure-отчёта.

Требования
- Python 3.8+
- Chrome + соответствующий chromedriver в PATH (или установить webdriver-manager/другие средства)
- Allure commandline для просмотра отчетов (инструкция ниже)

Установка
1. Создайте и активируйте виртуальное окружение (рекомендуется):
   - python -m venv .venv
   - source .venv/bin/activate  (Linux/macOS) или .venv\Scripts\activate (Windows)

2. Установите зависимости:
   pip install -r requirements.txt

Запуск тестов и генерация результатов Allure
1. Запустите тесты и сохраните результаты для Allure:
   pytest --alluredir=results

   Параметры:
   - Вы ��ожете запустить с видимым браузером, установив SHOW_BROWSER=1:
     SHOW_BROWSER=1 pytest --alluredir=results

2. Сформируйте и откройте отчёт Allure (требуется установленный allure commandline).

   Вариант 1 (временно запустить веб-��ервер и открыть браузер):
   allure serve results

   Вариант 2 (сгенерировать статический сайт и открыть):
   allure generate results -o report
   allure open report

Установка Allure commandline
- macOS (brew):
  brew install allure

- Windows (scoop):
  scoop install allure

- Linux:
  Скачайте подходящий архив с https://github.com/allure-framework/allure2/releases и добавьте `allure` в PATH.

Что поместить в VCS
- Папки с результатами (results/) и сгенерированным отчётом (report/) в репозиторий не нужно пушить.
- В репозитории в этом PR добавлены `.gitkeep` в папках results/ и report/ чтобы они присутствовали, но пусты.

Документация по разметке тестов
- Тесты используют `allure.step` (контекст-менеджер) и `@allure.step` для функций-проверок.
- Каждый тест помечен:
  - @allure.title
  - @allure.description
  - @allure.feature
  - @allure.severity

Примечания
- Тесты написаны для примера; они используют ChromeDriver и предполагают доступ к внешним URL (`https://www.saucedemo.com/` и `https://bonigarcia.dev/...`). При работе за прокси или без интернета — тесты не будут работать.
- Если нужен автоматический скачиватель chromedriver, можно добавить `webdriver-manager` и адаптировать фикстуру `driver`.