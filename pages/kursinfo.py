class Kursinfo:
    def __init__(self, page):
        self.page = page

    def hamta_rubrik(self):
        return self.page.locator('h1').first.text_content()

    def hamta_kursbeskrivning(self):
        return self.page.locator('p').first.text_content()

    def ansokan_knapp_finns(self):
        return self.page.locator('a:has-text("Ansok"), button:has-text("Ansok")').count() > 0
