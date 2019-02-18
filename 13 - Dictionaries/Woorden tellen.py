def woord_frequentie(text):
    # Alle woorden lowercase maken, punten verwijderen en woorden afzonderen in een lijst
    woorden = text.lower().replace(".", "").split(" ")

    telmachine = {}

    # voor elk woord in de tekst: woord bijtellen
    for woord in woorden:
        if woord in telmachine:
            telmachine[woord] += 1
        else:
            telmachine[woord] = 1

    return telmachine


def woorden_per_frequentie(text):
    # woorden tellen
    aantallen = woord_frequentie(text)

    gesorteerd = {}

    # Keys en values "omwisselen", als value er al in zit: woord in lijst toevoegen
    for key, value in aantallen.items():
        if value in gesorteerd:
            gesorteerd[value].append(key)
        else:
            gesorteerd[value] = [key]

    return gesorteerd


def meest_gebruikte_woorden(text):
    frequentie_woorden = woorden_per_frequentie(text)

    return frequentie_woorden[max(frequentie_woorden)]
