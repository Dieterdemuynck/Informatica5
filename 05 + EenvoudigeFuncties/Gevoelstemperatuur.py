# Inputs
t = float(input("De luchttemperatuur T in °C: "))
w = float(input("De windsnelheid W in km/u: "))

# Formule
temperatuur_gevoel = 13.12 + 0.6215 * t + (0.3965 * t - 11.37) * pow(w, 0.16)

# Printen
print(temperatuur_gevoel)