aantal = int(input("Aantal woorden in de zin: "))
zin = ""

for _ in range(aantal):
    woord = input("woord: ")
    zin += woord + " "

print(zin)