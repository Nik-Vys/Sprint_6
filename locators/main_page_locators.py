from selenium.webdriver.common.by import By

class MainPageLocators:

    yandex_logo = (By.XPATH, ".//a[@class = 'Header_LogoYandex__3TSOI']")       # Логотип Яндекс
    scooter_logo = (By.XPATH, ".//a[@class = 'Header_LogoScooter__3lsAR']")     # Логотип Самокат
    header_order_button =(By.CLASS_NAME,"Button_Button__ra12g") # Кнопка "Заказать" в шапке страницы
    order_button = (By.XPATH, "(//button[text()='Заказать'])[2]") # Кнопка "Заказать" внизу страницы
    questions_title = (By.XPATH, "//div[text() = 'Вопросы о важном']")      # Текст "Вопросы о важном"
    main_title = (By.CLASS_NAME, "Home_Header__iJKdX")      # Заголовок на главной странице

    # Локаторы кнопок вопросов
    questions = [
        (By.XPATH, "(//*[contains(@id, 'accordion__heading')])[1]"),
        (By.XPATH, "(//*[contains(@id, 'accordion__heading')])[2]"),
        (By.XPATH, "(//*[contains(@id, 'accordion__heading')])[3]"),
        (By.XPATH, "(//*[contains(@id, 'accordion__heading')])[4]"),
        (By.XPATH, "(//*[contains(@id, 'accordion__heading')])[5]"),
        (By.XPATH, "(//*[contains(@id, 'accordion__heading')])[6]"),
        (By.XPATH, "(//*[contains(@id, 'accordion__heading')])[7]"),
        (By.XPATH, "(//*[contains(@id, 'accordion__heading')])[8]")
    ]

    # Локаторы текста ответов
    questions_response = [
        (By.XPATH, "(//*[contains(@id, 'accordion__panel')])[1]"),
        (By.XPATH, "(//*[contains(@id, 'accordion__panel')])[2]"),
        (By.XPATH, "(//*[contains(@id, 'accordion__panel')])[3]"),
        (By.XPATH, "(//*[contains(@id, 'accordion__panel')])[4]"),
        (By.XPATH, "(//*[contains(@id, 'accordion__panel')])[5]"),
        (By.XPATH, "(//*[contains(@id, 'accordion__panel')])[6]"),
        (By.XPATH, "(//*[contains(@id, 'accordion__panel')])[7]"),
        (By.XPATH, "(//*[contains(@id, 'accordion__panel')])[8]")
    ]
