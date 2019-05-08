def vriend_of_kennis(kennissen, persoon_a, persoon_b):
    if persoon_b in kennissen[persoon_a] and persoon_a in kennissen[persoon_b]:
        message = persoon_a + " en " + persoon_b + " zijn vrienden"
    elif persoon_b in kennissen[persoon_a]:
        message = persoon_a + " kent " + persoon_b
    elif persoon_a in kennissen[persoon_b]:
        message = persoon_b + " kent " + persoon_a
    else:
        message = persoon_a + " en " + persoon_b + " kennen elkaar niet"

    return message


def unieke_kennissen(kennissen, persoon_a, persoon_b):
    uniek = set()

    for kennis in kennissen[persoon_a]:
        if kennis not in kennissen[persoon_b] and kennis != persoon_b:
            uniek.add(kennis)

    for kennis in kennissen[persoon_b]:
        if kennis not in kennissen[persoon_a] and kennis != persoon_a:
            uniek.add(kennis)

    return uniek


def bekendheid(kennissen):
    bekendheden = {}

    for persoon in kennissen.keys():
        bekendheden[persoon] = 0

        for personen in kennissen.values():
            if persoon in personen:
                bekendheden[persoon] += 1

    return bekendheden


def meest_gekende(bekendheden):
    bekendst = []

    highest = 0

    for persoon, gekend in bekendheden.items():
        if gekend > highest:
            bekendst = [persoon]
            highest = gekend
        elif gekend == highest:
            bekendst.append(persoon)

    return bekendst
