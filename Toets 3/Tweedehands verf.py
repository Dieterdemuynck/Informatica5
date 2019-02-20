def kleur_toevoegen(lijst, kleur):
    if kleur == "rood":
        lijst[0] += 1
    elif kleur == "groen":
        lijst[1] += 1
    elif kleur == "blauw":
        lijst[2] += 1

    return lijst


def is_wit(kleuren):
    wit = False

    if kleuren[0] == kleuren[1] and kleuren[1] == kleuren[2]:
        wit = True

    return wit


def verf_verzamelen(kleuren):
    lijst = [0, 0, 0]
    nummer = 0
    oplossing = None
    wit_mogelijk = False

    # als na een kleur toevoegen wit nog niet mogelijk is, volgend kleur toevoegen als die er is.
    while not wit_mogelijk and nummer < len(kleuren):
        # Kleur toevoegen aan de lijst
        kleur_toevoegen(lijst, kleuren[nummer])
        # Index + 1, wat toevallig ook gelijk is aan het volgnummer van de vorige toegevoegde verf
        nummer += 1

        # Als wit mogelijk is, oplossing veranderen van None naar (nummer, lijst met verf).
        if is_wit(lijst):
            oplossing = (nummer, lijst)
            wit_mogelijk = True

    return oplossing
