# Input
sol = float(input("Aantal verstreken sol: "))
# 1 sol = 24 uur, 39 minuten, 35.244 seconden

# 24 uur + 39 minuten + 35.244 seconden = 88775.244 seconden
# 1 sol = 88775.244 seconden

totaal_in_seconden = sol * 88775.244
# minuten
minuten = totaal_in_seconden // 60
seconden = totaal_in_seconden % 60
# uren
uren = minuten // 60
minuten %= 60
# dagen
dagen = uren // 24
uren %= 24

# Omzetting naar strings
sol = str(int(sol))
dagen = str(int(dagen))
uren = str(int(uren))
minuten = str(int(minuten))
seconden = str(int(seconden))

# print
print(sol, "sol =", dagen, "dagen,", uren, "uren,", minuten, "minuten en", seconden, "seconden")