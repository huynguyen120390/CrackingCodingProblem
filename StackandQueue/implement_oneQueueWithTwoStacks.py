class Stack:
    def __init__(self):
        self.arr = []
        self.size = 0
        self.top = -1

    def push(self,data):
        self.top += 1
        self.size += 1
        self.arr.append(data)
        return data
        
    def pop(self):
        if self.top < 0:
            raise EmptyStack
        data = self.arr[self.top]
        del self.arr[self.top]
        self.top -= 1
        self.size -= 1
        return data

    
    def peek(self):
        if self.top < 0:
            raise EmptyStack
        return self.arr[self.top]

class EmptyStack(Exception):pass

class QueueByTwoStack:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()
        self.size = 0
    
    def push(self,data):
        self.stack1.push(data)
        self.size += 1

    def pop(self): #O(n)
        if self.size < 0:
            raise EmptyStack
        data = None
        for i in range(self.stack1.size):
            data = self.stack1.pop()
            self.stack2.push(data)
        popData = self.stack2.pop()
        self.size -= 1
        for i in range(self.stack2.size):
            data = self.stack2.pop()
            self.stack1.push(data)
        return popData
        
    def peek(self):
        if self.size < 0:
            raise EmptyStack
        data = None
        for i in range(self.stack1.size):
            data = self.stack1.pop()
            self.stack2.push(data)
        peekData = self.stack2.peek()
        for i in range(self.stack2.size):
            data = self.stack2.pop()
            self.stack1.push(data)        
        return peekData

    def display(self):
        print(self.size)
        if self.size < 0:
            raise EmptyStack
        for _ in range(self.stack1.size):
            self.stack2.push(self.stack1.pop())
        print("Front-[",end='')
        for _ in range(self.stack2.size):
            print(f"{self.stack2.peek()},",end ='')
            self.stack1.push(self.stack2.pop())
        print("]-End")


if __name__ == "__main__":
    q = QueueByTwoStack()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(3)
    q.push(4)
    q.push(5)
    q.pop()
    q.pop()
    q.pop()
    q.pop()
    q.pop()
    q.pop()
    q.display()




    
    
