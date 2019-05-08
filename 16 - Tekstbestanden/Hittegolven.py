def bepaal_hittegolven(textfile):
    hittegolf, hittegolf_warmst = [], []
    aantal_hg, aantal_dg = 0, 0
    dag = 0

    with open(textfile, "r") as temps:
        templist = temps.readline().split()

        while templist != []:
            # Lees nummers in lijn
            for number in templist:
                if number != "":
                    dag += 1
                    # Test of temperatuur in hittegolf zit
                    if int(number) >= 30:
                        hittegolf.append(number)
                        hittegolf_warmst.append(number)
                    if int(number) >= 25:
                        hittegolf.append(number)

                    # Zoniet: test of er een hittegolf geweest is
                    else:
                        if len(hittegolf) >= 5 and len(hittegolf_warmst) >= 3:
                            aantal_hg += 1
                        hittegolf, hittegolf_warmst = [], []

            # Lees nieuwe lijn
            print(templist)
            templist = temps.readline().split()

    return aantal_hg


print(bepaal_hittegolven("temperaturen.txt"))