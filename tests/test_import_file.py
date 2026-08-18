from playwright.sync_api import expect

def test_import_single_file(page):
    page.goto('https://www.transfernow.net/pt')
    page.pause()
    page.get_by_role("button", name='Aceitar e Continuar').click()
    with page.expect_file_chooser() as fc_info:
        page.get_by_role('button', name='Começar').click()
    file_chooser = fc_info.value
    file_chooser.set_files('stores/test123.txt')
    page.get_by_role('button', name='Criar um link').click()
    page.get_by_role('textbox', name='Seu e-mail').fill('teste@teste12323434.com')
    page.get_by_role('button', name='Obter um link').click()
    expect(page.get_by_text('Seu link está pronto!')).to_be_visible(timeout=30000)

def test_import_multiple_files(page):
    page.goto('https://www.transfernow.net/pt')
    page.get_by_role("button", name='Aceitar e Continuar').click()
    with page.expect_file_chooser() as fc_info:
         page.get_by_role('button', name='Começar').click()
    file_chooser = fc_info.value
    file_chooser.set_files(['stores/test123.txt',
                                'stores/test1234.txt',
                                'stores/test12345.txt',])
    page.get_by_role('button', name='Criar um link').click()
    page.get_by_role('textbox', name='Seu e-mail').fill('teste@teste12323434.com')
    page.get_by_role('button', name='Obter um link').click()
    expect(page.get_by_text('Seu link está pronto!')).to_be_visible(timeout=30000)
