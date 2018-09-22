# Inputs
t = int(input("Aantal nanoseconden: ")) * (10 ** -9)

# Constanten
c = 299792458
n = 1.000277

# Berekening
d = (c * t) / (n * 2)

# Printen
print(str(d), "meter")