import allure
import pytest

from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage
from test_data import Questions

class TestMainPage:

    @allure.title('Проверка при нажатии на стрелочку вопроса , открывается соответствующий текст.')
    @allure.description('1.Скроллить до блока с вопросами'
                    '2.Кликнуть на вопрос '
                    '3.Получить текст ответа на вопрос'
                    '4.Сравнить полученный текст с ожидаемым')
    @pytest.mark.parametrize('question,question_response,expected_question_response',list(zip(MainPageLocators.questions,MainPageLocators.questions_response, Questions.responses)))
    def test_question_responses_response_appeared(self,driver,question,question_response,expected_question_response):
        main_page = MainPage(driver)
        response_text = main_page.get_question_response(question,question_response)

        assert response_text == expected_question_response