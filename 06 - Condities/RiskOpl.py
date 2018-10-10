a_1 = int(input("dobbelsteen 1: "))
a_2 = int(input("dobbelsteen 2: "))
a_3 = int(input("dobbelsteen 3: "))
v_1 = int(input("dobbelsteen 1: "))
v_2 = int(input("dobbelsteen 2: "))

# Sorteren
s_v_1 = max(v_1,v_2)
s_v_2 = min(v_1,v_2)

s_a_1 = max(a_1, max(a_2, a_3))
s_a_3 = min(a_1, a_2, a_3)
s_a_2 = min(max(a_1, a_2), max(a_1, a_3), max(a_2, a_3)) # (a_1 + a_2 + a_3) - s_a_1 - s_a_3

# Vergelijken
message = "aanvaller verliest 1 leger, verdediger verliest 1 leger"

if s_v_1 >= s_a_1 and s_v_2 >= s_a_2:
    message = "aanvaller verliest 2 legers, verdediger verliest 0 legers"
elif s_v_1 < s_a_1 and s_v_2 < s_a_2:
    message = "aanvaller verliest 0 legers, verdediger verliest 2 legers"
 print (message)