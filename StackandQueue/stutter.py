class Stack:
    def __init__(self,cap):
        self.arr = []
        self.size = 0
        self.cap = cap

    def push(self,data):
        if self.is_full():
            raise FullStack
        self.arr.append(data)
        self.size += 1
        return data

    def pop(self):
        if self.is_empty():
            raise EmptyStack
        data = self.arr[self.size-1]
        del self.arr[self.size - 1]
        self.size -= 1
        return data

    def peek(self):
        if self.is_empty():
            raise EmptyStack
        return self.arr[self.size-1]
    
    def is_full(self):
        if self.size == self.cap:
            return True
        return False
    
    def is_empty(self):
        if self.size == 0:
            return True
        return False
    
    def feed_arr(self,arr):
        if len(arr) > self.cap:
            raise OutOfStackBound
        for v in arr:
            self.push(v)
    
    def feed_randomArray(self,size):
        import random
        if size > self.cap :
            raise OutOfStackBound
        for _ in range (size):
            self.push(random.randint(0,100))

class FullStack(Exception):pass
class FullQueue(Exception):pass
class EmptyStack(Exception):pass
class EmptyQueue(Exception):pass
class OutOfStackBound(Exception):pass

def stutter(s,occurence):
    if s.is_empty():
        return s
    v = s.pop()
    newStack = stutter(s,occurence)
    for i in range(occurence):
        newStack.push(v)
    return s

    
if __name__ == "__main__":
    occurrence = 3
    s = Stack(20*occurrence)
    s.feed_randomArray(10)
    s = stutter(s,occurrence)
    print(s.arr)