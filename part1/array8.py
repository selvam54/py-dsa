#Find the index of a given element
array=list(map(int,input("enter the array must use space :").split()))
print(array)
user=int(input("what you find :"))

if user in array:
    index=array.index(user)
    print(index)
else:
    print("not found")