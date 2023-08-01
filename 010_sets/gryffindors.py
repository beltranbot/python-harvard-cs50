# filter

students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Gryffindor"},
    {"name": "Hermione", "house": "Ravenclaw"},
]


def is_gryffindor(student):
    return student["house"] == "Gryffindor"

gryffindors = filter(is_gryffindor, students)

gryffindors = sorted([student["name"] for student in gryffindors])

print(*gryffindors)

"""
gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

print(*sorted(gryffindors))
"""