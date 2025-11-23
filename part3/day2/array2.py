# Compute the sum of all elements in an array.

array=list(map(int,input("enter the array :").split()))

sum=sum(array)

print(f"this is built in function :{sum}")

sums=0
for i in array:
    sums+=i
print(f"dsa sum :{sums}")