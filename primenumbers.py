# Program to print all prime numbers in a given interval

# Take lower and upper range from user
lower = int(input("Enter lower limit: "))  # Example: 10
upper = int(input("Enter upper limit: "))  # Example: 20

print("Prime numbers between", lower, "and", upper, "are:")

# Loop through each number in the range
for num in range(lower, upper + 1):
    if num > 1:  # 1 is not a prime number
        # Check if num is divisible by any number from 2 to num-1
        for i in range(2, num):
            if (num % i) == 0:
                # Not a prime number
                break
        else:
            # Loop didn't break => number is prime
            print(num)
