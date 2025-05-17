import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Заполнение поля "Имя"')
    def fill_name_input(self, text):
        self.wait_for_visible_locator(OrderPageLocators.name_input).send_keys(text)

    @allure.step('Заполнение поля "Фамилия"')
    def fill_last_name_input(self, text):
        self.wait_for_visible_locator(OrderPageLocators.last_name_input).send_keys(text)

    @allure.step('Заполнение поля "Адрес"')
    def fill_address_input(self, text):
        self.wait_for_visible_locator(OrderPageLocators.address_input).send_keys(text)

    @allure.step('Заполнение поля "Станция метро"')
    def fill_metro_station_input(self, text):
        self.click_button(OrderPageLocators.metro_station_input)
        self.wait_for_visible_locator(OrderPageLocators.metro_station_input).send_keys(text)
        self.click_button(OrderPageLocators.metro_input)

    @allure.step('Заполнение поля "Телефон"')
    def fill_telephone_input(self, text):
        self.wait_for_visible_locator(OrderPageLocators.telephone_input).send_keys(text)

    @allure.step('Клик на кнопку "Далее"')
    def click_on_next_button(self):
        self.click_button(OrderPageLocators.next_button)

    @allure.step('Заполнение поля "Когда привезти заказ"')
    def fill_deliver_order_input(self, text):
        self.click_button(OrderPageLocators.deliver_order_input)
        self.wait_for_visible_locator(OrderPageLocators.deliver_order_input).send_keys(text)

    @allure.step('Заполнение поля "Срок аренды"')
    def fill_rent_time(self):
        self.click_button(OrderPageLocators.rent_time_arrow)
        self.click_button(OrderPageLocators.rent_time_five_days)

    @allure.step('Заполнение поля "Цвет самоката"')
    def fill_colour_scooter(self):
        self.click_button(OrderPageLocators.gray_color_scooter)

    @allure.step('Заполнение поля "Комментарий для курьера"')
    def fill_comment(self,text):
        self.wait_for_visible_locator(OrderPageLocators.comment_input).send_keys(text)

    @allure.step('Клик на кнопку "Заказать"')
    def click_on_order_button(self):
        self.click_button(OrderPageLocators.order_button)

    @allure.step('Заполнение формы "Для кого самокат"')
    def fill_form_who_is_scooter_for(self, user):
        self.fill_name_input(user['Имя'])
        self.fill_last_name_input(user['Фамилия'])
        self.fill_address_input(user['Адрес'])
        self.fill_metro_station_input(user['Станция метро'])
        self.fill_telephone_input(user['Телефон'])
        self.click_on_next_button()

    @allure.step('Заполнение формы "Про аренду"')
    def fill_form_about_rent(self, user):
        self.fill_deliver_order_input(user['Дата доставки'])
        self.fill_rent_time()
        self.fill_colour_scooter()
        self.fill_comment(user['Комментарий'])
        self.click_on_order_button()

    @allure.step('Клик на кнопку "Да" для подтверждения заказа')
    def click_on_yes_button(self):
            self.click_button(OrderPageLocators.yes_button)


    @allure.step('Оформление и подтверждение заказа')
    def order_scooter(self, user):
        self.fill_form_who_is_scooter_for(user)
        self.fill_form_about_rent(user)
        self.click_on_yes_button()


    @allure.step('Проверка отображения окна с текстом подтверждения заказа')
    def check_order_title_text(self):
        return WebDriverWait(self.driver, 30).until(expected_conditions.presence_of_element_located(OrderPageLocators.order_placed_text))
