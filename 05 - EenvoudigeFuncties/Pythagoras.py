# Inputs
a = float(input("a = "))
b = float(input("b = "))

# Formule
from math import sqrt
c = sqrt(pow(a, 2) + pow(b, 2))

# Printformule
print_formule = "In een rechthoekige driekhoek met rechthoekzijden a = {:.2f} en b = {:.2f} is de schuine zijde {:.2f}"

# Printen
print(print_formule.format(a, b, c))