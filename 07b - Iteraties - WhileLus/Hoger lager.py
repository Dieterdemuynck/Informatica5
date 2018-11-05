# Random functies importeren
import random
random.seed(1)

# Getallen genereren
juist = random.randint(1, 100)
getal = random.randint(1, 100)

# Variabelen
poging, kleinst, grootst = 1, 1, 100

print("[{},{}] --> computer gokt {}".format(kleinst, grootst, getal))  # Eerste gok

# Gegenereerde getal uittesten
while getal != juist:
    if getal < juist:
        kleinst = getal + 1
    elif getal > juist:
        grootst = getal - 1
    poging += 1
    getal = random.randint(kleinst, grootst)
    print("[{},{}] --> computer gokt {}".format(kleinst, grootst, getal))

# Eindbeslissing printen
print("computer had {} pogingen nodig om het getal {} te raden.".format(poging, juist))