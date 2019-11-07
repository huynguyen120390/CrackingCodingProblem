if __name__ == "__main__":
    import sys, os
    sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'DataStructureImplementations'))
    from SinglyLinkedList import *

def is_palindromeString(string):
    string = string.replace(" ","")  #if we dont care about space " "
    #stock char and their occurencies
    i= 0
    j = len(string)-1
    while(j>i):
        if string[i]!= string[j]:
            return False
        else:
            i += 1
            j -=1

    return True

def is_palindromeArray(arr):
    i = 0
    j = len(arr) - 1
    while(j>i):
        if arr[i] != arr[j]:
            return False
        else:
            i+= 1
            j-= 1
    return True

def is_palindromeInt(int):
    def int2arr(int):
        arr = []
        while(int>1):#O(n)
            last = int%10
            arr.append(last)
            int/=10
        return arr

    arr = int2arr(int)
    i = 0
    j = len(arr) - 1
    while(j>i): #O(n/2)
        if arr[i] != arr[j]:
            return False
        else:
            i+=1
            j+=1
    return True

def reverse(sll):
    if sll.head == None:
        raise EmptyLinkedList
    elif sll.length == 1:
        return 
    elif sll.length == 2:
        pointee = sll.head
        pivot = sll.head.next
        pivot.next = pointee
        pointee.next = None
        sll.head = pivot
        pivot = None 
        pointee = None 
    elif sll.length == 3:
        pointee = sll.head
        pivot = sll.head.next
        holder = sll.head.next.next
        pivot.next = pointee
        pointee.next = None 

        while(pivot != None):
            #Move 
            pivot = holder
            pointee = pivot
            holder = holder.next 
            #Pointing
            pivot.next = pointee
        
        sll.head = pointee 
        pointee = None
 
def is_palindromeLinkedList(sll): #Mem O(2n) , Time O(2n) or Mem O(n), Time O(n)
    sll1 = copy.deepcopy(sll)#Mem O(n) 
    sll2 = reverse(sll) #Mem O(n), Time O(n)
    p1 = sll1.head
    p2 = sll2.head
    while(p1!=None): #Time O(n)
        if p1.data != p2.data:
            return False
        else:
            p1 = p1.next
            p2 = p2.next
    return True
        
def is_palindromeLinkedList2(sll): #Mem O(n) ,Time (3/2*n) or Mem(n), Time O(n)
    arr = []
    p = sll.head
    while(p != None): 
        arr.append(p.data)
        p = p.next
    
    i = 0
    j = sll.length - 1
    while(j>i):
        if arr[i] == arr[j]:
            return False
        i+=1
        j-=1
    return True
        
if __name__ == "__main__":
    print(is_palindromeInt(10011))