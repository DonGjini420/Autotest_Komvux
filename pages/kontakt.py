import re
from pages.bas import BasSida


class Kontakt(BasSida):
    # Sajten har ingen /kontakt-sida, kontaktuppgifterna finns har
    sokvag = '/vuxenutbildningscentrum/'

    def telefon_finns(self):
        if self.page.locator('a[href^="tel:"]').count() > 0:
            return True
        text = self.page.locator('body').inner_text()
        return re.search(r'0\d{1,3}[-\s]\d{2,3}[\s\d]{3,}', text) is not None

    def fraga_lank(self):
        return self.page.get_by_role('link', name=re.compile('ställ en fråga', re.I)).first