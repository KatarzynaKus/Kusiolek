# Kształtowanie się filozoficznych intuicji 

Repozytorium projektu "Kształtowanie się intuicji filozoficznych".

Tutaj będą znajdować się materiały związane z badaniem ankietowym.

## Ankieta

W katalogu `semestr_1/ankieta` znajduje się plik `questionnaire.tex`, który jest plikiem z ankietą, który kompiluje się za pomocą standardowej instalacji LaTeX (nie potrzeba mieć zainstalowanego programu SDAPS). Przetestowałem, że bez błędów skompilować go można za pomocą: 

```
pdflatex questionnaire.tex
```

Polecenie to wygeneruje plik PDF z kwestionariuszem. 

W pliku `questionnaire.tex` znajduje się tylko struktura ankiety. W tym pliku nie powinno być na sztywno wpisanego ani jednego fragmentu tekstu. Elementy tekstowe ankiety znajdują się w pliku `variables.tex`. Zawartość tego pliku jest wczytywana przy kompilowaniu pliku.

### `questionnaire.tex`

### `variables.tex`
