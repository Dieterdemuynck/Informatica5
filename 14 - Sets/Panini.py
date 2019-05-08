def verzamel(new, verzameld, dubbels):
    dubbels_2 = {}

    for key, value in dubbels.items():
        dubbels_2[key] = value

    if new not in verzameld:
        verzameld.add(new)

    else:
        for amount in dubbels.keys():
            if new in dubbels[amount] and (amount + 1) in dubbels:
                dubbels_2[amount].discard(new)
                dubbels_2[amount + 1].add(new)
            elif new in dubbels[amount]:
                dubbels_2[amount].discard(new)
                dubbels_2[amount + 1] = set([new])

            if dubbels_2[amount] == set():
                dubbels_2.pop(amount)

        if dubbels == dubbels_2 and 1 in dubbels:
            dubbels_2[1].add(new)
        elif dubbels == dubbels_2:
            dubbels_2[1] = set([new])

    return verzameld, dubbels_2
