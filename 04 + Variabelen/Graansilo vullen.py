# Inputs
b = float(input("Breedte: "))
l = float(input("Lengte: "))
c = float(input("Graan per hectare in m^3: "))
r = float(input("Straal van de silo: "))
h = float(input("Hoogte van de silo: "))

# pi
pi = 3.1415926535897931

# Fractions
teller = (b * l * c)
noemer = (pi * (r ** 2) * h) * 10000

# Berekening silo's
aantal_silos = int(teller / noemer + 0.99999999999)

# Berekening hoogte
hoogte_silo = (teller / (pi * (r ** 2) * 10000)) % h

# Print
print(str(aantal_silos))
print(str(hoogte_silo))