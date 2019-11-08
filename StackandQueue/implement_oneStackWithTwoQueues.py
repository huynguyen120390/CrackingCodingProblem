class Queue:
    def __init__(self):
        self.arr = []
        self.size = 0
    
    def push(self,data):
        self.arr.append(data)
        self.size += 1
    
    def pop(self):
        if self.size < 1:
            raise EmptyQueue
        data = self.arr[0]
        self.size -= 1
        del self.arr[0]
        return data
    
    def peek(self):
        if self.size < 1:
            raise EmptyQueue
        return self.arr[0]    


class StackWithTwoQueue:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
        self.size = 0
    
    def push(self,data):
        self.queue1.push(data)
        self.size += 1

    def pop(self):
        if self.size < 0:
            raise EmptyQueue
        for _ in range(self.queue1.size - 1):
            self.queue2.push(self.queue1.pop())
        popData = self.queue1.pop()
        self.size -=1
        for _ in range(self.queue2.size):
            self.queue1.push(self.queue2.pop())
        return popData

    def peek(self):
        if self.size < 0:
            raise EmptyQueue
        for _ in range(self.queue1.size - 1):
            self.queue1.push(self.queue1.pop())
        peekData = self.queue1.peek()
        for _ in range(self.queue2.size):
            self.queue2.push(self.queue2.pop())
        return peekData
    

class StackWithTwoQueue2:
    """
        Manage to organize stack when push 
    """
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
        self.size = 0

    def push(self,data):
        if self.size == 0:
            self.queue1.push(data)
        elif self.size > 0:
            for _ in range(self.queue1.size):
                self.queue2.push(self.queue1.pop())
            self.queue1.push(data)
            for _ in range(self.queue2.size):
                self.queue1.push(self.queue2.pop())   
        self.size += 1
    
    def pop(self):
        if self.size < 0:
            raise EmptyStack
        data = self.queue1.pop()
        self.size -= 1
        return data

    def peek(self):
        if self.size < 0:
            raise EmptyStack
        return self.queue1.peek()
    
    def display(self):
        if self.queue1.size == 0:
            raise EmptyStack
        print("Top-[",end = '')
        for _ in range(self.queue1.size):
            data = self.queue1.pop()
            print(f"{data},",end='')
        print("]-Bot")

        for _ in range(self.queue2.size):
            data = self.queue2.pop()


class EmptyQueue(Exception):pass
class EmptyStack(Exception):pass

if __name__ == "__main__":
    stack = StackWithTwoQueue2()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    stack.display()
