def verlaat_ploeg(speler, ploeg, inschrijvingen):
    inschrijvingen[ploeg].remove(speler)

    if inschrijvingen[ploeg] == []:
        inschrijvingen.pop(ploeg)

    return inschrijvingen


def vervoegt_ploeg(speler, ploeg, inschrijvingen):
    if ploeg in inschrijvingen:
        inschrijvingen[ploeg].append(speler)
    else:
        inschrijvingen[ploeg] = [speler]

    return inschrijvingen
