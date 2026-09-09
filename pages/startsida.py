class Startsida:
    def __init__(self, page):
        self.page = page
        self.url = 'https://vuxenutbildning.stockholm'

    def ga_till(self):
        self.page.goto(self.url)

    def titel(self):
        return self.page.title()

    def sok(self, text):
        self.page.get_by_role('searchbox').fill(text)
        self.page.keyboard.press('Enter')
