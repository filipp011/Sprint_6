from locators.order_locators import OrderLocators
from page_objects.base_page import BasePage

class ForWhom(BasePage):
    def __init__(self, driver):
        # Инициализация родительского класса
        super().__init__(driver, OrderLocators)  # Передаем локаторы

    def fill_order_form(self, name, last_name, address, metro, telephone):
        # Ввод имени
        self.enter_text(OrderLocators.INPUT_NAME, name)

        # Ввод фамилии
        self.enter_text(OrderLocators.INPUT_LAST_NAME, last_name)  

        # Ввод адреса
        self.enter_text(OrderLocators.INPUT_ADDRESS, address)  

        # Клик на поле метро
        self.click(OrderLocators.INPUT_DEFAULT_METRO)  

        # Выбор метро
        metro_locators = {
            "Бульвар Рокоссовского": OrderLocators.METRO_BULVAR,
            "Черкизовская": OrderLocators.METRO_BULVAR_CHERKIZ
        }
        self.click(metro_locators[metro])  

        # Ввод номера телефона
        self.enter_text(OrderLocators.INPUT_TELEPHONE, telephone)  

        # Клик по кнопке Далее
        self.click(OrderLocators.BTN_NEXT)  


