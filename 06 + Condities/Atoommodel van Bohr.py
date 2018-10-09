# "De M-schil is de buitenste schil van een stabiel atoom met 11 elektronen."

e = int(input("Aantal elektronen: "))

if e > 124:
    schil = "Q"
elif e > 92:
    schil = "P"
elif e > 60:
    schil = "O"
elif e > 28:
    schil = "N"
elif e > 10:
    schil = "M"
elif e > 2:
    schil = "L"
else:
    schil = "K"

print("De " + schil + "-schil is de buitenste schil van een stabiel atoom met", e, "elektronen.")