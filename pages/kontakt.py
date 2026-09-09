class Kontakt:
    def __init__(self, page):
        self.page = page
        self.url = 'https://vuxenutbildning.stockholm/kontakt'

    def ga_till(self):
        self.page.goto(self.url)

    def telefon_finns(self):
        text = self.page.content().lower()
        return '08-' in text or 'tel:' in text

    def email_finns(self):
        return self.page.locator('a[href^="mailto:"]').count() > 0

    def ta_skarmdum(self):
        self.page.screenshot(path='screenshots/kontakt.png')
