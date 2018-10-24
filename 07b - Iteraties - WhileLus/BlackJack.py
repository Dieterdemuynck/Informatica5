# When Jack Black plays BlackJack does Jack Black become Black Jack?
# I have no idea what I just said, but it sounds funny.

kaart = int(input("Kaartwaarde: "))
som = kaart

while kaart > 0 and som < 21:
    kaart = int(input("Kaartwaarde: "))
    som += kaart

if som > 21:
    print("Verbrand ({})".format(som))
elif som == 21:
    print("Gewonnen!")
else:
    print("Voorzichtig gespeeld ({})".format(som))