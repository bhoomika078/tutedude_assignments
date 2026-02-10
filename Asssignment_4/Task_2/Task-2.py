# Task - 2. Write and Append Data to a File

# 1. Take user input and write it to the file
# The 'w' mode stands for 'write'
user_input = input("Enter the first line of text: ")
file = open("task2.txt", "w")
file.write(user_input + "\n")
file.close()

# 2. Append additional data to the same file
# The 'a' mode stands for 'append'
more_data = input("Enter something else to add: ")
file = open("task2.txt", "a")
file.write(more_data + "\n")
file.close()

# 3. Read and display the final content
print("\n--- Final File Content ---")
file = open("task2.txt", "r")
print(file.read())
file.close()