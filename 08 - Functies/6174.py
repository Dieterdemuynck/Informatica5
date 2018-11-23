def splits(getal):
    cijfer1, cijfer2, cijfer3, cijfer4 = -1, -1, -1, -1
    for i in str(getal):
        if cijfer1 < 0:
            cijfer1 = int(str(i))
        elif cijfer2 < 0:
            cijfer2 = int(i)
        elif cijfer3 < 0:
            cijfer3 = int(i)
        else:
            cijfer4 = int(i)
    return cijfer1, cijfer2, cijfer3, cijfer4


def oplopende_cijfers(a, b, c, d):
    cijfer1 = min(a, b, c, d)
    cijfer2 = min(max(a, b), max(c, d), max(a, d), max(b, c), max(a, c), max(b, d))
    cijfer3 = max(min(a, b), min(c, d), min(a, d), min(b, c), min(a, c), min(b, d))
    cijfer4 = max(a, b, c, d)

    return cijfer1, cijfer2, cijfer3, cijfer4


def op_af_getallen(a, b, c, d):
    cijfer_oplopend = str(a) + str(b) + str(c) + str(d)
    cijfer_aflopend = str(d) + str(c) + str(b) + str(a)
    return cijfer_oplopend, cijfer_aflopend


def verschil(cijfer_aflopend, cijfer_oplopend):
    uitkomst = int(cijfer_aflopend) - int(cijfer_oplopend)
    return str(uitkomst)


def kaprekar(getal):
    string = ""
    while getal != 6174:
        opgesplitst1, opgesplitst2, opgesplitst3, opgesplitst4 = splits(getal)
        cijfer1, cijfer2, cijfer3, cijfer4 = oplopende_cijfers(opgesplitst1, opgesplitst2, opgesplitst3, opgesplitst4)
        cijfer_oplopend, cijfer_aflopend = op_af_getallen(cijfer1, cijfer2, cijfer3, cijfer4)
        getal = int(verschil(cijfer_aflopend, cijfer_oplopend))
        string += "\n{} - {} = {}".format(cijfer_aflopend, cijfer_oplopend, getal)

    return string


print(kaprekar(1234))