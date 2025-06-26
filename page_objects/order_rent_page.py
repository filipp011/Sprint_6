from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_locators import OrderLocators
from page_objects.base_page import BasePage

class Rent(BasePage):
    def __init__(self, driver):
        # Инициализация родительского класса
        super().__init__(driver) 

    def fill_rent_order_form(self, delivery_date, rent_time, color, comment):
        # Клик по полю Когда привезти
        self.driver.find_element(*OrderLocators.INPUT_WHEN_DELIVERY).click()
        
        # Ожидание, что появилось меню-календарь с датами
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderLocators.LIST_DAY))
        
        # Клик по выбору даты доставки
        delivery_date_locators = {
            "29": OrderLocators.DATE_DELIVERY_25,
            "27": OrderLocators.DATE_DELIVERY
        }
        self.driver.find_element(*delivery_date_locators[delivery_date]).click()

        # Клик по выпадающему списку выбору времени аренды
        self.driver.find_element(*OrderLocators.BTN_DROP_DOWN_RENT).click()
        
        rent_locators = {
            "сутки": OrderLocators.SELECT_TIME_DAY,
            "двое суток": OrderLocators.SELECT_TIME_TWO_DAY
        }
        self.driver.find_element(*rent_locators[rent_time]).click()

        # Ожидание, что чек-бокс выбора самоката кликабелен
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(OrderLocators.BLACK_CHECKBOX))

        # Клик по выбору цвета самоката
        color_locators = {
            "black": OrderLocators.BLACK_CHECKBOX,
            "grey": OrderLocators.GREY_CHECKBOX
        }
        self.driver.find_element(*color_locators[color]).click()

        # Клик по полю комментарий для курьера и заполнение
        self.driver.find_element(*OrderLocators.INPUT_COMMENT).send_keys(comment)

        # Ожидание, что кнопка Заказать будет кликабельна
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(OrderLocators.BTN_ORDER))

        # Клик по кнопке Заказать
        self.driver.find_element(*OrderLocators.BTN_ORDER).click()

        