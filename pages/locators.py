from selenium.webdriver.common.by import By

# локаторы к элементам страницы
class AddToCartLocators():
	BUTTON_CART = (By.CSS_SELECTOR, ".btn-add-to-basket") #кнопка добавить в корзину
	
	ALERT_CART_NAME = (By.XPATH, "//div[1]/div[@class='alertinner ']") #уведомление о добавлении книги с её названием
	ALERT_CART_NAME_BOOK = (By.XPATH, "//div[1]/div[1][@class='alertinner ']/strong") #уведомление с именем книги о добавлении в корзину
	NAME_BOOK = (By.XPATH, "//div[contains(@class, 'product_main')]/h1") # название книги
	
	ALERT_CART_PRICE = (By.XPATH, "//div[3]/div[@class='alertinner ']") #уведомление о добавлении книги с её ценой
	ALERT_CART_PRICE_NUM = (By.XPATH, "//div[@class='alertinner ']/p/strong") #цена книги в уведомлении
	PRICE_BOOK = (By.XPATH, "//div[contains(@class, 'product_main')]/p[contains(@class, 'price_color')]") #цена книги

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    