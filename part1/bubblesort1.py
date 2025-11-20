#Sort this array using Bubble Sort (ascending order):[6, 3, 8, 5, 2]

arr=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


for i in range(len(arr)-1):
    for j in range(len(arr)-1):
        if arr[j]<arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            
print(arr)