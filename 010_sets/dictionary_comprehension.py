# dictionary comprehension

students = ["Hermione", "Harry", "Ron"]

gryffindors = {student: "Gryffindor" for student in students}
print(gryffindors)

"""
gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
print(gryffindors)
"""

"""
for student in students:
    gryffindors.append({
        "name": student,
        "house": "Gryffindor"
    })
"""


