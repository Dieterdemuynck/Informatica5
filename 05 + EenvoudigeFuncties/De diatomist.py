# Inputs
r_klein = float(input("Straal kleine cirkel: "))
r_groot = float(input("Straal grote cirkel: "))

# Formule
n = int(0.83 * (pow(r_groot, 2) / pow(r_klein, 2)) - 1.9)
opp_percentage = pow(r_klein, 2) * n / pow(r_groot, 2) * 100

# Printformulering
print_formule = "{:d} kleine cirkels bedekken {:.2f}% van de grote cirkel"

# Print
print(print_formule.format(n, opp_percentage))