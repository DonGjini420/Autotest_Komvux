import sys
sys.path.insert(0, '.')
from pages.ansokan import Ansokan

def test_ansokan_sida_laddar(page):
    ansokan = Ansokan(page)
    ansokan.ga_till()
    assert page.url is not None

def test_ansokan_tar_skarmdum(page):
    ansokan = Ansokan(page)
    ansokan.ga_till()
    ansokan.ta_skarmdum('ansokan')
    import os
    assert os.path.exists('screenshots/ansokan.png')

def test_ansokan_har_innehall(page):
    ansokan = Ansokan(page)
    ansokan.ga_till()
    assert len(page.content()) > 100

def test_ansokan_https(page):
    ansokan = Ansokan(page)
    ansokan.ga_till()
    assert page.url.startswith('https://')

def test_ansokan_har_lankar(page):
    ansokan = Ansokan(page)
    ansokan.ga_till()
    assert page.locator('a').count() > 0
