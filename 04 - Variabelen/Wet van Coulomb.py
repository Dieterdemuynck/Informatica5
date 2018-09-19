# Constante k in vacuüm
k = 8.99 * (10 ** 9)

# Puntladingen
q_een = 1.0 * (10 ** -6)
q_twee = 2.0 * (10 ** -6)

# Input straal in cm, omgezet naar m
r = float(input("Straal tussen ladingen (in cm): ")) * (10 ** -2)

# Coulombkracht berekenen en printen
kracht_Coulomb = k * ((q_een * q_twee) / (r ** 2))
print(kracht_Coulomb)