class node:
    
    def __init__(self,data):
        self.data=data
        self.pointer=None
        
class linkedList:
    def __init__(self):
        self.head=None
        
            
    def add(self,data):
        newNode=node(data)
        if self.head is None:
            self.head=newNode
        else:
            cur=self.head
            while cur.pointer is not None:
                cur=cur.pointer
            cur.pointer=newNode   
            
    def print(self):
        cur=self.head
        while cur is not None:
            print(cur.data)
            cur=cur.pointer
                     
            
LinkedList=linkedList()
LinkedList.add(10)
LinkedList.add(11)
LinkedList.add(12)
LinkedList.print()
