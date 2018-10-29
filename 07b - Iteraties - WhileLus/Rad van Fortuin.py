woord = input("verborgen woord: ")
geldbedrag = int(input("Gedraaide geldbedrag: "))

letter = input("Geef een letter: ")
gebruikt = ""
som = 0

while letter in woord and not letter in gebruikt:
    som += geldbedrag
    gebruikt += letter
    letter = input("Geef een letter: ")

print(som)