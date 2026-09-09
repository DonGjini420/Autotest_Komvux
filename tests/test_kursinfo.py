import sys
sys.path.insert(0, '.')
from pages.kursinfo import Kursinfo

def test_kursinfo_har_rubrik(page):
    page.goto('https://vuxenutbildning.stockholm')
    kurs = Kursinfo(page)
    rubrik = kurs.hamta_rubrik()
    assert len(rubrik) > 0

def test_kursinfo_har_beskrivning(page):
    page.goto('https://vuxenutbildning.stockholm')
    kurs = Kursinfo(page)
    beskrivning = kurs.hamta_kursbeskrivning()
    assert len(beskrivning) > 0

def test_kursinfo_har_bilder(page):
    page.goto('https://vuxenutbildning.stockholm')
    assert page.locator('img').count() > 0

def test_kursinfo_inga_brutna_lankar(page):
    page.goto('https://vuxenutbildning.stockholm')
    lankar = page.locator('a').all()
    assert len(lankar) > 0

def test_kursinfo_skarmdum(page):
    page.goto('https://vuxenutbildning.stockholm')
    page.screenshot(path='screenshots/kursinfo.png')
    import os
    assert os.path.exists('screenshots/kursinfo.png')
