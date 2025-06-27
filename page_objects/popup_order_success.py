from locators.order_locators import OrderLocators
from page_objects.base_page import BasePage

class PopUpSuccess(BasePage):
    def __init__(self, driver):
        # Инициализация родительского класса
        super().__init__(driver, OrderLocators)  # Передаем локаторы

    # Ожидание появления поп-апа об успешном оформлении
    def wait_pop_up(self):
        self.wait_visible(OrderLocators.TEXT_ORDER_SUCCESS)  # Используем метод из BasePage

    # Получение текста из поп-апа успешного оформления заказа
    def get_description(self):
        return self.get_text(OrderLocators.TEXT_ORDER_SUCCESS)  # Используем метод из BasePage

    # Переход в профиль статуса заказа
    def click_button_status(self):
        self.click(OrderLocators.BTN_STATUS)  # Используем метод из BasePage

        