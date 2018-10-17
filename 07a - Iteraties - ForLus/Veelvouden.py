getal = int(input("Geef een getal: "))

som = 0
for getal in range(getal, 101, getal):
    som += getal

print(som)