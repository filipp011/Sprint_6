from selenium.webdriver.common.by import By

class BaseLocators():
    # Кнопка куки
    COOKIE = (By.XPATH, ".//button[@class='App_CookieButton__3cvqF']")
    #Кнопка Заказать в header
    BTN_ORDER_HEADER = (By.XPATH, ".//button[@class='Button_Button__ra12g' and text()='Заказать']")
    # Кнопка заказать в footer 
    BTN_ORDER_FOOTER = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    # Поле ввода Имя
    INPUT_NAME = (By.XPATH, ".//div[contains(@class, 'Input_InputContainer')]//input[@placeholder='* Имя']")
    # Поле ввода Фамилия
    INPUT_LAST_NAME = (By.XPATH, ".//div[contains(@class, 'Input_InputContainer')]//input[@placeholder='* Фамилия']")
    # Поле ввода Адреса
    INPUT_ADDRESS = (By.XPATH, ".//div[contains(@class, 'Input_InputContainer')]//input[@placeholder='* Адрес: куда привезти заказ']")
    # Дефолтное поле выбора Станции метро
    INPUT_DEFAULT_METRO = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    # Выпадающий список станций метро 
    LIST_METRO = (By.XPATH, ".//div[@class='select-search__select']")
    # Выбор метро Бульвара Рокоссовского
    METRO_BULVAR = (By.XPATH, ".//div[@class='Order_Text__2broi' and text()='Бульвар Рокоссовского']")
    # Выбор метро Черкизовская
    METRO_BULVAR_CHERKIZ = (By.XPATH, ".//div[@class='Order_Text__2broi' and text()='Черкизовская']")
    # Поле ввода Телефона
    INPUT_TELEPHONE = (By.XPATH, ".//div[contains(@class, 'Input_InputContainer')]//input[@placeholder='* Телефон: на него позвонит курьер']")
    # Кнопка Далее 
    BTN_NEXT = (By.XPATH,".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Далее']")

    #Следующая страница заказа Про аренду
    # Поле Когда привезти
    INPUT_WHEN_DELIVERY = (By.CSS_SELECTOR,'input[placeholder="* Когда привезти самокат"]')
    # Выпадающее меню-календарь 
    LIST_DAY = (By.CLASS_NAME, "react-datepicker__month")
    # Кнопка далее в календаре
    NEXT_MONTH = (By.CLASS_NAME, "react-datepicker__navigation react-datepicker__navigation--next")
    # Выбор даты Когда привезти 27
    DATE_DELIVERY = (By.XPATH, "//div[text()='27']")
    # Выбор даты Когда привезти 25
    DATE_DELIVERY_25 = (By.XPATH, "//div[text()='29']")
    # Дроп-даун Срок Аренды
    BTN_DROP_DOWN_RENT = (By.CLASS_NAME,"Dropdown-root")
    # Список времени аренды самоката
    LIST_TIME = (By.CLASS_NAME, "Dropdown-menu")
    # Выбор времени аренды самоката (Сутки)
    SELECT_TIME_DAY = (By.XPATH, ".//div[@class='Dropdown-option' and text()='сутки']")
    # Выбор времени аренды самоката (Двое суток)
    SELECT_TIME_TWO_DAY = (By.XPATH, ".//div[@class='Dropdown-option' and text()='двое суток']")
    # Выбор цвета самоката
    BLACK_CHECKBOX = (By.XPATH, "//div[@class='Order_Checkboxes__3lWSI']//input[@id='black']")
    # Выбор цвета самоката серый
    GREY_CHECKBOX = (By.XPATH, "//div[@class='Order_Checkboxes__3lWSI']//input[@id='grey']")
    # Поле Комментарий курьера
    INPUT_COMMENT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    # Кнопка заказать
    BTN_ORDER = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']")
    # Поп-ап подтверждения заказа
    POP_UP_YES_NO = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    # Кнопка Да в поп-апе подтверждения заказа
    BTN_YES = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Да']")
    # POP_UP успешного оформления заказа 
    POP_UP_ORDER_SUCCESS = (By.CLASS_NAME, "Order_Modal__YZ-d3")
    # Текст заказа: Заказ оформлен
    TEXT_ORDER_SUCCESS = (By.XPATH, ".//div[@class='Order_ModalHeader__3FDaJ' and text()='Заказ оформлен']")
    # Клик на кнопку Посмотреть статус
    BTN_STATUS = (By.CSS_SELECTOR, 'div.Order_NextButton__1_rCA > button.Button_Button__ra12g.Button_Middle__1CSJM')
    # Кнопка лого Яндекс
    BTN_LOGO_YA = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    # Кнопка Самокат
    BTN_SAMOKAT = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")