import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.order_locators import OrderLocators

class PopUpConfirmation():
    def __init__(self, driver):
        self.driver = driver

    # Ожидание поп-апа подтверждения
    def wait_pop_up_yes_or_no(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderLocators.POP_UP_YES_NO))

    # Клик по кнопке Да-подтверждение заказа
    def click_button_yes(self):
        self.driver.find_element(*OrderLocators.BTN_YES).click()
        