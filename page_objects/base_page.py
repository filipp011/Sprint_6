from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.order_locators import OrderLocators
from locators.question_locators import QuestionLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        
    # Скролл до элемента
    def scroll_to_element(self, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)
        self.driver.find_element(*OrderLocators.COOKIE).click()