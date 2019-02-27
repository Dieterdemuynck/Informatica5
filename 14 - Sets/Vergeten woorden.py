def vergeten_woorden(zin, verplichte_woorden):
    woorden = zin.split(" ")
    gebruikt = 0

    for woord in verplichte_woorden:
        if woord in woorden:
            gebruikt += 1

    vergeten = len(verplichte_woorden) - gebruikt

    return len(verplichte_woorden), vergeten, gebruikt
