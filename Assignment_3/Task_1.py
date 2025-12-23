# TASK - 1 : Calculate Factorial Using a Function

# Function to calculate factorial of a number
def factorial(num):
    fact = 1    #Initialize fact variable to 1

    # Calculate factorial using a for loop
    for i in range(1, num+1):
        fact *= i
    return fact

# Call the function to calculate
factorial(5)

# Print the factorial of 5
print(f"The factorial of 5 is: {factorial(5)}")