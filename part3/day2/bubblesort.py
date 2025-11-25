array=[3,5,7,2,9]

for i in range(len(array)-1):
    for j in range(len(array)-1):
        if array[j]>array[j+1]:
            array[j],array[j+1]=array[j+1],array[j]
            
print(array) 