from pages.base_page import BasePage

class CadastroLogin(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.input_email_login = page.locator('form').filter(has_text='Login').get_by_placeholder('Email Address')
        self.input_password_login = page.locator('form').filter(has_text='Login').get_by_placeholder('Password')
        self.cadastro_login = page.get_by_role('link', name='Signup / Login')
        self.botao_login = page.get_by_role('button', name='Login')
        self.input_name_registration = page.get_by_role("textbox", name="Name")
        self.input_email_registration = page.locator("form").filter(has_text="Signup").get_by_placeholder("Email Address")
        self.button_registration = page.get_by_role("button", name="Signup")

    def fazer_login(self, email='',senha='' ):
        self.input_email_login.fill(email)
        self.input_password_login.fill(senha)
        self.botao_login.click()

    def fazer_cadastro(self, nome='',email='' ):
        self.input_name_registration.fill(nome)
        self.input_email_registration.fill(email)
        self.button_registration.click()