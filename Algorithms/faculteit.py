def is_palindroom(w):
    if len(w) == 1 or len(w) == 0:
        return True
    else:
        res = is_palindroom(w[1: -1])
        return w[0] == w[-1] and res


print(is_palindroom("koortsmeetsyseemstrook"))