import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class MainPage:
    # заголовок Вопросы о важном
    head_list_home_subHeader = [By.XPATH, "//div[text()='Вопросы о важном']"]

    # кнопка заказать
    order_button = [By.XPATH, "//button[contains(@class,'Middle') and text()='Заказать']"]

    # изображение самоката на главной странице
    image_on_main_page = [By.XPATH, "//img[@src='/assets/ya.svg']"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step("прокручиваем страницу до списка Аккордиона на главной")
    def scroll_to_list(self):
        element = self.driver.find_element(*self.head_list_home_subHeader)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("прокручиваем страницу до кнопки Заказа в теле страницы")
    def scroll_to_button_ortder(self):
        element = self.driver.find_element(*self.order_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("кликаем по названию в списке: {name_list}")
    def click_accordion_name_by_text(self, name_list):
        elem = self.driver.find_element(By.XPATH, f"//div[text()='{name_list}']")
        elem.click()

    @allure.step("проверяем доступность элемента: {text_accordion_panel}")
    def get_len_elem_by_text(self, text_accordion_panel):
        elems = self.driver.find_elements(By.XPATH, f"//div[not (@hidden)]/p[text()='{text_accordion_panel}']")
        return len(elems) == 1

    @allure.step("клик по кнопке заказать")
    def press_button_order(self):
        self.driver.find_element(*self.order_button).click()

    @allure.step("ожидаем картинку самоката на главной")
    def wait_print_on_main(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(self.image_on_main_page))

    @allure.step("проверка содержания {expect_url} в {current_url}")
    def check_current_url(self, current_url, expect_url):
        return expect_url in current_url
