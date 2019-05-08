def lees_bestand(txt):
    filelist = []

    with open(txt, "r") as file:
        linelist = file.readline().split(";")
        filelist.append(linelist)

    return filelist


print(lees_bestand("Apple.txt"))