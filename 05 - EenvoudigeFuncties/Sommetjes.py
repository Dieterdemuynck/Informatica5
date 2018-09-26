# Bijkomende getallen en bewerkingen
i = 0
formule_print = "{:>6d} + {:<6d} = {:<6d}"

# Inputs
a = int(input("Getal 1, van 0 tot 20: "))
b = int(input("Getal 2, van 0 tot 20: "))

# Formule
c = a + b

# Formats en printen
print(formule_print.format(a * (10 ** i), b * (10 ** i), c * (10 ** i)))
i += 1
print(formule_print.format(a * (10 ** i), b * (10 ** i), c * (10 ** i)))
i += 1
print(formule_print.format(a * (10 ** i), b * (10 ** i), c * (10 ** i)))
i += 1
print(formule_print.format(a * (10 ** i), b * (10 ** i), c * (10 ** i)))
i += 1
print(formule_print.format(a * (10 ** i), b * (10 ** i), c * (10 ** i)))