def remove_chars(string):
    return string [1:-1]

friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]

cleaned_list = map(lambda string : string[1: -1], friends_map)

for x in cleaned_list:
    print(x)