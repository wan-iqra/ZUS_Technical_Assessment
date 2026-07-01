from selenium.webdriver.common.by import By


class InventoryPage:

    PRICES = (By.CLASS_NAME, "inventory_item_price")
    ADD_BUTTONS = (By.CSS_SELECTOR, "button.btn_inventory")
    CART = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver

    def add_two_cheapest_items(self):

        prices = self.driver.find_elements(*self.PRICES)

        items = []

        for index, price in enumerate(prices):
            items.append((float(price.text.replace("$", "")), index))

        items.sort()

        buttons = self.driver.find_elements(*self.ADD_BUTTONS)

        buttons[items[0][1]].click()
        buttons[items[1][1]].click()

    def open_cart(self):
        self.driver.find_element(*self.CART).click()