from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """
    Страница входа (Login).

    Атрибуты:
        driver (WebDriver): Экземпляр WebDriver для управления браузером.
        url (str): URL страницы логина.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы логина.

        Параметры:
            driver (WebDriver): WebDriver для управления браузером.

        Возвращает:
            None
        """
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")

    def open(self) -> None:
        """
        Открывает страницу логина.

        Параметры:
            отсутствуют (кроме self)

        Возвращает:
            None
        """
        self.driver.get(self.url)

    def enter_username(self, username: str) -> None:
        """
        Вводит имя пользователя.

        Параметры:
            username (str): Имя пользователя.

        Возвращает:
            None
        """
        self.driver.find_element(*self.username).send_keys(username)

    def enter_password(self, password: str) -> None:
        """
        Вводит пароль пользователя.

        Параметры:
            password (str): Пароль.

        Возвращает:
            None
        """
        self.driver.find_element(*self.password).send_keys(password)

    def click_login(self) -> None:
        """
        Нажимает кнопку входа.

        Параметры:
            отсутствуют (кроме self)

        Возвращает:
            None
        """
        self.driver.find_element(*self.login_button).click()

    def login(self, username: str, password: str) -> None:
        """
        Полный сценарий логина: ввод логина, пароля и нажатие кнопки входа.

        Параметры:
            username (str): Имя пользователя.
            password (str): Пароль.

        Возвращает:
            None
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
