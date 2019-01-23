def geldige_zet(zet):
    pion_ind = "KDTLP"
    letter_ind = "abcdefgh"
    cijfer_ind =

    if len(zet) == 2 and zet[0] in letter_ind and zet[1] in cijfer_ind:
        juistheid = True
    elif len(zet) == 3 and zet[0] in pion_ind and zet[1] in letter_ind and zet[2] in cijfer_ind:
        juistheid = True
    else:
        juistheid = False

    return juistheid

print(geldige_zet("De5"))