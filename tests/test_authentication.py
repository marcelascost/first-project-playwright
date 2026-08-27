from playwright.sync_api import expect
from pages.login_page import CadastroLogin
from pages.products import Products
from pages.cart import Cart

def teste_login(page):
    login = CadastroLogin(page)
    login.access_cad_login()
    login.fazer_login(email='teste@testeabcde.com', senha='123456789')
    expect(page.get_by_role("link", name="Logout")).to_be_visible()

def test_adicionar_produtos_ao_carrinho(page):
    products = Products(page)
    products.access_products()
    products.add_product_to_cart(index='0')