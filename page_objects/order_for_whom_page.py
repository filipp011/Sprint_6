from selenium.webdriver.support import expected_conditions as EC
from locators.order_locators import OrderLocators
from page_objects.base_page import BasePage


class ForWhom(BasePage):
    def __init__(self, driver):
        # Инициализация родительского класса
        super().__init__(driver) 

    # Ввод имени в поле имя
    def input_name(self, name):
        self.driver.find_element(*OrderLocators.INPUT_NAME).send_keys(name)

    # Ввод фамилии в поле фамилия
    def input_last_name(self, last_name):
        self.driver.find_element(*OrderLocators.INPUT_LAST_NAME).send_keys(last_name)

    # Ввод адреса в поле адрес
    def input_address(self, address):
        self.driver.find_element(*OrderLocators.INPUT_ADDRESS).send_keys(address)

    # Клик на поле метро
    def click_input_metro(self):
        self.driver.find_element(*OrderLocators.INPUT_DEFAULT_METRO).click()

    # Выбор метро
    def select_metro(self, metro):
        metro_locators = {
        "Бульвар Рокоссовского": OrderLocators.METRO_BULVAR,
        "Черкизовская": OrderLocators.METRO_BULVAR_CHERKIZ
    }
        self.driver.find_element(*metro_locators[metro]).click()

    # Ввод номера телефона в поле телефон
    def input_telephone(self, telephone):
        self.driver.find_element(*OrderLocators.INPUT_TELEPHONE).send_keys(telephone)

    # Клик по кнопке Далее
    def click_button_next(self):
        self.driver.find_element(*OrderLocators.BTN_NEXT).click()
