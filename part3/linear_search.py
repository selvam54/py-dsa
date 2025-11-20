def linear(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            print(i)
            return i
    return -1
arr=list(map(int,input("enter the values :").split()))
target=int(input("enter the target :"))

result=linear(arr,target)
