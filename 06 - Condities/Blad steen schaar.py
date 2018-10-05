hand_1 = input("Hand van speler 1? ")
hand_2 = input("Hand van speler 2? ")

if hand_1 == hand_2:
    uitkomst = "onbeslist"
elif (hand_1 == "blad" and hand_2 == "steen") or (hand_1 == "steen" and hand_2 == "schaar") or (hand_1 == "schaar" and hand_2 == "blad"):
    uitkomst = "speler 1 wint"
else:
    uitkomst = "speler 2 wint"

print(uitkomst)