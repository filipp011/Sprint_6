import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.order_locators import OrderLocators

class Rent():
    def __init__(self, driver):
        self.driver = driver

    # Клик по полю Когда привезти
    def click_when_delivery(self):
        self.driver.find_element(*OrderLocators.INPUT_WHEN_DELIVERY).click()

    # Ожидание, что появилось меню-клаендарь с датами
    def wait_list_day(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(OrderLocators.LIST_DAY))

    # Клик по выбору даты доставки
    def select_delivery_date(self, delivery_date):
        delivery_date_locators = {
        "29": OrderLocators.DATE_DELIVERY_25,
        "27": OrderLocators.DATE_DELIVERY
    }
        # Кликаем по локатору, соответствующему выбранной дате
        self.driver.find_element(*delivery_date_locators[delivery_date]).click()

    # Клик по выпадающему списку выбору времени аренды. Выбрали сутки
    def click_select_time(self, rent_time):
        self.driver.find_element(*OrderLocators.BTN_DROP_DOWN_RENT).click()
        
        rent_locators = {
            "сутки": OrderLocators.SELECT_TIME_DAY,
            "двое суток": OrderLocators.SELECT_TIME_TWO_DAY
        }
        
        # Клик по локатору, соответствующему времени аренды
        self.driver.find_element(*rent_locators[rent_time]).click()

    # Ожидание что чек-бок выбора самоката кликабелен
    def wait_chekboks_clickable(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(OrderLocators.BLACK_CHECKBOX))

    # Клик по выбору цвета самоката. Выбираем черный.
    def click_color_samokat(self, color):
        # Словарь локаторов для цветов самоката
        color_locators = {
        "black": OrderLocators.BLACK_CHECKBOX,
        "grey": OrderLocators.GREY_CHECKBOX
    }
    
        # Кликаем по локатору, соответствующему выбранному цвету
        self.driver.find_element(*color_locators[color]).click()
        

    # Клик по полю комментарий для курьера. И заполнение
    def input_comment(self, comment):
        self.driver.find_element(*OrderLocators.INPUT_COMMENT).send_keys(comment)

    # Ожидание что кнопка Заказать будет кликабельна
    def wait_clikable_button_order(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(OrderLocators.BTN_ORDER))

    # Клик по кнопке Заказать
    def click_button_order(self):
        self.driver.find_element(*OrderLocators.BTN_ORDER).click()
        