# Assignment 4: Files, Exceptions, and Errors in Python

This repository contains the solutions for the Module 5 Assignment from TuteDude.

## Task 1: Read a File and Handle Errors
This script attempts to read `task1.txt`. If the file exists, it prints the content line by line. If the file is missing, it catches the `FileNotFoundError` and displays a user-friendly message.

### Expected Output (If file exists):
Reading file content:
Line 1: This is a sample text file.
Line 2: It contains multiple lines.

### Expected Output (If file is missing):
Error: The file 'task1.txt' was not found.

---

## Task 2: Write and Append Data to a File
This script interacts with the user to create and update a file named `task2.txt`. It demonstrates how to overwrite a file using 'w' mode and add to it using 'a' mode.

### Expected Output:
Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.
Enter additional text to append: Learning file handling in Python.
Data successfully appended.

Final content of task2.txt:
Hello, Python!
Learning file handling in Python.

---

## Technical Skills Used
* **File I/O:** Using `open()`, `write()`, and `read()` functions.
* **Error Handling:** Implementing `try-except` blocks for robustness.
* **File Modes:** Understanding the difference between Write (`w`), Append (`a`), and Read (`r`).