# Check for balanced parentheses
# Example:

# Input: "({[]})" → Output: ✅ Balanced

# Input: "({[})" → Output: ❌ Not Balanced

#**********************************************************dought*******************************************


def funct(parenth):
    stack=[]
    pairs = {')': '(', '}': '{', ']': '['}

    
    for ch in parenth:
        if ch in "({[":
            stack.append(ch)
        elif ch in ")}]":
            if not stack or stack[-1] != pairs[ch]:
                return "not balance"
            stack.pop()
            
    if stack:
        return "not balanced"
    else:
        return "balanced"




print(funct("[[[]]]"))   # ✅ Balanced
print(funct("[[[]]")) 