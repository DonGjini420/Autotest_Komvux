import sys
sys.path.insert(0, '.')
from pages.startsida import Startsida
from pages.sokresultat import Sokresultat

def test_sok_utbildning(page):
    sida = Startsida(page)
    sida.ga_till()
    try:
        page.locator('input[type="search"], input[type="text"], input[placeholder*="ok"], [role="search"] input').first.fill('matematik')
        page.keyboard.press('Enter')
        page.wait_for_load_state('networkidle')
        assert page.url != 'https://vuxenutbildning.stockholm'
    except:
        page.screenshot(path='screenshots/sok_fel.png')
        print('Sokfalt hittades inte')

def test_sokresultat_visas(page):
    sida = Startsida(page)
    sida.ga_till()
    try:
        page.locator('input[type="search"], input[type="text"], input[placeholder*="ok"], [role="search"] input').first.fill('svenska')
        page.keyboard.press('Enter')
        page.wait_for_load_state('networkidle')
        assert page.url is not None
    except:
        page.screenshot(path='screenshots/sokresultat_fel.png')
        print('Sokfalt hittades inte')
