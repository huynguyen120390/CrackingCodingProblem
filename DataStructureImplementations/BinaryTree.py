class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None 
        self.right = None
        

class BinaryTree:
    def __init__(self,data):
        self.root = BinaryTreeNode(data)
    
    def add(self, node, data, left = None ,right = None):     
        newNode = BinaryTreeNode(data)  
        if node == None:
            node = BinaryTreeNode(data)
        pass
            
        
            