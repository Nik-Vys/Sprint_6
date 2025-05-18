from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class BasePage:

    def __init__(self,driver):
        self.driver = driver


    # Получение URL
    def get_current_url(self):
        return self.driver.current_url

    # Ожидание отображения
    def wait_for_visible_locator(self, locator):
        return WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))

    # Ожидание кликабельности элемента
    def wait_for_clickable_locator(self, locator):
        return WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(locator))

    # Ожидание получение url
    def wait_for_url(self,url):
        return WebDriverWait(self.driver, 30).until(expected_conditions.url_contains(url))

    # Клик на элемент
    def click_button(self,locator):
        self.wait_for_clickable_locator(locator).click()

    # Перейти к элeменту
    def scroll_to_locator(self,locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.wait_for_visible_locator(locator))

    # Получить текст элемента
    def get_text_locator(self, locator):
        return self.wait_for_visible_locator(locator).text

    # Переход на новую вкладку браузера
    def go_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    # Проверить появление элемента
    def check_element_is_displayed(self, locator):
        return self.driver.find_element(*locator).is_displayed()



