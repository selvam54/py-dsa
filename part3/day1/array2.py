# Find the second largest element in an array.

arr=[3,4,3,2,77,66,44]

largest=float("-inf")
second_largest=float("-inf")

for num in arr:
    if num>largest:
        second_largest=largest
        largest=num
    elif num>second_largest and num != largest:
        second_largest=num
        
print(second_largest)
