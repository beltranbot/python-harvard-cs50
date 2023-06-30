import csv

students = []

# for files without header
# with open("students_homes.csv") as file:
#     reader = csv.reader(file)
#     for name, home in reader:
#         students.append({"name": name, "home": home})

#for files with header 
with open("students_homes.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
