# TASK - 2 : Sum of Integers from 1 to 50 Using a Loop

# Initialize sum variable
sum = 0

# Loop through numbers from 1 to 50 and add to sum
# ending value in range is exclusive, so we use 51
for i in range(1,51):
    sum += i

# Print the final sum 
print(f"The sum of numbers from 1 to 50: {sum}")