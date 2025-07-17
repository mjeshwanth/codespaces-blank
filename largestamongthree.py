# Take three integer inputs from the user
num1 = int(input("Enter first number: "))   # Example: 10
num2 = int(input("Enter second number: "))  # Example: 25
num3 = int(input("Enter third number: "))   # Example: 15

# Compare the numbers to find the largest
if num1 >= num2 and num1 >= num3:
    largest = num1  # num1 is greater than or equal to both
elif num2 >= num1 and num2 >= num3:
    largest = num2  # num2 is greater than or equal to both
else:
    largest = num3  # num3 is the greatest

# Print the result
print("The largest number is", largest)
