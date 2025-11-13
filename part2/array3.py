# Count Occurrences of an Element
# Input: [2, 3, 2, 4, 2], element = 2
# Output: 3

arr=[1,2,4,2,5,5,6,5,4,3]

print(arr)
element=int(input("enter the number :"))
# print(arr.count(int(input(element))))
count=0
for i in arr:
    if i==element:
        count+=1
        
print(count)