import pytest
from selenium import webdriver
from locators.question_locators import QuestionLocators
from page_objects.main_page import Question

class TestAssertQuestion:
    @pytest.mark.parametrize("question_locator, answer_locator, expected_text", [
        (
            QuestionLocators.BTN_DROP_DOWN_CLOSE_ONE,
            QuestionLocators.QUESTION_TEXT_ONE,
            'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        ),
        (
            QuestionLocators.BTN_DROP_DOWN_CLOSE_TWO,
            QuestionLocators.QUESTION_TEXT_TWO,
            'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
        ),
        (
            QuestionLocators.BTN_DROP_DOWN_CLOSE_THREE,
            QuestionLocators.QUESTION_TEXT_THREE,
            'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
        ),
        (   
            QuestionLocators.BTN_DROP_DOWN_CLOSE_FOUR,
            QuestionLocators.QUESTION_TEXT_FOUR,
            "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
        ),
        (   
            QuestionLocators.BTN_DROP_DOWN_CLOSE_FIVE,
            QuestionLocators.QUESTION_TEXT_FIVE,
            "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
        ),
        (   
            QuestionLocators.BTN_DROP_DOWN_CLOSE_SIX,
            QuestionLocators.QUESTION_TEXT_SIX,
            "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
        ),
        (
            QuestionLocators.BTN_DROP_DOWN_CLOSE_SEVEN,
            QuestionLocators.QUESTION_TEXT_SEVEN,
            "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
        ),
        (
            QuestionLocators.BTN_DROP_DOWN_CLOSE_EIGHT,
            QuestionLocators.QUESTION_TEXT_EIGHT,
            "Да, обязательно. Всем самокатов! И Москве, и Московской области."
        )
    ])
    def test_faq_question(self, driver, question_locator, answer_locator, expected_text):
        # Открываем страницу
        driver.get('https://qa-scooter.praktikum-services.ru/')
        
        # Инициализация страницы с параметрами
        page = Question(driver, question_locator, answer_locator, expected_text)
        
        # Скроллим и кликаем по вопросу
        page.scroll_to_element()
        
        # Ждем появления текста
        page.wait_open_drop_down_and_text_visible()
        
        # Получаем текст и сравниваем
        description = page.get_description()
        assert description == expected_text