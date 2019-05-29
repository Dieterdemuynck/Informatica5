from random import randint
from time import time
import matplotlib.pyplot as plt


def genereer_rij(aantal):
    rij = []
    for i in range(aantal):
        rij.append(randint(0, aantal))
    return rij


def linear_search(lijst, getal):

    index = 0
    while index < len(lijst) and lijst[index] != getal:
        index += 1

    return index < len(lijst)


def binary_search(lijst, low, high, num):
    if low > high:
        return False
    else:
        mid = (high + low) // 2

        if lijst[mid] == num:
            return True
        elif num < lijst[mid]:
            return binary_search(lijst, low, mid - 1, num)
        else:
            return binary_search(lijst, mid + 1, high, num)


n, t_bs, t_ls = [], [], []
i = 10
while i < 30000:
    rij_1 = genereer_rij(i)
    rij_1.sort()
    rij_2 = rij_1.copy()
    getal = rij_1[randint(0, i)]

    # Time of Binary Search
    start = time()
    binary_search(rij_1, 0, len(rij_1) - 1, getal)
    stop = time()
    t_bs.append(stop - start)

    # Time of Linear Search
    start = time()
    linear_search(rij_2, getal)
    stop = time()
    t_ls.append(stop - start)

    n.append(i)
    i += 50

plt.plot(n, t_bs)
plt.plot(n, t_ls)
plt.xlabel("N")
plt.ylabel("t")
plt.gcf().legend(("binary search", "linear search"))
plt.gcf().canvas.set_window_title("Dieter Demuynck")
plt.title("Time measurements")
plt.show()
