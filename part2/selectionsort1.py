
arr=[2,4,2,57,4,3]

for i in range(len(arr)):
    max_index=i
    for j in range(i+1,len(arr)):
        if arr[j]>arr[max_index]:
            max_index=j
    arr[i],arr[max_index]=arr[max_index],arr[i]
print(arr)
            
            