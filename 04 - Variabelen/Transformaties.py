# a en b van f(x) en print f(x)
a = 3
b = 4
print("f(x) = 2(x - " + str(a) + ")^2 + " + str(b))

# inputs toevoegen
a += int(input("Horizontale verschuiving van f(x)over hoeveel eenheden? "))
b += int(input("Verticale verschuiving van f(x) over hoeveel eenheden? "))

# g(x) printen
print("g(x) = 2(x - " + str(a) + ")^2 + " + str(b))