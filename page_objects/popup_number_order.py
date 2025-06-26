from selenium.webdriver.support import expected_conditions as EC
from locators.order_locators import OrderLocators
from page_objects.base_page import BasePage

class PopUpNumberOrder(BasePage):
    def __init__(self, driver):
        # Инициализация родительского класса
        super().__init__(driver) 

    # Переход в профиль статуса заказа по кнопке Посмотреть статус
    def click_button_status(self):
        self.driver.find_element(*OrderLocators.BTN_STATUS).click()
        