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
from data import BASE_URL, DZEN_URL, CUSTOMER_1, CUSTOMER_2

class TestOrder:
    @pytest.mark.parametrize("info", [
        CUSTOMER_1,
        CUSTOMER_2
    ])
    def test_order_success_text(self, driver, info):
        name, last_name, address, metro, telephone, comment, delivery_date, rent_time, color, button = info
        
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
    @pytest.mark.parametrize("info", [
        CUSTOMER_1,
        CUSTOMER_2
    ])
    def test_redirect_main_page(self, driver, info):
        name, last_name, address, metro, telephone, comment, delivery_date, rent_time, color, button = info
        
        order_for_whom_page = ForWhom(driver)
        main_page = Main(driver)
        order_rent_page = Rent(driver)
        popup_confirmation_page = PopUpConfirmation(driver)
        popup_number_order = PopUpNumberOrder(driver)
        status_page = StatusPage(driver)

        # Открытие страницы и принятие куки
        main_page.open_main_page_and_accept_cookies()
        
        # Оформление заказа
        main_page.scroll_and_click_button(button)

        # Заполнение формы заказа
        order_for_whom_page.fill_order_form(name, last_name, address, metro, telephone)
        
        # Выбор даты доставки и деталей аренды
        order_rent_page.fill_rent_order_form(delivery_date, rent_time, color, comment)
        
        # Подтверждение заказа
        popup_confirmation_page.click_button_yes()
        
        # Переход на страницу статуса заказа
        popup_number_order.click_button_status()
        
        # Клик на логотип Самоката
        status_page.click_logo_samokat()

        current_url = status_page.is_on_main_page()
        assert current_url == BASE_URL


class TestRedirectDzen:
    @pytest.mark.parametrize("info", [
        CUSTOMER_1,
        CUSTOMER_2
    ])
    def test_redirect_dzen_page(self, driver, info):
        name, last_name, address, metro, telephone, comment, delivery_date, rent_time, color, button = info
        # Инициализация страниц
        order_for_whom_page = ForWhom(driver)
        main_page = Main(driver)
        order_rent_page = Rent(driver)
        popup_confirmation_page = PopUpConfirmation(driver)
        popup_number_order = PopUpNumberOrder(driver)
        status_page = StatusPage(driver)

        # Открытие главной страницы и принятие куки
        main_page.open_main_page_and_accept_cookies()

        # Оформление заказа
        main_page.scroll_and_click_button(button)  # Прокрутка и клик по кнопке

        # Заполнение формы заказа
        order_for_whom_page.fill_order_form(name, last_name, address, metro, telephone)

        # Выбор даты доставки и деталей аренды
        order_rent_page.fill_rent_order_form(delivery_date, rent_time, color, comment)

        # Подтверждение заказа
        popup_confirmation_page.click_button_yes()

        # Переход на страницу статуса заказа
        popup_number_order.click_button_status()

        # Переход на страницу Дзен через клик на логотип Яндекса
        status_page.click_logo_and_switch_window()

        # Проверка, что перешли на Дзен
        current_url = status_page.check_new_window_dzen()
        assert current_url == DZEN_URL