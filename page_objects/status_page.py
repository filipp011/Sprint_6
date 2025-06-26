from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_locators import OrderLocators
from page_objects.base_page import BasePage

class StatusPage(BasePage):
    def __init__(self, driver):
        # Инициализация родительского класса
        super().__init__(driver) 
    
    # Клик на лого Самоката
    def click_logo_samokat(self):
        self.driver.find_element(*OrderLocators.BTN_SAMOKAT).click()

    # Проверяем что перешли на главную страницу Яндекс Самоката
    def get_url_main_page(self):
        expected_url = "https://qa-scooter.praktikum-services.ru/"
        current_url = self.driver.current_url
        return current_url == expected_url

     # Клик на лого Яндекса
    def click_logo_ya(self):
        self.driver.find_element(*OrderLocators.BTN_LOGO_YA).click()

    # Ожидаем появление нового окна
    def wait_new_window_dzen(self):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
    
    # Переключаемся на новое окно 
    def switch_new_window(self):
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)

    # Проверяем что перешли на Дзен
    def check_new_window_dzen(self):
        WebDriverWait(self.driver, 10).until(EC.url_to_be("https://dzen.ru/?yredirect=true"))
        current_url = self.driver.current_url
        return current_url
    