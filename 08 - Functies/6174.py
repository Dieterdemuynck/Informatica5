def splits(getal):
    cijfer1, cijfer2, cijfer3, cijfer4 = -1, -1, -1, -1
    for i in str(getal):
        if cijfer1 < 0:
            cijfer1 = int(i)
        elif cijfer2 < 0:
            cijfer2 = int(i)
        elif cijfer3 < 0:
            cijfer3 = int(i)
        else:
            cijfer4 = int(i)
    return cijfer1, cijfer2, cijfer3, cijfer4