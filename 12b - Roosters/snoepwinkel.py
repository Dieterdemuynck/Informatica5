from operator import itemgetter


def bereken_prijs(artikelen):
    prijs = 0
    for artikel in artikelen:
        prijs += artikel[1]

    return prijs


def winkelbriefje(artikelen):
    lijst = []
    for artikel in artikelen:
        lijst.append(artikel[0])

    return lijst


def sorteer(artikelen):
    artikelen.sort(key=itemgetter(1))

    return artikelen
