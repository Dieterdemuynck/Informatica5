def boot_overlappend(boot, boten):
    overlappend = False
    for vak in boot:
        if vak in boten:
            overlappend = True

    return overlappend


def boot_toevoegen(boot, boten):
    if not boot_overlappend(boot, boten):
        boten.update(boot)

    return boten


def vuur(schot, boten):
    raak = False
    if schot in boten:
        raak = True

    boten.discard(schot)

    return raak, boten
