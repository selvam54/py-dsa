# . Count how many times a target element appears in an array.

arr=[2,4,5,7,3,4,7,7,7]

count=0
target=7
for i in arr:
    if i==target:
        count+=1
print(arr)
print(count)