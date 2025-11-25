array=[3,5,7,2,9]

for i in range(len(array)):
    min=i
    for j in range(i+1,len(array)):
        if array[min]>array[j]:
            min=j
    array[min],array[i]=array[i],array[min]
        
print(array)