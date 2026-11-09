import os
import pytest

BASE_URL = 'https://vuxenutbildning.stockholm'


@pytest.fixture(scope='session')
def base_url():
    # pytest-playwright anvander base_url, sa page.goto('/kontakt') fungerar
    return BASE_URL


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Ta skarmdump automatiskt nar ett test misslyckas
    outcome = yield
    rapport = outcome.get_result()
    if rapport.when == 'call' and rapport.failed:
        page = item.funcargs.get('page')
        if page is not None:
            os.makedirs('screenshots', exist_ok=True)
            try:
                page.screenshot(path=f'screenshots/{item.name}.png', full_page=True)
            except Exception:
                pass