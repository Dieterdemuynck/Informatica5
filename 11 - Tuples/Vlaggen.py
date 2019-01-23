def vlag(richting, kleuren):
    if richting == "verticaal":
        sep = " | "
    else:
        sep = "\n-\n"

    string = ""
    for kleur in kleuren:
        string += kleur + sep

    return string[:-3]