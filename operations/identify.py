x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1, 2, 3]
y3 = [1, 2, 3]

# Check if x1 and y1 are not the same object in memory
print(x1 is not y1)  
# Output: False
# Explanation: Small integers (like 5) are **interned** (cached), so x1 and y1 point to the same memory location

# Check if x2 and y2 are the same object
print(x2 is y2)
# Output: True
# Explanation: String literals are **interned** too in Python, so x2 and y2 refer to the same string object

# Check if x3 and y3 are the same object
print(x3 is y3)
# Output: False
# Explanation: Lists are **mutable**, so even if contents are the same, x3 and y3 are stored at different memory locations
