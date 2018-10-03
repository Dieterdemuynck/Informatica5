# Indien vader werd opgegeven, print je: Krokodil geeft kind terug.
# Indien krokodil werd opgegeven, print je: Krokodil eet kind op.
# In alle andere geval toon je: Moe van het denken.

naam = input("Wie heeft stalen zenuwen? ")

if naam == "vader":
    boodschap = "Krokodil geeft kind terug"
elif naam == "krokodil":
    boodschap = "Krokodil eet kind op"
else:
    boodschap = "Moe van het denken"

print(boodschap)