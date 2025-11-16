#check balanced prantheses in a exprission

def funct(expr):
    stack=[]
    opening="({["
    closing=")}]"
    match = {')':'(','}':'{',']':'['}
    for char in expr:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack or stack.pop() !=match[char]:
                return False
            
    return len(stack)==0

expr=input("enter the prantheses :")

if funct(expr):
    print("is balanced")
else:
    print("not balanced")
            