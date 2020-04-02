class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class sLL:
    def __init__(self):
        self.head = None

    def insertData(self,data):
        obj = Node(data)
        if self.head == None:
            self.head=obj
        else:
            temp=self.head
            while temp.next!=None:temp=temp.next
            temp.next=obj

    def printData(self):
        temp=self.head
        while temp!=None:
            print(temp.data)
            temp=temp.next

    def deleteData(self,data):
        if self.head==None:
            return False
        temp =self.head
        prev = temp
        while temp.next!=None :
            if temp.data==data:
                if temp==self.head:
                    self.head=temp.next
                else:prev.next=temp.next
                return True
            prev = temp
            temp=temp.next
        if temp==None:
            return False


def sortList(lis):
    if lis.head==None:
        print("Empty list")
        return 0
    else:
        prev=lis.head
        while prev.next!=None:
            temp=prev.next
            while temp.next!=None:
                print("in loop2")
                if prev.data>temp.data:
                    #print("in if1")
                    prev.data,temp.data=temp.data ,prev.data
                temp=temp.next
            prev=prev.next
        print("sorted")




if __name__=='__main__':

    while True:
        print("1.Create Node\n2.Insert Node\n3.Delete Node\n4.Print\n5.sort\n6.exit5")
        option = int(input())
        if option == 1:
            linkedList = sLL()
        elif option == 2:
            N = input("Enter data: ")
            linkedList.insertData(N)
            print("************Data********")
            linkedList.printData()
            print("************Data********")
        elif option == 3:
            D = input("Enter data: ")
            if linkedList.deleteData(D):
                print("Deleted")
            else:
                print("Element not found")
            print("************Data********")
            linkedList.printData()
            print("************Data********")
        elif option == 4:
            print("************Data********")
            linkedList.printData()
            print("************Data********")
        elif option == 5:
            sortList(linkedList)
            print("************Data********")
            linkedList.printData()
            print("************Data********")
        else:
            break
