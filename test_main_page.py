from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest

#для запуска: pytest -v -s --tb=line --language=en test_main_page.py

link = "http://selenium1py.pythonanywhere.com"

@pytest.mark.login_guest
class TestLoginFromMainPage():
	@pytest.mark.xfail
	# не забываем передать первым аргументом self
	def test_guest_can_go_to_login_page(self, browser):
		page = MainPage(browser, link)			# инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
		page.open()								# открываем страницу
		page.go_to_login_page()					
		#login_page = page.go_to_login_page()	# выполняем метод страницы - переходим на страницу логина
		login_page = LoginPage(browser, browser.current_url)
		login_page.should_be_login_page()

	def test_guest_should_see_login_link(self, browser):
		page = MainPage(browser, link)
		page.open()
		page.should_be_login_link()
		
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
	page = BasketPage(browser, link)
	page.open()
	page.go_to_basket_from_header_of_the_site()
	page.is_basket_empty()
	page.is_basket_not_empty()
