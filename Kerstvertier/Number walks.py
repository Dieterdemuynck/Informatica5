from math import sin, cos, radians
getal = input("Geef een getal: ")

x_coor = 0
y_coor = 0
for number in getal:
    if number != ".":
        y_walk = sin(radians(int(number) * -36 + 90))
        x_walk = cos(radians(int(number) * -36 + 90))

    x_coor += x_walk
    y_coor += y_walk


print("Number {} walks to position ({:.2f}, {:.2f}).".format(getal, x_coor, y_coor))