# Count vowels in a string.

user=input("enter the string i count how many vowels :")
vowels="aeiou"
count=0
for i in user:
    if i in vowels:
        count=count+1
print(count) 