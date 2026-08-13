from pages.products import Products

def test_add_products_to_cart(page):
    products = Products(page)
    products.access_products()
    products.add_product_to_cart(indice_produto='0')
    products.button_continue_shopping.click()
    products.add_product_to_cart(indice_produto='1')
    products.button_continue_shopping.click()
    page.pause()