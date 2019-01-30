def dubbels(list):
    dubbels = []

    # overlopen: als huidig in lijst meer dan 1 => dubbel + als dubbel niet in andere lijst: dubbel toevoegen aan lijst
    for element in list:
        if list.count(element) > 1 and not element in dubbels:
            dubbels.append(element)

    return dubbels