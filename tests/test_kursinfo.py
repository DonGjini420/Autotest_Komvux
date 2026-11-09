from pages.kursinfo import Kursinfo


def test_kurssida_svarar_200(page):
    sida = Kursinfo(page)
    sida.ga_till()
    assert sida.status() == 200


def test_kurssida_har_rubrik(page):
    sida = Kursinfo(page)
    sida.ga_till()
    assert 'komvux' in sida.hamta_rubrik().lower()


def test_kurssida_har_beskrivning(page):
    sida = Kursinfo(page)
    sida.ga_till()
    assert len(sida.hamta_kursbeskrivning()) > 20


def test_kurssida_har_ansokan_lank(page):
    sida = Kursinfo(page)
    sida.ga_till()
    assert sida.ansokan_lank().is_visible()


def test_kurssida_lankar_till_kurskatalogen(page):
    sida = Kursinfo(page)
    sida.ga_till()
    assert sida.kurskatalog_lank().count() == 1