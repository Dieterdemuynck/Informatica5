def germaniseer(string):
    germaans = ""
    for i in range(len(string)):
        if i == 0 or string[i-1] == " ":
            letter = string[i].upper()
        else:
            letter = string[i]
        germaans += letter

    return germaans