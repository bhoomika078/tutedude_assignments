# Task - 2. Demonstrate list slicing

# 1. Create a list of numbers from 1 to 10
original_list = list(range(1, 11))

# 2. Extract the first five elements using slicing
extracted_elements = original_list[:5]

# 3. Reverse the extracted elements using the slice trick [::-1]
reversed_elements = extracted_elements[::-1]

# 4. Print the results to match your expected output
print("Original list:", original_list)
print("Extracted first five elements:", extracted_elements)
print("Reversed extracted elements:", reversed_elements)