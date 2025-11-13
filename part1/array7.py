#Find the sum of even and odd numbers separately

array=list(map(int,input("enter the array :").split()))
print(array)
sumofeven=0
sumofodd=0

for num in array:
    if num%2==0:
        sumofeven=sumofeven+num
    else:
        sumofodd=sumofodd+num
        
print(sumofeven)
print(sumofodd)