from random import randint
from time import time


def genereer_rij(aantal):
    rij = []
    for i in range(aantal):
        rij.append(randint(0, aantal))
    return rij


def insertion_sort(a):

    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key

    return a


rij_1 = genereer_rij(25000)
rij_2 = rij_1.copy()

# insertion sort
start = time()
insertion_sort(rij_1)
stop = time()
print(stop - start)

# python sort
start = time()
rij_2.sort()
stop = time()
print(stop - start)
