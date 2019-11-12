def swapXY_withoutTemp(x,y):
    print(x,bin(x),y,bin(y))
    x = x^y
    print(x,bin(x),y,bin(y))
    y = x^y
    print(x,bin(x),y,bin(y))
    x = x^y
    return x,y

print(swapXY_withoutTemp(2,3))