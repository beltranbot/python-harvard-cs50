students = [
    "Hermione",
    "Harry",
    "Ron"
]

for i in range(len(students)):
    print(i + 1, students[i])

for student in students:
    print(student)

for index, student in enumerate(students):
    print(index, student)
