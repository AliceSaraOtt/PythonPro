class Node():
    def __init__(self,v,n=0):
        self.data = v
        self.link = n

class L:
    def __init__(self):
        self.head = 0
    def initL(self,L):
        self.head = Node(L[0])
        p = self.head
        for i in L[1:]:
            p.link = Node(i)
            p = p.link

    def append(self,v):
        node = Node(v)
        if self.head == 0:
            self.head = node
        else:
            p = self.head
            while p.link != 0:
                p = p.link
            p.link = node

    def insert(self, index,v):
        if index == 0:
            new_node = Node(v,self.head)
            self.head = new_node
        else:
            p = self.head
            pre = self.head
            i = 0
            while i < index and p.link != 0:
                pre = p
                p = p.link
                i += 1
            if index == i:
                new_node = Node(v,p)
                pre.link = new_node

l = L()
l.initL([1,2,3])
l.insert(0,100)
print l.head.data
