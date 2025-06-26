from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.order_locators import OrderLocators
from page_objects.base_page import BasePage

class Main(BasePage):
    def __init__(self, driver):
        # Инициализация родительского класса
        super().__init__(driver) 

    # Клик по кнопке заказать и принять куки
    def click_button_order(self):
        self.driver.find_element(*OrderLocators.BTN_ORDER_HEADER).click()
        self.driver.find_element(*OrderLocators.COOKIE).click()
