from selenium.webdriver.support import expected_conditions as EC
from locators.order_locators import OrderLocators
from page_objects.base_page import BasePage
from data import BASE_URL  # Импортируем BASE_URL

class Main(BasePage):
    def __init__(self, driver):
        # Инициализация родительского класса
        super().__init__(driver, OrderLocators)  # Передаем локаторы

    # Клик по кнопке "Заказать"
    def click_button_order(self):
        # Ожидание, что кнопка "Заказать" будет кликабельна
        self.wait.until(EC.element_to_be_clickable(OrderLocators.BTN_ORDER_HEADER))
        self.click(OrderLocators.BTN_ORDER_HEADER)  # Кликаем по кнопке "Заказать" в заголовке

    # Метод для открытия главной страницы и принятия куки
    def open_main_page_and_accept_cookies(self):
        self.driver.get(BASE_URL)  # Открываем главную страницу, используя импортированный BASE_URL
        self.accept_cookies()  # Принимаем куки
