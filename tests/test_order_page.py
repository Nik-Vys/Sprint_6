import allure
import pytest

from test_data import Users
from locators.main_page_locators import MainPageLocators
from pages.order_page import OrderPage

class TestOrderPage:

    @allure.title('Проверка позитивного сценария на заказ самоката')
    @allure.description('1.Нажать на кнопку "Заказать" '
                        '2.Заполнить форму "Для кого самокат", "Про аренду" и подтвердить заказ'
                        '3. Проверить, что появилось всплывающее окно с сообщением об успешном создании заказа')
    @pytest.mark.parametrize('user, order_button',[(Users.user_1, MainPageLocators.order_button),(Users.user_2, MainPageLocators.header_order_button)])
    def test_order_scooter_order_completed(self,driver,user,order_button):
        order_page = OrderPage(driver)
        order_page.scroll_to_locator(order_button)
        order_page.click_button(order_button)
        order_page.order_scooter(user)

        assert "Заказ оформлен" in order_page.check_order_title_text().text


