# Find the minimum element in an array.

array=list(map(int,input("enter the array :").split()))
minimum_array=float("inf")
for i in array:
    if i<minimum_array:
        minimum_array=i
        
print(f"minimum array :{minimum_array}")