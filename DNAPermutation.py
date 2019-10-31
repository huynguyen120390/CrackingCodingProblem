import random as rand
""" 
    For CS study purposes, we might have more than 4 types nucleotides AGTC
    1. Check if 2 DNA piece is a permutation of each other //DNA Self-Permutation
    2. Check if a long DNA string has permutations of a DNA piece //DNA Permutation Detection
"""
def random_defection(nucSet,length):
    """
        Create random defected string from a set of nuc at . We can set length of string
    """
    defectedString = ""
    for i in range(length):
        typeNo = rand.randint(0,len(nucSet)-1)
        defectedString += nucSet[typeNo]
    
    return defectedString


def is_permutation(a,b): #O(n)
    """
        Check if 2 DNA piece is permuation of each other ( DNA Self-Permutation )
        args:   a[str]
                b[str]
        ret:    True if yes, False if not

    """
    if len(a) != len(b):
        return False

    dict= {}  #Create an empty dict of a

    for nuc in a : #Fill occurences of nuc in a into occurence Dict
        try:
            dict[nuc] += 1
        except KeyError:
            dict[nuc] = 1

    for nuc in b : #Fill negative occurences of nuc in b into occurence Dict
        try:
            dict[nuc] -= 1
        except KeyError:
            dict[nuc] = 1

    for nuc in dict: #Check if any occurences is left 
        if dict[nuc] != 0:
            return False
    
    return True
            

def return_permutations(piece,sample): #O(n)
    if len(piece) > len(sample):
        return None
    slidingWindowLimit = len(sample) - len(piece) +1 # The sliding window will skip len(piece) - 1 items to avoid overbound
    permutations = {}
    indices = []
    for i in range(slidingWindowLimit):
        comparedPiece = sample[i:i + len(piece)]
        if (is_permutation(piece,comparedPiece)):
            try:
                permutations[comparedPiece] += 1
            except KeyError:
                permutations[comparedPiece] = 1
            finally:
                indices.append(i)

    return indices, permutations


if __name__ == "__main__":
    a = "abab"
    b = "baba"
    is_permuted = is_permutation(a,b)
    print(is_permuted)

    piece = "atgc"
    defectedString = random_defection(piece,10)
    indices, permutations= return_permutations(piece,defectedString)

    print(defectedString)
    print(permutations)
    print(indices)



    


