#Write a program to check if the stack is empty or not.

stack=[]

stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)

print(stack)

if len(stack) == 0:
    print("stack is empty")
else:
    print("some elements in the stack")
    

