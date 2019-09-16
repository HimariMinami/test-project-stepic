from pages.product_page import ProductPage

# файл с тест кейсами
def test_guest_can_add_product_to_basket(browser):
	#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
	page = ProductPage(browser, link)	# инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
	page.open()							# открываем страницу
	page.should_be_cart_button()
	page.add_to_cart()
	page.solve_quiz_and_get_code()
	page.should_be_alert_name()
	page.ale_name_book_assert_name_book()
	page.should_be_alert_price()
	page.ale_price_book_assert_price_book()