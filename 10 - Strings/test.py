woord = input("Woord: ")

for i in range(0, len(woord), 2):
    print(woord[i - 1] + " " + str(i))