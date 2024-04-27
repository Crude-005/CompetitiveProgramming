class node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class qnode():
    def __init__(self ,node):
        self.node = node
        self.next = None

class Queue():
    def __init__(self):
        self.head = None
        self.last = None

    def Enqueue(self ,data):
        newNode = qnode(data)
        if (not self.head):
            self.last = newNode
            self.head = self.last
        else:
            self.last.next = newNode
            self.last = self.last.next
        return

    def Dequeue(self):
        if(not self.head):
            return None
        temp = self.head
        node = temp.node
        self.head = self.head.next
        if (not self.head):
            self.last = None
        del temp
        return node
    


class BinaryTree():
    def __init__(self):
        self.root = None
        self.size = 0
    
    def insert(self,data):
        self.size += 1
        if (not self.root):
            self.root = node(data)
            return
        temp = self.root
        for i in (bin(self.size)[3::]):
            if (int(i)):
                if(not temp.right):
                    temp.right = node(data)
                else:
                    temp= temp.right
            else:
                if(not temp.left):
                    temp.left = node(data)
                else:
                    temp = temp.left
        return
    
    def delete(self):
        if (not self.size):
            return
        elif(self.size == 1):
            self.root = None
            return
        temp = self.root
        n = bin(self.size)[3::]
        for i in (n[:-1]):
            if (int(i)):
                temp = temp.right
            else:
                temp = temp.left
        if int(n[-1]):
            temp.right = None
        else:
            temp.left = None
        self.size -= 1


    def linearInsert(self,data):
        leaf = node(data)
        self.size += 1
        if not self.root:
            self.root = leaf
            return
        queue = Queue()
        queue.Enqueue(self.root)
        n = queue.Dequeue()
        while(n):              
            if n.left:
                queue.Enqueue(n.left)
            else:
                n.left = leaf
                del(queue)
                return
            if n.right:
                queue.Enqueue(n.right)
            else:
                n.right = leaf
                del (queue)
                return
            n = queue.Dequeue()
        
        

    def linearTraversal(self):
        if not self.root:
            return
        queue = Queue()
        queue.Enqueue(self.root)
        node = queue.Dequeue()
        while(node):
            print(str(node.data),end=' ')
            if node.left:
                queue.Enqueue(node.left)
            if node.right:
                queue.Enqueue(node.right)
            node = queue.Dequeue()



    def __inOrderTraversal(root : node):
        if root == None:
            return
        BinaryTree.__inOrderTraversal(root.left)
        print(str(root.data),end = ' ')
        BinaryTree.__inOrderTraversal(root.right)


    def inOrderTraversal(self):
        temp = self.root
        BinaryTree.__inOrderTraversal(temp)
        print('')

        
    def __postOrderTraversal(root : node):
        if root == None:
            return
        BinaryTree.__postOrderTraversal(root.left)
        BinaryTree.__postOrderTraversal(root.right)
        print(str(root.data),end = ' ')


    def postOrderTraversal(self):
        temp = self.root
        BinaryTree.__postOrderTraversal(temp)
        print('')

    def __preOrderTraversal(root : node):
        if root == None:
            return
        print(str(root.data),end = ' ')
        BinaryTree.__preOrderTraversal(root.left)
        BinaryTree.__preOrderTraversal(root.right)


    def preOrderTraversal(self):
        temp = self.root
        BinaryTree.__preOrderTraversal(temp)
        print('')
        

def main():        
    nana = BinaryTree()


    for i in range(1,16):
        nana.insert(i)
    # nana.delete()
    # for i in range(4):
    #     nana.delete()
    nana.linearTraversal()

if __name__ == "__main__":
    main()
        
        