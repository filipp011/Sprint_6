import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.order_locators import BaseLocators


class OrderPage():
    def __init__(self, driver):
        self.driver = driver

    # Клик по кнопке Принять куки
    def click_button_cookie(self):
        self.driver.find_element(*BaseLocators.COOKIE).click()

    # Клик по кнопке заказать
    def click_button_order(self):
        self.driver.find_element(*BaseLocators.BTN_ORDER_HEADER).click()

    # Ввод имени в поле имя
    def input_name(self, name):
        self.driver.find_element(*BaseLocators.INPUT_NAME).send_keys(name)

    # Ввод фамилии в поле фамилия
    def input_last_name(self, last_name):
        self.driver.find_element(*BaseLocators.INPUT_LAST_NAME).send_keys(last_name)

    # Ввод адреса в поле адрес
    def input_address(self, address):
        self.driver.find_element(*BaseLocators.INPUT_ADDRESS).send_keys(address)

    # Клик на поле метро
    def click_input_metro(self):
        self.driver.find_element(*BaseLocators.INPUT_DEFAULT_METRO).click()

    # Выбор метро
    def select_metro(self, metro):
        metro_locators = {
        "Бульвар Рокоссовского": BaseLocators.METRO_BULVAR,
        "Черкизовская": BaseLocators.METRO_BULVAR_CHERKIZ
    }
        self.driver.find_element(*metro_locators[metro]).click()

    # Ввод номера телефона в поле телефон
    def input_telephone(self, telephone):
        self.driver.find_element(*BaseLocators.INPUT_TELEPHONE).send_keys(telephone)

    # Клик по кнопке Далее
    def click_button_next(self):
        self.driver.find_element(*BaseLocators.BTN_NEXT).click()

    # Клик по полю Когда привезти
    def click_when_delivery(self):
        self.driver.find_element(*BaseLocators.INPUT_WHEN_DELIVERY).click()

    # Ожидание, что появилось меню-клаендарь с датами
    def wait_list_day(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(BaseLocators.LIST_DAY))

    # Клик по выбору даты доставки
    def select_delivery_date(self, delivery_date):
        delivery_date_locators = {
        "29": BaseLocators.DATE_DELIVERY_25,
        "27": BaseLocators.DATE_DELIVERY
    }
        # Кликаем по локатору, соответствующему выбранной дате
        self.driver.find_element(*delivery_date_locators[delivery_date]).click()

    # Клик по выпадающему списку выбору времени аренды. Выбрали сутки
    def click_select_time(self, rent_time):
        self.driver.find_element(*BaseLocators.BTN_DROP_DOWN_RENT).click()
        
        rent_locators = {
            "сутки": BaseLocators.SELECT_TIME_DAY,
            "двое суток": BaseLocators.SELECT_TIME_TWO_DAY
        }
        
        # Клик по локатору, соответствующему времени аренды
        self.driver.find_element(*rent_locators[rent_time]).click()

    # Ожидание что чек-бок выбора самоката кликабелен
    def wait_chekboks_clickable(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(BaseLocators.BLACK_CHECKBOX))

    # Клик по выбору цвета самоката. Выбираем черный.
    def click_color_samokat(self, color):
        # Словарь локаторов для цветов самоката
        color_locators = {
        "black": BaseLocators.BLACK_CHECKBOX,
        "grey": BaseLocators.GREY_CHECKBOX
    }
    
        # Кликаем по локатору, соответствующему выбранному цвету
        self.driver.find_element(*color_locators[color]).click()
        

    # Клик по полю комментарий для курьера. И заполнение
    def input_comment(self, comment):
        self.driver.find_element(*BaseLocators.INPUT_COMMENT).send_keys(comment)

    # Ожидание что кнопка Заказать будет кликабельна
    def wait_clikable_button_order(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(BaseLocators.BTN_ORDER))

    # Клик по кнопке Заказать
    def click_button_order(self):
        self.driver.find_element(*BaseLocators.BTN_ORDER).click()

    # Ожидание поп-апа подтверждения
    def wait_pop_up_yes_or_no(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(BaseLocators.POP_UP_YES_NO))

    # Клик по кнопке Да-подтверждение заказа
    def click_button_yes(self):
        self.driver.find_element(*BaseLocators.BTN_YES).click()

    # Ожидание появление поп-апа об успешном оформлении
    def wait_pop_up(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(BaseLocators.TEXT_ORDER_SUCCESS))

    # Получение текста из поп-апа успешного оформления заказа
    def get_description(self):
        return self.driver.find_element(*BaseLocators.TEXT_ORDER_SUCCESS).text

    # Переход в профиль статуса заказа
    def click_button_status(self):
        self.driver.find_element(*BaseLocators.BTN_STATUS).click()

    # Клик на лого Самоката
    def click_logo_samokat(self):
        self.driver.find_element(*BaseLocators.BTN_SAMOKAT).click()

    # Проверяем что перешли на главную страницу Яндекс Самоката
    def get_url_main_page(self):
        expected_url = "https://qa-scooter.praktikum-services.ru/"
        current_url = self.driver.current_url
        return current_url == expected_url
    
    # Клик на лого Яндекса
    def click_logo_ya(self):
        self.driver.find_element(*BaseLocators.BTN_LOGO_YA).click()

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
        

