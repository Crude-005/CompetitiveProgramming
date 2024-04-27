class TreeNode():
    def __init__(self,data):
        self.data = data
        self.left:TreeNode = None
        self.right:TreeNode = None

class BinarySearchTree():
    def __init__(self):
        self.root = None
    
    def insertNode(self, data):
        self.root = self.__insertnode(self.root,data)

    def __insertnode(self,root:TreeNode,data):
        if root == None:
            return TreeNode(data)
        if data > root.data:
            root.right = self.__insertnode(root.right,data)
        elif data < root.data:
            root.left = self.__insertnode(root.left,data)
        return root
        
    def __inOrderTraversal(self,root : TreeNode):
        if root == None:
            return
        self.__inOrderTraversal(root.left)
        print(str(root.data),end = ' ')
        self.__inOrderTraversal(root.right)


    def inOrderTraversal(self):
        temp = self.root
        self.__inOrderTraversal(temp)
        print('')

        
    def __postOrderTraversal(self,root : TreeNode):
        if root == None:
            return
        self.__postOrderTraversal(root.left)
        self.__postOrderTraversal(root.right)
        print(str(root.data),end = ' ')


    def postOrderTraversal(self):
        temp = self.root
        self.__postOrderTraversal(temp)
        print('')

    def __preOrderTraversal(self,root : TreeNode):
        if root == None:
            return
        print(str(root.data),end = ' ')
        self.__preOrderTraversal(root.left)
        self.__preOrderTraversal(root.right)


    def preOrderTraversal(self):
        temp = self.root
        self.__preOrderTraversal(temp)
        print('')

    def __Successor(self,root:TreeNode):
        root = root.right
        while(root.left):
            root = root.left
        return root

    def __del(self ,root:TreeNode ,key):
        if not root:
            return None
        elif root.data > key:
            root.left = self.__del(root.left , key)
        elif root.data < key:
            root.right = self.__del(root.right , key)
        elif not root.left:
            root = root.right
        elif not root.right:
            root = root.left
        else:
            new_root : TreeNode = self.__Successor(root)
            root.data = new_root.data
            root.right = root.right = self.__del(root.right , new_root.data)
        return root
    
    def deleteNode(self,key):
        self.root = self.__del(self.root,key)

def main():
    Chirag = BinarySearchTree()
    l1 = [10,6,11,12,1,7,0,2,3]
    for i in l1:
        Chirag.insertNode(i)

    Chirag.preOrderTraversal()
    Chirag.deleteNode(10)
    Chirag.preOrderTraversal()
    
if __name__ == '__main__':
    main()