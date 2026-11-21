# Cvičení 2 – Kdo myje nádobí
# Doplň kód pod zadání a soubor spusť (Run).

# Máš seznam lidí z bytu. Vylosuj, kdo dnes myje nádobí,
#    a vypiš to. Pomůže ti funkce choice z modulu random.

from random import choice
lide = ["Anna", "Petra", "Jana", "Eva"]
nadobi = choice(lide)
print("Dnes myje nádobi", nadobi,".")