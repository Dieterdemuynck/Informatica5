straal = float(input("Straal: "))

pi = 3.14159

oppervlakte_cirkel = pi * (straal ** 2)
# Antwoordzin formuleren
uitvoer = "De oppervlakte van een cirkel met straal "
uitvoer += str(straal)
uitvoer += " is "
uitvoer += str(oppervlakte_cirkel)
# Antwoordzin printen
print(uitvoer)