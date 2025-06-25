import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.order_locators import OrderLocators

class PopUpNumberOrder():
    def __init__(self, driver):
        self.driver = driver

    # Переход в профиль статуса заказа по кнопке Посмотреть статус
    def click_button_status(self):
        self.driver.find_element(*OrderLocators.BTN_STATUS).click()
        