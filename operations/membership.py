a = 'Hello World'      # a is a string
b = 9                  # b is an integer
list = [1, 2, 3, 4, 5] # list is a list of integers

# Check if character 'H' is present in string a
print('H' in a)         
# Output: True (because 'H' is in "Hello World")

# Check if string 'hello' is present in a (case-sensitive)
print('hello' in a)     
# Output: False (case-sensitive: 'hello' ≠ 'Hello')

# Check if string 'Hello' is in a
print('Hello' in a)     
# Output: True

# Check if string 'world' is in a (case-sensitive)
print('world' in a)     
# Output: False (should be 'World' with capital W)

# Check if b is NOT in list
print(b not in list)    
# Output: True (9 is not in [1,2,3,4,5])
