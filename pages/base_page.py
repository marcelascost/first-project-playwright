class BasePage:
    def __init__(self, page):
        self.page = page
        self.botao_home = page.get_by_role('link', name='Home')
        self.button_products = page.get_by_role('link', name='Products')
        self.botao_carrinho = page.get_by_role('link', name='Cart')
        self.botao_cadastro = page.get_by_role('link', name='Signup / Login')
        self.button_logout = page.get_by_role("link", name="Logout")

    def acessar_home(self):
        self.page.goto('')

    def acessar_carrinho(self):
        self.page.click('view_cart')

    def access_products(self):
        self.page.click('products')

    def acessar_cadastro_login(self):
        self.page.goto('login')
