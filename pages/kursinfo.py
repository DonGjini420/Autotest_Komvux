import re
from pages.bas import BasSida


class Kursinfo(BasSida):
    # Informationssidan om komvux pa gymnasieniva
    sokvag = '/gymnasial-komvux/'

    def hamta_rubrik(self):
        return (self.page.locator('h1').first.text_content() or '').strip()

    def hamta_kursbeskrivning(self):
        # Forsta stycket i huvudinnehallet som faktiskt innehaller text
        for text in self.page.locator('main p').all_text_contents():
            if text.strip():
                return text.strip()
        return ''

    def ansokan_lank(self):
        return self.page.get_by_role('link', name=re.compile('ansök till komvux', re.I)).first

    def kurskatalog_lank(self):
        return self.page.locator('a[href*="komvux.stockholm.se"]').first