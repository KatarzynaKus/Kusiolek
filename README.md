# Kształtowanie się filozoficznych intuicji 

Repozytorium projektu "Kształtowanie się intuicji filozoficznych".

Tutaj znajdują się materiały związane z badaniem ankietowym.

## Ankieta

W katalogu `semestr_1/ankieta` znajduje się plik `questionnaire.tex`, który jest plikiem z ankietą, który kompiluje się za pomocą standardowej instalacji LaTeX (nie potrzeba mieć zainstalowanego programu SDAPS). Przetestowałem, że bez błędów skompilować go można za pomocą: 

```
pdflatex questionnaire.tex
```

Polecenie to wygeneruje plik PDF z kwestionariuszem. 

W pliku `questionnaire.tex` znajduje się tylko struktura ankiety. W tym pliku nie powinno być na sztywno wpisanego ani jednego fragmentu tekstu. Elementy tekstowe ankiety znajdują się w pliku `variables.tex` oraz w odpowiednich plikach w katalogu `scenarios`. Zawartość tych plików jest wczytywana przy kompilowaniu ankiety.

## Formularz do wyrażania zgody

W katalogu `agreement` znajduje się formularz ze zgodą uczestników badania. Skompilować go można za pomocą:

```
pdflatex agreement.tex
```

## Naklejki

W katalogu `stickers` znajduje się skrypt generujący naklejki. Uruchamia się go poleceniem:

```
python3 generate_stickers.py
```

W efekcie tworzy plik z naklejkami `stickers.pdf`. W pliku `labels_template.tex` znajduje się szablon jednej kolumny papieru naklejkowego. Skrypt generuje tyle kolumn, ile jest uczestników, każda z unikatowym kodem badanego. 

## Obróbka danych

W katalogu `data_cleaner` znajduje się skrypt, służący do obróbki i złączenia danych z papierowej i internetowej wersji kwestionariusza. Używa go się w następujący sposób:

```
python3 cleaner.py --sdaps-file plik_csv_wygenerowany_przez_sdaps --lime-login login_do_kognilabu --lime-password haslo_do_kognilabu --lime-sid numer_ankiety --output plik_wyjsciowy
```

