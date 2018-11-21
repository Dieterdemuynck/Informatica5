def is_letter(n):
    if ord(n) in range(65, 91) or ord(n) in range(97, 123):
        return True
    return False


def roteer_letter(letter, rotatie):
    if is_letter(letter) and ord(letter) in range(65, 91):
        letter = chr(ord(letter) + rotatie)
        if ord(letter) > 90:
            letter = chr(ord(letter) - 26)
    elif is_letter(letter) and ord(letter) in range(97, 123):
        letter = chr(ord(letter) + rotatie)
        if ord(letter) > 122:
            letter = chr(ord(letter) - 26)
    return letter


def versleutel(tekst, rotatie):
    string = ""
    for letter in tekst:
        string += roteer_letter(letter, rotatie)
    return string