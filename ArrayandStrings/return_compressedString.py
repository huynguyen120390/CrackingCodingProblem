def return_compressedString(string):
    if string == None:
        raise NullString 
    string.strip()

    #Add to Array the pairs of (char,count)
    count = 0
    prev = ''
    cur =''
    pair = []
    pairArray = []
    is_alterSingleChar = True
    for c in string:
        cur = c
        if prev == cur:
            count += 1
        elif prev != cur:
            count = 1
            if prev != '':
                pairArray.append(pair)
        prev = cur
        pair = [cur,count]
        if count > 1:
            is_alterSingleChar = False

    pairArray.append(pair)
    print(pairArray)

    #Return compressed string
    newString = ""
    for pair in pairArray:
        char,count = pair
        newString += char + str(count)

    if is_alterSingleChar:
        return string
    else:
        return newString

def return_compressedString2(string): # Mem O(n), Time O(n)
    if string == None:
        raise NullString 
    string.strip()

    #Add to Array the pairs of (char,count)
    count = 0
    prev = ''
    cur =''
    pair = []
    newString = ""
    is_alterSingleChar = True
    for c in string:
        cur = c
        if prev == cur:
            count += 1
        elif prev != cur:
            count = 1
            if prev != '':
                newString += pair[0] + str(pair[1])
        prev = cur
        pair = [cur,count]
        if count > 1:
            is_alterSingleChar = False
    newString += pair[0] + str(pair[1])
    
    if is_alterSingleChar:
        return string
    else:
        return newString
        
print(return_compressedString2("Helollo"))
        



class NullString(Exception):pass