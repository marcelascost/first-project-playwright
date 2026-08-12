from pages.login_page import CadastroLogin

class RegistrationPage(CadastroLogin):
    def __init__(self, page):
        super().__init__(page)
        self.checkbox_mr = page.get_by_role("radio", name="Mr.")
        self.checkbox_mrs = page.get_by_role("radio", name="Mrs.")
        self.input_name_registration = page.get_by_role("textbox", name="Name", exact=True)
        self.input_password = page.get_by_role("textbox", name="Password")
        self.checkbox_sign_up_for_our_newsletter = page.get_by_text("Sign up for our newsletter!")
        self.checkbox_recieve_special_offers_from = page.get_by_text("Receive special offers from")
        self.select_dia = page.locator('#days')
        self.select_mes = page.locator('#months')
        self.select_ano = page.locator('#years')
        self.input_first_name = page.get_by_role("textbox", name="First name *")
        self.input_last_name = page.get_by_role("textbox", name="Last name *")
        self.input_company = page.get_by_role("textbox", name="Company", exact=True)
        self.input_address = page.get_by_role("textbox", name="Address * (Street address, P.")
        self.input_address_2 = page.get_by_role("textbox", name="Address 2")
        self.input_state = page.get_by_role("textbox", name="State *")
        self.input_city = page.get_by_role("textbox", name="City * Zipcode *")
        self.input_zipcode = page.locator("#zipcode")
        self.input_mobile = page.get_by_role("textbox", name="Mobile Number *")
        self.select_country = page.get_by_label('Country *')

    def fill_registration_form(self, titulo="", nome="", senha="", data_aniversario="",
                               sign_up_for_our_newsletter= True, recieve_special_offers_from= True):
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
            if dia.startswith("0"):
                dia = dia[1:]
            if mes.startswith("0"):
                mes = mes[1:]
            self.select_dia.select_option(dia)
            self.select_mes.select_option(mes)
            self.select_ano.select_option(ano)
        if sign_up_for_our_newsletter:
            self.checkbox_sign_up_for_our_newsletter.check()
        else:
            self.checkbox_sign_up_for_our_newsletter.uncheck()
        if recieve_special_offers_from:
            self.checkbox_recieve_special_offers_from.check()
        else:
            self.checkbox_recieve_special_offers_from.uncheck()

    def fill_address_form(self, first_name='', last_name='', company='', address='', address_2='', country='', state='', city='', zipcode='', mobile=''):
        if first_name:
            self.input_first_name.fill(first_name)
        if last_name:
            self.input_last_name.fill(last_name)
        if company:
            self.input_company.fill(company)
        if address:
            self.input_address.fill(address)
        if country:
            self.select_country.select_option(country)
        if state:
            self.input_state.fill(state)
        if city:
            self.input_city.fill(city)
        if zipcode:
            self.input_zipcode.fill(zipcode)
        if mobile:
            self.input_mobile.fill(mobile)