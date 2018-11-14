landsnelheid = int(input("Geef de gewenste snelheid om te landen: "))
snelheid = int(input("Geef de huidige snelheid: "))

remmen = 0
while snelheid > landsnelheid:
    snelheid *= 0.7 # Oftewel - 3/10 van de oorspronkelijke snelheid
    remmen += 1

print("na {:d} rembewegingen is de snelheid {:.2f}".format(remmen, snelheid))