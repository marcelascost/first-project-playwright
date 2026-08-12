from pages.login_page import CadastroLogin
from playwright.sync_api import expect

def test_login_invalid(page):
    login = CadastroLogin(page)
    login.acessar_cadastro_login()
    login.fazer_login(email='charlinho35@com', senha='blaublau')
    expect(page.get_by_text("Your email or password is")).to_be_visible()

def teste_login_valid(page):
    login = CadastroLogin(page)
    login.acessar_cadastro_login()
    login.fazer_login(email='teste@testeabcde.com', senha='123456789')
    expect(page.get_by_role('link', name='logout')).to_be_visible()
    expect(page.get_by_text("Logged in as teste")).to_be_visible()


def teste_logout(page):
    login = CadastroLogin(page)
    login.acessar_home()
    login.button_logout.click()
    expect(page.get_by_role('heading', name='Login to your account')).to_be_visible()

def teste_nao_logado(page):
    login = CadastroLogin(page)
    login.acessar_home()
    expect(page.get_by_role('link', name='logout')).not_to_be_visible()

