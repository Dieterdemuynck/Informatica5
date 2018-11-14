n = int(input("priemgetallen: "))

i = 2
while n // i != n/i and i < (n // 2) + 1:
    i += 1

if i == n // 2 + 1:
    print(str(n) + " is een priemgetal")
else:
    print(str(n) + " is geen priemgetal")