#Write a Python program to perform linear search on an array.

x=30

array=[23,34,67,2,67,6,89,30,7,54,43]

for i in range(0,len(array)):
    if array[i]==x:
        print(i)
        break
else:
    print("not found")
