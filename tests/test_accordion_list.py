import allure
import pytest
from selenium import webdriver
from pages.MainPage import MainPage


@allure.feature("Вопросы о важном")
class TestAccordion:
    driver = None

    @classmethod
    @allure.title("открытие браузера")
    def setup_class(cls):
        cls.driver = webdriver.Firefox("/Users/iv/webdriver/bin")
        cls.driver.get("https://qa-scooter.praktikum-services.ru/")
        cls.driver.maximize_window()
        MainPage(cls.driver).scroll_to_list()

    pytestmark = pytest.mark.parametrize("name_accordion_button,text_accordion_panel",
                                         [("Сколько это стоит? И как оплатить?",
                                           "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
                                          ("Хочу сразу несколько самокатов! Так можно?",
                                           "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
                                          ("Как рассчитывается время аренды?",
                                           "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
                                          ("Можно ли заказать самокат прямо на сегодня?",
                                           "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
                                          ("Можно ли продлить заказ или вернуть самокат раньше?",
                                           "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
                                          ("Вы привозите зарядку вместе с самокатом?",
                                           "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
                                          ("Можно ли отменить заказ?",
                                           "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
                                          ("Я жизу за МКАДом, привезёте?",
                                           "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
                                          ])

    @allure.feature("Вопросы о важном")
    @allure.suite("Проверка списка Вопросы о важном")
    @allure.title("Проверка списка: {name_accordion_button}")
    def test_accordion_list_check_all(self, name_accordion_button, text_accordion_panel):
        mainpage = MainPage(self.driver)
        mainpage.click_accordion_name_by_text(name_accordion_button)
        assert mainpage.get_len_elem_by_text(text_accordion_panel)

    @classmethod
    @allure.title("закрытие браузера")
    def teardown_class(cls):
        cls.driver.quit()
