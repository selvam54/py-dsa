# Write a Python program to reverse a string using a stack.

stack=[]
reversed_stack=[]

for i in "selvam":
    stack.append(i)
    
print(stack)

while stack:
    reversed_stack.append(stack.pop())
    
print(reversed_stack)