hand_1 = input("Hand van speler 1? ")
hand_2 = input("Hand van speler 2? ")

blad_v_steen = hand_1 == "blad" and hand_2 == "steen"
steen_v_schaar = hand_1 == "steen" and hand_2 == "schaar"
schaar_v_blad = hand_1 == "schaar" and hand_2 == "blad"

if hand_1 == hand_2:
    uitkomst = "onbeslist"
elif (blad_v_steen == True) or (steen_v_schaar == True) or (schaar_v_blad == True):
    uitkomst = "speler 1 wint"
else:
    uitkomst = "speler 2 wint"

print(uitkomst)