bod = float(input('startprijs: '))
doorgedraaid = float(input('doorgedraaid onder: '))
akkoord = int(input('€{:.2f}? (0/1): '.format(bod)))

# Zolang (geen bod) AND (iets kan van de prijs weg)
while (not akkoord) and (bod >= doorgedraaid + 0.01):
    # Iets van de prijs
    bod -= 0.01

    # Iemand geïnteresseerd?
    akkoord = int(input('€{:.2f}? (0/1): '.format(bod)))


if akkoord:
    print('verkocht aan {:.2f}'.format(bod))
else:
    print('doorgedraaid')