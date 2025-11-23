# Count the frequency of each element in an array using a dictionary.

arr=[0,2,3,4,45,42,11,22,12,2]
frequency={}

for num in arr:
    if num in frequency:
        frequency[num]+=1
    else:
        frequency[num]=1
        
print(frequency)