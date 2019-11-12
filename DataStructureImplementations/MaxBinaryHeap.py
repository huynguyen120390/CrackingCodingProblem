import math
class MaxBinaryHeap:
    def __init__(self):
        self.heap = []
        self.size = 0
    
    def insert(self,data):
        def __insert(id,data):
            if id <= 0:
                return 
            if id % 2 == 0:  #right
                print("Adding even",data,id)
                parent = int(math.floor((id - 2)/2))
                if self.heap[parent] < self.heap[id]:
                    print("PreSwap",self.heap)
                    self.heap[parent],self.heap[id] = self.heap[id],self.heap[parent]
                    print("Swap",self.heap)
                    __insert(parent,data)
                else:
                    return 
            else:
                print("Adding odd",data,id)
                parent = int(math.floor((id - 1)/2))
                if self.heap[parent] < self.heap[id]:
                    print("PreSwap",self.heap)
                    self.heap[parent],self.heap[id] = self.heap[id],self.heap[parent]
                    print("Swap",self.heap)
                    __insert(parent,data)
                else:
                    return 
        length = len(self.heap)
        if length < 1:
            self.heap.append(data)
        else:
            self.heap.append(data)
            id = length
            __insert(id,data)
        self.size += 1
    

    def extract_max(self):
        def __sink(id):
            left = 2*id + 1
            right = 2*id + 2
            exist_left = self.if_exist(left)
            exist_right = self.if_exist(right)
            if exist_left and exist_right:
                if self.heap[left] - self.heap[right] > 0:
                    if self.heap[id] < self.heap[left]:
                        self.heap[left],self.heap[id] = self.heap[id],self.heap[left]
                        __sink(id)
                    else:
                        return
                else:
                    if self.heap[id] < self.heap[right]:
                        self.heap[right],self.heap[id] = self.heap[id],self.heap[right]
                        __sink(id)
                    else:
                        return
            elif exist_left:
                if self.heap[id] < self.heap[left]:
                    self.heap[left],self.heap[id] = self.heap[id],self.heap[left]
                    __sink(id)
                else:
                    return
            elif exist_right:
                if self.heap[id] < self.heap[right]:
                    self.heap[right],self.heap[id] = self.heap[id],self.heap[right]
                    __sink(id)
                else:
                    return
        if self.size < 1:
            return None
        elif self.size == 1:
            max = self.heap[0]
            del self.heap[0]
            return max 
        elif self.size == 2:
            self.heap[0], self.heap[1] = self.heap[1],self.heap[0]
            max = self.heap[0]
            del self.heap[0]
            return max 
        else:
            self.heap[0], self.heap[len(self.heap)-1] = self.heap[len(self.heap)-1],self.heap[0]
            del self.heap[len(self.heap)-1]
            __sink(0)
        self.size -= 1

           
        
    def if_exist(self,id):
        try:
            x = self.heap[id]
            return True
        except:
            return False

    def level(self):
        level = lambda x : math.ceil(math.log(x,2)) + 1
        return level(len(self.heap))

    def is_empty(self):
        if len(self.heap) < 1:
            return None

        
    def display(self):
        i = 0
        level = self.level()
        for l in range(level):
            nodeNum = 2**l
            for j in range(0,nodeNum):
                if i >= len(self.heap):
                    break
                print(f"{self.heap[i]} ",end = '')
                i += 1
            print("")

    def return_max(self):
        if self.is_empty():
            return None
        return self.heap[0]
                


if __name__ == "__main__":
    maxbiheap = MaxBinaryHeap()
    maxbiheap.insert(1)
    maxbiheap.insert(2)
    maxbiheap.insert(3)
    maxbiheap.insert(1)
    maxbiheap.insert(2)
    maxbiheap.insert(3)
    maxbiheap.insert(4)
    maxbiheap.insert(5)
    maxbiheap.insert(6)
    print(maxbiheap.heap)
    maxbiheap.display()
    print("Max",maxbiheap.return_max())
    maxbiheap.extract_max()
    maxbiheap.display()

            
                    


                



    