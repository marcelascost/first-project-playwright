from pages.products import Products
from pages.cart import Cart

def test_add_product_to_cart_if_less_than_500(page):
    products = Products(page)
    products.access_products()
    product_price: int = int(products.card_product.nth(1).locator('.productinfo h2').inner_text().replace('Rs. ',''))
    print(product_price)
    print(type(product_price))
    if product_price <= 500:
        products.add_product_to_cart(index=1)
        print('Produto com valor abaixo de 500 reais')
    else:
        print('Produto com valor acima de 500 reais')

def test_delete_all_products_in_cart(page):
    cart = Cart(page)
    cart.access_cart()
    while cart.button_delete_product.first.is_visible():
       cart.button_delete_product.first.click()
       page.wait_for_timeout(1000)
