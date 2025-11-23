# Remove duplicate elements from an array.

arr=[3,4,2,5,6,2]

correct_array=[]
for i in arr:
    if i not in correct_array:
        correct_array.append(i)
        
print(correct_array) 