# Take input from the user and convert to integer
a = int(input("Enter a value: "))  # Example: 10 (binary: 1010)
b = int(input("Enter b value: "))  # Example: 4  (binary: 0100)

# Bitwise AND - only 1 where both bits are 1
print(a & b)  # 10 & 4 = 1010 & 0100 = 0000 => 0

# Bitwise OR - 1 where at least one bit is 1
print(a | b)  # 10 | 4 = 1010 | 0100 = 1110 => 14

# Bitwise XOR - 1 where bits are different
print(a ^ b)  # 10 ^ 4 = 1010 ^ 0100 = 1110 => 14

# Bitwise NOT - flips all the bits (and returns negative due to 2's complement)
print(~a)     # ~10 = -(10 + 1) = -11

# Right shift - shifts bits to the right by 2 positions (equivalent to floor divide by 4)
print(a >> 2) # 10 >> 2 = 1010 >> 2 = 0010 => 2

# Left shift - shifts bits to the left by 2 positions (equivalent to multiply by 4)
print(a << 2) # 10 << 2 = 1010 << 2 = 101000 => 40
