# Find Maximum and Minimum
# Input: [3, 7, 1, 9, 2]
# Output: Max = 9, Min = 1

array=[1,5,3,4,7,76]
max=array[0]
min=array[0]
for i in array:
    if i>max:
        max=i
    if i<min:
        min=i
print("max",max)
print("min",min)