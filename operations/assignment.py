# Take input from the user and convert it to integers
a = int(input("Enter a value: "))  # Example: 5
b = int(input("Enter b value: "))  # Example: 2

# a = a + b (Addition assignment)
a += b
print(a)  # 5 + 2 = 7

# a = a - b (Subtraction assignment)
a -= b
print(a)  # 7 - 2 = 5

# a = a * b (Multiplication assignment)
a *= b
print(a)  # 5 * 2 = 10

# a = a / b (Division assignment)
a /= b
print(a)  # 10 / 2 = 5.0 (note: now 'a' becomes a float)

# a = a % b (Modulus assignment)
a %= b
print(a)  # 5.0 % 2 = 1.0

# a = a // b (Floor division assignment)
a //= b
print(a)  # 1.0 // 2 = 0.0 (floor division on float gives float)

# a = a ** b (Exponentiation assignment)
a **= b
print(a)  # 0.0 ** 2 = 0.0
