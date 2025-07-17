# Take input from the user
a = int(input("Enter first number: "))   # Example: 5
b = int(input("Enter second number: "))  # Example: 3

# Display original values
print("Before swapping:", a, b)

# Swapping without using a temporary variable
a = a + b  # a becomes 5 + 3 = 8
b = a - b  # b becomes 8 - 3 = 5
a = a - b  # a becomes 8 - 5 = 3

# Display values after swap
print("After swapping:", a, b)
