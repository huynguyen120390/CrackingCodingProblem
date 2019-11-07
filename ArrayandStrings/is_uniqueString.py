def is_uniqueString(string):
    if string == None:
        raise NullString
    elif len(string) == 1:
        return True
        
    set = {}
    for i, v in enumerate(string):
        if v in set:
            return False
        else:
            set[v] = 1
    return True

class NullString(Exception):pass