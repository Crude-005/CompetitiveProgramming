from time import sleep

class node():
    def __init__(self ,data: int):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end=' ')
            temp = temp.next
        print("")
    
    def Push(self ,data):
        if (not self.head):
            self.head = node(data)
            return
        
        temp = self.head
        while(temp.next != None):
            temp = temp.next
        temp.next = node(data)

    def Pop(self):
        if(not self.head):
            return -1
        elif(not self.head.next):
            data = self.head.data
            del self.head
            self.head = None
            return data
        else:
            temp = self.head
            while(temp.next.next):
                temp = temp.next
            data = temp.next.data
            del temp.next
            temp.next = None
            return data



def main():
    head = LinkedList()
    l = [2,3,4,5,6,8]
    for i in l:
        head.Push(i)
    del(l,i)

    head.printList()
    a = head.Pop()
    print(dir())

if __name__ == '__main__':
    main()
