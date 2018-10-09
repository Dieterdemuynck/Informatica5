temperatuur = float(input("Temperatuur: "))
lichtkracht = float(input("Lichtkracht: "))

if lichtkracht > 10 ** 4:
    print("superreuzen (a)")
elif lichtkracht > 1000:
    print("superreuzen (b)")
elif lichtkracht > 100:
    if temperatuur > 7500:
        print("hoofdreeks")
    else:
        print("heldere reuzen")
elif lichtkracht > 10:
    if temperatuur > 6000:
        print("hoofdreeks")
    else:
        print("reuzen")
elif lichtkracht > 0.01:
    print("hoofdreeks")
elif lichtkracht > 0.0001:
    if temperatuur > 5000:
        print("witte dwergen")
    else:
        print("hoofdreeks")
else:
    if temperatuur > 3000:
        print("hoofdreeks")
    else:
        print("witte dwergen")