# Check if a string is a palindrome.

user=input("enter the string i check if a sting palindrome or not palindrome :")
reverse=user[::-1]

if user==reverse:
    print("this palindrome")
else:
    print("not palindrome")