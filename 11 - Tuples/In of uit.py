from math import sqrt


def binnen_of_buiten(middelpunt, cirkelpunt, punt):

    straal = sqrt(pow(middelpunt[0] - cirkelpunt[0], 2) + pow(middelpunt[1] - cirkelpunt[1], 2))
    afstand = sqrt(pow(middelpunt[0] - punt[0], 2) + pow(middelpunt[1] - punt[1], 2))

    if afstand < straal:
        uitkomst = "binnen"
    elif afstand == straal:
        uitkomst = "op"
    else:
        uitkomst = "buiten"

    return uitkomst, round(afstand, 4)