# Given an array, check if it is sorted or not.

arr1=list(map(int,input("enter the array :").split()))
arr2=sorted(arr1)


if arr1==arr2:
    print("this is sorted")
else:
    print("not sorted")