def behoort_tot_taal(woord, taal):
    in_taal = True

    for letter in woord:
        if letter not in taal and letter != " ":
            in_taal = False

    return in_taal


def is_onleesbaar(woord, taal):
    onleesbaar = True

    for letter in woord:
        if letter in taal:
            onleesbaar = False

    return onleesbaar


def perfect_woord(woord, taal):
    perfect = False

    for letter in woord:
        if letter in taal:
            taal.discard(letter)

    if taal == set():
        perfect = True

    return perfect
