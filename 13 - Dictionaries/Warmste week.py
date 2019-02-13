def gift_inschrijven(gift, klassen):
    if gift[0] in klassen:
        klassen[gift[0]] += gift[1]
    else:
        klassen[gift[0]] = gift[1]

    return klassen
