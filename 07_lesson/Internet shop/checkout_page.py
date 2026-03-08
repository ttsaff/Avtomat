from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    first_name = (By.ID, "first-name")
    last_name = (By.ID, "last-name")
    postal_code = (By.ID, "postal-code")
    continue_button = (By.ID, "continue")
    total_price = (By.CLASS_NAME, "summary_total_label")

    def enter_first_name(self, name):
        self.driver.find_element(*self.first_name).send_keys(name)

    def enter_last_name(self, name):
        self.driver.find_element(*self.last_name).send_keys(name)

    def enter_postal_code(self, code):
        self.driver.find_element(*self.postal_code).send_keys(code)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()

    def fill_form(self, first, last, zip_code):
        self.enter_first_name(first)
        self.enter_last_name(last)
        self.enter_postal_code(zip_code)
        self.click_continue()

    def get_total(self):
        return self.driver.find_element(*self.total_price).text