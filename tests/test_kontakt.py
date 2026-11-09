from pages.kontakt import Kontakt


def test_kontakt_svarar_200(page):
    sida = Kontakt(page)
    sida.ga_till()
    assert sida.status() == 200


def test_kontakt_har_telefonnummer(page):
    sida = Kontakt(page)
    sida.ga_till()
    assert sida.telefon_finns()


def test_kontakt_har_fraga_lank(page):
    sida = Kontakt(page)
    sida.ga_till()
    assert sida.fraga_lank().count() == 1