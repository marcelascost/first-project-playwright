import pytest

@pytest.fixture(scope='function')
def contexto(browser):
    contexto = browser.new_context(base_url='https://automationexercise.com/',
                                   record_video_dir='videos')
    yield contexto
    contexto.close()

@pytest.fixture(scope='function')
def page(contexto):
    pagina = contexto.new_page()
    pagina.set_default_timeout(10000)
    pagina.set_default_navigation_timeout(30000)
    yield pagina
    pagina.close()

