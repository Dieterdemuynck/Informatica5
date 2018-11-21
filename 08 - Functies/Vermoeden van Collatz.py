def volgend_collatz_getal(n):
    if n % 2 == 0:
        volgend = n // 2
    else:
        volgend = n * 3 + 1
    return volgend

def collatz(n):
    aantal = 1
    while n != 1:
        aantal += 1
        n = volgend_collatz_getal(n)
    return aantal