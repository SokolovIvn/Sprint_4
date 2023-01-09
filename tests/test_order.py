import allure
from pages.HeaderPage import HeaderPage
from pages.OrderPage import OrderPage
from pages.MainPage import MainPage
import UserData


@allure.feature("Кнопка заказа на главной")
@allure.suite("проверка кнопки заказа")
@allure.title("тест на проверку кнопки заказа в шапке")
@allure.description("проверка перехода на страницу заказа при клике на кнопку в шапке")
def test_click_on_the_order_button_in_headeer_check_page_order_page(get_driver):
    driver = get_driver
    header = HeaderPage(driver)
    order_page = OrderPage(driver)

    header.click_order_button_header()
    order_page.wait_order_page()
    assert driver.current_url == "https://qa-scooter.praktikum-services.ru/order"


@allure.feature("Кнопка заказа на главной")
@allure.suite("проверка кнопки заказа")
@allure.title("тест на проверку кнопки заказа в теле страницы")
@allure.description("проверка перехода на страницу заказа при клике на кнопку в теле главной страницы")
def test_click_on_the_order_button_on_body_check_page_order_page(get_driver):
    driver = get_driver
    order_page = OrderPage(driver)
    main_page = MainPage(driver)

    main_page.scroll_to_button_ortder()
    main_page.press_button_order()
    order_page.wait_order_page()
    assert driver.current_url == "https://qa-scooter.praktikum-services.ru/order"


@allure.feature("Оформление заказа")
@allure.suite("полный заказ")
@allure.title("полный тест на проверку создания заказа")
@allure.description("проходит все этапы заполнения перед оформлением заказа")
def test_full_order_check_order_complite(get_driver):
    driver = get_driver
    order_page = OrderPage(driver)
    userdata = UserData
    driver.get("https://qa-scooter.praktikum-services.ru/order")
    user = userdata.get_user1_data()
    order_page.fill_order_full(user)
    assert order_page.check_confirm_order()
