def test_abrir_google(page):
    page.goto("https://www.google.com/")
    assert "Google" in page.title()
