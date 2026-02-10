# Module 5: Files, Exceptions, and Errors in Python
# Task - 1 : Read a File and Handle Errors 

# Attempt to open and read a file. 
filename = "task1.txt"

data = open(filename, 'w')
data.write("Hello Duniya!!\nWelcome to my assignment on Files and Exceptions in Python.\nHave a great day ahead!")
data.close()

try:
    with open(filename, "rt") as fh:    
        # Read all lines from the file in a list format.
        content = fh.readlines() 
        print("Reading file content: ")

        # Print each line with its corresponding line number.
        for i in range(len(content)): 
            print(f"Line {i + 1}: {content[i].strip()}")

# In case we try to open a file that does not exist or is inaccessible.
except FileNotFoundError:
    print(f"Error: The file {filename} was not found.")

finally:
    print("Execution completed.")