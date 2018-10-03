trek_hendel = input("Trek aan de hendel van de wissel? ")
duw_man = input("Man van de brug duwen? ")

doden = 0

if trek_hendel == "ja":
    doden += 1

if duw_man == "ja":
    doden += 1

if duw_man == "nee" and trek_hendel == "nee":
    doden = 5

print(doden)