students = [
    {"name": "Alice", "department": "CSE", "marks": 85},
    {"name": "Bob", "department": "ECE", "marks": 72},
    {"name": "Charlie", "department": "CSE", "marks": 90},
    {"name": "David", "department": "ME", "marks": 65},
    {"name": "Eva", "department": "ECE", "marks": 88},
]

department_count = {}
department_total_marks = {}

for student in students:

    dept = student["department"]
    marks = student["marks"]

    department_count[dept] = department_count.get(dept, 0) + 1

    department_total_marks[dept] = (
        department_total_marks.get(dept, 0) + marks
    )

print("Department-wise Student Count:")
print(department_count)

print("\nDepartment-wise Average Marks:")

for dept in department_total_marks:

    avg = (
        department_total_marks[dept]
        / department_count[dept]
    )

    print(f"{dept} : {avg:.2f}")