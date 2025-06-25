import pytest
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from conftest import driver
from page_objects.order_page import OrderPage
import time

class TestOrder:
    @pytest.mark.parametrize("name, last_name, address, metro, telephone, comment, delivery_date, rent_time, color", [
        ("Иван", "Иванов", "Москва, ул. Пушкина, д. 1", "Бульвар Рокоссовского", "+79001234567", "Оставьте у двери", "29", "сутки", "black"),
        ("Петр", "Петров", "Москва, ул. Лермонтова, д. 2", "Черкизовская", "+79007654321", "Позвоните перед приездом", "27", "двое суток", "grey")
    ])
    def test_order_success_text(self, driver: WebDriver, name, last_name, address, metro, telephone, comment, delivery_date, rent_time, color):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        order_page = OrderPage(driver)

        # Клик по кнопке принять куки
        order_page.click_button_cookie()
        # Выполняем оформление заказа
        order_page.click_button_order()
        # Вводим имя
        order_page.input_name(name)
        # Вводим фамилию
        order_page.input_last_name(last_name)
        # Вводим адрес
        order_page.input_address(address)
        # Выбираем метро
        order_page.click_input_metro()
        order_page.select_metro(metro)
        # Вводим телефон
        order_page.input_telephone(telephone)
        # Кликаем по кнопке далее
        order_page.click_button_next()
        # Выбираем дату доставки
        order_page.click_when_delivery()
        # Ожидаем что меню с датами появилось
        order_page.wait_list_day()
        order_page.select_delivery_date(delivery_date)
        # Выбор сутки
        order_page.click_select_time(rent_time)
        # Ожидание что чек-бокс кликабелен
        order_page.wait_chekboks_clickable()
        # Выбор цвета самоката
        order_page.click_color_samokat(color)
        # Комментарий для курьера
        order_page.input_comment(comment)
        # Ожидаем что кнопка заказа кликабельна
        order_page.wait_clikable_button_order()
        # Оформляем заказ
        order_page.click_button_order()
        # Ожидаем поп-ап с подтверждением
        order_page.wait_pop_up_yes_or_no()
        # Подтверждаем заказ
        order_page.click_button_yes()
        # Ожидаем поп-ап
        order_page.wait_pop_up()
        # Проверяем текст в поп-апе
        result_text = order_page.get_description()
        # Проверяем, что заказ оформлен
        assert "Заказ оформлен" in result_text


class TestRedirectMainPage:
    @pytest.mark.parametrize("name, last_name, address, metro, telephone, comment, delivery_date, rent_time, color", [
        ("Иван", "Иванов", "Москва, ул. Пушкина, д. 1", "Бульвар Рокоссовского", "+79001234567", "Оставьте у двери", "29", "сутки", "black"),
        ("Петр", "Петров", "Москва, ул. Лермонтова, д. 2", "Черкизовская", "+79007654321", "Позвоните перед приездом", "27", "двое суток", "grey")
    ])
    def test_order_success_text(self, driver: WebDriver, name, last_name, address, metro, telephone, comment, delivery_date, rent_time, color):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        order_page = OrderPage(driver)

        # Клик по кнопке принять куки
        order_page.click_button_cookie()
        # Выполняем оформление заказа
        order_page.click_button_order()
        # Вводим имя
        order_page.input_name(name)
        # Вводим фамилию
        order_page.input_last_name(last_name)
        # Вводим адрес
        order_page.input_address(address)
        # Выбираем метро
        order_page.click_input_metro()
        order_page.select_metro(metro)
        # Вводим телефон
        order_page.input_telephone(telephone)
        # Кликаем по кнопке далее
        order_page.click_button_next()
        # Выбираем дату доставки
        order_page.click_when_delivery()
        # Ожидаем что меню с датами появилось
        order_page.wait_list_day()
        order_page.select_delivery_date(delivery_date)
        # Выбор сутки
        order_page.click_select_time(rent_time)
        # Ожидание что чек-бокс кликабелен
        order_page.wait_chekboks_clickable()
        # Выбор цвета самоката
        order_page.click_color_samokat(color)
        # Комментарий для курьера
        order_page.input_comment(comment)
        # Ожидаем что кнопка заказа кликабельна
        order_page.wait_clikable_button_order()
        # Оформляем заказ
        order_page.click_button_order()
        # Ожидаем поп-ап с подтверждением
        order_page.wait_pop_up_yes_or_no()
        # Подтверждаем заказ
        order_page.click_button_yes()
        # Кликаем переходим на страницу статуса заказа
        order_page.click_button_status()
        # Кликаем на часть лого самокат
        order_page.click_logo_samokat()
        # Проверяем, что перешли на главную страницу Яндекс Самоката
        order_page.get_url_main_page()

        assert order_page.get_url_main_page()


    class TestRedirectDzen:
        @pytest.mark.parametrize("name, last_name, address, metro, telephone, comment, delivery_date, rent_time, color", [
        ("Иван", "Иванов", "Москва, ул. Пушкина, д. 1", "Бульвар Рокоссовского", "+79001234567", "Оставьте у двери", "29", "сутки", "black"),
        ("Петр", "Петров", "Москва, ул. Лермонтова, д. 2", "Черкизовская", "+79007654321", "Позвоните перед приездом", "27", "двое суток", "grey")
    ])
        def test_order_success_text(self, driver: WebDriver, name, last_name, address, metro, telephone, comment, delivery_date, rent_time, color):
            driver.get('https://qa-scooter.praktikum-services.ru/')
            order_page = OrderPage(driver)

            # Клик по кнопке принять куки
            order_page.click_button_cookie()
            # Выполняем оформление заказа
            order_page.click_button_order()
            # Вводим имя
            order_page.input_name(name)
            # Вводим фамилию
            order_page.input_last_name(last_name)
            # Вводим адрес
            order_page.input_address(address)
            # Выбираем метро
            order_page.click_input_metro()
            order_page.select_metro(metro)
            # Вводим телефон
            order_page.input_telephone(telephone)
            # Кликаем по кнопке далее
            order_page.click_button_next()
            # Выбираем дату доставки
            order_page.click_when_delivery()
            # Ожидаем что меню с датами появилось
            order_page.wait_list_day()
            order_page.select_delivery_date(delivery_date)
            # Выбор сутки
            order_page.click_select_time(rent_time)
            # Ожидание что чек-бокс кликабелен
            order_page.wait_chekboks_clickable()
            # Выбор цвета самоката
            order_page.click_color_samokat(color)
            # Комментарий для курьера
            order_page.input_comment(comment)
            # Ожидаем что кнопка заказа кликабельна
            order_page.wait_clikable_button_order()
            # Оформляем заказ
            order_page.click_button_order()
            # Ожидаем поп-ап с подтверждением
            order_page.wait_pop_up_yes_or_no()
            # Подтверждаем заказ
            order_page.click_button_yes()
            # Кликаем и переходим на страницу статуса заказа
            order_page.click_button_status()
            # Кликаем на лого Яндекса
            order_page.click_logo_ya()
            # Ожидаем появление нового окна
            order_page.wait_new_window_dzen()
            # Переключаемся на новое окно
            order_page.switch_new_window()
            # Проверяем, что перешли на Дзен
            order_page.check_new_window_dzen()
            current_url = order_page.check_new_window_dzen()
            assert current_url == "https://dzen.ru/?yredirect=true"
