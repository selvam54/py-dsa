# Input: "hello"
# Output: "olleh"

stack=[]
reverse_string=[]

stack.append("h")
stack.append("e")
stack.append("l")
stack.append("l")
stack.append("0")

print(stack)

while stack:
    reverse_string.append(stack.pop())
print(reverse_string)