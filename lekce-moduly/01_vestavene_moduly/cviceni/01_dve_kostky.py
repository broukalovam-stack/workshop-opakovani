# Cvičení 1 – Dvě kostky
# Doplň kód pod zadání a soubor spusť (Run).

# Hoď dvěma kostkami (každá má čísla 1 až 6) a vypiš obě čísla
#    i jejich součet. Použij randrange z modulu random.
#    Ukázka výstupu:
#
#    Padlo 3 a 5, dohromady 8.

from random import randrange
hod_jedna = randrange (1,7)
hod_dva = randrange (1,7)

print ("Padlo",hod_jedna, "a",hod_dva,"a dohromady to je", hod_dva+hod_jedna,".")