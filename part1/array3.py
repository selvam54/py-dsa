#5️⃣ Count even and odd numbers

array=[2,3,5,3,5,7,58,54,23,59]
print(array)
even=0
odd=0

for i in array:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1

print(odd)
print(even)