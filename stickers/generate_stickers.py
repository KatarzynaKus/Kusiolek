import uuid # do generowania unikatowych numerów, żeby nikt nie mógł wypełnić nie swoich ankiet w internecie zgadując
import jinja2 # obsługa szablonowania
import os # wywołuje z pythona latexa
from jinja2 import Template 
import pandas as pd

# tutaj definiujemy środowisko jinja2 dla LaTeXa - to jest konfig ściągnięty
# z internetu, ale działa znakomicie - chodzi o to, żeby elementy szablonu
# nie konfliktowały ze składnią latexa

latex_jinja_env = jinja2.Environment(
	block_start_string = '\BLOCK{',
	block_end_string = '}',
	variable_start_string = '\VAR{',
	variable_end_string = '}',
	comment_start_string = '\#{',
	comment_end_string = '}',
	line_statement_prefix = '%%',
	line_comment_prefix = '%#',
	trim_blocks = True,
	autoescape = False,
	loader = jinja2.FileSystemLoader(os.path.abspath('.'))
)

# liczba uczestników badania
n_participants = 150

# generujemy tyle losowych stringów, ile jest uczestników
id_ns = [uuid.uuid4().hex[:3].upper() for i in range(n_participants)]

# sprawdzamy, żeby były unikatowe
unique_ids = list(set(id_ns))

# FILOZOFOWIE

# wczytujemy plik szablonu
template = latex_jinja_env.get_template('labels_template_p.tex')

# generowanie pliku z naklejkami
labels = []
for i, j in enumerate(unique_ids):
    labels.append(template.render(UID=j, # funkcja render wstawia w miejsce zmiennych w szablonie
                                  ID=i)) # odpowiednie dane, które wygenerowaliśmy pythonem

labels = '\n\n'.join(labels) # tworzymy z tego wszystkiego jeden plik

with open('labels.tex', 'w') as f: # zapisujemy go w 'labels.tex', który jest wczytywany przez 'stickers.tex'
    f.write(labels)

os.system('pdflatex stickers.tex') # kompilujemy 'stickers.tex' latexem
os.system('mv stickers.pdf stickers_phil.pdf')

# zapisujemy kody i tak dalej do pliku excela w celu wprowadzenia ich do limesurveya

stickers_data = pd.DataFrame(
    {
        'semestr 1': ['S1{code}{n}P'.format(code = c, n = n) for n,c in enumerate(unique_ids)],
        'semestr 2': ['S2{code}{n}P'.format(code = c, n = n) for n,c in enumerate(unique_ids)],
        'semestr 3': ['S3{code}{n}P'.format(code = c, n = n) for n,c in enumerate(unique_ids)],
        'semestr 4': ['S4{code}{n}P'.format(code = c, n = n) for n,c in enumerate(unique_ids)],
        'semestr 5': ['S5{code}{n}P'.format(code = c, n = n) for n,c in enumerate(unique_ids)],
        'semestr 6': ['S6{code}{n}P'.format(code = c, n = n) for n,c in enumerate(unique_ids)],
     })

stickers_data.to_excel('stickers_phil.xlsx')
print('Plik z naklejkami dla filozofów wygenerowany') # puff

# generujemy tyle losowych stringów, ile jest uczestników
id_ns = [uuid.uuid4().hex[:3].upper() for i in range(n_participants)]

# sprawdzamy, żeby były unikatowe
unique_ids = list(set(id_ns))

# wczytujemy plik szablonu
template = latex_jinja_env.get_template('labels_template_c.tex')

# generowanie pliku z naklejkami
labels = []
for i, j in enumerate(unique_ids):
    labels.append(template.render(UID=j, # funkcja render wstawia w miejsce zmiennych w szablonie
                                  ID=i)) # odpowiednie dane, które wygenerowaliśmy pythonem

labels = '\n\n'.join(labels) # tworzymy z tego wszystkiego jeden plik

with open('labels.tex', 'w') as f: # zapisujemy go w 'labels.tex', który jest wczytywany przez 'stickers.tex'
    f.write(labels)

os.system('pdflatex stickers.tex') # kompilujemy 'stickers.tex' latexem
os.system('mv stickers.pdf stickers_contr.pdf')

# zapisujemy kody i tak dalej do pliku excela w celu wprowadzenia ich do limesurveya

stickers_data = pd.DataFrame(
    {
        'semestr 1': ['S1{code}{n}C'.format(code = c, n = n) for n,c in enumerate(unique_ids)],
        'semestr 2': ['S2{code}{n}C'.format(code = c, n = n) for n,c in enumerate(unique_ids)],
        'semestr 3': ['S3{code}{n}C'.format(code = c, n = n) for n,c in enumerate(unique_ids)],
        'semestr 4': ['S4{code}{n}C'.format(code = c, n = n) for n,c in enumerate(unique_ids)],
        'semestr 5': ['S5{code}{n}C'.format(code = c, n = n) for n,c in enumerate(unique_ids)],
        'semestr 6': ['S6{code}{n}C'.format(code = c, n = n) for n,c in enumerate(unique_ids)],
     })

stickers_data.to_excel('stickers_contr.xlsx')
print('Plik z ankietami wygenerowany') # puff
