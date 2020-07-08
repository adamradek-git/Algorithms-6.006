class Node:
    def __init__(self, val, parent = None):
        self.val = val
        self.leftChild = None
        self.rightChild = None
        self.parent = parent
    
    def get(self):
        return self.val
    
    def set(self, val):
        self.val = val
        
    def getChildren(self):
        children = []
        if(self.leftChild != None):
            children.append(self.leftChild)
        if(self.rightChild != None):
            children.append(self.rightChild)
        return children
        
class BST:
    def __init__(self):
        self.root = None

    def setRoot(self, val):
        self.root = Node(val)

    def getRoot(self):
        return self.root

    def insert(self, val):
        if(self.root is None):
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)

    def insertNode(self, currentNode, val): #recursive iteration
        if(val <= currentNode.val):
            if(currentNode.leftChild):
                self.insertNode(currentNode.leftChild, val)
            else:
                currentNode.leftChild = Node(val, currentNode)
        elif(val > currentNode.val):
            if(currentNode.rightChild):
                self.insertNode(currentNode.rightChild, val)
            else:
                currentNode.rightChild = Node(val, currentNode)

    def find(self, val):
        return self.findNode(self.root, val)

    def findNode(self, currentNode, val):
        if(currentNode is None):
            return False
        elif(val == currentNode.val):
            return True
        elif(val < currentNode.val):
            return self.findNode(currentNode.leftChild, val)
        else:
            return self.findNode(currentNode.rightChild, val)

    def getMin(self, currentNode): #something wrong here I do not understand
        if currentNode.leftChild:
            self.getMin(currentNode.leftChild)
        else: 
            return currentNode.parent

data = [7,4,2,1,7,3,9]

new_structure = BST()
new_structure.setRoot(data[0])
data.pop(0)

for num in data: 
    new_structure.insert(num)

print(new_structure.getMin(new_structure.getRoot()))



