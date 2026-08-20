from pages.products import Products

def test_add_product_to_cart_if_less_than_500(page):
    products = Products(page)
    products.access_products()
    product_price = int(products.card_product.nth(1).locator('productinfo h2').inner_text().replace('Rs. ',''))
    print(product_price)
    print(type(product_price))
    page.pause()

#REVER AULA