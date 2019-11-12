class Node:
    def __init__(self,data,id):
        self.id = id
        self.data = data
        self.right = None
        self.left = None
    
class BST:
    def __init__(self):
        self.root = None
        self.id = 0

    def add(self,data):
        def helper(root,data):
            if root == None:
                self.id += 1
                node = Node(data,self.id)
                root = node
            else:
                if data < root.data:
                    root.left = helper(root.left,data)
                else:
                    root.right = helper(root.right,data)
            return root
        self.root = helper(self.root,data)
    

    
    
    def return_minNode(self,root):
        if root == None:
            return root
        if root.left == None and root.right == None:
            return root
        
        return self.return_minNode(root.left)

    
    def if_exist(self,data):
        def helper(root,data):
            if root == None:
                return False
            if root.data == data:
                return True
            else:
                if data < root.data:
                    return helper(root.left,data)
                else:
                    return helper(root.right,data)
        return helper(self.root,data)

    def display(self,treeNode):
        if treeNode == None:
            return None
        print(f"Node{treeNode.id}:{treeNode.data}",end = '')
        if treeNode.left is not None:
            print(f"->L-Node{treeNode.left.id}:{treeNode.left.data}",end = '')
        else:
            print(f"->L-null",end = '')
        
        if treeNode.right is not None:
            print(f" & R-Node{treeNode.right.id}:{treeNode.right.data}",end = '')
        else:
            print(f" & R-null",end = '')
        print("")
        self.display(treeNode.left)
        self.display(treeNode.right)
    
    def feed_array(self,arr):
        for v in arr:
            self.add(v)
        return arr

    def feed_randomArray(self,length,start,end):
        import random
        arr = []
        for _ in range(length):
            num = random.randint(start,end)
            arr.append(num)
        return self.feed_array(arr)

if __name__ == "__main__":
    bst = BST()
    bst.feed_randomArray(10,0,10)
    bst.display(bst.root)
    minNode = bst.return_minNode(bst.root)
    print(minNode.id,minNode.data)



        
        