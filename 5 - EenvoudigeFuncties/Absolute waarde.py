# Inputs
x = float(input("Getal 1: "))
y = float(input("Getal 2: "))

# Berekeningen
l_l = abs(abs(x) - abs(y))
r_l = abs(x - y)

# Printen
print("{:.4f}".format(l_l), "\N{LESS-THAN OR EQUAL TO}", "{:.4f}".format(r_l))