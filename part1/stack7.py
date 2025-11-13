# Check if a string is a palindrome using a stack
# Example: "madam" → ✅ True

user=input("enter the name :")
stack=[]
reversed_string=[]

for i in user:
    stack.append(i)
print(stack)

for j in user:
    reversed_string.append(stack.pop())

if user=="".join(reversed_string):
    print(True)
else:
    print(False)
    
print("original",user)
print("user",reversed_string)

