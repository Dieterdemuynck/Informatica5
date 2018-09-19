# inputs
uur_1 = int(input("Uur naar vriendin = "))
minuten_1 = int(input("Minuten naar vriendin = "))
uur_2 = int(input("Uur bij vriendin = "))
minuten_2 = int(input("Minuten bij vriendin = "))
uur_3 = int(input("Uur naar huis = "))
minuten_3 = int(input("Minuten naar huis = "))
uur_4 = int(input("Uur thuis = "))
minuten_4 = int(input("Minuten thuis = "))

# Berekenen in minuten
minuten_weg = (minuten_4 - minuten_1) + ((uur_4 - uur_1) * 60)
minuten_bij_vriendin = minuten_3 - minuten_2 + ((uur_3 - uur_2) * 60)

# Getallen positief houden
minuten_weg += 1440
minuten_bij_vriendin += 1440
minuten_weg %= 1440
minuten_bij_vriendin %= 1440

# Verder berekenen in minuten
totaal_minuten_onderweg = (minuten_weg - minuten_bij_vriendin) // 2

# Optellen en Opsplitsen
minuten_voor_vetrek = int(uur_3 * 60 + minuten_3)
minuten_juist = int(minuten_voor_vetrek + totaal_minuten_onderweg)

uur = minuten_juist // 60
minuten = minuten_juist % 60
uur %= 24

# Optellen en Printen
print(str(uur))
print(str(minuten))