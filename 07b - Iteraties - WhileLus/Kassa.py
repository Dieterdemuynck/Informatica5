prijs = float(input("Prijs volgend product (0 als geen): "))
som = 0

while prijs > 0:
    som += prijs
    prijs = float(input("Prijs volgend product (0 als geen): "))

print("De totale prijs is € {:.2f}".format(som))