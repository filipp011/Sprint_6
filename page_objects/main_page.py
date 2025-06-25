import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.order_locators import OrderLocators
from locators.question_locators import QuestionLocators

class Main():
    def __init__(self, driver):
        self.driver = driver

    # Клик по кнопке Принять куки
    def click_button_cookie(self):
        self.driver.find_element(*OrderLocators.COOKIE).click()

    # Клик по кнопке заказать
    def click_button_order(self):
        self.driver.find_element(*OrderLocators.BTN_ORDER_HEADER).click()
