from selenium.webdriver.support import expected_conditions as EC
from locators.order_locators import OrderLocators
from page_objects.base_page import BasePage
from data import BASE_URL 

class Main(BasePage):
    def __init__(self, driver):
        # Инициализация родительского класса
        super().__init__(driver, OrderLocators)  # Передаем локаторы

    # Метод для открытия главной страницы и принятия куки
    def open_main_page_and_accept_cookies(self):
        self.open(BASE_URL)  # Открываем главную страницу, используя импортированный BASE_URL
        self.accept_cookies()  # Принимаем куки

    # Метод для прокрутки до кнопки и клика по ней
    def scroll_and_click_button(self, locator):
        self.scroll_to_element(locator)  # Прокручиваем до элемента
        self.click(locator)  # Кликаем по элементу