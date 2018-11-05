getal = int(input("Geef me eens jouw mooi getalletje: "))
i = 2
priemgetal = 1

if getal < i:
    priemgetal = 0
elif getal == i:
    priemgetal = 1
elif getal % i == 0:
    priemgetal = 0

while getal % i != 0 and i - 1 < getal:
    i += 1
    if getal == i:
        priemgetal = 1
    elif getal % i == 0:
        priemgetal = 0
    else:
        priemgetal = 1

if priemgetal:
    print("{} is een priemgetal".format(getal))
else:
    print("{} is geen priemgetal".format(getal))