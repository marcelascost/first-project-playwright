from pages.registration_page import RegistrationPage
from playwright.sync_api import expect

def test_create_new_account(page):
    registration = RegistrationPage(page)
    registration.acessar_home()
    registration.botao_cadastro.click()
    expect(page.get_by_text('New User Signup!', exact=True)).to_be_visible()
    registration.fazer_cadastro(nome='charlinhos', email='charlinhos35@teste.com')
    expect(page.get_by_text('Enter Account Information', exact=True)).to_be_visible()
    registration.fill_registration_form(titulo='Mr', senha='123456', data_aniversario='27/07/1990',
                                   recieve_special_offers_from=True, sign_up_for_our_newsletter=True)
    registration.fill_address_form(first_name='Fulano', last_name= 'Couves', company='essyh', address='epa lele',
                                   country='United States', state= 'rj', city='rio',
                                   zipcode= '12345', mobile='12344536456')
    registration.button_new_registration.click()
    expect(page.get_by_text('Account Created')).to_be_visible()
    registration.button_continue.click()
    expect(page.get_by_text('Logged in as charlinhos')).to_be_visible()

def test_remove_account(page):
    registration = RegistrationPage(page)
    registration.acessar_home()
    registration.button_remove_account.click()
    expect(page.get_by_text('Account Deleted')).to_be_visible()
    page.get_by_role("link", name="Continue").click()
    page.pause()

