# Constanten
molaire_massa_zwavel = 32.06
avogadro_constante = 6.020 * (10 ** 23)

# Input
mol_zwavel = float(input("Aantal mol zwavel deeltjes: "))

# Berekeningen + Printen
massa_zwavel = molaire_massa_zwavel * mol_zwavel
print(massa_zwavel)

deeltjes_zwavel = avogadro_constante * mol_zwavel
print(deeltjes_zwavel)