import allure
import pytest

from pages.main_page import MainPage

class TestLogoRedirect:

    @allure.title('Проверка при нажатии на логотип «Самоката»,происходит переход на главную страницу «Самоката».')
    @allure.description('1.Нажать на кнопку "Заказать" '
                        '2.Нажать на кнопку "Самокат" в шапке страницы')
    def test_click_scooter_logo_main_page_is_displayed(self, driver):
        main_page = MainPage(driver)
        main_page.click_header_order_button()
        main_page.click_scooter_logo()

        assert main_page.get_current_url() == 'https://qa-scooter.praktikum-services.ru/' and main_page.check_main_title_is_displayed()


    @allure.title('Проверка при нажатии на логотип «Яндекс»,в новом окне через редирект откроется главная страница Дзена.')
    @allure.description('1.Нажать на логотип "Яндекс" '
                        '2.Проверить переход на новую вкладку'
                        '3. Проверить URL')
    def test_click_yandex_logo_dzen_page_is_displayed(self,driver):
        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        main_page.go_to_new_tab()
        main_page.wait_for_url("https://dzen.ru/?yredirect=true")

        assert "?yredirect=true" in main_page.get_current_url() and main_page.check_dzen_element_is_displayed() == 'Главная'
