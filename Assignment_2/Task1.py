# TASK - 1 : Check if a Number is Even or Odd

# Take integer input from the user
num = int(input("Enter a number to check even or odd: "))

# Check if the number is even or odd
if num % 2 == 0:
    print(f"{num} is an Even!")
else:
    print(f"{num} is an Odd!")