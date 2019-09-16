from .base_page import BasePage
from .locators import AddToCartLocators
from selenium.webdriver.common.by import By
import time

# класс Page Object
class ProductPage(BasePage):
	def should_be_cart_button(self):
		assert self.is_element_present(*AddToCartLocators.BUTTON_CART), "Button 'add to cart' is not presented"

	def add_to_cart(self):
		button_add = self.browser.find_element(*AddToCartLocators.BUTTON_CART)
		button_add.click()

	def should_be_alert_name(self):
		assert self.is_element_present(*AddToCartLocators.ALERT_CART_NAME), "Alert with name of book is not presented"

	def ale_name_book_assert_name_book(self):
		alert_name_book = self.browser.find_element(*AddToCartLocators.ALERT_CART_NAME_BOOK)
		name_book = self.browser.find_element(*AddToCartLocators.NAME_BOOK)
		assert alert_name_book.text == name_book.text, "Alert with name of book != name of book"

	def should_be_alert_price(self):
		assert self.is_element_present(*AddToCartLocators.ALERT_CART_PRICE), "Alert with price of book is not presented"

	def ale_price_book_assert_price_book(self):
		alert_price_book = self.browser.find_element(*AddToCartLocators.ALERT_CART_PRICE_NUM)
		price_book = self.browser.find_element(*AddToCartLocators.PRICE_BOOK)
		assert alert_price_book.text == price_book.text, "Alert with price of book != price of book"

