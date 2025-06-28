from locators.order_locators import OrderLocators
from page_objects.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from data import BASE_URL, DZEN_URL

class StatusPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, OrderLocators)

    # Клик на лого Самоката
    def click_logo_samokat(self):
        self.click(OrderLocators.BTN_SAMOKAT)
        # Ожидаем, что URL изменится на ожидаемый
        self.wait.until(EC.url_to_be(BASE_URL))

    # Проверяем, что перешли на главную страницу Яндекс Самоката
    def is_on_main_page(self):
        self.wait.until(EC.url_to_be(BASE_URL))
        return self.get_current_url()

    # Ожидаем появление нового окна
    def wait_new_window_dzen(self):
        self.wait.until(EC.number_of_windows_to_be(2))

    def click_logo_and_switch_window(self):
        self.click(OrderLocators.BTN_LOGO_YA)
        self.switch_to_window(1)  # Используем метод из BasePage

    # Проверяем, что перешли на Дзен
    def check_new_window_dzen(self):
        self.wait.until(EC.url_to_be(DZEN_URL))
        return self.get_current_url()  # Используем метод из BasePage



    