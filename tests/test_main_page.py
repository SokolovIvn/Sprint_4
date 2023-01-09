from time import sleep
import allure
from pages.HeaderPage import HeaderPage
from pages.MainPage import MainPage


@allure.feature("Шапка")
@allure.suite("Проверка логотипа Самокат")
@allure.title("Проверка перехода на главную страницу")
def test_click_logo_scooter_check_main_page(get_driver_without_main_page):
    driver = get_driver_without_main_page
    header = HeaderPage(driver)
    main_page = MainPage(driver)
    driver.get("https://qa-scooter.praktikum-services.ru/order")

    header.click_logo_samokat()
    main_page.wait_print_on_main()
    assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"


@allure.feature("Шапка")
@allure.suite("Проверка логотипа Яндекс")
@allure.title("проверка перехода на dzen")
def test_click_logo_yandex_check_main_page(get_driver):
    driver = get_driver
    header = HeaderPage(driver)
    main_page = MainPage(driver)

    header.click_logo_yandex()
    sleep(5)
    driver.switch_to.window(driver.window_handles[-1])

    assert main_page.check_current_url(driver.current_url, "https://dzen.ru")
