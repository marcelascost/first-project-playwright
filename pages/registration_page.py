from pages.login_page import CadastroLogin

class RegistrationPage(CadastroLogin):
    def __init__(self, page):
        super().__init__(page)
        self.checkbox_mr = page.get_by_role("radio", name="Mr.")
        self.checkbox_mrs = page.get_by_role("radio", name="Mrs.")
        self.input_name_registration = page.get_by_role("textbook", name="Name", exact=True)
        self.input_password = page.get_by_role("textbook", name="Password")
        self.checkbox_sign_up_for_our_newsletter = page.get_by_text("Sign up for our newsletter!")
        self.checkbox_recieve_special_offers_from = page.get_by_text("Recieve special offers from")
        self.select_dia = page.locator('#days')
        self.select_mes = page.locator('#months')
        self.select_ano = page.locator('#years')

    def fill_registration_form(self, titulo="", nome="", senha="", data_aniversario=""):
        if titulo == 'Mr':
            self.checkbox_mr.check()
        if titulo == 'Mrs':
            self.checkbox_mr.check()
        if nome:
            self.input_name_registration.fill(nome)
        if senha:
            self.input_password.fill(senha)
        if data_aniversario:
            dia, mes, ano = data_aniversario.split("/")
            if mes.startswith("0"):
                mes = mes[1:]
            self.select_dia.select_option(dia)
            self.select_mes.select_option(mes)
            self.select_ano.select_option(ano)
