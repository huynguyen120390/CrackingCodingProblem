def is_permutation(string1, string2):
    if len(string1) != len(string2):
        return False
    set = {}
    #stock chars of string1 with positive occurency
    for i, v in enumerate(string1):
        v = v.lower()
        if v not in set:
            set[v] = 1
        else:
            set[v] += 1

    #stock chars of string2 with negative occurency, if new char occurs means not permutation-> return False
    for i, v in enumerate(string2):
        v = v.lower()
        if v not in set:
            return False
        else:
            set[v] -= 1
    #if stocking chars from two strings is done, and no return False, check if any occurence > 0, if yes -> return False
    for v in set:
        if set[v] > 0:
            return False
        
    return True