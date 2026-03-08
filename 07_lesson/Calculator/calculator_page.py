from selenium.webdriver.common.by import By


class CalculatorPage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    delay_input = (By.CSS_SELECTOR, "#delay")
    result = (By.CSS_SELECTOR, ".screen")

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, value):
        field = self.driver.find_element(*self.delay_input)
        field.clear()
        field.send_keys(value)

    def click_button(self, value):
        button = self.driver.find_element(By.XPATH, f"//span[text()='{value}']")
        button.click()

    def get_result(self):
        return self.driver.find_element(*self.result).text