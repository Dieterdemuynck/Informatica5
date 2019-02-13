def verlaat_ploeg(speler, ploeg, inschrijvingen):
    if speler in inschrijvingen[ploeg]:
        inschrijvingen[ploeg].pop(inschrijvingen[ploeg].index([speler]))

    return inschrijvingen


print(verlaat_ploeg('Tom','Sinbox',{'Sinbox': ['An', 'Tom', 'Griet'], 'Levies': ['Fien'], 'Quist Het': ['Jens', 'Lies', 'Jesse'], 'verKWISting': ['Renzo', 'Jan', 'Annelies']}))