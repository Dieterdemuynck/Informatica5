l1 = [2, 5, 9, 13]
l2 = [4, 6, 8, 10, 11]


# Voegt twee gesorteerde lijsten samen tot 1 gesorteerde lijst
def merge(l1, l2):

    lijst = []
    i_1, i_2 = 0, 0
    while i_1 < len(l1) and i_2 < len(l2):
        if l1[i_1] < l2[i_2]:
            lijst.append(l1[i_1])
            i_1 += 1
        else:
            lijst.append(l2[i_2])
            i_2 += 1

    if i_1 < len(l1):
        lijst = lijst + l1[i_1:]
    else:
        lijst = lijst + l2[i_2:]

    return lijst


def merge_sort(lijst):
    if len(lijst) > 1:
        mid = len(lijst) // 2
        deel1 = merge_sort(lijst[:mid])
        deel2 = merge_sort(lijst[mid:])
        return merge(deel1, deel2)
    else:
        return lijst


print(merge(l1, l2))
print(merge_sort([3, 7, 1, 2, 8, 5, 10, 4, 6, 9]))