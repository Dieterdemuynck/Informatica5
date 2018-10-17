aantal = int(input("Aantal getallen: "))

maximum = int(input("Eerste getal: "))
som = maximum

for aantal in range(2, (aantal + 1)):

    getal = int(input("Volgend getal: "))
    maximum = max(getal, maximum)

    som += getal

gemiddelde = round((som / aantal), 2)
print("Het grootste getal is {} en het gemiddelde is {}".format(maximum, gemiddelde))