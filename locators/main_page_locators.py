from selenium.webdriver.common.by import By

# заголовок Вопросы о важном
head_list_home_subHeader = [By.XPATH, "//div[text()='Вопросы о важном']"]

# кнопка заказать
order_button = [By.XPATH, "//button[contains(@class,'Middle') and text()='Заказать']"]

# изображение самоката на главной странице
image_on_main_page = [By.XPATH, "//img[@src='/assets/ya.svg']"]
