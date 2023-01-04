import allure
from selenium.webdriver.common.by import By


class HeaderPage:
    # лого скутера. ведет на главную страницу скутеры
    scooter_logo = [By.XPATH, "//*[@alt='Scooter']"]

    # лого яндекса. ведет на главную страницу скутеры
    yandex_logo = [By.XPATH, "//*[@alt='Yandex']"]

    # Кнопка заказа в header страницы
    button_order_header = [By.XPATH, "//div[contains(@class,'Header')]/button[text()='Заказать']"]

    # кнопка "статус заказа"
    button_order_status = [By.XPATH, "//div[contains(@class,'Header')]/button[text()='Статус заказа']"]

    # форма ввода номера заказа
    field_order_number = [By.XPATH, "//input[@type='text' and @placeholder='Введите номер заказа']"]

    # кнопка GO!, что бы проверить статус заказа
    button_order_check = [By.XPATH, "//button[text()='Go!']"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step("кликаем по кнопке Заказ в шапке")
    def click_order_button_header(self):
        self.driver.find_element(*self.button_order_header).click()

    @allure.step("кликаем по логотипу Самокат")
    def click_logo_samokat(self):
        self.driver.find_element(*self.scooter_logo).click()

    @allure.step("кликаем по логотипу Яндекс")
    def click_logo_yandex(self):
        self.driver.find_element(*self.yandex_logo).click()
