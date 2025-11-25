# linked liist

class node:
    
    def __init__(self,data):
        self.data=data
        self.pointer=None
        
head=node(20)
node2=node(30)
node3=node(40)

head.pointer=node2
node2.pointer=node3

cur = head

while (cur is not None):
    print(cur.data)
    cur=cur.pointer
