from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By
import operator

# класс Page Object
class BasketPage(BasePage):
	def is_basket_empty(self):
		basket_content_text = self.browser.find_element(*BasketPageLocators.BASKET_CONT_TEXT)
		assert operator.contains(basket_content_text.text, "Your basket is empty."), "Your basket is not empty!"

	def is_basket_not_empty(self):
		assert self.is_not_element_present(*BasketPageLocators.BASKET_NOT_EMPTY), \
			"Basket not empty, but should not be"
		