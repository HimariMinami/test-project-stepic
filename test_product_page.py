import pytest
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import time

#для запуска: pytest -v -s --tb=line --language=en test_product_page.py

#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])

linkNY = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
linkP = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"

# файл с тест кейсами
#def test_guest_can_add_product_to_basket(browser, link):
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
	page = ProductPage(browser, linkNY)	# инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
	page.open()							# открываем страницу
	page.should_be_cart_button()
	page.add_to_cart()
	page.solve_quiz_and_get_code()
	page.should_be_alert_name()
	page.ale_name_book_assert_name_book()
	page.should_be_alert_price()
	page.ale_price_book_assert_price_book()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	page = ProductPage(browser, linkNY)	# инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
	page.open()
	page.add_to_cart()
	page.solve_quiz_and_get_code()
	page.cant_see_success_message()

def test_guest_cant_see_success_message(browser):
	page = ProductPage(browser, linkNY)	# инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
	page.open()
	page.cant_see_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
	page = ProductPage(browser, linkNY)	# инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
	page.open()
	page.add_to_cart()
	page.solve_quiz_and_get_code()
	page.message_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):	
	page = ProductPage(browser, linkP)
	page.open()
	page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
	page = ProductPage(browser, linkP)
	page.open()
	page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
	page = BasketPage(browser, linkNY)	# инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
	page.open()
	page.go_to_basket_from_header_of_the_site()
	page.is_basket_empty()
	page.is_basket_not_empty()

class TestUserAddToBasketFromProductPage():
	@pytest.fixture(scope="function", autouse=True)
	def setup(self, browser):
		link = "http://selenium1py.pythonanywhere.com/accounts/login/"
		lpage = LoginPage(browser, link)
		lpage.open()
		email = str(time.time()) + "@fakemail.org"
		password = "Q12wSx4321"
		print("email = " + email)
		lpage.register_new_user(email, password)
		lpage.should_be_authorized_user() #проверка, что пользователь залогинен

	@pytest.mark.need_review
	def test_user_can_add_product_to_basket(self, browser):
		page = ProductPage(browser, linkNY)	# инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
		page.open()							# открываем страницу
		page.should_be_cart_button()
		page.add_to_cart()
		page.solve_quiz_and_get_code()
		page.should_be_alert_name()
		page.ale_name_book_assert_name_book()
		page.should_be_alert_price()
		page.ale_price_book_assert_price_book()

	def test_user_cant_see_success_message(self, browser):
		page = ProductPage(browser, linkNY)	# инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
		page.open()
		page.cant_see_success_message()
