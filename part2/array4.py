# Find Duplicate Elements
# Input: [1, 2, 3, 2, 4, 1]
# Output: [1, 2]

arr=[-1,-1,2, 3, 2, 4, 1]
orderd_array=[]
duplicatearr=[]

for i in arr:
    if arr.count(i)>1 and i not in duplicatearr:
        duplicatearr.append(i)

    
print(arr)
print(duplicatearr)
print(orderd_array)


