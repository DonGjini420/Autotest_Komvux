import sys
sys.path.insert(0, '.')
from pages.startsida import Startsida

def test_startsidan_laddar(page):
    sida = Startsida(page)
    sida.ga_till()
    assert 'vuxenutbildning' in page.url.lower()

def test_startsidan_har_titel(page):
    sida = Startsida(page)
    sida.ga_till()
    assert len(sida.titel()) > 0

def test_startsidan_https(page):
    sida = Startsida(page)
    sida.ga_till()
    assert page.url.startswith('https://')

def test_startsidan_har_navigation(page):
    sida = Startsida(page)
    sida.ga_till()
    assert page.locator('nav, header').count() > 0

def test_startsidan_har_lankar(page):
    sida = Startsida(page)
    sida.ga_till()
    assert page.locator('a').count() > 0

def test_startsidan_skarmdum(page):
    sida = Startsida(page)
    sida.ga_till()
    page.screenshot(path='screenshots/startsida.png')
    import os
    assert os.path.exists('screenshots/startsida.png')
