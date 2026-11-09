class BasSida:
    sokvag = '/'

    def __init__(self, page):
        self.page = page
        self.svar = None

    def ga_till(self):
        self.svar = self.page.goto(self.sokvag)
        return self.svar

    def status(self):
        return self.svar.status if self.svar else None