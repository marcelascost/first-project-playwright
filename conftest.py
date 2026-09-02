import pytest
import pytest
import pytest_html
from slugify import slugify # pip install python-slugify
import os

@pytest.fixture(scope='session')
def contexto(browser):
    contexto = browser.new_context(base_url='https://automationexercise.com/')
                                   #record_video_dir='videos'
    yield contexto
    contexto.close()

@pytest.fixture(scope='session')
def set_up_page(contexto):
    pagina = contexto.new_page()
    pagina.set_default_timeout(10000)
    pagina.set_default_navigation_timeout(30000)
    yield pagina
    pagina.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    This hook runs after each test phase.
    It checks for failures and attaches screenshots to the HTML report.
    """
    outcome = yield
    report = outcome.get_result()

    # List of extras for the HTML report
    extras = getattr(report, 'extra', [])

    # Only capture during the 'call' phase (actual test execution)
    if report.when == 'call':
        xfail = hasattr(report, 'wasxfail')
        try:
            # Capture if failed (but not an expected XFAIL)
            if (report.skipped and xfail) or (report.failed and not xfail):
                # Ensure a safe file name
                screen_file = f"imagens/{slugify(item.nodeid)}.png"

                # page should be available via Playwright fixture
                page = item.funcargs.get("page")
                if page:
                    page.screenshot(path=screen_file, full_page=True)
                    extras.append(pytest_html.extras.png(screen_file))
        except Exception as e:
            print(f"Error capturing screenshot: {e}")
    report.extra = extras

STORAGE_FILE = "playwright/auth/state.json"
@pytest.fixture(scope='session')
def context(browser):
 if os.path.isfile(STORAGE_FILE):
     contexto = browser.new_context(
         base_url='https://automationexercise.com/',
         record_video_dir='videos',
         storage_state=STORAGE_FILE
     )
 else:
     context = browser.new_context(
         base_url='https://automationexercise.com/',
         record_video_dir='videos'
     )
     yield context
     os.makedirs(os.path.dirname(STORAGE_FILE), exist_ok=True)
     if not os.path.isfile(STORAGE_FILE):
         context.storage_state(path=STORAGE_FILE)
     context.close()