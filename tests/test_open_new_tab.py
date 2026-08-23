from playwright.sync_api import expect

def test_new_tab(page):
    page.goto('https://www.demoqa.com/browser-windows')

    with page.expect_popup() as popup_info:
        page.get_by_text('New Tab').click()

    new_tab = popup_info.value
    new_tab.wait_for_load_state()
    print(f'Texto da pagina: {new_tab.locator('#sampleHeading').text_content()}')
    expect(new_tab.locator('#sampleHeading')).to_have_text('This is a sample page')

    new_tab.close()
    print(f'Voltamos para: {page.title()}')