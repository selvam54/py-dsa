# 6️⃣ Reverse the array (without using reverse())

# Example:
# Input → [1, 2, 3, 4, 5]
# Output → [5, 4, 3, 2, 1]

array=list(map(int,input("enter the array must use space :").split()))
print("the input is \n",array)
reversed_array=[]

while array:
    reversed_array.append(array.pop())
print(reversed_array)
    