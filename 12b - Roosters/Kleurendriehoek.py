def volgende_rij(rij):
    volgende_rij = []
    for i in range(len(rij) - 1):
        if rij[i] == rij[i+1]:
            volgende_rij += rij[i]
        elif rij[i] == "G" and rij[i+1] == "Y" or rij[i] == "Y" and rij[i+1] == "G":
            volgende_rij.append("R")
        elif rij[i] == "G" and rij[i+1] == "R" or rij[i] == "R" and rij[i+1] == "G":
            volgende_rij.append("Y")
        elif rij[i] == "Y" and rij[i+1] == "R" or rij[i] == "R" and rij[i+1] == "Y":
            volgende_rij.append("G")

    return volgende_rij


def driehoek(rij):
    driehoek = [rij]
    for i in range(1, len(rij)):
        driehoek.append(volgende_rij(driehoek[i - 1]))

    return driehoek


def kleuren(driehoek):
    g = 0
    y = 0
    r = 0
    for i in range(len(driehoek)):
        for j in range(len(driehoek[i])):
            if driehoek[i][j] == "G":
                g += 1
            elif driehoek[i][j] == "R":
                r += 1
            elif driehoek[i][j] == "Y":
                y += 1

    return g, r, y
