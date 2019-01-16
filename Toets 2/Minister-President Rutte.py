def tel_woorden(zin):
    woorden = 0

    for char in zin:
        if char == " " or char == ".":
            woorden += 1

    return woorden


def langste_zin(text):
    zin = ""
    woorden = 0

    for i in range(len(text)):
        if text[i] != "." and text[i-1] != ".":
            zin += text[i]
        elif text[i] == ".":
            zin += text[i]
            woorden = max(woorden, tel_woorden(zin))
            zin = ""

    return woorden