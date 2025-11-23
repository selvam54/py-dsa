# binary search

def binary(arr,target):
    start=0
    end=len(arr)-1
    
    while start<=end:
        mid=(start+end)//2
        
        if arr[mid]==target:
            return mid
        elif arr[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return -1

arr=[2,4,5,7,8]
target=int(input("enter the target :"))
result=binary(arr,target)
print(result)

