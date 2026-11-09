from pages.bas import BasSida


class Ansokan(BasSida):
    sokvag = '/ansok'

    def formular_finns(self):
        return self.page.locator('form, input:not([type="hidden"])').count() > 0