from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.question_locators import QuestionLocators
from page_objects.base_page import BasePage


class Faq(BasePage):
    def __init__(self, driver, question_locator, answer_locator, expected_text):
        super().__init__(driver)  # Инициализация родительского класса
        self.locators = QuestionLocators
        self.question_locator = question_locator
        self.answer_locator = answer_locator
        self.expected_text = expected_text

    # Ожидание, что видно таблицу с вопросами
    def wait_open_drop_down_and_text_visible(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.answer_locator))
        
    # Получение текста на вопрос
    def get_description(self):
        return self.driver.find_element(*self.answer_locator).text
    
