# Autotest Komvux
Skapad av: Donaldo Gjini
Praktik: Vuxenutbildningscentrum, Arbetsmarknadsförvaltningen 2026

## Vad gör projektet?
Automatiserade tester med Playwright, pytest och Page Object Model mot
https://vuxenutbildning.stockholm

Testerna körs automatiskt med GitHub Actions vid varje push och varje natt.

## Projektstruktur
```
Autotest_Komvux/
├── .github/workflows/tester.yml   # CI med GitHub Actions
├── pages/                         # Page Objects
│   ├── bas.py                     # Gemensam bas (navigering, statuskod)
│   ├── startsida.py
│   ├── sokresultat.py
│   ├── kursinfo.py
│   ├── ansokan.py
│   └── kontakt.py
├── tests/
│   ├── test_startsida.py
│   ├── test_sokresultat.py
│   ├── test_kursinfo.py
│   ├── test_ansokan.py
│   └── test_kontakt.py
├── conftest.py                    # base_url + skärmdump vid fel
└── requirements.txt
```

## Vad testas?
- **Startsida:** svarar 200, HTTPS, titel, navigation, Sök-länk, inga brutna länkar
- **Sökning:** sökning på "matematik" och "svenska" via /sok/ ger träffar
- **Komvux på gymnasienivå:** rubrik, beskrivning, länk "Ansök till komvux" och länk till kurskatalogen
- **Ansökan:** sidan svarar och har ett formulär
- **Kontakt (Vuxenutbildningscentrum):** sidan svarar, visar telefonnummer och länken "Ställ en fråga"

## Installation
```
pip install -r requirements.txt
playwright install chromium
```

## Köra tester
```
python -m pytest tests/ -v --html=rapport/testrapport.html --self-contained-html
```
Testerna körs utan synligt webbläsarfönster. Lägg till `--headed` om du vill se webbläsaren.

När ett test misslyckas sparas en skärmdump automatiskt i `screenshots/`.

## Öppna rapport
```
start rapport/testrapport.html
```