# Inputs
b = float(input("Breedte: ")) / 100
l = float(input("Lengte: ")) / 100
c = float(input("Graan per hectare in m^3: "))
r = float(input("Straal van de silo: "))
h = float(input("Hoogte van de silo: "))

# pi
pi = 3.1415926535897931

# Berekening silo's
aantal_silos = int((b * l * c) / (pi * (r ** 2) * h) + 0.9999999999999999)

# Berekening hoogte
hoogte_silo = (b * l * c) / (pi * (r ** 2) * h) * h % h

# Print
print(str(aantal_silos))
print(str(hoogte_silo))