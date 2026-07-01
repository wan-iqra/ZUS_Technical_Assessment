from selenium.webdriver.common.by import By


class CheckoutPage:

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL = (By.ID, "postal-code")

    CONTINUE = (By.ID, "continue")
    FINISH = (By.ID, "finish")

    def __init__(self, driver):
        self.driver = driver

    def fill_information(self, first, last, postal):

        self.driver.find_element(*self.FIRST_NAME).send_keys(first)
        self.driver.find_element(*self.LAST_NAME).send_keys(last)
        self.driver.find_element(*self.POSTAL).send_keys(postal)

    def continue_checkout(self):
        self.driver.find_element(*self.CONTINUE).click()

    def finish(self):
        self.driver.find_element(*self.FINISH).click()