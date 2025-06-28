import pytest
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from conftest import driver
from page_objects.main_page import Main
from page_objects.order_for_whom_page import ForWhom
from page_objects.order_rent_page import Rent
from page_objects.popup_confirmation_page import PopUpConfirmation
from page_objects.popup_order_success import PopUpSuccess
from page_objects.popup_number_order import PopUpNumberOrder
from page_objects.status_page import StatusPage
from locators.order_locators import OrderLocators
from data import BASE_URL, DZEN_URL

class TestOrder:
    @pytest.mark.parametrize("name, last_name, address, metro, telephone, comment, delivery_date, rent_time, color, button", [
        ("Иван", "Иванов", "Москва, ул. Пушкина, д. 1", "Бульвар Рокоссовского", "+79001234567", "Оставьте у двери", "29", "сутки", "black", OrderLocators.BTN_ORDER_HEADER),
        ("Петр", "Петров", "Москва, ул. Лермонтова, д. 2", "Черкизовская", "+79007654321", "Позвоните перед приездом", "27", "двое суток", "grey", OrderLocators.BTN_ORDER_FOOTER)
    ])
    def test_order_success_text(self, driver, name, last_name, address, metro, telephone, comment, delivery_date, rent_time, color, button):
        # Инициализация страниц
        main_page = Main(driver)
        order_for_whom_page = ForWhom(driver)
        order_rent_page = Rent(driver)
        popup_order_success = PopUpSuccess(driver)
        popup_confirmation_page = PopUpConfirmation(driver)

        # Открытие страницы и принятие куки
        main_page.open_main_page_and_accept_cookies()
        
        # Оформление заказа
        main_page.scroll_and_click_button(button)  # Используем метод для прокрутки и клика по кнопке

        # Заполнение формы заказа
        order_for_whom_page.fill_order_form(name, last_name, address, metro, telephone)
        
        # Выбор даты доставки и деталей аренды
        order_rent_page.fill_rent_order_form(delivery_date, rent_time, color, comment)
        
        # Подтверждение заказа
        popup_confirmation_page.click_button_yes()

        # Проверка успешного оформления заказа
        result_text = popup_order_success.get_description()
        assert "Заказ оформлен" in result_text


class TestRedirectMainPage:
    @pytest.mark.parametrize("name, last_name, address, metro, telephone, comment, delivery_date, rent_time, color, button", [
        ("Иван", "Иванов", "Москва, ул. Пушкина, д. 1", "Бульвар Рокоссовского", "+79001234567", "Оставьте у двери", "29", "сутки", "black", OrderLocators.BTN_ORDER_HEADER),
        ("Петр", "Петров", "Москва, ул. Лермонтова, д. 2", "Черкизовская", "+79007654321", "Позвоните перед приездом", "27", "двое суток", "grey", OrderLocators.BTN_ORDER_FOOTER)
    ])
    def test_redirect_main_page(self, driver, name, last_name, address, metro, telephone, comment, delivery_date, rent_time, color, button):
        
        order_for_whom_page = ForWhom(driver)
        main_page = Main(driver)
        order_rent_page = Rent(driver)
        popup_confirmation_page = PopUpConfirmation(driver)
        popup_number_order = PopUpNumberOrder(driver)
        status_page = StatusPage(driver)

        # Открытие страницы и принятие куки
        main_page.open_main_page_and_accept_cookies()
        
        # Оформление заказа
        main_page.scroll_and_click_button(button)  # Используем метод для прокрутки и клика по кнопке

        # Заполнение формы заказа
        order_for_whom_page.fill_order_form(name, last_name, address, metro, telephone)
        
        # Выбор даты доставки и деталей аренды
        order_rent_page.fill_rent_order_form(delivery_date, rent_time, color, comment)
        
        # Подтверждение заказа
        popup_confirmation_page.click_button_yes()
        # Кликаем переходим на страницу статуса заказа
        popup_number_order.click_button_status()
        # Кликаем на часть лого самокат
        status_page.click_logo_samokat()

        # Проверяем, что перешли на главную страницу Яндекс Самоката
        status_page.get_url_main_page()
        assert status_page.get_url_main_page()


    class TestRedirectDzen:
        @pytest.mark.parametrize("name, last_name, address, metro, telephone, comment, delivery_date, rent_time, color, button", [
        ("Иван", "Иванов", "Москва, ул. Пушкина, д. 1", "Бульвар Рокоссовского", "+79001234567", "Оставьте у двери", "29", "сутки", "black", OrderLocators.BTN_ORDER_HEADER),
        ("Петр", "Петров", "Москва, ул. Лермонтова, д. 2", "Черкизовская", "+79007654321", "Позвоните перед приездом", "27", "двое суток", "grey", OrderLocators.BTN_ORDER_FOOTER)
    ])
        def test_redirect_dzen_page(self, driver, name, last_name, address, metro, telephone, comment, delivery_date, rent_time, color, button):
            order_for_whom_page = ForWhom(driver)
            main_page = Main(driver)
            order_rent_page = Rent(driver)
            popup_confirmation_page = PopUpConfirmation(driver)
            popup_number_order = PopUpNumberOrder(driver)
            status_page = StatusPage(driver)
            
            # Открытие страницы и принятие куки
            main_page.open_main_page_and_accept_cookies()
        
            # Оформление заказа
            main_page.scroll_and_click_button(button)  # Используем метод для прокрутки и клика по кнопке

            # Заполнение формы заказа
            order_for_whom_page.fill_order_form(name, last_name, address, metro, telephone)
        
            # Выбор даты доставки и деталей аренды
            order_rent_page.fill_rent_order_form(delivery_date, rent_time, color, comment)
        
            # Подтверждение заказа
            popup_confirmation_page.click_button_yes()
            # Кликаем переходим на страницу статуса заказа
            popup_number_order.click_button_status()
            # Кликаем на лого Яндекса
            status_page.click_logo_and_switch_window()
            # Проверяем, что перешли на Дзен
            status_page.check_new_window_dzen()
            
            current_url = status_page.check_new_window_dzen()
            assert current_url == DZEN_URL
