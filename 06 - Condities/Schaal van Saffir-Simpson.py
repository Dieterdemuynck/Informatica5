windsnelheid = int(input("Windsnelheid van de orkaan = "))

categorie = 0

if windsnelheid >= 250:
    categorie = 5
elif windsnelheid >= 210:
    categorie = 4
elif windsnelheid >= 178:
    categorie = 3
elif windsnelheid >= 154:
    categorie = 2
elif windsnelheid >= 119:
    categorie = 1

if categorie >= 1:
    print("categorie", categorie)
else:
    print("geen orkaan")