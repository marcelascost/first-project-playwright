class BasePage:
    def __init__(self, page):
        self.page = page
        self.botao_home = page.get_by_role('link', name='Home')
        self.botao_produtos = page.get_by_role('link', name='Products')
        self.botao_carrinho = page.get_by_role('link', name='Cart')
        self.botao_cadastro = page.get_by_role('link', name='Signup / Login')

    def acessar_home(self):
        self.botao_home.click()

    def acessar_carrinho(self):
        self.botao_carrinho.click()
