import sys
sys.path.insert(0, '.')
from pages.kontakt import Kontakt

def test_kontakt_sida_laddar(page):
    kontakt = Kontakt(page)
    kontakt.ga_till()
    assert page.url is not None

def test_kontakt_tar_skarmdum(page):
    kontakt = Kontakt(page)
    kontakt.ga_till()
    kontakt.ta_skarmdum()
    import os
    assert os.path.exists('screenshots/kontakt.png')

def test_kontakt_har_innehall(page):
    kontakt = Kontakt(page)
    kontakt.ga_till()
    assert len(page.content()) > 100

def test_kontakt_https(page):
    kontakt = Kontakt(page)
    kontakt.ga_till()
    assert page.url.startswith('https://')

def test_kontakt_har_lankar(page):
    kontakt = Kontakt(page)
    kontakt.ga_till()
    assert page.locator('a').count() > 0
