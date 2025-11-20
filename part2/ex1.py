# binary_search

def binary(arr,target):
    start=0
    end=len(arr)-1
    
    while start<=end:
        mid=(start+end)//2
        
        if arr[mid]==target:
            return mid
        if arr[mid]< target:
            start=mid+1
        else:
            end=mid-1
    return -1

arr=sorted([4,3,5,3,7,4,3,3,555])
target=arr[4]

result=binary(arr,target)

if result != -1:
    print("found it")    
else:
    print("not found it")