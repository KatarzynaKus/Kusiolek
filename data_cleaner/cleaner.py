import argparse
import pandas as pd
from numpy import nan
from pandas import Series
from limesurvey_helper import LimeSurveyRPC

parser = argparse.ArgumentParser(description='Ściąga i obrabia wyniki ankiet')
parser.add_argument('--sdaps-file', action = 'store', dest = 'sdapsfile')
parser.add_argument('--lime-sid', action = 'store', dest = 'lime_sid')
parser.add_argument('--lime-login', action = 'store', dest = 'lime_login')
parser.add_argument('--lime-password', action = 'store', dest='lime_pass')
parser.add_argument('--output', dest = 'outputfile' )
args = vars(parser.parse_known_args()[0])

sdapsfile = args['sdapsfile']
lime_sid = args['lime_sid']
lime_login = args['lime_login']
lime_pass = args['lime_pass']
outputfile = args['outputfile']



data = pd.read_csv(sdapsfile)

column_map = {
    'questionnaire_id' :'ID kwestionariusza',
    'global_id': 'ID badanego',
    'verified' : 'Zweryfikowany',
    '1_1_0':'Naklejka',
    '1_2_0':'Podstawowy kierunek',
    '1_3_0':'Rok urodzenia',
    '1_4_0': 'Płeć - kobieta',
    '1_4_1': 'Płeć - mężczyzna',
    '1_4_2': 'Płeć - inna',
    '1_4_3': 'Płeć - odmowa odpowiedzi',
    '1_5_0':'Filozofia lub etyka w szkole średniej - tak',
    '1_5_1':'Filozofia lub etyka w szkole średniej - nie',
    '1_6_0':'Olimpiada lub Konkurs Filozoficzny - tak',
    '1_6_1':'Olimpiada lub Konkurs Filozoficzny - nie',
    '1_7_0':'Rok rozpoczęcia studiów filozoficznych',
    '1_8_0':'Inne studia - tak',
    '1_8_1':'Inne studia - nie',
    '1_8_2':'Inne studia - a',
    '1_8_3':'Inne studia - b',
    '1_8_4':'Inne studia - c',
    '1_9_0':'Dziedziny filozofii - epistemologia',
    '1_9_1':'Dziedziny filozofii - logika',
    '1_9_2':'Dziedziny filozofii - etyka',
    '1_9_3':'Dziedziny filozofii - filozofia polityki',
    '1_9_4':'Dziedziny filozofii - filozofia społeczna',
    '1_9_5':'Dziedziny filozofii - historia filozofii',
    '1_9_6':'Dziedziny filozofii - filozofia kultury',
    '1_9_7':'Dziedziny filozofii - estetyka',
    '1_9_8':'Dziedziny filozofii - filozofia religii',
    '1_9_9':'Dziedziny filozofii - filozofia nauki',
    '1_9_10':'Dziedziny filozofii - filozofia analityczna',
    '1_9_11':'Dziedziny filozofii - ontologia',
    '1_9_12':'Dziedziny filozofii - filozofia nieanalityczna',
    '1_9_13':'Dziedziny filozofii - inne',
    '2_1_0':'Gettier - tak',
    '2_1_1':'Gettier - nie',
    '2_2':'Gettier - poziom',
    '3_1_0':'Stodoły - tak',
    '3_1_1':'Stodoły - nie',
    '3_2':'Stodoły - poziom',
    '4_1_0':'Truetemp - tak',
    '4_1_1':'Truetemp - nie',
    '4_2':'Truetemp - poziom',
    '5_1_0':'Parfit - żona',
    '5_1_1':'Parfit - matka',
    '5_1_2':'Parfit - żadna',
    '5_1_3':'Parfit - obie',
    '5_2':'Parfit - poziom',
    '6_1_0':'Knobe - tak',
    '6_1_1':'Knobe - nie',
    '6_2':'Knobe - poziom',
    '7_1_0':'Putnam - tak',
    '7_1_1':'Putnam - nie',
    '7_2_0':'Putnam - poziom',
    '8_1_0':'Kripke - autor',
    '8_1_1':'Kripke - oszust',
    '8_2':'Kripke - poziom',
    '9_1_0':'Frankfurt1 - tak',
    '9_1_1':'Frankfurt1 - nie',
    '9_2_0':'Frankfurt2 - tak',
    '9_2_1':'Frankfurt2 - nie',
    '9_3_0':'Frankfurt3 - tak',
    '9_3_1':'Frankfurt3 - nie',
    '9_4':'Frankfurt - poziom',
    '10_1_0':'Skrzypek - tak',
    '10_1_1':'Skrzypek - nie',
    '10_2':'Skrzypek - poziom',
    '11_1_0':'Maszyna przyjemności - podłączyć',
    '11_1_1':'Maszyna przyjemności - pozostać',
    '11_2':'Maszyna przyjemności - poziom',
}

data.rename(columns=column_map, inplace=True)

response = Series()

response = response.append ([
data['Płeć - kobieta'].map({1:'Kobieta', 0:nan}).dropna(),
data['Płeć - mężczyzna'].map({1:'Mężczyzna', 0:nan}).dropna(),
data['Płeć - inna'].map({1:'Inna', 0:nan}).dropna(),
data['Płeć - odmowa odpowiedzi'].map({1:'Odmowa odpowiedzi', 0:nan}).dropna()
])

data['Płeć'] = response

response = Series()

response = response.append ([
data['Filozofia lub etyka w szkole średniej - tak'].map({1:'Tak', 0:nan}).dropna(),
data['Filozofia lub etyka w szkole średniej - nie'].map({1:'Nie', 0:nan}).dropna()
])

data['Filozofia lub etyka w szkole średniej'] = response

response = Series()

response = response.append ([
data['Olimpiada lub Konkurs Filozoficzny - tak'].map({1:'Tak', 0:nan}).dropna(),
data['Olimpiada lub Konkurs Filozoficzny - nie'].map({1:'Nie', 0:nan}).dropna()
])

data['Olimpiada lub Konkurs Filozoficzny'] = response

response = Series()

response = response.append ([
data['Inne studia - tak'].map({1:'Tak', 0:nan}).dropna(),
data['Inne studia - nie'].map({1:'Nie', 0:nan}).dropna()
])

data['Inne studia'] = response

dziedziny = ['Dziedziny filozofii - epistemologia',
    'Dziedziny filozofii - logika',
    'Dziedziny filozofii - etyka',
    'Dziedziny filozofii - filozofia polityki',
    'Dziedziny filozofii - filozofia społeczna',
    'Dziedziny filozofii - historia filozofii',
    'Dziedziny filozofii - filozofia kultury',
    'Dziedziny filozofii - estetyka',
    'Dziedziny filozofii - filozofia religii',
    'Dziedziny filozofii - filozofia nauki',
    'Dziedziny filozofii - filozofia analityczna',
    'Dziedziny filozofii - ontologia',
    'Dziedziny filozofii - filozofia nieanalityczna']
for d in dziedziny:
    data[d] = data[d].map({1:'Tak', 0:'Nie'})

response = Series()

response = response.append ([
data['Gettier - tak'].map({1:'Tak', 0:nan}).dropna(),
data['Gettier - nie'].map({1:'Nie', 0:nan}).dropna()
])

data['Gettier'] = response

response = Series()

response = response.append ([
data['Stodoły - tak'].map({1:'Tak', 0:nan}).dropna(),
data['Stodoły - nie'].map({1:'Nie', 0:nan}).dropna()
])

data['Stodoły'] = response

response = Series()

response = response.append ([
data['Truetemp - tak'].map({1:'Tak', 0:nan}).dropna(),
data['Truetemp - nie'].map({1:'Nie', 0:nan}).dropna()
])

data['Truetemp'] = response

response = Series()

response = response.append ([
data['Truetemp - tak'].map({1:'Tak', 0:nan}).dropna(),
data['Truetemp - nie'].map({1:'Nie', 0:nan}).dropna()
])

data['Truetemp'] = response

response = Series()

response = response.append ([
data['Parfit - żona'].map({1:'Żona', 0:nan}).dropna(),
data['Parfit - matka'].map({1:'Matka', 0:nan}).dropna(),
data['Parfit - żadna'].map({1:'Żadna', 0:nan}).dropna(),
data['Parfit - obie'].map({1:'Obie', 0:nan}).dropna()
])

data['Parfit'] = response

response = Series()

response = response.append ([
data['Knobe - tak'].map({1:'Tak', 0:nan}).dropna(),
data['Knobe - nie'].map({1:'Nie', 0:nan}).dropna()
])

data['Knobe'] = response

response = Series()

response = response.append ([
data['Putnam - tak'].map({1:'Tak', 0:nan}).dropna(),
data['Putnam - nie'].map({1:'Nie', 0:nan}).dropna()
])

data['Putnam'] = response

response = Series()

response = response.append ([
data['Kripke - autor'].map({1:'Autor', 0:nan}).dropna(),
data['Kripke - oszust'].map({1:'Oszust', 0:nan}).dropna()
])

data['Kripke'] = response

response = Series()

response = response.append ([
data['Frankfurt1 - tak'].map({1:'Tak', 0:nan}).dropna(),
data['Frankfurt1 - nie'].map({1:'Nie', 0:nan}).dropna()
])

data['Frankfurt1'] = response

response = Series()

response = response.append ([
data['Frankfurt2 - tak'].map({1:'Tak', 0:nan}).dropna(),
data['Frankfurt2 - nie'].map({1:'Nie', 0:nan}).dropna()
])

data['Frankfurt2'] = response

response = Series()

response = response.append ([
data['Frankfurt3 - tak'].map({1:'Tak', 0:nan}).dropna(),
data['Frankfurt3 - nie'].map({1:'Nie', 0:nan}).dropna()
])

data['Frankfurt3'] = response

response = Series()

response = response.append ([
data['Skrzypek - tak'].map({1:'Tak', 0:nan}).dropna(),
data['Skrzypek - nie'].map({1:'Nie', 0:nan}).dropna()
])

data['Skrzypek'] = response

response = Series()

response = response.append ([
data['Maszyna przyjemności - podłączyć'].map({1:'Podłączyć', 0:nan}).dropna(),
data['Maszyna przyjemności - pozostać'].map({1:'Pozostać', 0:nan}).dropna()
])

data['Maszyna przyjemności'] = response

columns = [
    'ID kwestionariusza',
    'ID badanego',
    'Zweryfikowany',
    'Naklejka',
    'Podstawowy kierunek',
    'Rok urodzenia',
    'Płeć', 
    'Filozofia lub etyka w szkole średniej',
    'Olimpiada lub Konkurs Filozoficzny',
    'Dziedziny filozofii - inne',
    'Inne studia', 
    'Gettier',
    'Stodoły', 
    'Truetemp', 
    'Parfit', 
    'Knobe', 
    'Putnam', 
    'Kripke',
    'Frankfurt1', 
    'Frankfurt2', 
    'Frankfurt3', 
    'Skrzypek',
    'Maszyna przyjemności'
]
columns = columns + dziedziny

data = data[columns]
data['Kanał'] = 'Papier'
data.to_csv('papier-clean.csv')

kognilab = LimeSurveyRPC(login=lime_login, password=lime_pass, 
                         url='http://kognilab.pl/limesurvey/index.php/admin/remotecontrol')

kognilab.get_survey(dest='.', lang='pl', sid=int(lime_sid))

data = pd.read_csv('{lime_sid}.csv'.format(lime_sid = lime_sid))

column_map = {
    'demographics1' : 'Podstawowy kierunek',
    'demographics2' : 'Rok urodzenia',
    'demographics3' : 'Płeć',
    'demographics4' : 'Filozofia lub etyka w szkole średniej',
    'demographics5' : 'Olimpiada lub Konkurs Filozoficzny',
    'demographics6' : 'Rok rozpoczęcia studiów filozoficznych',
    'demographics7[SQ001]' : 'Inne studia - a',
    'demographics7[SQ001]' : 'Inne studia - b',
    'demographics7[SQ001]' : 'Inne studia - c',
    'demographics8[SQ001]' : 'Dziedziny filozofii - epistemologia',
    'demographics8[SQ002]' : 'Dziedziny filozofii - etyka',
    'demographics8[SQ003]' : 'Dziedziny filozofii - filozofia społeczna',
    'demographics8[SQ004]' : 'Dziedziny filozofii - filozofia kultury',
    'demographics8[SQ005]' : 'Dziedziny filozofii - filozofia religii',
    'demographics8[SQ006]' : 'Dziedziny filozofii - filozofia analityczna',
    'demographics8[SQ007]' : 'Dziedziny filozofii - filozofia nieanalityczna',
    'demographics8[SQ008]' : 'Dziedziny filozofii - logika',
    'demographics8[SQ009]' : 'Dziedziny filozofii - filozofia polityki',
    'demographics8[SQ010]' : 'Dziedziny filozofii - historia filozofii',
    'demographics8[SQ011]' : 'Dziedziny filozofii - estetyka',
    'demographics8[SQ012]' : 'Dziedziny filozofii - filozofia nauki',
    'demographics8[SQ013]' : 'Dziedziny filozofii - ontologia',
    'demographics8[other]' : 'Dziedziny filozofii - inne',
    'survey1' : 'Gettier', 
    'survey1Certainty[SQ001]' : 'Gettier - poziom',
    'survey2' : 'Stodoły', 
    'survey2Certainty[SQ001]' : 'Stodoły - poziom',
    'survey3' : 'Truetemp', 
    'survey3Certainty[SQ001]' : 'Truetemp - poziom',
    'survey4' : 'Parfit', 
    'survey4Certainty[SQ001]' : 'Parfit - poziom',
    'survey5' : 'Knobe', 
    'survey5Certainty[SQ001]' : 'Knobe - poziom',
    'survey6' : 'Putnam', 
    'survey6Certainty[SQ001]' : 'Putnam - poziom',
    'survey7' : 'Kripke', 
    'survey7Certainty[SQ001]' : 'Kripke - poziom',
    'survey8' : 'Frankfurt1', 
    'survey8Question2' : 'Frankfurt2',
    'survey8Question3' : 'Frankfurt3',
    'survey8Certainty[SQ001]' : 'Frankfurt - poziom',
    'survey9' : 'Skrzypek', 
    'survey9Certainty[SQ001]' : 'Skrzypek - poziom',
    'survey10' : 'Maszyna przyjemności', 
    'survey10Certainty[SQ001]' : 'Maszyna przyjemności - poziom',
}

data.rename(columns=column_map, inplace=True)

data['Płeć'] = data['Płeć'].map({'A1':'Kobieta', 'A2':'Mężczyzna', 'A3':'Odmowa odpowiedzi'})

data['Filozofia lub etyka w szkole średniej'] = data['Filozofia lub etyka w szkole średniej'].map({'Y':'Tak', 'N':'Nie'})

data['Olimpiada lub Konkurs Filozoficzny'] = data['Olimpiada lub Konkurs Filozoficzny'].map({'Y':'Tak', 'N':'Nie'})

for d in dziedziny:
    data[d] = data[d].map({'Y':'Tak', nan:'Nie'})

data['Gettier'] = data['Gettier'].map({'Y':'Tak', 'N':'Nie'})

data['Stodoły'] = data['Stodoły'].map({'Y':'Tak', 'N':'Nie'})

data['Truetemp'] = data['Truetemp'].map({'Y':'Tak', 'N':'Nie'})

data['Putnam'] = data['Putnam'].map({'Y':'Tak', 'N':'Nie'})

data['Parfit'] = data['Parfit'].map({'A1':'Żona', 'A2':'Matka', 'A3':'Żadna', 'A4':'Obie'})

data['Knobe'] = data['Knobe'].map({'Y':'Tak', 'N':'Nie'})

data['Kripke'] = data['Kripke'].map({'A1':'Autor', 'A2':'Oszust'})

data['Frankfurt1'] = data['Frankfurt1'].map({'Y':'Tak', 'N':'Nie'})
data['Frankfurt2'] = data['Frankfurt2'].map({'Y':'Tak', 'N':'Nie'})
data['Frankfurt3'] = data['Frankfurt3'].map({'Y':'Tak', 'N':'Nie'})

data['Skrzypek'] = data['Skrzypek'].map({'Y':'Tak', 'N':'Nie'})

data['Maszyna przyjemności'] = data['Maszyna przyjemności'].map({'A1':'Podłączyć', 'A2':'Pozostać'})

data = data[list(set(columns).intersection(data.columns))]

data.to_csv('limesurvey-clean.csv')



data_sdaps = pd.read_csv('papier-clean.csv')
data_limesurvey = pd.read_csv('limesurvey-clean.csv')

data = pd.concat([data_sdaps, data_limesurvey])

data.to_csv(outputfile)
