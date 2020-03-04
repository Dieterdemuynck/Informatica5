aantal_lijsten = int(input())

for i in range(0, aantal_lijsten):
    aantal_nummers = int(input())

    maximum = int(input())
    minimum = maximum

    for _ in range(1, aantal_nummers):

        volgend = int(input())
        maximum = max(maximum, volgend)
        minimum = min(minimum, volgend)


    print(i + 1, minimum, maximum)