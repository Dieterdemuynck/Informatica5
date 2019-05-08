from random import randint

number = randint(0, 100)

cheats_answer = input("Hello! Would you like to enter a cheatcode? \n")
if cheats_answer == "Yes" or cheats_answer == "yes" or cheats_answer == "y":
    password = input("Enter the cheatcode: \n")

guess = int(input("Guess the number: \n"))
tries = 1

while guess != number:
    if guess > number:
        message = "Guess lower...\n"
    else:
        message = "Guess higher...\n"

    guess = int(input(message))
    tries += 1

print("Congratulations! The number was indeed", number, ".")
print("It took you", tries, "tries to get it.")
if tries > 10:
    print("That could be better...")
elif tries == 10:
    print("That's a decent job.")
else:
    print("That's a good job!")