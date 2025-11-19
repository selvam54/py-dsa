size = 10                          # hash table size is 10
table = [None] * size              # create list of 10 empty slots

def hash_func(key):                # hash function definition
    return key % size              # returns index within range (0–9)

def insert(key, value):            # function to insert key-value pair
    index = hash_func(key)         # compute index using hash function
    table[index] = value           # store the value at calculated index

insert(12, "apple")                # stored at index 2 (12 % 10 = 2)
insert(22, "banana")               # collision → overwrites apple at index 2

print(table)                       # prints final hash table
