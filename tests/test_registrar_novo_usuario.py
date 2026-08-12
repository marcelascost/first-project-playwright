from pages.registration_page import RegistrationPage
from playwright.sync_api import expect

def test_registrar_novo_usuario(page):
    registration = RegistrationPage(page)
    registration.acessar_home()
    registration.botao_cadastro.click()
    expect(page.get_by_text('New User Signup!', exact=True)).to_be_visible()
    registration.fazer_cadastro(nome='Fulano', email='teste123234243@teste.com')
    expect(page.get_by_text('Enter Account Information', exact=True)).to_be_visible()
    registration.fill_registration_form(titulo='Mr', senha='123456', data_aniversario='27/07/1990',
                                   recieve_special_offers_from=True, sign_up_for_our_newsletter=True)
    registration.fill_address_form(first_name='Fulano', last_name= 'Couves', company='essyh', address='epa lele',
                                   country='United States', state= 'rj', city='rio',
                                   zipcode= '12345', mobile='12344536456')
    page.pause()

 #falta botao de criar /// parei em 34min