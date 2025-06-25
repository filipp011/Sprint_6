import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.question_locators import QuestionLocators

class Question():
    def __init__(self, driver, question_locator, answer_locator, expected_text):
        self.driver = driver
        self.locators = QuestionLocators
        self.question_locator = question_locator
        self.answer_locator = answer_locator
        self.expected_text = expected_text

    def scroll_to_element(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(self.question_locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    def wait_open_drop_down_and_text_visible(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.answer_locator))

    def get_description(self):
        return self.driver.find_element(*self.answer_locator).text