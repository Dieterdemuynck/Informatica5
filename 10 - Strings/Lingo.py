def hint(gok, juist):
    hint = ""
    for i in range(0, 5):
        if gok[i] == juist[i]:
            letter = gok[i].upper()
        elif gok[i] in juist:
            letter = gok[i]
        else:
            letter = "."
        hint += letter

    return hint