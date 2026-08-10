from pages.login_page import CadastroLogin
from playwright.sync_api import expect

def test_registrar_novo_usuario(page):
    login_page = CadastroLogin(page)
    login_page.acessar_home()
    login_page.botao_cadastro.click()
    expect(page.get_by_text('New User Signup!', exact=True)).to_be_visible()
    page.pause()
    login_page.fazer_cadastro(nome='Fulano', email='teste123234243@teste.com')
    expect(page.get_by_text('Enter Account Information', exact=True)).to_be_visible()

