kleur_1 = input("Hoed 1: ")
kleur_2 = input("Hoed 2: ")
persoon_omgekeerd = int(input("Persoon die het omgekeerde zegt van wat hij of zij ziet: "))

if kleur_1 == "zwart" and kleur_2 == "zwart":
    if persoon_omgekeerd == 1:
        statering_1 = "wit"
        statering_2 = kleur_1
    else:
        statering_1 = kleur_2
        statering_2 = "wit"
elif kleur_1 == "zwart" and kleur_2 == "wit":
    if persoon_omgekeerd == 1:
        statering_1 = "zwart"
        statering_2 = kleur_1
    else:
        statering_1 = kleur_2
        statering_2 = "wit"
elif kleur_1 == "wit" and kleur_2 == "zwart":
    if persoon_omgekeerd == 1:
        statering_1 = "wit"
        statering_2 = kleur_1
    else:
        statering_1 = kleur_2
        statering_2 = "zwart"
elif kleur_1 == "wit" and kleur_2 == "wit":
    if persoon_omgekeerd == 1:
        statering_1 = "zwart"
        statering_2 = kleur_1
    else:
        statering_1 = kleur_2
        statering_2 = "zwart"

print(statering_1)
print(statering_2)