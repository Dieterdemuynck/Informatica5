from random import randint

number = randint(0, 100)

cheats_answer = input("Hello! Would you like to enter a cheatcode? \n")
if cheats_answer.lower() == "yes" or cheats_answer.lower() == "y":
    password = input("Enter the cheatcode: \n")

    if password.lower() == "hayasaka ftw":
        print("The number you're looking for is", number, ", your majesty")
    elif password.lower() == "raphtalia":
        range_1 = number - randint(0, 20)
        range_2 = number + randint(0, 20)
        print("Your number is somewhere between", range_1, "and", range_2, ".")
    else:
        print("that wasn't a correct cheatcode. Try again next game.")


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

if tries == 1:
    print("It took you", tries, "try to get it.\nThat's amazing! Lucky you!")
else:
    print("It took you", tries, "tries to get it.")
    if tries > 10:
        print("That could be better...")
    elif tries == 10:
        print("That's a decent job.")
    else:
        print("That's a good job!")