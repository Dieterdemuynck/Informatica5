getal = int(input("Geef me eens jouw mooi getalletje: "))
i = 2
priemgetal = 1

if getal < 2 or getal % i == 0:
    priemgetal = 0

while getal % i != 0 and i < getal - 1:
    i += 1
    if getal % i == 0:
        priemgetal = 0

if priemgetal:
    print("{} is een priemgetal".format(getal))
else:
    print("{} is geen priemgetal".format(getal))