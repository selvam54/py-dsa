#Sort this array using Bubble Sort (ascending order):[6, 3, 8, 5, 2]

arr=[4, 1, 7, 3, 9]

for i in range(0,len(arr)-1):
    for j in range(0,len(arr)-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            
            
print(arr)
