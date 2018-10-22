getalnummer = int(input("Hoeveelste getal uit de Fibonacci sequence? "))

getal_1, getal_2, getal_3 = 1, 1, 1

for i in range(3, getalnummer + 1):
    getal_3 = getal_1 + getal_2
    getal_1, getal_2 = getal_2, getal_3

print(getal_3)