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
        
        








class Queue:
    def __init__(self,cap):
        self.arr = []
        self.size = 0
        self.cap = cap
    
    def push(self,data):
        if is_full():
            raise FullQueue
        self.arr.append(data)
        self.size += 1
        return data
    
    def pop(self):
        if is_empty():
            raise EmptyQueue
        data = self.arr[0]
        del self.arr[0]
        self.size -= 1
        return data

    def is_full(self):
        if self.size == self.cap:
            return True
        return False

    def is_empty(self):
        if self.size == 0:
            return True
        return False 


def sort_stack(s1): 
    #O(n^2) 
    # if n = 2000, time = 6.904273986816406s 
    # if n = 10000 , time = 188.9385049343109
    if s1.is_empty():
        raise EmptyStack
    elif s1.size == 1:
        return s

    s2 = Stack(s.cap)
    swap = 0
    count = 0
    size = s1.size
    while(swap < size-1):
        max = s1.pop()
        while(not s1.is_empty()):
            new = s1.pop()
            if new < max:
                s2.push(new)
            else:
                new,max = max,new
                s2.push(new)
                count += 1
            #print("S1",s1.arr,"\nS2",s2.arr,"\nCount",count,"Swap",swap,"Size",size)
        s2.push(max)
        #print("S1",s1.arr,"\nS2",s2.arr,"\nCount",count,"Swap",swap,"Size",size)
        while(not s2.is_empty()):
            s1.push(s2.pop())
        swap = count
        count = 0
        #print("________________________________________________________________")
    #print("S1",s1.arr,"\nS2",s2.arr,"\nCount",count,"Swap",swap,"Size",size)
   
    return s1

def sort_stack2(s1): 
    #O(n^2) 
    # if n = 2000, time = 1.8272910118103027 
    # if n = 10000 , time = 50.47556400299072
    if s1.is_empty():
        raise EmptyStack
    elif s1.size == 1:
        return s

    s2 = Stack(s.cap)
    swap = 0
    count = 0
    size = s1.size
    while(swap < size-1):
        max = s1.pop()
        while(not s1.is_empty()):
            new = s1.pop()
            if new < max:
                s2.push(new)
            else:
                new,max = max,new
                s2.push(new)
                count += 1
            #print("S1",s1.arr,"\nS2",s2.arr,"\nCount",count,"Swap",swap,"Size",size)
        s2.push(max)
       # print("S1",s1.arr,"\nS2",s2.arr,"\nCount",count,"Swap",swap,"Size",size)
        min = s2.pop()
        while(not s2.is_empty()):
            new = s2.pop()
            if new > min:
                s1.push(new)
            else:
                new,min = min,new
                s1.push(new)
           # print("S1",s1.arr,"\nS2",s2.arr,"\nCount",count,"Swap",swap,"Size",size)
        s1.push(min)
        swap = count
        count = 0
        #print("________________________________________________________________")
    #print("S1",s1.arr,"\nS2",s2.arr,"\nCount",count,"Swap",swap,"Size",size)
   
    return s1

class FullStack(Exception):pass
class FullQueue(Exception):pass
class EmptyStack(Exception):pass
class EmptyQueue(Exception):pass
class OutOfStackBound(Exception):pass
    
if __name__ == "__main__":
    import time
    s = Stack(10000)
    s.feed_randomArray(10000)
    start = time.time()
    s = sort_stack2(s)
    print(time.time()-start)
   
    # The following is for stack push() arranging min on top 
    #stack 1: B[     ]T  ; stack2 - small or equal come in here first:B[      ]T
    # s1 [6]   s2[]
    # 1. In: 5 s1 [6] s2[]  , pop 6 , 6 > 5 
    #       s1 [] s2[5,6] , move back s1[6,5]
    # 2. In: 7 s1 [6] s2[]  , pop 6 , 7 > 6
    #       s1 [] s2[6,7] , move back s1[7,6]
    #    In : 8 s1 [7,6] , pop 6, 8>6, In 8  s1[7]  s2[6], pop 7, 8> 7, s1[] s2[6,7,8], move back s1[8,7,6] s2[]
    #    In : 7 s1 [8,7,6] s2[], pop 6 , 6<7 | in 7 s1[8,7]  s2[6], pop 7, 7==7, s1[8,7] s2[6,7], in 7 , pop 8, s1 [] s2 [6,7,7,8], move back s1[8,7,7,6]




