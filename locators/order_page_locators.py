from selenium.webdriver.common.by import By

class OrderPageLocators:

    # Форма заказа самоката
    name_input = (By.XPATH, "//input[@placeholder = '* Имя']")
    last_name_input = (By.XPATH, "//input[@placeholder = '* Фамилия']")
    address_input = (By.XPATH, "//input[@placeholder = '* Адрес: куда привезти заказ']")
    metro_station_input = (By.XPATH, "//input[@placeholder = '* Станция метро']")
    metro_input = (By.XPATH, "//div[text() = 'Тверская']")
    telephone_input = (By.XPATH, "//input[@placeholder = '* Телефон: на него позвонит курьер']")
    next_button = (By.XPATH, "//button[text() = 'Далее']")

    # Об аренде
    deliver_order_input = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    rent_time_arrow = (By.XPATH, ".//span[@class='Dropdown-arrow']")
    rent_time_five_days = (By.XPATH, ".//div[text() = 'пятеро суток']")
    black_color_scooter = (By.ID, 'black')
    gray_color_scooter = (By.ID, 'grey')
    comment_input = (By.XPATH, ".//input[@placeholder= 'Комментарий для курьера']")
    back_button = (By.XPATH, ".//button[text() = 'Назад']")
    order_button = (By.XPATH, ".//button[contains(@class, 'Button_Middle') and text() = 'Заказать']")

    # Окно подтверждения заказа
    no_button = (By.XPATH, "//button[contains(@class, 'Button_Button') and text() = 'Нет']")
    yes_button = (By.XPATH, "//button[contains(@class, 'Button_Button') and contains(text(), 'Да')]")

    # Окно заказа
    order_placed_text = (By.XPATH, ".//div[contains(@class, 'Order_ModalHeader__3FDaJ') and contains(text(), 'Заказ оформлен')]")
    view_status_button = (By.XPATH, ".//button[text() = 'Посмотреть статус']")