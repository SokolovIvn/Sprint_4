from selenium.webdriver.common.by import By

# Заголовок первой страницы заказа
order_header = [By.XPATH, "//*[text()='Для кого самокат']"]

# Заголовок второй страницы "Про аренду"
order_header_second = [By.XPATH, "//*[text()='Про аренду']"]

# поле с вводом имени
first_name_field = [By.XPATH, "//input[@placeholder='* Имя']"]

# поле с вводом фамилии
second_name_field = [By.XPATH, "//input[@placeholder='* Фамилия']"]

# поле выбора метро
subway_field = [By.XPATH, "//div[@class='select-search__value']"]

# поле ввода станции метро
subway_input = [By.XPATH, "//input[@placeholder='* Станция метро']"]

# выпадающий список выбора метро
subway_list = [By.XPATH, "//div[@class='select-search__select']"]

# выпадающий список со станциями метро
subway_list_text = [By.XPATH, "//div[@class='select-search__select']//li"]

# поле ввода телефона
phone_number_field = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]

# поле ввода адреса
address_field = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]

# кнопка далее
next_button = [By.XPATH, "//button[text()='Далее']"]

# календарь
data = [By.XPATH, "//div[contains(@class'react-datepicker__day')]"]

# поле с календарем
field_date = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]

# поле выбора суток аренды
field_ours = [By.XPATH, "//div[text()='* Срок аренды']"]

# поле выбора черного цвета
checkbox_black_color = [By.ID, "black"]

# поле выбора черного цвета
field_comment_courier = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]

# кнопка заказать
order_button = [By.XPATH, "//button[contains(@class,'Middle') and text()='Заказать']"]

# кнопка подтверждения заказа "да"
yes_button = [By.XPATH, "//button[contains(@class,'Button_Middle') and text()='Да']"]

# заголовок подтверждения заказа
header_order_confirmed = [By.XPATH, "//div[text()='Заказ оформлен']"]
