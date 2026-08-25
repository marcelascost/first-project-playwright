from pages.base_page import BasePage
from playwright.sync_api import expect

def test_validate_home(page):
    """
    -Acessar a home
    -Validar se header é visivel
    """
    print(test_validate_home.__doc__)
    page = BasePage(page)
    page.access_home()
    expect(page.get_by_role("heading", name="AutomationExercise")).to_be_visible()

def test_validate_products(page):
    page = BasePage(page)
    page.access_products()
    expect(page.get_by_role("img", name="Website for practice")).to_be_visible()

def test_validate_cart(page):
    page = BasePage(page)
    page.access_cart()
    expect(page.get_by_text("Home Shopping Cart")).to_be_visible()

def test_validate_login(page):
    page = BasePage(page)
    page.access_cad_login()
    expect(page.get_by_role("heading", name="Login to your account")).to_be_visible()