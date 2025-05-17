import allure
import pytest

from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from confitest import driver

class TestMainPage:

    @allure.title('Проверка при нажатии на стрелочку вопроса 1, открывается соответствующий текст.')
    @allure.description('1.Скроллить до блока с вопросами'
                    '2.Кликнуть на вопрос 1'
                    '3.Получить текст ответа на вопрос'
                    '4.Сравнить полученный текст с ожидаемым')
    def test_first_question_responses_response_appeared(self,driver):
        main_page = MainPage(driver)
        response_text = main_page.get_question_response(MainPageLocators.questions[0], MainPageLocators.questions_response[0])

        assert response_text == driver.find_element(*MainPageLocators.questions_response[0]).text

    @allure.title('Проверка при нажатии на стрелочку вопроса 2, открывается соответствующий текст.')
    @allure.description('1.Скроллить до блока с вопросами'
                    '2.Кликнуть на вопрос 2'
                    '3.Получить текст ответа на вопрос'
                    '4.Сравнить полученный текст с ожидаемым')
    def test_second_question_responses_response_appeared(self,driver):
        main_page = MainPage(driver)
        response_text = main_page.get_question_response(MainPageLocators.questions[1], MainPageLocators.questions_response[1])

        assert response_text == driver.find_element(*MainPageLocators.questions_response[1]).text

    @allure.title('Проверка при нажатии на стрелочку вопроса 3, открывается соответствующий текст.')
    @allure.description('1.Скроллить до блока с вопросами'
                    '2.Кликнуть на вопрос 3'
                    '3.Получить текст ответа на вопрос'
                    '4.Сравнить полученный текст с ожидаемым')
    def test_third_question_responses_response_appeared(self,driver):
        main_page = MainPage(driver)
        response_text = main_page.get_question_response(MainPageLocators.questions[2], MainPageLocators.questions_response[2])

        assert response_text == driver.find_element(*MainPageLocators.questions_response[2]).text

    @allure.title('Проверка при нажатии на стрелочку вопроса 4, открывается соответствующий текст.')
    @allure.description('1.Скроллить до блока с вопросами'
                    '2.Кликнуть на вопрос 4'
                    '3.Получить текст ответа на вопрос'
                    '4.Сравнить полученный текст с ожидаемым')
    def test_fourth_question_responses_response_appeared(self,driver):
        main_page = MainPage(driver)
        response_text = main_page.get_question_response(MainPageLocators.questions[3], MainPageLocators.questions_response[3])

        assert response_text == driver.find_element(*MainPageLocators.questions_response[3]).text

    @allure.title('Проверка при нажатии на стрелочку вопроса 5, открывается соответствующий текст.')
    @allure.description('1.Скроллить до блока с вопросами'
                    '2.Кликнуть на вопрос 5'
                    '3.Получить текст ответа на вопрос'
                    '4.Сравнить полученный текст с ожидаемым')
    def test_fifth_question_responses_response_appeared(self,driver):
        main_page = MainPage(driver)
        response_text = main_page.get_question_response(MainPageLocators.questions[4], MainPageLocators.questions_response[4])

        assert response_text == driver.find_element(*MainPageLocators.questions_response[4]).text

    @allure.title('Проверка при нажатии на стрелочку вопроса 6, открывается соответствующий текст.')
    @allure.description('1.Скроллить до блока с вопросами'
                    '2.Кликнуть на вопрос 6'
                    '3.Получить текст ответа на вопрос'
                    '4.Сравнить полученный текст с ожидаемым')
    def test_sixth_question_responses_response_appeared(self,driver):
        main_page = MainPage(driver)
        response_text = main_page.get_question_response(MainPageLocators.questions[5], MainPageLocators.questions_response[5])

        assert response_text == driver.find_element(*MainPageLocators.questions_response[5]).text

    @allure.title('Проверка при нажатии на стрелочку вопроса 7, открывается соответствующий текст.')
    @allure.description('1.Скроллить до блока с вопросами'
                    '2.Кликнуть на вопрос 7'
                    '3.Получить текст ответа на вопрос'
                    '4.Сравнить полученный текст с ожидаемым')
    def test_seventh_question_responses_response_appeared(self,driver):
        main_page = MainPage(driver)
        response_text = main_page.get_question_response(MainPageLocators.questions[6], MainPageLocators.questions_response[6])

        assert response_text == driver.find_element(*MainPageLocators.questions_response[6]).text

    @allure.title('Проверка при нажатии на стрелочку вопроса 8, открывается соответствующий текст.')
    @allure.description('1.Скроллить до блока с вопросами'
                    '2.Кликнуть на вопрос 8'
                    '3.Получить текст ответа на вопрос'
                    '4.Сравнить полученный текст с ожидаемым')
    def test_eighth_question_responses_response_appeared(self,driver):
        main_page = MainPage(driver)
        response_text = main_page.get_question_response(MainPageLocators.questions[7], MainPageLocators.questions_response[7])

        assert response_text == driver.find_element(*MainPageLocators.questions_response[7]).text




