import allure
import locators.header_locators as header

class HeaderPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("кликаем по кнопке Заказ в шапке")
    def click_order_button_header(self):
        self.driver.find_element(*header.button_order_header).click()

    @allure.step("кликаем по логотипу Самокат")
    def click_logo_samokat(self):
        self.driver.find_element(*header.scooter_logo).click()

    @allure.step("кликаем по логотипу Яндекс")
    def click_logo_yandex(self):
        self.driver.find_element(*header.yandex_logo).click()
