import uuid # do generowania unikatowych numerów, żeby nikt nie mógł wypełnić nie swoich ankiet w internecie zgadując
import jinja2 # obsługa szablonowania
import os # wywołuje z pythona latexa
from jinja2 import Template 

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
n_participants = 100

# generujemy tyle losowych stringów, ile jest uczestników
id_ns = [uuid.uuid4().hex[:4].upper() for i in range(n_participants)]

# sprawdzamy, żeby były unikatowe
unique_ids = list(set(id_ns))

# wczytujemy plik szablonu
template = latex_jinja_env.get_template('labels_template.tex')

# generowanie pliku z naklejkami
labels = []
for i, j in enumerate(unique_ids):
    labels.append(template.render(UID=j, # funkcja render wstawia w miejsce zmiennych w szablonie
                                  ID=i)) # odpowiednie dane, które wygenerowaliśmy pythonem

labels = '\n\n'.join(labels) # tworzymy z tego wszystkiego jeden plik

with open('labels.tex', 'w') as f: # zapisujemy go w 'labels.tex', który jest wczytywany przez 'stickers.tex'
    f.write(labels)

os.system('pdflatex stickers.tex') # kompilujemy 'stickers.tex' latexem
print('Plik z ankietami wygenerowany') # puff
