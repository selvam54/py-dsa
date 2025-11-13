# 2️⃣ Reverse a Queue

# Use stack logic to reverse a queue.

# 📘 Input: [1, 2, 3, 4, 5]
# 📘 Output: [5, 4, 3, 2, 1]

queue=[1,2,3,4,5]
print(f"correct order {queue}")
stack= []

while queue:
    stack.append(queue.pop(0))

while stack:
    queue.append(stack.pop())
    
print(f"reversed_queue {queue}")