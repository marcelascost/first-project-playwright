from pages.products import Products
from pages.cart import Cart

def test_add_products_to_cart(page):
    products = Products(page)
    cart = Cart(page)
    products.access_products()
    products.add_product_to_cart(index='0')
    products.button_continue_shopping.click()
    products.add_product_to_cart(index='1')
    products.button_continue_shopping.click()
    products.button_cart.click()
    page.pause()
    cart.validate_cart(index=0,
                       header_description='Blue Top',
                       description_product='Women > Tops',
                       product_price='Rs. 500',
                       total_price='Rs. 500')
    cart.validate_cart(index=1,
                       header_description='Men Tshirt',
                       description_product='Men > Tshirts',
                       product_price='Rs. 400',
                       total_price='Rs. 400')
    page.pause()