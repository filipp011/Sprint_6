from selenium.webdriver.support import expected_conditions as EC
from locators.question_locators import QuestionLocators
from page_objects.base_page import BasePage

class Faq(BasePage):
    def __init__(self, driver, question_locator, answer_locator, expected_text):
        super().__init__(driver, QuestionLocators)  # Передаем локаторы
        self.question_locator = question_locator
        self.answer_locator = answer_locator
        self.expected_text = expected_text

    def scroll_to_element_and_click(self, locator):
    # Ожидание, что элемент видим
        element = self.wait.until(EC.visibility_of_element_located(locator))
    
    # Прокрутка к элементу
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    
    # Ожидание, что элемент кликабельный
        self.wait.until(EC.element_to_be_clickable(locator))
    
    # Клик по элементу
        element.click()


    # Ожидание, что видно ответ на вопрос
    def wait_open_drop_down_and_text_visible(self):
        self.wait_visible(self.answer_locator)  # Используем метод из BasePage

    # Получение текста на вопрос
    def get_description(self):
        return self.get_text(self.answer_locator)  # Используем метод из BasePage

