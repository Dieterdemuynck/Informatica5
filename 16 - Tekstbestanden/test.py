names = ["Jan", "Piet", "Joris", "Korneel"]
punten = [7, 9, 8, 10]

data = ""

for i in range(4):
    data += names[i] + " " + str(punten[i]) + "\n"

with open("klas.txt", "w") as file:
    file.write(data)
