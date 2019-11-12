def get_key(pair):
    pair = pair.split()
    return pair[0]
def sort():
    winfile = ["11 hi","2 hello"]
    winfile.sort(key= get_key)
    return winfile

print(sort())