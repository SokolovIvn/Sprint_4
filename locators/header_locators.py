from selenium.webdriver.common.by import By

# лого скутера. ведет на главную страницу скутерыz
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
