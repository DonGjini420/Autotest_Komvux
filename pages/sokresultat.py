class Sokresultat:
    def __init__(self, page):
        self.page = page

    def vanta_pa_resultat(self):
        self.page.wait_for_load_state('networkidle')

    def antal_resultat(self):
        return self.page.locator('.search-result, article, .result').count()

    def forsta_resultat_text(self):
        return self.page.locator('h2, h3').first.text_content()
