import allure

from config.constants import *

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_complete_page import CheckoutCompletePage


@allure.id("TC0001")
@allure.epic("SauceDemo")
@allure.feature("Purchase")
@allure.story("Purchase Flow")
@allure.title("Purchase the two cheapest products")
def test_purchase_flow(driver):
    LoginPage(driver).login(USERNAME, PASSWORD)

    inventory = InventoryPage(driver)
    inventory.add_two_cheapest_items()
    inventory.open_cart()

    CartPage(driver).checkout()

    checkout = CheckoutPage(driver)
    checkout.fill_information(
        FIRST_NAME,
        LAST_NAME,
        POSTAL_CODE
    )

    checkout.continue_checkout()
    checkout.finish()

    message = CheckoutCompletePage(driver).get_message()

    assert message == "Thank you for your order!"
