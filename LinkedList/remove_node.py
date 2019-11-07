if __name__ == "__main__":
    import sys, os
    sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'DataStructureImplementations'))
    print(os.path.join(os.path.dirname(sys.path[0]),'DataStructureImplementations'))
    from SinglyLinkedList import *


def remove_node(node):
    
    if node == None or node.next == None : #Empty, 1st (one item list) ,last node 
        return None 
    
    cur = node
    cur.data = node.next.data
    cur.next = node.next.next 

    return cur.data


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


if __name__=="__main__":
    sll = SLLIntLinkedList()
    sll.feed_array([0,1,2,3,4,5,6,7,8,9,10])
    node = sll.head.next.next
    print(node.data)
    curdata = remove_node(node)
    print(node.data)
    print(curdata)
    print_intSLL(cur)