if __name__ == "__main__":
    import sys,os
    sys.path.append(os.path.join(os.path.dirname(sys.path[0]),"DataStructureImplementations"))
    from SinglyLinkedList import *


def return_chain_kth_from_last(sll,k): # assume we dont know length of sll
    p1 = sll.head
    p2 = sll.head
    i = 0
    for i in range(k): # Notice p1 will point to kth, even i != kth
        if p1 == None:
            return None
        p1 = p1.next 
    while(p1 != None):
        p1 = p1.next
        p2 = p2.next 
    sll.head = p2
    return sll.head


def print_intSLL(sll):
    if sll == None:
            raise EmptyLinkedList("List is empty")
    else:
        print('[',end='')
        cur = sll
        while(cur != None):
            print(cur.data,end='')
            if cur.next != None:
                print(',',end='')
            cur = cur.next
        print(']')


if __name__ == "__main__":
    sll = SLLIntLinkedList()
    sll.feed_array([0,1,2,3,4,5,6,7,8,9,10])
    k = 6
    sll = return_chain_kth_from_last(sll,k)
    print_intSLL(sll)

    