import pytest as pytest
from selenium import webdriver


@pytest.fixture()
def get_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()


@pytest.fixture()
def get_driver_without_main_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def get_driver_firefox():
    driver = webdriver.Firefox("/Users/iv/webdriver/bin")
    driver.maximize_window()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()
