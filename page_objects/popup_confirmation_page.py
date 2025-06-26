from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_locators import OrderLocators
from page_objects.base_page import BasePage

class PopUpConfirmation(BasePage):
    def __init__(self, driver):
        # Инициализация родительского класса
        super().__init__(driver) 

    # Ожидание поп-апа подтверждения
    def wait_pop_up_yes_or_no(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderLocators.POP_UP_YES_NO))

    # Клик по кнопке Да-подтверждение заказа
    def click_button_yes(self):
        self.driver.find_element(*OrderLocators.BTN_YES).click()
        