def hoogtemeters(list):
    hoogtemeters = []

    for i in range(1, len(list)):
        verschil = list[i] - list[i-1]
        hoogtemeters.append(verschil)

    return hoogtemeters


def dalen_en_stijgen(hoogtemeters):
    gedaalde_meters = 0
    gestegen_meters = 0

    for i in hoogtemeters:
        if i < 0:
            gedaalde_meters -= i
        else:
            gestegen_meters += i

    return gedaalde_meters, gestegen_meters
