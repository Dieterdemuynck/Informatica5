def splits(getal):
    cijfer1 = int(str(getal)[0])
    cijfer2 = int(str(getal)[1])
    cijfer3 = int(str(getal)[2])
    cijfer4 = int(str(getal)[3])

    return cijfer1, cijfer2, cijfer3, cijfer4


def oplopende_cijfers(a, b, c, d):
    cijfer1 = min(a, b, c, d)
    cijfer2 = min(max(a, b), max(c, d), max(a, d), max(b, c), max(a, c), max(b, d))
    cijfer3 = max(min(a, b), min(c, d), min(a, d), min(b, c), min(a, c), min(b, d))
    cijfer4 = max(a, b, c, d)

    # kandidaat1 = max(min(a, b), min(a, c), min(b, c))
    # kandidaat2 = a + b + c + d - cijfer1 - kandidaat1 - cijfer4

    # cijfer2 = min(kandidaat1, kandidaat2)
    # cijfer3 = max(kandidaat1, kandidaat2)

    return cijfer1, cijfer2, cijfer3, cijfer4


def op_af_getallen(a, b, c, d):
    cijfer_oplopend = str(a) + str(b) + str(c) + str(d)
    cijfer_aflopend = str(d) + str(c) + str(b) + str(a) # cijfer_aflopend = cijfer_oplopend[::-1]
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
        string += "{} - {} = {}\n".format(cijfer_aflopend, cijfer_oplopend, getal)

    return string[:-1]


print(kaprekar(1234))