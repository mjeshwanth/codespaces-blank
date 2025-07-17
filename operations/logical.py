# Take three integer inputs from the user
a = int(input("Enter a value: "))  # Example: 10
b = int(input("Enter b value: "))  # Example: 7
c = int(input("Enter c value: "))  # Example: 5

# Logical AND: True only if both conditions are True
print((a > b) and (b > c))  
# True if a > b AND b > c
# Example: 10 > 7 (True) and 7 > 5 (True) => True

# Logical OR: True if at least one condition is True
print((a > b) or (b > c))  
# True if a > b OR b > c
# Example: 10 > 7 (True) or 7 > 5 (True) => True

# Logical NOT: Reverses the condition
print(not(a > b))  
# not(True) => False
# Example: a > b is True => not(True) = False
