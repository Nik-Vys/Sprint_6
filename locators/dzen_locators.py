from selenium.webdriver.common.by import By

class DzenPageLocators:
    main_button_dzen = (By.XPATH, "//span[contains(@class, 'dzen-layout--navigation-tab__text-2g') and contains(text(), 'Главная')]")
