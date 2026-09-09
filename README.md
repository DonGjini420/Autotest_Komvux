@"
# Autotest Komvux
Skapad av: Donaldo Gjini
Praktik: Vuxenutbildningscentrum, Arbetsmarknadsforvaltningen 2026

## Vad gor projektet?
Automatiserade tester med Playwright och Page Object Model mot
https://vuxenutbildning.stockholm

## Projektstruktur
Autotest_komvux/
├── tests/
│   ├── test_startsida.py
│   ├── test_sokresultat.py
│   ├── test_kursinfo.py
│   ├── test_ansokan.py
│   └── test_kontakt.py
├── pages/
│   ├── startsida.py
│   ├── sokresultat.py
│   ├── kursinfo.py
│   ├── ansokan.py
│   └── kontakt.py
├── rapport/
├── screenshots/
├── conftest.py
├── requirements.txt
├── .gitignore
└── README.md

## Pages (Page Object Model)
- startsida.py - Startsidan och navigering
- sokresultat.py - Sokresultatsidan
- kursinfo.py - Kursinformationssidan
- ansokan.py - Ansokan till kurs
- kontakt.py - Kontaktsidan

## Installation
pip install -r requirements.txt
playwright install chromium

## Kor tester
C:\Users\User\AppData\Local\Programs\Python\Python313\python.exe -m pytest tests/ -v --html=rapport/testrapport.html --self-contained-html

## Oppna rapport
start rapport/testrapport.html

## Hemsida som testas
https://vuxenutbildning.stockholm
