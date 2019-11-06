def is_uniqueString(string):
    set = {}
    for i, v in enumerate(string):
        if v in set:
            return False
        else:
            set[v] = 1
    return True