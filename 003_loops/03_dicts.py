houses = {
    "gryffindor": {
        "name": "Gryffindor" ,
        "students": [
            {"name": "Hermione", "patronus": "Otter"},
            {"name": "Harry", "patronus": "Stag"},
            {"name": "Ron", "patronus": "Jack russell terrier"},
        ]
    },
    "slytherin": {
        "name": "Slytherin",
        "students": [
            {"name": "Draco", "patronus": ""},
        ]
    }
}

for house in houses:
    print(houses[house]["name"] + ":")
    for student in houses[house]["students"]:
        print("\t" + student["name"] + ",", 'Patronus:', student["patronus"])

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack rusell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"] + ",", "Patronus:", student["patronus"])
