
def test_new_tab(page):
    page.goto('https://www.demoqa.com/browser-windows')

    page.pause()
    page.locator('#tabButton').click()
    page.locator('#tabButton').click()
    page.locator('#tabButton').click()
    page.locator('#tabButton').click()
    page.wait_for_timeout(2000)
    context = page.context

    print(context.pages)

    new_window = context.page(0)

    new_window.screenshot('nova_janela2.png')
    new_window.close()