import allure
import pytest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.main_page_locators import MainPageLocators
from locators.dzen_locators import DzenPageLocators
from pages.main_page import MainPage
from confitest import driver

class TestLogoRedirect:

    @allure.title('Проверка при нажатии на логотип «Самоката»,происходит переход на главную страницу «Самоката».')
    @allure.description('1.Нажать на кнопку "Заказать" '
                        '2.Нажать на кнопку "Самокат" в шапке страницы')
    def test_click_scooter_logo_main_page_is_displayed(self,driver):
        main_page = MainPage(driver)
        main_page.click_header_order_button()
        main_page.click_scooter_logo()

        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/' and driver.find_element(*MainPageLocators.main_title).is_displayed()


    @allure.title('Проверка при нажатии на логотип «Яндекс»,в новом окне через редирект откроется главная страница Дзена.')
    @allure.description('1.Нажать на логотип "Яндекс" '
                        '2.Проверить переход на новую вкладку'
                        '3. Проверить URL')
    def test_click_yandex_logo_dzen_page_is_displayed(self,driver):
        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        main_page.go_to_new_tab()
        WebDriverWait(driver, 30).until(expected_conditions.url_contains("https://dzen.ru/?yredirect=true"))
        WebDriverWait(driver, 30).until(expected_conditions.element_to_be_clickable(DzenPageLocators.main_button_dzen))

        assert "?yredirect=true" in driver.current_url and driver.find_element(*DzenPageLocators.main_button_dzen).text == 'Главная'
