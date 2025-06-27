from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_locators import OrderLocators
from page_objects.base_page import BasePage

class Rent(BasePage):
    def __init__(self, driver):
        # Инициализация родительского класса
        super().__init__(driver, OrderLocators)

    def fill_rent_order_form(self, delivery_date, rent_time, color, comment):
        # Клик по полю Когда привезти
        self.click(OrderLocators.INPUT_WHEN_DELIVERY)

        # Ожидание, что появилось меню-календарь с датами
        self.wait_visible(OrderLocators.LIST_DAY)

        # Клик по выбору даты доставки
        delivery_date_locators = {
            "29": OrderLocators.DATE_DELIVERY_25,
            "27": OrderLocators.DATE_DELIVERY
        }
        self.click(delivery_date_locators[delivery_date])

        # Клик по выпадающему списку выбору времени аренды
        self.click(OrderLocators.BTN_DROP_DOWN_RENT)

        rent_locators = {
            "сутки": OrderLocators.SELECT_TIME_DAY,
            "двое суток": OrderLocators.SELECT_TIME_TWO_DAY
        }
        self.click(rent_locators[rent_time])

        # Ожидание, что чек-бокс выбора самоката кликабелен
        self.wait_visible(OrderLocators.BLACK_CHECKBOX)

        # Клик по выбору цвета самоката
        color_locators = {
            "black": OrderLocators.BLACK_CHECKBOX,
            "grey": OrderLocators.GREY_CHECKBOX
        }
        self.click(color_locators[color])

        # Клик по полю комментарий для курьера и заполнение
        self.enter_text(OrderLocators.INPUT_COMMENT, comment)

        # Ожидание, что кнопка Заказать будет кликабельна
        self.wait_visible(OrderLocators.BTN_ORDER)

        # Клик по кнопке Заказать
        self.click(OrderLocators.BTN_ORDER)


        