aantal = int(input("Aantal getallen: "))

maximum = -100
som = 0

for aantal in range(1, (aantal + 1)):

    getal = int(input("Getal: "))
    maximum = max(getal, maximum)

    som += getal
gemiddelde = round((som / aantal), 2)
print("Het grootste getal is {} en het gemiddelde is {}".format(maximum, gemiddelde))