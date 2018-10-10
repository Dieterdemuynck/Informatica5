lengte = float(input("Lengte van beide even lange personen: "))
naam_1 = input("Naam van de eerste persoon: ")
gewicht_1 = float(input("Gewicht persoon 1: "))
naam_2 = input("Naam van de tweeder persoon: ")
gewicht_2 = float(input("Gewicht persoon 2: "))

bmi_1 = gewicht_1 / pow(lengte, 2)
bmi_2 = gewicht_2 / pow(lengte, 2)

bmi = max(bmi_1, bmi_2)
if bmi_1 == bmi:
    naam = naam_1
else:
    naam = naam_2
if gewicht_1 == gewicht_2:
    naam = naam_2

if bmi >= 30:
    message = naam + " heeft het hoogste BMI ({:.2f}) en is obees.".format(bmi)
elif bmi >= 25:
    message = naam + " heeft het hoogste BMI ({:.2f}) en heeft overgewicht.".format(bmi)
elif bmi >= 18.5:
    message = naam + " heeft het hoogste BMI ({:.2f}) en heeft een gezond gewicht.".format(bmi)
else:
    message = naam + " heeft het hoogste BMI ({:.2f}) en heeft ondergewicht.".format(bmi)
print(message)