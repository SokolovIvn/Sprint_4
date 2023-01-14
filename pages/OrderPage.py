import datetime
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import locators.order_page_locators as order_page


class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("ожидание локатора: {elem}")
    def wait_element_visible(self, elem):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(elem))

    @allure.step("ввод имени: {name}")
    def fill_name_in_the_name_input_field(self, name):
        self.driver.find_element(*order_page.first_name_field).send_keys(name)

    @allure.step("ввод фамилии: {second_name}")
    def fill_second_name(self, second_name):
        self.driver.find_element(*order_page.second_name_field).send_keys(second_name)

    @allure.step("клик по полю с выпадающим списком станций метро")
    def click_subway_field(self):
        self.driver.find_element(*order_page.subway_field).click()

    # ввод номера телефона
    @allure.step("ввод номера телефона: {phone}")
    def fill_phone_number(self, phone):
        self.driver.find_element(*order_page.phone_number_field).send_keys(phone)

    @allure.step("ввод адреса: {address}")
    def fill_address(self, address):
        self.driver.find_element(*order_page.address_field).send_keys(address)

    @allure.step("ввод названия станции метро: {name_subway}")
    def fill_subway_name(self, name_subway):
        self.driver.find_element(*order_page.subway_input).send_keys(name_subway)

    # выбор станции метро
    @allure.step("клик по станции метро по названию: {name_subway}")
    def select_subway(self, name_subway):
        self.driver.find_element(By.XPATH,
                                 f"//li[@class='select-search__row']//div[contains(text(),'{name_subway}')]").click()

    @allure.step("клик на кнопку далее")
    def click_on_next_button(self):
        self.driver.find_element(*order_page.next_button).click()

    @allure.step("клик проверка перехода на вторую страницу заказа")
    def check_second_page_order(self):
        return len(self.driver.find_elements(*order_page.order_header_second)) == 1

    @allure.step("выбор даты")
    def select_current_day(self):
        self.driver.find_element(*order_page.field_date).click()
        WebDriverWait(self.driver, 2).until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='react-datepicker__tab-loop']")))
        self.driver.find_element(By.XPATH,
                                 f"//div[contains(@class, 'react-datepicker__day') and text()='{datetime.datetime.now().day}']").click()

    @allure.step("выбор время аренды")
    def select_rent_ours(self, ours):
        self.driver.find_element(*order_page.field_ours).click()
        self.driver.find_element(By.XPATH, f"//div[@class = 'Dropdown-option' and text()='{ours}']").click()

    # выбор черного цвета
    @allure.step("выбор цвета")
    def select_black_color(self):
        self.driver.find_element(*order_page.checkbox_black_color).click()

    @allure.step("ввод комментария для курьера")
    def fill_comment_for_courier(self, comment):
        self.driver.find_element(*order_page.field_comment_courier).send_keys(comment)

    # подтверждаем заказ
    @allure.step("заполнение комментария для курьера")
    def press_button_order(self):
        self.driver.find_element(*order_page.order_button).click()

    @allure.step("клик по кнопке Да")
    def press_button_yes(self):
        self.driver.find_element(*order_page.yes_button).click()

    # метод для заполнения полей для заказа
    def fill_order_full(self, user_data):
        self.wait_element_visible(order_page.first_name_field)
        self.fill_name_in_the_name_input_field(user_data["Name"])
        self.fill_second_name(user_data["LastName"])
        self.fill_address(user_data["Address"])
        self.fill_phone_number(user_data["Phone"])
        self.fill_subway_name(user_data["Metro"])
        self.select_subway(user_data["Metro"])
        self.click_on_next_button()
        self.select_current_day()
        self.select_rent_ours(user_data["day"])
        self.select_black_color()
        self.fill_comment_for_courier(user_data["comment"])
        self.press_button_order()
        self.press_button_yes()

    @allure.step("проверка завершения заказа")
    def check_confirm_order(self):
        return len(self.driver.find_elements(*order_page.header_order_confirmed)) == 1

    @allure.step("Проверка загрузки страницы с итогом заказа")
    def wait_order_page(self):
        WebDriverWait(self.driver, 2).until(
            expected_conditions.visibility_of_element_located(order_page.order_header))
