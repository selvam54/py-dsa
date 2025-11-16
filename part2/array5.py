# Move All Zeros to End
# Input: [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]

array=[0, 1, 0, 3, 12]
zero=[]
nonzero=[]

for i in array:
    if i==0:
        zero.append(i)
    else:
        nonzero.append(i)
    
        
print(array)
print(nonzero+zero)
    
