def test_get_by_role(page):
    '''page.goto('https://automationexercise.com/')
    page.pause()
    page.get_by_role('link', name='Signup / Login').click()
    page.get_by_role('button', name='Login').click()'''
    page.goto('https://bootswatch.com/default')
    page.locator('#navbarColor01').get_by_role('button', name='Dropdown').click()