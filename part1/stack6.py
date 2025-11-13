# Example: [1, 2, 3, 4, 5] → Remove 3 → [1, 2, 4, 5]

stack =[1,2,3,4,5]
print(stack)
temp=[]
remove_element=3
while stack:
    top = stack.pop()
    if top == remove_element:
        break
    temp.append(top)
    
while temp:
    stack.append(temp.pop())
    
print(stack)

#**********************************************this is my logic*********************************************

# stack=[]

# stack.append(1)
# stack.append(2)
# stack.append(3)
# stack.append(4)
# stack.append(5)

# print(stack)

# stackpop=[]

# stack.pop()
# stack.pop()
# stack.pop()
# stack.append(4)
# stack.append(5)
        
# print(stack)

