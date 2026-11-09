from pages.startsida import Startsida


def test_startsidan_svarar_200(page):
    sida = Startsida(page)
    sida.ga_till()
    assert sida.status() == 200


def test_startsidan_https(page):
    Startsida(page).ga_till()
    assert page.url.startswith('https://')


def test_startsidan_har_titel(page):
    sida = Startsida(page)
    sida.ga_till()
    assert sida.titel().strip() != ''


def test_startsidan_har_navigation(page):
    Startsida(page).ga_till()
    assert page.locator('nav').count() > 0


def test_startsidan_har_sok_lank(page):
    sida = Startsida(page)
    sida.ga_till()
    assert sida.sok_lank().is_visible()


def test_startsidan_inga_brutna_lankar(page):
    sida = Startsida(page)
    sida.ga_till()
    lankar = sida.interna_lankar()
    assert len(lankar) > 0
    brutna = []
    for url in lankar:
        svar = page.request.get(url)
        if svar.status >= 400:
            brutna.append(f'{svar.status} {url}')
    assert brutna == [], 'Brutna lankar:\n' + '\n'.join(brutna)