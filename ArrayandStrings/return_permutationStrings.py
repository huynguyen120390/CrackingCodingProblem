def __is_permutation(string1, string2):
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

def return_permutations(piece,longString):
    
    n = len(longString)
    np = len(piece)
    if np > n:
        return None
    permutationDict = {}
    for i in range(n-(np-1)):
        comparee = longString[i:i+np]
        if __is_permutation(piece,comparee):
            if comparee not in permutationDict:
                permutationDict[comparee] = []
            permutationDict[comparee].append(i)
    return permutationDict






if __name__ == "__main__":
    print(__is_permutation("tagc","tgat"))
    print(return_permutations("tagc","atgc"))
    