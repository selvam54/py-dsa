# Find the index of first occurrence of a target.

arr=[2,3,4,2,56,5]
index_value=-1
target=int(input("enter the targeted array :"))

for i in range(len(arr)):
    if arr[i]==target:
        index_value=i 
print(index_value)