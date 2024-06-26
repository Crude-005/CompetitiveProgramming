class node():
    def __init__(self ,data):
        self.data = data
        self.next = None

class Stack():
    def __init__(self):
        self.head = None

    def Traverse(self):
        temp = self.head
        while(temp):
            print(temp.data,end=' ')
            temp = temp.next
        print("")
    
    def __revtraverse(temp):
        if temp == None:
            return
        Stack.__revtraverse(temp.next)
        print(temp.data,end = ' ')

    def reverseTraversal(self):
        temp = self.head
        Stack.__revtraverse(temp)
        print("")
        
    def Push(self ,data):
        newNode = node(data)
        newNode.next = self.head
        self.head = newNode
        return

    def Pop(self):
        if(not self.head):
            return
        temp = self.head
        data = temp.data
        self.head = self.head.next
        del temp
        return data

def main():
    head = Stack()
    l = [2,3,4,5,6,8]
    for i in l:
        head.Push(i)

    head.Traverse()
    head.reverseTraversal()
    a = head.Pop()
    print(a)
    while(a != None):
        head.Traverse()
        a = head.Pop()
        print (a)
    print("End")

if __name__ == '__main__':
    main()

