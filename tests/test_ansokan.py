from pages.ansokan import Ansokan


def test_ansokan_svarar_200(page):
    sida = Ansokan(page)
    sida.ga_till()
    assert sida.status() == 200


def test_ansokan_https(page):
    Ansokan(page).ga_till()
    assert page.url.startswith('https://')


def test_ansokan_har_formular(page):
    sida = Ansokan(page)
    sida.ga_till()
    assert sida.formular_finns()