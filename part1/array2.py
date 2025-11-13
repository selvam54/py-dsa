#Find the second largest element.

array=list(map(int,input("enter the array :").split()))
second_maximum=array[0]

for num in array:
    if num>second_maximum:
        second_maximum=num
        
print(second_maximum)
        
        
    