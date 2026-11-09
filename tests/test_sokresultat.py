import pytest
from pages.startsida import Startsida
from pages.sokresultat import Sokresultat


@pytest.mark.parametrize('sokord', ['matematik', 'svenska'])
def test_sok_ger_resultat(page, sokord):
    sida = Startsida(page)
    sida.ga_till()
    start_url = page.url
    sida.sok(sokord)
    assert page.url != start_url, 'Sokningen ledde inte till en ny sida'
    assert Sokresultat(page).antal_resultat(sokord) > 0, f'Inga traffar for "{sokord}"'