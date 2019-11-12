
import math 


class ThreeStack:
    def __init__(self,capacity,divisor):
        self.capacity = capacity
        self.divisor = divisor
        self.arr = [None]*capacity
        self.cap = [0]*divisor
        self.size = [0]*divisor
        self.topIndex = [0]*divisor
        self.__init_stacks()


    def __init_stacks(self):
        for i in range(self.divisor):
            start,end,_,_ = self.malloc(i)
            self.topIndex[i] = end + 1
            self.cap[i] = end - start + 1
            
    def malloc(self,id):
        eachSize = math.floor(self.capacity/self.divisor)
        if id == self.divisor - 1:
            start,end = eachSize * id, self.capacity - 1
        else:
            start,end = eachSize * id, eachSize*(id + 1) - 1
        top = self.topIndex[id]
        cap = self.cap[id]
        return start,end,top,cap

    def is_full(self,id):
        start,_,top,cap = self.malloc(id)
        if top == start:
            return True
        return False
    
    def is_empty(self,id):
        _,end,top,_ = self.malloc(id)
        if end + 1 == top:
            return True
        return False
    
    def __update_top(self,id,is_push):
        if is_push:
            self.topIndex[id] -= 1
            self.size[id] +=1
        else:
            self.topIndex[id] += 1
            self.size[id] -=1
        
    def push(self,data,id):
        if self.is_full(id):
            raise FullStack
        print('push',self.topIndex)
        self.__update_top(id,is_push = True)
        _,_,top,_= self.malloc(id)
        self.arr[top] = data
        
        return data
    
    def push_selfAllocate(self,data):
        for id in range(self.divisor):
            if  not self.is_full(id):
                self.push(data,id)
                break
    
    def pop_selfAllocate(self,popNum):
        pop = 0
        for id in range(self.divisor):
            for i in range(popNum):
                if pop == popNum:
                    break
                if not self.is_empty(id):
                    self.pop(id)
                    pop += 1
                else:
                    break
            if pop == popNum:
                break

    def pop(self,id):
        if self.is_empty(id):
            raise EmptyStack
        _,_,top,_ = self.malloc(id)
        data = self.arr[top] 
        print(self.topIndex)
        self.arr[top]= None
        self.__update_top(id,is_push = False)
        return data
    
    def peek(self,data,id):
        if self.is_empty(id):
            raise EmptyStack
        _,_,top,_ = self.malloc(id)
        return self.arr[top]


class FullStack(Exception):pass
class EmptyStack(Exception):pass
if __name__ == "__main__":
    stacks = ThreeStack(3,3)
    stacks.push(1,1)
    stacks.push(1,0)
    stacks.push(1,2)
   # stacks.pop(1)
    print(stacks.arr)

        

        
