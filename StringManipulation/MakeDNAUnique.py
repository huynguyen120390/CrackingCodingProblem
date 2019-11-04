def make_unique(str): #O(n + k)
    set = {}
    for i,v in enumerate(str): #O(n)
        if v in set: #O(1)
            set[v] += 1
        else:
            set[v] = 1
    
    str = ""
    for i in set: #O(k)
        str += i

    return str

print(make_unique("happppppy"))
        

