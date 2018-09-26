# Inputs
r = float(input("Afstand satelliet naar middelpunt Aarde: "))
v = float(input("Snelheid satelliet t.o.v. de Aarde: "))

# Constante
u = 398600.4418 * pow(10, 9)

# Formules
from math import pi, sqrt
a = (u * r) / ((2 * u) - r * pow(v, 2)) # in meter
p = 2 * pi * sqrt(pow(a, 3) / u) # in seconden

# Omrekenen
p_minuten = p // 60

p_uren = p_minuten // 60
p_minuten %= 60

p_dagen = p_uren // 24
p_uren %= 24

# Printen
print("grote as:", a, "meter")
print("periode:", p, "seconden")
print("periode:", int(p_dagen), "dagen,", int(p_uren), "uren en", int(p_minuten), "minuten")

# YEET