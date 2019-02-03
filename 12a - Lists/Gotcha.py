def ik_heb_gemoord(opdrachtenlijst, moordenaar):
    m_index = opdrachtenlijst.index(moordenaar)

    # moordenaar + 1 verwijderen
    if m_index + 1 > len(opdrachtenlijst) - 1 and len(opdrachtenlijst) != 1:
        opdrachtenlijst.pop(0)
    elif len(opdrachtenlijst) != 1:
        opdrachtenlijst.pop(m_index + 1)

    # moordenaar + 2 = volgende opdracht
    if m_index + 1 > len(opdrachtenlijst) - 1 or len(opdrachtenlijst) == 1:
        volgende_opdracht = opdrachtenlijst[0]
    else:
        volgende_opdracht = opdrachtenlijst[m_index + 1]

    return volgende_opdracht, opdrachtenlijst


def ik_ben_vermoord(opdrachtenlijst, slachtoffer):
    s_index = opdrachtenlijst.index(slachtoffer)

    # volgende opdracht = slachtoffer + 1
    if len(opdrachtenlijst) < s_index + 2 or len(opdrachtenlijst) == 1:
        volgende_opdracht = opdrachtenlijst[0]
    else:
        volgende_opdracht = opdrachtenlijst[s_index + 1]

    # slachtoffer verwijderen
    if len(opdrachtenlijst) != 1:
        opdrachtenlijst.pop(s_index)

    return volgende_opdracht, opdrachtenlijst
