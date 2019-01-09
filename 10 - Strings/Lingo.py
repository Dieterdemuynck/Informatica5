def hint(gok, juist):
    hint = ""
    for i in range(0, len(gok)):
        if gok[i] == juist[i]:
            letter = gok[i].upper()
        elif gok[i] in juist:
            letter = gok[i]
        else:
            letter = "."
        hint += letter

    return hint