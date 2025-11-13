# Reverse an Array
# Input: [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]

array=[1,2,3,4,5]
reverse_array=[]
print(array)
while array:
    reverse_array.append(array.pop())
    
    

print(reverse_array)