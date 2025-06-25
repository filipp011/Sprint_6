import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Создаем экземпляр драйвера Chrome
    driver = webdriver.Firefox()
    yield driver
    # После теста закрываем браузер
    driver.quit()