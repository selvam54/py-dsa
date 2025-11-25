# linked list

class node:
    def __init__(self,data):
        self.data=data
        self.pointer=None
        
class linkedlist:
    def __init__(self):
        self.head=None
            
    def add(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
        else:
            cur=self.head
            while(cur.pointer is not None):
                cur=cur.pointer
            cur.pointer=newnode
                
    def print(self):
            
        cur = self.head
        while(cur is not None):
            print(cur.data)
            cur=cur.pointer
                
linkedlists=linkedlist()

linkedlists.add(10)
linkedlists.add(20)
linkedlists.add(30)
linkedlists.add(40)
linkedlists.print()      
            