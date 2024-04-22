class node():
    def __init__(self ,data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.root = None

    def Traverse(self):
        temp = self.root
        while(temp):
            print(temp.data,end=' ')
            temp = temp.next
        print("")
    
    def Push(self ,data):
        newNode = node(data)
        newNode.next = self.root
        self.root = newNode
        return

    def Pop(self):
        if(not self.root):
            return
        temp = self.root
        data = temp.data
        self.root = self.root.next
        del temp
        return data

def main():
    root = Stack()
    l = [2,3,4,5,6,8]
    for i in l:
        root.Push(i)

    root.Traverse()
    a = root.Pop()
    print(a)
    while(a != None):
        root.Traverse()
        a = root.Pop()
        print (a)
    print("End")

if __name__ == '__main__':
    main()
