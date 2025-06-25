from selenium.webdriver.common.by import By

class QuestionLocators():

    # Кнопка дроп-дауна "Сколько это стоит? И как оплатить?"
    BTN_DROP_DOWN_CLOSE_ONE = (By.XPATH, ".//div[@aria-disabled='false' and text()='Сколько это стоит? И как оплатить?']")
    # Текст после клика на дроп-даун
    QUESTION_TEXT_ONE = (By.XPATH, ".//div[@class='accordion__panel']//p[contains(text(), 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.')]")
    # Кнопка дроп-дауна Хочу сразу несколько самокатов! Так можно?
    BTN_DROP_DOWN_CLOSE_TWO = (By.XPATH, ".//div[@aria-disabled='false' and text()='Хочу сразу несколько самокатов! Так можно?']")
    # Текст после клика на дроп-даун
    QUESTION_TEXT_TWO = (By.XPATH, ".//div[@class='accordion__panel']//p[contains(text(), 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.')]")
    # Кнопка дроп-дауна "Как рассчитывается время аренды?"
    BTN_DROP_DOWN_CLOSE_THREE = (By.XPATH, ".//div[@aria-disabled='false' and text()='Как рассчитывается время аренды?']")
    # Текст после клика на дроп-даун
    QUESTION_TEXT_THREE = (By.XPATH, ".//div[@class='accordion__panel']//p[contains(text(), 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')]")
    # Кнопка дроп-дауна "Можно ли заказать самокат прямо на сегодня?"
    BTN_DROP_DOWN_CLOSE_FOUR = (By.XPATH, ".//div[@aria-disabled='false' and text()='Можно ли заказать самокат прямо на сегодня?']")
    # Текст после клика на дроп-даун
    QUESTION_TEXT_FOUR = (By.XPATH, ".//div[@class='accordion__panel']//p[contains(text(), 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.')]")
    # Кнопка дроп-дауна "Можно ли продлить заказ или вернуть самокат раньше?"
    BTN_DROP_DOWN_CLOSE_FIVE = (By.XPATH, ".//div[@aria-disabled='false' and text()='Можно ли продлить заказ или вернуть самокат раньше?']")
    # Текст после клика на дроп-даун
    QUESTION_TEXT_FIVE = (By.XPATH, ".//div[@class='accordion__panel']//p[contains(text(), 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.')]")
    # Кнопка дроп-дауна "Вы привозите зарядку вместе с самокатом?"
    BTN_DROP_DOWN_CLOSE_SIX = (By.XPATH, ".//div[@aria-disabled='false' and text()='Вы привозите зарядку вместе с самокатом?']")
    # Текст после клика на дроп-даун
    QUESTION_TEXT_SIX = (By.XPATH, ".//div[@class='accordion__panel']//p[contains(text(), 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.')]")
    # Кнопка дроп-дауна "Можно ли отменить заказ?"
    BTN_DROP_DOWN_CLOSE_SEVEN = (By.XPATH, ".//div[@aria-disabled='false' and text()='Можно ли отменить заказ?']")
    # Текст после клика на дроп-даун
    QUESTION_TEXT_SEVEN = (By.XPATH, ".//div[@class='accordion__panel']//p[contains(text(), 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.')]")
    # Кнопка дроп-дауна "Я жизу за МКАДом, привезёте?"
    BTN_DROP_DOWN_CLOSE_EIGHT = (By.XPATH, ".//div[@aria-disabled='false' and text()='Я жизу за МКАДом, привезёте?']")
    # Текст после клика на дроп-даун
    QUESTION_TEXT_EIGHT = (By.XPATH, ".//div[@class='accordion__panel']//p[contains(text(), 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')]")



