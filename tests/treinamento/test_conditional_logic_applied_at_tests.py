from pages.products import Products

def test_add_product_to_cart_if_less_than_500(page):
    products = Products(page)
    products.access_products()
    product_price: int = int(products.card_product.nth(2).locator('.productinfo h2').inner_text().replace('Rs. ',''))
    print(product_price)
    print(type(product_price))
    if product_price <= 500:
        products.add_product_to_cart(index=1)
        print('Produto com valor abaixo de 500 reais')
    else:
        print('Produto com valor acima de 500 reais')
    page.pause()

