# Input bedrag
bedrag = int(input("Bedrag in eurocent: "))
origineel_bedrag = bedrag

# BEREKENEN
# 1 euro stukken
munten = bedrag // 100
bedrag %= 100
# 50 cent stukken
munten += bedrag // 50
bedrag %= 50
# 20 cent stukken
munten += bedrag // 20
bedrag %= 20
# 10 cent stukken
munten += bedrag // 10
bedrag %= 10
# 5 cent stukken
munten += bedrag // 5
bedrag %= 5
# 2 cent stukken
munten += bedrag // 2
bedrag %= 2
# 1 cent stukken
munten += bedrag // 1

# aantal munten printen
print(str(origineel_bedrag) + " cent kan je omwisselen in " + str(munten) + " muntstukken")