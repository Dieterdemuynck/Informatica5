# inputs
vertrek_uur_naar_vriendin = int(input("Uur naar vriendin = "))
vertrek_minuten_naar_vriendin = int(input("Minuten naar vriendin = "))
aankomst_uur_naar_vriendin = int(input("Uur bij vriendin = "))
aankomst_minuten_naar_vriendin = int(input("Minuten bij vriendin = "))
vertrek_uur_naar_huis = int(input("Uur naar huis = "))
vertrek_minuten_naar_huis = int(input("Minuten naar huis = "))
aankomst_uur_naar_huis = int(input("Uur thuis = "))
aankomst_minuten_naar_huis = int(input("Minuten thuis = "))

# Berekenen in minuten
minuten_weg = aankomst_minuten_naar_huis - vertrek_minuten_naar_vriendin + ((aankomst_uur_naar_huis - vertrek_uur_naar_vriendin) * 60)
minuten_bij_vriendin = vertrek_minuten_naar_huis - aankomst_minuten_naar_vriendin + ((vertrek_uur_naar_huis - aankomst_uur_naar_vriendin) * 60)
totaal_minuten_onderweg = (minuten_weg - minuten_bij_vriendin) // 2

# Optellen en Opsplitsen
minuten_verkeerd = int(aankomst_uur_naar_huis * 60 + aankomst_minuten_naar_huis)
minuten_juist = int(minuten_verkeerd + totaal_minuten_onderweg)

uur = minuten_juist // 60
minuten = minuten_juist % 60

# Optellen en Printen
print(str(uur))
print(str(minuten))