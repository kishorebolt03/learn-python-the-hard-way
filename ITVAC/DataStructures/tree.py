class Node:
    def __init__(self,data=None):
        self.data=data
        self.left = self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insertData(self,data):
        node = Node(data)
        if self.root==None:
            self.root = node
            return self.root

        if data < self.root.data:
            if self.root.left !=None:
                self.root.left.insertData(data)
            else:
                self.root.left = node
        else:
            if self.root.right !=None:
                self.root.right.insertData(data)
            else:
                self.root.right = node
        return self.root
    def display(self):
        # self.root.left.display()
        # print(self.root.data)
        # self.root.right.display()
        if(self.root==None):
            return
        else:
            self.display_all(self.root)

    def display_all(self,Root):
        if Root == None:
            return
        if Root.left !=None:
            self.display_all(Root.left)
        print(Root.data)
        if Root.right !=None:
            self.display_all(Root.right)





if __name__=='__main__':
    t=Tree()
    t.insertData(5)
    t.insertData(4)
    t.insertData(6)
    t.display()
