def positie_laagste_ascii(string):
    character_min = ord(string[0])
    for character in string:
        character_min = min(character_min, ord(character))

    return string.find(chr(character_min))


def sorteer(string):
    string_sorted = ""
    for _ in string:
        string_sorted += string[positie_laagste_ascii(string)]
        string = string[:positie_laagste_ascii(string)] + string[positie_laagste_ascii(string)+1:]

    return string_sorted


def is_alfabetisch(string):
    if string == sorteer(string):
        return True
    else:
        return False