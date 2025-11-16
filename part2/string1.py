name=input("enter the string :")
print(name)
print(type(name))
reverse_name=name[::-1]
print(reverse_name)
if name==reverse_name:
    print("palindrome")
else:
    print("not palindrome")
    