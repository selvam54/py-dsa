# Implement binary search logic and return index.


def binary(array,target):
    start=0
    end=len(array)-1
    
    while end >=start:
        mid = (start+end)//2
        
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            end=mid+1
        
    return -1
            
array=list(map(int,input("enter the array :").split()))
target=int(input("enter the target :"))

result=binary(array,target)
print(result)