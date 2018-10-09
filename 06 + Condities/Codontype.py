codon = input("Codon: ")

if len(codon) != 3:
    output = "ongeldig"
elif codon == "AUG":
    output = "start"
elif codon == "UAG" or codon == "UGA" or codon == "UAA":
    output = "stop"
else:
    output = "gewoon"

print("Het codon", codon, "is een", output, "codon."