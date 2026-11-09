import re


class Sokresultat:
    def __init__(self, page):
        self.page = page

    def resultat_lankar(self, sokord):
        return self.page.locator('main').get_by_role('link', name=re.compile(sokord, re.I))

    def antal_resultat(self, sokord):
        return self.resultat_lankar(sokord).count()

    def oppna_forsta(self, sokord):
        self.resultat_lankar(sokord).first.click()
        self.page.wait_for_load_state('domcontentloaded')