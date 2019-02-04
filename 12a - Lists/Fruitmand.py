def fruitstuk_toevoegen(fruitmand, fruitstuk):
    fruitstuk_toegevoegd = False

    for i in range(len(fruitmand)):
        if len(fruitmand[i]) == len(fruitstuk):
            fruitmand[i] = fruitstuk
        elif len(fruitmand[i]) > len(fruitstuk) and not fruitstuk_toegevoegd:
            fruitmand.insert(i, fruitstuk)
            fruitstuk_toegevoegd = True
        elif i == len(fruitmand) - 1:
            fruitmand.append(fruitstuk)

    return fruitmand


def maak_fruitmand(fruitmand):
    fruitmand_vol = [fruitmand[1]]

    for i in range(1, len(fruitmand)):
        fruitmand_vol = fruitstuk_toevoegen(fruitmand_vol, fruitmand[i])

    return fruitmand_vol


print(maak_fruitmand(['aardbei', 'peer', 'bes']))