from selenium.webdriver.support import expected_conditions as EC
from locators.order_locators import OrderLocators
from page_objects.base_page import BasePage


class ForWhom(BasePage):
    def __init__(self, driver):
        # Инициализация родительского класса
        super().__init__(driver) 

    def fill_order_form(self, name, last_name, address, metro, telephone):
    # Ввод имени
        self.driver.find_element(*OrderLocators.INPUT_NAME).send_keys(name)
    
    # Ввод фамилии
        self.driver.find_element(*OrderLocators.INPUT_LAST_NAME).send_keys(last_name)
    
    # Ввод адреса
        self.driver.find_element(*OrderLocators.INPUT_ADDRESS).send_keys(address)
    
    # Клик на поле метро
        self.driver.find_element(*OrderLocators.INPUT_DEFAULT_METRO).click()
    
    # Выбор метро
        metro_locators = {
        "Бульвар Рокоссовского": OrderLocators.METRO_BULVAR,
        "Черкизовская": OrderLocators.METRO_BULVAR_CHERKIZ
    }
        self.driver.find_element(*metro_locators[metro]).click()
    
    # Ввод номера телефона
        self.driver.find_element(*OrderLocators.INPUT_TELEPHONE).send_keys(telephone)
    
    # Клик по кнопке Далее
        self.driver.find_element(*OrderLocators.BTN_NEXT).click()
