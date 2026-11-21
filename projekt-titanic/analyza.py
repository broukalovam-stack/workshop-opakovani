# Titanic – ANALÝZA
#
# Sem piš funkce, které něco spočítají a výsledek vrátí (return).
# Nepatří sem žádný input() ani print(), ty piš do zprava.py.
# Díky tomu půjdou funkce z tohohle souboru testovat.
#
# Začni krokem 1: cviceni/01_nacteni.md

import csv
from pathlib import Path

# Složka, ve které leží tenhle soubor, a cesta k datům v ní.
# Díky tomu program data najde, ať ho spouštíš odkudkoliv.
SLOZKA = Path(__file__).parent
SOUBOR = SLOZKA / "Titanic-Dataset.csv"



def nacti_pasazery(soubor):
    with open(soubor, encoding="utf-8") as f:
        radky = list(csv.DictReader(f))
        return radky

def cislo_nebo_nic(text):
    if text =="":
        return None
    else:
        return (float(text))
    
#uprava radku
def uprav_pasazera(radek):
    pasazer = radek.copy()
    pasazer["Survived"] = int(radek["Survived"])
    pasazer["Pclass"] = int(radek["Pclass"])
    pasazer["SibSp"] = int(radek["SibSp"])
    pasazer["Parch"] = int(radek["Parch"])
    pasazer["Fare"] = float(radek["Fare"])
    pasazer ["Age"] = cislo_nebo_nic(radek["Age"])
    return pasazer

def uprav_pasazery(radky):
    upraveni_pasazeri =[]
    for radek in radky:
        upraveni_pasazeri.append(uprav_pasazera(radek))
    return upraveni_pasazeri