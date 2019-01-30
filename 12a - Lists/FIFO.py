invoer = input("Geef invoer: ")
queue = []

while invoer != "STOP":

    # Geen ? => aan lijst toevoegen
    if invoer != "?":
        queue.append(invoer)

    # Wel ? => als lijst niet leeg is, print en verwijder het eerste element
    elif len(queue) != 0:
        print(queue[0])
        queue.pop(0)

    # Vraag voor nieuwe invoer
    invoer = input("Geef invoer: ")