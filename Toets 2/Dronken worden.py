def dronken_voeren(woord):
    dronken_woord = woord[0]

    for i in range(1, len(woord)):
        if i % 2 == 0:
            letter = woord[i].upper()
        elif i % 2 != 0 and dronken_woord[-1] in "AEOUI":
            letter = woord[i].upper()
        else:
            letter = woord[i].lower()

        dronken_woord += letter

    return dronken_woord