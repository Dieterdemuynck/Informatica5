def is_letter(n):
    if n in "azertyuiopqsdfghjklmwxcvbnAZERTYUIOPQSDFGHJKLMWXCVBN":
        return True
    else:
        return False

def roteer_letter(letter, rotatie):
    if is_letter(letter):
        letter = chr(ord(letter) + rotatie)
        if not is_letter(letter):
            letter = chr(ord(letter) - 26)
    return letter

def versleutel(tekst, rotatie):
    string = ""
    for letter in tekst:
        string += roteer_letter(letter, rotatie)
    return string

print(is_letter("3"))
print(is_letter("A"))
print(roteer_letter("Z", 13))
print(roteer_letter("a", 2))
print(versleutel("zZALLO, HOE gaat HET?", 12))