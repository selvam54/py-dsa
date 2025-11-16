#Implement a queue using stacks.

queue=[1,2,3,4,5,6]
print("this is queue",queue)
stack=[]

while queue:
    stack.append(queue.pop(0))
while stack:
    queue.append(stack.pop())
print("this is stack",queue)
