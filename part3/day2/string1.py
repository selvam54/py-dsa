# Find the longest word in a sentence.

user=input("enter the string :").split()
user=list(user)
longest_word=""

for i in user:
    if len(i)>len(longest_word):
        longest_word=i
         
         
print(longest_word)