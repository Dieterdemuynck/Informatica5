# Idea: Make a tiny RPG-game through python.
# Images are not necessary, therefor try to make it through text only.

### POINT SYSTEM ###
# HP: Health Points of a character.
# MP: Magic Points (used for spells).
# LP: Luck Points, these will determine your "luck" with random-chance-encounters and looting chests, etc.

### EXTRA IDEAS ###
# Items: You can find items such as weapons, scrolls, armor, etc in chests or from loot drops, for use in combat.
# LV: Level of a character. These determine the strength of someone's attacks, defense, etc.

### GENERAL GAMEPLAY ###
# Still up for decision:
#   Pick a "class" and a number of monsters to fight
#       The player gets his stats through his class, can upgrade a little between each fight.

from random import randint, random

line = "--------------------------------------------------------------------------------------------------------------"
### CHARACTER ###
character = input("What class would you like to be? Choose between: Warrior, Mage, Rogue:  ")

character_decided = False
while not character_decided:
    if character == "Mage" or character == "mage":
        current_char = "Mage"
        character_decided = True
    elif character == "Warrior" or character == "warrior":
        current_char = "Warrior"
        character_decided = True
    elif character == "Rogue" or character == "rogue":
        current_char = "Rogue"
        character_decided = True
    else:
        character = input("That was not a valid class. Please choose between Mage, Warrior or Rogue:  ")

print("\nYou chose '{}'. \n{}\n".format(current_char, line))

stats_answer = input("Would you like to see your current statistics? (Yes/No)  ")