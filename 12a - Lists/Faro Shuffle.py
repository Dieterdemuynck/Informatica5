def nieuw_kaartspel(kleuren, waarden):
    lijst = []
    for kleur_i in range(len(kleuren)):
        for waarde_i in range(len(waarden)):
            lijst.append(kleuren[kleur_i] + str(waarden[waarde_i]))

    return lijst


def splits_kaartspel(lijst):
    splits_1 = lijst[:(len(lijst)//2)]
    splits_2 = lijst[len(lijst)//2:]

    return splits_1, splits_2


def faro_shuffle(list_0, list_1):
    shuffle = []

    if len(list_1) > len(list_0):
        for i in range(len(list_0)):
            shuffle.append(list_0[i])
            shuffle.append(list_1[i])
        shuffle.append(list_1[-1])
    else:
        for i in range(len(list_0)):
            shuffle.append(list_0[i])
            shuffle.append(list_1[i])

    return shuffle
