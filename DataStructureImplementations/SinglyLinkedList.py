import copy
class SLLIntNode:
    def __init__(self,data = None):
        self.data = data
        self.next = None

    def __repr__(self):
        return {'data[int]':self.data,'next[SLLIntNode]':self.next}
    
    def __str__(self):
        return f"SLLIntNode(name[int]={self.data},next[SLLIntNode]={self.next})"




class SLLIntLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0


    def append(self,data = None):
        newNode = SLLIntNode(data)
        if self.head == None:
            self.head = newNode
        else:
            cur = self.head
            prev = None
            while(cur != None):
                prev = cur
                cur = cur.next
            prev.next = newNode
            prev = None
        self.length += 1
       
    
    def prepend(self,data = None):
        newNode = SLLIntNode(data)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    
    def print_SLL(self):
        if self.head == None:
            raise EmptyLinkedList("List is empty")
        else:
            print('[',end='')
            cur = self.head
            while(cur != None):
                print(cur.data,end='')
                if cur.next != None:
                    print(',',end='')
                cur = cur.next
            print(']')

    def delete(self,position):
        if self.head == None:
            raise EmptyLinkedList("List is empty")
        elif position >= self.length:
            raise OutOfListBound(f"List is not that long, only {self.length}")
        else:
            cur = self.head
            prev = None
            i = 0
            while(cur!=None):
                if i == position:
                    prev.next = cur.next
                    break
                prev = cur
                cur = cur.next
                i += 1
            prev = None 
            cur = None 
        self.length -= 1
    

    def feed_array(self,arr):
        for v in arr:
            self.append(v)
        return self.head
    

def reverse(sll):
    if sll.head == None:
        raise EmptyLinkedList
    elif sll.length == 1:
        return sll
    elif sll.length == 2:
        pointee = sll.head
        pivot = sll.head.next
        pivot.next = pointee
        pointee.next = None
        sll.head = pivot
        pivot = None 
        pointee = None 
    else:
        pointee = sll.head
        pivot = sll.head.next
        holder = sll.head.next.next
        pointee.next = None 

        while( pivot != None):
            #sll.print_SLL()
            #sll.head = pivot
            pivot.next = pointee
            #Move 
            pointee = pivot
            pivot = holder
            if holder != None:
                holder = holder.next 
            
        sll.head = pointee
        pointee = None
    return sll


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
        

class EmptyLinkedList(Exception):pass
class OutOfListBound(Exception):pass




if __name__ == "__main__":
    sll = SLLIntLinkedList()
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.append(2)
    sll.append(1)
    print(is_palindromeLinkedList2(sll))
        



        


