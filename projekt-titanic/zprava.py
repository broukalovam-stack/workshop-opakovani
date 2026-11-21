# Titanic – ZPRÁVA
#
# Tenhle soubor spouštíš (Run). Volá funkce z analyza.py a vypisuje
# výsledky. Patří sem všechno s print() a input().
#
# Začni krokem 1: cviceni/01_nacteni.md

import analyza
import csv

print("Titanic")
print(f"Data jsou v souboru {analyza.SOUBOR.name}.")

#print(analyza.nacti_pasazery(analyza.SOUBOR))
seznam = analyza.nacti_pasazery(analyza.SOUBOR)


""" #1 počet pasažeru
sum_pasazeri = len(seznam)
print(sum_pasazeri)

#2 vypiš Klíče
klice = list(seznam[0])
print(klice)

#3 první pasažer
prvni_pasazer = seznam[0]['Name']
print(prvni_pasazer)

#=== 2 část
#celkový počat pasažeru
sum_pasazeri = len(seznam)
print(sum_pasazeri) """


seznam_novy = analyza.uprav_pasazery(seznam)
print(seznam_novy)

pasazer_bez_veku = 0
for pasezer in seznam_novy:
    if pasezer["Age"] is None:
        pasazer_bez_veku= pasazer_bez_veku + 1

print("Pasažerů bez věku je",pasazer_bez_veku)