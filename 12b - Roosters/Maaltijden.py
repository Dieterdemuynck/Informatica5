def dagprijs(maaltijden):
    totale_prijs = 0
    for i in range(1, len(maaltijden), 2):
        if maaltijden[i-1] == "middagmaal":
            totale_prijs += maaltijden[i] * 5.3
        elif maaltijden[i-1] == "soep":
            totale_prijs += maaltijden[i] * 1.7
        elif maaltijden[i - 1] == "vieruurtje":
            totale_prijs += maaltijden[i] * 2.3

    return totale_prijs


def weekprijs(maaltijden_week):
    weekprijs = 0
    for maaltijden_dag in maaltijden_week:
        weekprijs += dagprijs(maaltijden_dag)

    return weekprijs
