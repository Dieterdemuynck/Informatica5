aanval_1 = int(input("Dobbelsteen 1 van de aanvaller: "))
aanval_2 = int(input("Dobbelsteen 2 van de aanvaller: "))
aanval_3 = int(input("Dobbelsteen 3 van de aanvaller: "))
verdediging_1 = int(input("Dobbelsteen 1 van de verdediger: "))
verdediging_2 = int(input("Dobbelsteen 2 van de verdediger: "))

# Aanvallen sorteren
if aanval_3 > aanval_2:
    aanval_3, aanval_2 = aanval_2, aanval_3
if aanval_2 > aanval_1:
    aanval_2, aanval_1 = aanval_1, aanval_2
if aanval_3 > aanval_2:
    aanval_3, aanval_2 = aanval_2, aanval_3

# Verdediging sorteren
if verdediging_2 > verdediging_1:
    verdediging_1, verdediging_2 = verdediging_2, verdediging_1

# Uitkomsten
if aanval_1 > verdediging_1 and aanval_2 > verdediging_2:
    print("aanvaller verliest 0 legers, verdediger verliest 2 legers")
elif aanval_1 <= verdediging_1 and aanval_2 <= verdediging_2:
    print("aanvaller verliest 2 legers, verdediger verliest 0 legers")
else:
    print("aanvaller verliest 1 leger, verdediger verliest 1 leger")