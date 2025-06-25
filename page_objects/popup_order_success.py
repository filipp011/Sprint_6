import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.order_locators import OrderLocators

class PopUpSuccess():
    def __init__(self, driver):
        self.driver = driver

    # Ожидание появление поп-апа об успешном оформлении
    def wait_pop_up(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderLocators.TEXT_ORDER_SUCCESS))

    # Получение текста из поп-апа успешного оформления заказа
    def get_description(self):
        return self.driver.find_element(*OrderLocators.TEXT_ORDER_SUCCESS).text

    # Переход в профиль статуса заказа
    def click_button_status(self):
        self.driver.find_element(*OrderLocators.BTN_STATUS).click()
        