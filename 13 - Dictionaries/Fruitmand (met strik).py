def fruitmand_maken(fruit):
    fruitmand = {}

    for i in range(len(fruit)):
        fruitmand[len(fruit[i])] = fruit[i]

    return fruitmand


def fruitmand_inpakken(fruitstukken):
    fruitmand = []

    while len(fruitstukken) != 0:
        fruitmand.append(fruitstukken[min(fruitstukken)])
        fruitstukken.pop(min(fruitstukken))

    return fruitmand
