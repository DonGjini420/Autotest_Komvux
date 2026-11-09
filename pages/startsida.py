from urllib.parse import urlparse
from pages.bas import BasSida

# Sokfaltet finns pa sidan /sok/ (startsidan har bara en "Sök"-lank)
SOKFALT = '[role="searchbox"], input[type="search"], form input[type="text"]'


class Startsida(BasSida):
    sokvag = '/'

    def titel(self):
        return self.page.title()

    def sok_lank(self):
        return self.page.get_by_role('link', name='Sök', exact=True).first

    def sok(self, text):
        self.page.goto('/sok/')
        falt = self.page.locator(SOKFALT).first
        falt.fill(text)
        falt.press('Enter')
        self.page.wait_for_load_state('domcontentloaded')

    def interna_lankar(self, max_antal=30):
        doman = urlparse(self.page.url).netloc
        hrefs = self.page.eval_on_selector_all('a[href]', 'els => els.map(e => e.href)')
        unika = []
        for h in hrefs:
            h = h.split('#')[0]
            if urlparse(h).netloc == doman and h not in unika:
                unika.append(h)
        return unika[:max_antal]