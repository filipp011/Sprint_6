from selenium.webdriver.support import expected_conditions as EC
from locators.order_locators import OrderLocators
from page_objects.base_page import BasePage
from data import BASE_URL 

class Main(BasePage):
    def __init__(self, driver):
        # Инициализация родительского класса
        super().__init__(driver, OrderLocators)  # Передаем локаторы

    # Клик по кнопке "Заказать" в заголовке
    def click_button_order(self):
        self.scroll_to_element(OrderLocators.BTN_ORDER_HEADER)  # Прокручиваем к кнопке "Заказать"
        self.click(OrderLocators.BTN_ORDER_HEADER)  # Кликаем по кнопке "Заказать" в заголовке

    # Клик по кнопке "Заказать" в футере
    def click_button_order_footer(self):
        self.scroll_to_element(OrderLocators.BTN_ORDER_FOOTER)  # Прокручиваем к кнопке "Заказать"
        self.click(OrderLocators.BTN_ORDER_FOOTER)  # Кликаем по кнопке "Заказать" в футере

    # Метод для открытия главной страницы и принятия куки
    def open_main_page_and_accept_cookies(self):
        self.open(BASE_URL)  # Открываем главную страницу, используя импортированный BASE_URL
        self.accept_cookies()  # Принимаем куки

