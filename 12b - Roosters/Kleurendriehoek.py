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