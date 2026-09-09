class Ansokan:
    def __init__(self, page):
        self.page = page
        self.url = 'https://vuxenutbildning.stockholm/ansok'

    def ga_till(self):
        self.page.goto(self.url)

    def formular_finns(self):
        return self.page.locator('form, input').count() > 0

    def fyll_i_namn(self, namn):
        self.page.locator('input[name="namn"], input[type="text"]').first.fill(namn)

    def ta_skarmdum(self, namn):
        self.page.screenshot(path=f'screenshots/{namn}.png')
