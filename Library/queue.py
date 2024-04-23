class node():
    def __init__(self ,data):
        self.data = data
        self.next = None

class Queue():
    def __init__(self):
        self.head = None
        self.last = None

    def Traverse(self):
        temp = self.head
        while(temp):
            print(temp.data,end=' ')
            temp = temp.next
        print("")
    
    def Enqueue(self ,data):
        newNode = node(data)
        if (not self.head):
            self.last = newNode
            self.head = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        return

    def Dequeue(self):
        if(not self.head):
            return
        temp = self.head
        data = temp.data
        self.head = self.head.next
        if (not self.head):
            self.last = None
        del temp
        return data

def main():
    q = Queue()
    l = [2,3,4,5,6,8]
    for i in l:
        q.Enqueue(i)

    q.Traverse()
    a = q.Dequeue()
    print(a)
    while(a != None):
        q.Traverse()
        a = q.Dequeue()
        print (a)
        print('head -',q.head)
        print('last -',q.last)
    print("123456")
    
    print("End")

if __name__ == '__main__':
    main()

