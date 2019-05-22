from random import randint
from time import time
import matplotlib.pyplot as plt


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
            i -= 1
        a[i + 1] = key

    return a


def bubble_sort(rij):
    for i in range(0, len(rij) - 1):
        for j in range(len(rij) - 1, i, -1):
            if rij[j] < rij[j - 1]:
                rij[j], rij[j - 1] = rij[j - 1], rij[j]

    return rij

n, t_insertion, t_python, t_bubble = [], [], [], []

i = 10

while i < 1000:

    rij_1 = genereer_rij(i)
    rij_2 = rij_1.copy()
    rij_3 = rij_1.copy()

    # insertion sort
    start = time()
    insertion_sort(rij_1)
    stop = time()

    t_insertion.append(stop - start)

    # python sort
    start = time()
    rij_2.sort()
    stop = time()

    t_python.append(stop - start)

    n.append(i)
    i += 50

    # bubble sort
    start = time()
    bubble_sort(rij_3)
    stop = time()

    t_bubble.append(stop - start)

plt.plot(n, t_insertion, "-ro")
plt.plot(n, t_python, "-bo")
plt.plot(n, t_bubble, "-go")
plt.xlabel("N")
plt.ylabel("t")
plt.gcf().legend(("Insertion sort", "Python sort", "Bubble sort"))
plt.gcf().canvas.set_window_title("Dieter Demuynck")
plt.title("Time measurements")
plt.show()
