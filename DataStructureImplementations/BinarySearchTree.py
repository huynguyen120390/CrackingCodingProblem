#rom numba import jit
#@jit(nopython = True)
class TreeNode:
    def __init__(self,data,id):
        self.data = data
        self.id = id
        self.left = None
        self.right = None

    def show(self):
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

#@jit(nopython = True)
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.id = 0

    def insert(self,data):
        def insert_at(root,data):
            self.id += 1
            newNode = TreeNode(data,self.id)
            if root == None:
                print("Adding node")
                root = newNode
                return root
            else:
                cur = root
                while(1):
                    if data < cur.data:
                        if cur.left == None:
                            cur.left = newNode
                            break
                        else:
                            cur = cur.left
                    else:
                        if cur.right == None:
                            cur.right = newNode
                            break
                        else:
                            cur = cur.right
                return root
        self.root = insert_at(self.root,data)
    
    def add(self,data):
        def add_at(root,data):
            if root == None:
                self.id += 1
                newNode = TreeNode(data,self.id)
                root = newNode   
                return root 
            if root.data < data:
                root.right = add_at(root.right,data)
            else:
                root.left = add_at(root.left,data)

            return root
            
        self.root = add_at(self.root,data)
    
    def remove(self,data):
        def remove_at(root,data):
            if root == None:
                return root
            if data < root.data:
                root.left = remove_at(root.left,data)
            elif data > root.data:
                root.right = remove_at(root.right,data)
            else:
               # if root.left == None and root.right == None: return None  # Notice this cond implies by the two below
                if root.left == None:
                    return root.right
                elif root.right == None:
                    return root.left
                else:
                    minNode = self.return_minNode(root.right)
                    root.data, root.id = minNode.data, minNode.id
                    root.right = remove_at(root.right,root.data) # now go to the right, find node with min data to delete
            return root
        self.root = remove_at(self.root,data)

    def search(self,data):
        def search_at(root,data):
            """
                Traverse left or right as data tendency, 
            """
            if root == None:
                return root
            if data < root.data:
                root = search_at(root.left,data)
            elif data > root.data:
                root = search_at(root.right,data)
            return root
        
        return search_at(self.root,data)
    

    def return_height(self):
        def return_height_at(root):
            if root == None:
                return 0
            height_right = return_height_at(root.right)
            height_left = return_height_at(root.left)

            if height_right > height_left:
                return height_right + 1
            elif height_right < height_left:
                return height_left + 1
            else:
                return 1
            

        return return_height_at(self.root)
        

    def return_minNode(self,root): 
        """
            Aim to the left node of branches
        """
        if root == None:
            return None
        if root.left == None and root.right == None:
            return root
        if root.left == None:
            return root
        elif root.right == None:
            return root.left
        return self.return_minNode(root.left)


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
            self.insert(v)
        return arr

    def feed_randomArray(self,length,start,end):
        import random
        arr = []
        for _ in range(length):
            num = random.randint(start,end)
            arr.append(num)
        return self.feed_array(arr)

    
    


def remove_leaves(root):
    if root == None:
        return None
    if root.left == None and root.right == None:
        return None
    
    root.right = remove_leaves(root.right)
    root.left = remove_leaves(root.left)

    return root


def BFS_treeLevel(root):
    if root == None:
        return None
    import queue
    q = queue.Queue()
    q.put(root)
    data = []
    data.append(root.data)
    family = {}
    while(not q.empty()):
        node = q.get()
        family[node.data] = {'R': None, 'L': None}
        leftData = None
        rightData = None
        if (node.left != None):
            q.put(node.left)
            leftData = node.left.data
        if (node.right != None):
            q.put(node.right)
            rightData = node.right.data
        family[node.data] = {'R':rightData,'L':leftData}
        data.append(family)

    return data

def count_leaves(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1

    leafNum_right = count_leaves(root.right)
    leafNum_left = count_leaves(root.left)

    return leafNum_right + leafNum_left


def sum_values_need_to_check(root):
    def sum_v(root,sum):
        if root == None:
            return 0

        sum += root.data
        print(sum,root.data)
        sum = sum_v(root.right,sum)
        sum = sum_v(root.left,sum)
        return sum
    return sum_v(root,0)

def sum_values(root):
    def sum_v(root):
        if root == None:
            return 0
        return root.data + sum_v(root.right) + sum_v(root.left)
    return sum_v(root)

def count_leftNodes(root):
    if root == None:
        return 0
    if root.left != None:
        return 1 + count_leftNodes(root.left) + count_leftNodes(root.right)
    else:
        return count_leftNodes(root.left) + count_leftNodes(root.right)

def double_positives(root):
    if root == None:
        return None
    
    if root.data > 0:
        root.data *= 2
    
    root.left = double_positives(root.left)
    root.right = double_positives(root.right)
    # STudy pass by reference and value in python , the following works, sometimes does't
    #double_positives(root.left)
    #double_positives(root.right)

    return root


def count_emptyBranch(root):
    if root == None:
        return 0


    # if root.left == None and root.right == None:
    #     return 2
    # elif root.left != None or root.right != None:
    #     return 1

    if root.left == None and root.right != None:
        return 1 + count_emptyBranch(root.right)
    elif root.left != None and root.right == None:
        return 1 + count_emptyBranch(root.left)
    elif root.left == None and root.right == None:
        return 2
    else:
        return count_emptyBranch(root.right) + count_emptyBranch(root.left)


def measure_height(root):
    if root == None:
        return 0

    height_right = measure_height(root.right)
    height_left = measure_height(root.left)

    if height_right > height_left:
        return height_right + 1
    elif height_right <= height_left:
        return height_left + 1
  
def is_full(root):
    if root == None:
        return True
    if root.left == None and root.right == None:
        return True
    elif root.left == None and root.right != None:
        return False
    elif root.right == None and root.left != None:
        return False
    return is_full(root.left) and is_full(root.right)

def complete_tree(root):
    if root == None:
        return None
    
    if (root.left == None and root.right == None) :
        return root
    elif root.left != None and root.right == None:
        root = complete_tree(root.left)
    elif root.left == None and root.right != None:
        root = complete_tree(root.right)
    elif(root.left != None and root.right != None):
        root.left = complete_tree(root.left)
        root.right = complete_tree(root.right)

    return root

def remove_leaves(root):
    if root == None:
        return None

    if (root.left == None and root.right == None):
        return None
    root.left = remove_leaves(root.left)
    root.right = remove_leaves(root.right)
    return root


def make_complete_till_level(root,level):
    def helper(root,level,maxLevel):
        if root == None:
            return None
        level += 1
        if level >= maxLevel:
            return root
        else:
            newNode = TreeNode(-1,0)
            if root.left != None and root.right == None:
                root.right = newNode
            elif root.left == None and root.right != None:
                root.left = newNode
            
            root.left = helper(root.left,level,maxLevel)
            root.right = helper(root.right,level,maxLevel)
        
        return root

    return helper(root,0,level)

def preOrder(root):
    if root == None:
        return None
    preOrder(root.left)
    print(root.data)
    preOrder(root.right)
    


    
    
    

 
    
    

    

    




        





    
            

if __name__ == "__main__":
    bst = BinarySearchTree()
    #bst.feed_randomArray(10,0,10)
   # bst.insert(1)
   # bst.insert(-10)
   # bst.insert(10)
   # bst.insert(-15)
    #bst.insert(5)
   # bst.insert(-5)
   # bst.insert(15)
   # bst.insert(-4)
   # bst.insert(6)

    # bst.add(5)
    # bst.add(-4)
    # bst.add(-3)
    # bst.add(1)
    # bst.add(-10)
    # bst.add(10)
    # bst.add(-15)
    # bst.add(5)
    # bst.add(-5)
    # bst.add(15)
    # bst.add(6)
    
    
    # bst.display(bst.root)
    # print("")
    # min = bst.return_minNode(bst.root.right)
    # print(min.data)
    # print(bst.remove(60))
    # #bst.display(bst.root)
    # node = bst.search(6)
    # print(node.id,node.data)
    # print(bst.return_height())
    # bst.root = remove_leaves(bst.root)
    # #bst.display(bst.root)
    bst.feed_randomArray(30,-10,10)
    bst.root.show()
    print("__________________________________________________")
    #bst.root = remove_leaves(bst.root)
   # bst.root.show()
    print(count_leaves(bst.root))
    print(sum_values(bst.root))
    print(count_leftNodes(bst.root))
    print("__________________________________________________")
    double_positives(bst.root)
    bst.root.show()
    print(count_emptyBranch(bst.root))
    print(is_full(bst.root))
    print("__________________________________________________")
    complete_tree(bst.root)
    bst.root.show()
    print("__________________________________________________")
    remove_leaves(bst.root)
    bst.root.show()
    print("__________________________________________________")
    make_complete_till_level(bst.root,10)
    bst.root.show()
    preOrder(bst.root)
    

            
        
        
        
