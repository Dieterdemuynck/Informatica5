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
    aantallen = woord_frequentie(text)
