import allure

from locators.dzen_locators import DzenPageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    @allure.step('Клик по логотипу Яндекс')
    def click_yandex_logo(self):
        self.click_button(MainPageLocators.yandex_logo)

    @allure.step('Клик по логотипу Самокат')
    def click_scooter_logo(self):
        self.click_button(MainPageLocators.scooter_logo)

    @allure.step('Проверить появление заголовка страницы')
    def check_main_title_is_displayed(self):
        self.wait_for_visible_locator(MainPageLocators.main_title)
        return self.check_element_is_displayed(MainPageLocators.main_title)

    @allure.step('Проверить появление элемента на странице Дзен')
    def check_dzen_element_is_displayed(self):
        self.wait_for_clickable_locator(DzenPageLocators.main_button_dzen)
        return self.get_text_locator(DzenPageLocators.main_button_dzen)

    @allure.step('Клик по кнопке Заказать в шапке страницы')
    def click_header_order_button(self):
        self.click_button(MainPageLocators.header_order_button)

    @allure.step('Скролл и клик по кнопке Заказать внизу')
    def scroll_and_click_order_button(self):
        self.scroll_to_locator(MainPageLocators.order_button)
        self.click_button(MainPageLocators.order_button)

    @allure.step('Скролл до "Вопросы о важном"')
    def scroll_to_questions_title(self):
        self.scroll_to_locator(MainPageLocators.questions_title)

    @allure.step('Клик по вопросу')
    def click_question(self, question_button):
        self.scroll_to_questions_title()
        self.click_button(question_button)

    @allure.step('Получение текста ответа на вопрос')
    def get_question_response(self, question,question_response):
        self.click_question(question)
        return self.get_text_locator(question_response)