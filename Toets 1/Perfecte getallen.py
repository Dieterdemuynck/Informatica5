getal = int(input("Een getal: "))

delersom = 0
delers = ""
for i in range(1, (getal // 2) + 1):
    if getal % i == 0:
        delers += str(i) + " "
        delersom += i  # De som van de delers moet gelijk zijn aan het oorspronkelijk getal

if delersom == getal:  # Zie vorige comment (line 8)
    print("{} is een perfect getal en de delers zijn {}".format(getal, delers))
else:
    print("{} is geen perfect getal".format(getal))