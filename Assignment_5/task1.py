# Task - 1. Create a dictionary of students and their marks
student_data = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 95
}

# 2. Ask the user for a student's name
search_name = input("Enter the student's name to find their marks: ")

# 3 & 4. Retrieve marks or display a "not found" message
if search_name in student_data:
    marks = student_data[search_name]
    print(f"{search_name} scored {marks} marks.")
else:
    print(f"Sorry, '{search_name}' is not in our records.")