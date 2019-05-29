def is_palindroom(string):
    foutheid = False
    for i in range(0, len(string)):
        if string[i] != string[-i - 1]:
            foutheid = True
    return not foutheid


print(is_palindroom("koortsmeetsysteemstrook"))