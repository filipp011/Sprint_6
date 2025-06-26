from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_locators import OrderLocators
from page_objects.base_page import BasePage

class PopUpSuccess(BasePage):
    def __init__(self, driver):
        # Инициализация родительского класса
        super().__init__(driver) 

    # Ожидание появление поп-апа об успешном оформлении
    def wait_pop_up(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderLocators.TEXT_ORDER_SUCCESS))

    # Получение текста из поп-апа успешного оформления заказа
    def get_description(self):
        return self.driver.find_element(*OrderLocators.TEXT_ORDER_SUCCESS).text

    # Переход в профиль статуса заказа
    def click_button_status(self):
        self.driver.find_element(*OrderLocators.BTN_STATUS).click()
        