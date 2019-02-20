def fruitstuk_toevoegen(fruitmand, fruitstuk):
    fruitstuk_toegevoegd = False

    for i in range(len(fruitmand)):
        if len(fruitmand[i]) == len(fruitstuk) and not fruitstuk_toegevoegd:
            fruitmand[i] = fruitstuk
            fruitstuk_toegevoegd = True
        elif len(fruitmand[i]) > len(fruitstuk) and not fruitstuk_toegevoegd:
            fruitmand.insert(i, fruitstuk)
            fruitstuk_toegevoegd = True
        elif i == len(fruitmand) - 1 and not fruitstuk_toegevoegd:
            fruitmand.append(fruitstuk)

    return fruitmand


def maak_fruitmand(fruit):
    fruitmand = [fruit[0]]

    for i in range(1, len(fruit)):
        fruitmand = fruitstuk_toevoegen(fruitmand, fruit[i])

    return fruitmand
