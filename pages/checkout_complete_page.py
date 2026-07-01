from selenium.webdriver.common.by import By


class CheckoutCompletePage:

    COMPLETE = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver

    def get_message(self):
        return self.driver.find_element(*self.COMPLETE).text