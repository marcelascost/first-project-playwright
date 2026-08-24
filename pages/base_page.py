class BasePage:
    def __init__(self, page):
        self.page = page
        self.botao_home = page.get_by_role('link', name='Home')
        self.button_products = page.get_by_role('link', name='Products')
        self.button_cart = page.get_by_role('link', name='Cart')
        self.botao_cadastro = page.get_by_role('link', name='Signup / Login')
        self.button_logout = page.get_by_role("link", name="Logout")

    def access_home(self):
        self.page.goto('')

    def access_cart(self):
        self.page.goto('view_cart')

    def access_products(self):
        self.page.goto('products')

    def access_cad_login(self):
        self.page.goto('login')
