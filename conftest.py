import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture(scope='module')
def driver() -> WebDriver:
    """Фикстура для инициализации WebDriver.

    Returns:
        WebDriver: Экземпляр WebDriver для управления браузером.
    """
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()