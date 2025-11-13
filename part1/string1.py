#Count the number of vowels in a string

name = input("enter a string :")
count=0

for i in name:
    if i in ("a","e","i","o","u"):
        count=count+1
        
print(count)