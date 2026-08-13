from pages.base_page import BasePage
from playwright.sync_api import expect

class Cart(BasePage):
    def __init__(self,page):
        super().__init__(page)
        self.label_header_description = page.locator('.cart_description h4')
        self.label_description_product = page.locator('.cart_description p')
        self.label_product_price = page.locator('.cart_price')
        self.label_total_price = page.locator('.cart_total_price')

    def validate_cart(self, index, header_description, description_product, product_price, total_price):
        expect(self.label_header_description.nth(index)).to_have_text(header_description)
        expect(self.label_description_product.nth(index)).to_have_text(description_product)
        expect(self.label_product_price.nth(index)).to_have_text(product_price)
        expect(self.label_total_price.nth(index)).to_have_text(total_price)
