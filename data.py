from locators.order_locators import OrderLocators  # Импортируйте локаторы из вашего файла с локаторами
BASE_URL = 'https://qa-scooter.praktikum-services.ru/'

DZEN_URL = "https://dzen.ru/?yredirect=true"


CUSTOMER_1 = (
    "Иван", "Иванов", "Москва, ул. Пушкина, д. 1", 
    "Бульвар Рокоссовского", "+79001234567", 
    "Оставьте у двери", "29", "сутки", "black", 
    OrderLocators.BTN_ORDER_HEADER  # Добавляем локатор кнопки
)

CUSTOMER_2 = (
    "Петр", "Петров", "Москва, ул. Лермонтова, д. 2", 
    "Черкизовская", "+79007654321", 
    "Позвоните перед приездом", "27", "двое суток", "grey", 
    OrderLocators.BTN_ORDER_FOOTER  # Добавляем локатор кнопки
)