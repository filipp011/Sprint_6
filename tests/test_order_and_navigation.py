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
from data import BASE_URL, DZEN_URL

class TestOrder:
    @pytest.mark.parametrize("name, last_name, address, metro, telephone, comment, delivery_date, rent_time, color", [
        ("Иван", "Иванов", "Москва, ул. Пушкина, д. 1", "Бульвар Рокоссовского", "+79001234567", "Оставьте у двери", "29", "сутки", "black"),
        ("Петр", "Петров", "Москва, ул. Лермонтова, д. 2", "Черкизовская", "+79007654321", "Позвоните перед приездом", "27", "двое суток", "grey")
    ])
    def test_order_success_text(self, driver: WebDriver, name, last_name, address, metro, telephone, comment, delivery_date, rent_time, color):
        driver.get(BASE_URL)
        order_for_whom_page = ForWhom(driver)
        main_page = Main(driver)
        order_rent_page = Rent(driver)
        popup_order_success = PopUpSuccess(driver)
        popup_confirmation_page = PopUpConfirmation(driver)

        # Выполняем оформление заказа
        main_page.click_button_order()
        # Вводим имя
        order_for_whom_page.input_name(name)
        # Вводим фамилию
        order_for_whom_page.input_last_name(last_name)
        # Вводим адрес
        order_for_whom_page.input_address(address)
        # Выбираем метро
        order_for_whom_page.click_input_metro()
        order_for_whom_page.select_metro(metro)
        # Вводим телефон
        order_for_whom_page.input_telephone(telephone)
        # Кликаем по кнопке далее
        order_for_whom_page.click_button_next()
        # Выбираем дату доставки
        order_rent_page.click_when_delivery()
        order_rent_page.select_delivery_date(delivery_date)
        # Выбор сутки
        order_rent_page.click_select_time(rent_time)
        # Выбор цвета самоката
        order_rent_page.click_color_samokat(color)
        # Комментарий для курьера
        order_rent_page.input_comment(comment)
        # Оформляем заказ
        order_rent_page.click_button_order()
        # Подтверждаем заказ
        popup_confirmation_page.click_button_yes()
        # Проверяем текст в поп-апе
        result_text = popup_order_success.get_description()
        # Проверяем, что заказ оформлен
        assert "Заказ оформлен" in result_text


class TestRedirectMainPage:
    @pytest.mark.parametrize("name, last_name, address, metro, telephone, comment, delivery_date, rent_time, color", [
        ("Иван", "Иванов", "Москва, ул. Пушкина, д. 1", "Бульвар Рокоссовского", "+79001234567", "Оставьте у двери", "29", "сутки", "black"),
        ("Петр", "Петров", "Москва, ул. Лермонтова, д. 2", "Черкизовская", "+79007654321", "Позвоните перед приездом", "27", "двое суток", "grey")
    ])
    def test_order_success_text(self, driver: WebDriver, name, last_name, address, metro, telephone, comment, delivery_date, rent_time, color):
        driver.get(BASE_URL)
        order_for_whom_page = ForWhom(driver)
        main_page = Main(driver)
        order_rent_page = Rent(driver)
        popup_confirmation_page = PopUpConfirmation(driver)
        popup_number_order = PopUpNumberOrder(driver)
        status_page = StatusPage(driver)

        # Выполняем оформление заказа
        main_page.click_button_order()
        # Вводим имя
        order_for_whom_page.input_name(name)
        # Вводим фамилию
        order_for_whom_page.input_last_name(last_name)
        # Вводим адрес
        order_for_whom_page.input_address(address)
        # Выбираем метро
        order_for_whom_page.click_input_metro()
        order_for_whom_page.select_metro(metro)
        # Вводим телефон
        order_for_whom_page.input_telephone(telephone)
        # Кликаем по кнопке далее
        order_for_whom_page.click_button_next()
        # Выбираем дату доставки
        order_rent_page.click_when_delivery()
        order_rent_page.select_delivery_date(delivery_date)
        # Выбор сутки
        order_rent_page.click_select_time(rent_time)
        # Выбор цвета самоката
        order_rent_page.click_color_samokat(color)
        # Комментарий для курьера
        order_rent_page.input_comment(comment)
        # Оформляем заказ
        order_rent_page.click_button_order()
        # Подтверждаем заказ
        popup_confirmation_page.click_button_yes()
        # Кликаем переходим на страницу статуса заказа
        popup_number_order.click_button_status()
        # Кликаем на часть лого самокат
        status_page.click_logo_samokat()
        # Проверяем, что перешли на главную страницу Яндекс Самоката
        status_page.get_url_main_page()

        assert status_page.get_url_main_page()


    class TestRedirectDzen:
        @pytest.mark.parametrize("name, last_name, address, metro, telephone, comment, delivery_date, rent_time, color", [
        ("Иван", "Иванов", "Москва, ул. Пушкина, д. 1", "Бульвар Рокоссовского", "+79001234567", "Оставьте у двери", "29", "сутки", "black"),
        ("Петр", "Петров", "Москва, ул. Лермонтова, д. 2", "Черкизовская", "+79007654321", "Позвоните перед приездом", "27", "двое суток", "grey")
    ])
        def test_order_success_text(self, driver: WebDriver, name, last_name, address, metro, telephone, comment, delivery_date, rent_time, color):
            driver.get(BASE_URL)
            order_page_for_whom_page = ForWhom(driver)
            main_page = Main(driver)
            order_rent_page = Rent(driver)
            popup_confirmation_page = PopUpConfirmation(driver)
            popup_number_order = PopUpNumberOrder(driver)
            status_page = StatusPage(driver)

            # Выполняем оформление заказа
            main_page.click_button_order()
            # Вводим имя
            order_page_for_whom_page.input_name(name)
            # Вводим фамилию
            order_page_for_whom_page.input_last_name(last_name)
            # Вводим адрес
            order_page_for_whom_page.input_address(address)
            # Выбираем метро
            order_page_for_whom_page.click_input_metro()
            order_page_for_whom_page.select_metro(metro)
            # Вводим телефон
            order_page_for_whom_page.input_telephone(telephone)
            # Кликаем по кнопке далее
            order_page_for_whom_page.click_button_next()
            # Выбираем дату доставки
            order_rent_page.click_when_delivery()
            order_rent_page.select_delivery_date(delivery_date)
            # Выбор сутки
            order_rent_page.click_select_time(rent_time)
            # Выбор цвета самоката
            order_rent_page.click_color_samokat(color)
            # Комментарий для курьера
            order_rent_page.input_comment(comment)
            # Оформляем заказ
            order_rent_page.click_button_order()
            # Подтверждаем заказ
            popup_confirmation_page.click_button_yes()
            # Кликаем переходим на страницу статуса заказа
            popup_number_order.click_button_status()
            # Кликаем на лого Яндекса
            status_page.click_logo_ya()
            # Переключаемся на новое окно
            status_page.switch_new_window()
            # Проверяем, что перешли на Дзен
            status_page.check_new_window_dzen()
            current_url = status_page.check_new_window_dzen()
            assert current_url == DZEN_URL
