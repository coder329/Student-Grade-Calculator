# Student Grade Calculator
# Task 2 - Level 1 - Day 2

def calculate_grade(marks):
    """
    Calculate the grade based on student marks.
    """

    # Check for invalid marks
    if marks < 0 or marks > 100:
        return "Invalid"

    # Assign grade
    elif marks >= 90:
        return "A"

    elif marks >= 80:
        return "B"

    elif marks >= 70:
        return "C"

    elif marks >= 60:
        return "D"

    else:
        return "F"


# Manually created student marks
students = {
    "Student 1": 95,
    "Student 2": 88,
    "Student 3": 76,
    "Student 4": 64,
    "Student 5": 52,
    "Student 6": 91,
    "Student 7": 83,
    "Student 8": 71,
    "Student 9": 59,
    "Student 10": 105
}


# Display results
print("===== Student Grade Calculator =====")
print(f"{'Student':<15}{'Marks':<10}{'Grade'}")
print("-" * 35)

for student, marks in students.items():
    grade = calculate_grade(marks)
    print(f"{student:<15}{marks:<10}{grade}")