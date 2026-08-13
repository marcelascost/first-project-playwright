from pages.base_page import BasePage

class Products(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.card_product =  page.locator('.single-products').nth(0)
        self.button_add_to_cart =  page.locator('.overlay-content > .btn').nth(0)
        self.button_continue_shopping = page.get_by_role("button", name="Continue Shopping")

    def add_product_to_cart(self, indice_produto='6'):
        self.card_product.nth(indice_produto).hover()
        self.button_add_to_cart.nth(indice_produto).click()
