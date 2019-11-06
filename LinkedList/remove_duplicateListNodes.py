if __name__ == "__main__":
    import sys, os
    sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'DataStructureImplementations'))
    print(os.path.join(os.path.dirname(sys.path[0]),'DataStructureImplementations'))
    from SinglyLinkedList import *

def remove_duplicateSLLNodes(sll): #Mem O(n), Time O(n)
    if sll.head == None:
        raise EmptyLinkedList
    elif sll.length == 1:
        return sll

    itemSet = {}
    prev = None
    cur = sll.head

    while(cur != None):
        if cur.data not in itemSet:
            itemSet[cur.data] = 1
            prev = cur
            cur = cur.next
        else:
            prev.next = cur.next 
            cur.next = None
            if prev.next != None:
                cur = prev.next
            else:
                cur = None

    return sll

def remove_duplicateSLLNodes2(sll) : #Mem O(1), Time O(n^2) , cracking coding can't find better solution without using extra memory
    if sll.head == None:
        raise EmptyLinkedList
    elif sll.length == 1:
        return sll
    
    prev = sll.head
    cur = sll.head.next
    anchor = sll.head 

    while(anchor != None):
        while(cur != None):
            if anchor.data == cur.data:
                prev.next = cur.next
                cur.next = None
                if prev.next != None:
                    cur = prev.next
                else:
                    cur = None
            else:
                prev = cur
                cur = cur.next
        
        anchor = anchor.next
        if anchor != None:
            cur = anchor.next
            prev = anchor
    
    return sll


if __name__ == "__main__":
    sll = SLLIntLinkedList()
    arr = [1,2,3,4,4,4,4,4,4,5,2,3,10]
    sll.feed_array(arr)
    sll = remove_duplicateSLLNodes2(sll)
    sll.print_SLL()




