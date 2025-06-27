from locators.order_locators import OrderLocators
from page_objects.base_page import BasePage

class PopUpConfirmation(BasePage):
    def __init__(self, driver):
        # Инициализация родительского класса
        super().__init__(driver, OrderLocators)  # Передаем локаторы

    # Ожидание поп-апа подтверждения
    def wait_pop_up_yes_or_no(self):
        self.wait_visible(OrderLocators.POP_UP_YES_NO)  # Используем метод из BasePage

    # Клик по кнопке Да-подтверждение заказа
    def click_button_yes(self):
        self.click(OrderLocators.BTN_YES)  # Используем метод из BasePage

        