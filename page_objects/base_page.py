import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, locators):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.locators = locators

    @allure.step("Открываем страницу")
    def open(self, url):
        self.driver.get(url)

    @allure.step("Ожидаем открытие страницы")
    def is_opened(self, url):
        self.wait.until(EC.url_contains(url))

    @allure.step("Кликаем по элементу")
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Вводим текст в поле")
    def enter_text(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    @allure.step("Ожидаем, что элемент видим")
    def wait_visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Получаем текст элемента")
    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step("Скроллим до элемента")
    def scroll_to_element(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step("Принимаем куки")
    def accept_cookies(self):
        self.wait.until(EC.element_to_be_clickable(self.locators.COOKIE)).click()

    @allure.step('Прокрутить до элемента и кликнуть')
    def scroll_and_click(self, locator):
        self.scroll_to_element(locator)
        self.click(locator)

    @allure.step("Получаем текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Переключаемся на новое окно")
    def switch_to_window(self, window_index):
        new_window = self.driver.window_handles[window_index]
        self.driver.switch_to.window(new_window)
