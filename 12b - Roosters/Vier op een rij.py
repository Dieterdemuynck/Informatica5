def printbaar_rek(rek):
    # Bovenste rij eerst plaatsen:
    rek.reverse()

    string = ""
    for rij in rek:
        string += "".join(rij) + "\n"

    return string[:-1]


def speel(kleur, kolom_index, rek):
    placed = False
    i = -1
    while not placed:
        # Als geen 0: ofwel geplaatst ofwel geen plaats: stop de loop
        if rek[i][kolom_index] != "O":
            placed = True
        # Als i minimaal: plaats, stop de loop
        elif i == -1 * len(rek):
            rek[i][kolom_index] = kleur
            placed = True
        # Als op aangeduide plaats 0 staat, en rij eronder niet: plaats, stop de loop.
        elif rek[i][kolom_index] == "O" and rek[i-1][kolom_index] != "O":
            rek[i][kolom_index] = kleur
            placed = True

        i -= 1

    return rek
