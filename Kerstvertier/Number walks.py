from math import sin, cos
getal = input("Geef een getal: ")

for number in getal:
    if number == ".":
        None
    else:
        x_coor = sin(int(number) * 36)
        y_coor = cos(int(number) * 36)

print("Number {} walks to position ({}, {}).".format(getal, x_coor, y_coor))