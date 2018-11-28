tweet = input("De tweet: ")

for i in range(1, len(tweet)):
    if tweet[i-1] == "#":
        hashtag = ""
        while tweet[i] != " ":
            hashtag += tweet[i]
            i += 1
        print(hashtag)