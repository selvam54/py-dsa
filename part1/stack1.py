
# #Implement a stack using an array.

# 👉 Push, pop, peek, and check if empty/full.

stack = []

#stack push 

stack.append(10)
stack.append(20)
stack.append(30)

# pop
print(stack)
top=stack.pop()
print("removed lost",top)
print(stack)

#peek
peek=stack[-1]

print("peek",peek)
print(stack)

#check stack empty

# check stack empty
# if len(stack) == 0:
#     print("empty")
# else:
#     print("its stored")

# check stack full

max=len(stack)

if max<0:
    stack.append(30)
    print(stack)
else:
    print("full")