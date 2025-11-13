#Find the maximum and minimum element in an array.

array=list(map(int,input("enter the array :").split()))

maximum=array[0]
minimum=array[0]

for num in array:
    if num > maximum:
        maximum=num
    if num<minimum:
        minimum=num

print(maximum)
print(minimum)