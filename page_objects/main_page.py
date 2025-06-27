from selenium.webdriver.support import expected_conditions as EC
from locators.order_locators import OrderLocators
from page_objects.base_page import BasePage

class Main(BasePage):
    def __init__(self, driver):
        # Инициализация родительского класса
        super().__init__(driver, OrderLocators)  # Передаем локаторы

    # Клик по кнопке "Заказать"
    def click_button_order(self):
    # Ожидание, что кнопка "Заказать" будет кликабельна
        self.wait.until(EC.element_to_be_clickable(OrderLocators.BTN_ORDER_HEADER))
        self.click(OrderLocators.BTN_ORDER_HEADER)  # Кликаем по кнопке "Заказать" в заголовке

    # Принять куки
    def accept_cookies(self):
    # Ожидание, что кнопка куки будет кликабельна
        self.wait.until(EC.element_to_be_clickable(OrderLocators.COOKIE))
        self.click(OrderLocators.COOKIE)  # Кликаем по кнопке куки


