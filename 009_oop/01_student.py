class Student:
    def __init__(self, name, house) -> None:
        self.name = name
        self.house = house
        pass

    def __str__(self) -> str:
        return f"{self._name} from {self._house}"

    @property
    def house(self):
        self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

    @property
    def name(self):
        self._name

    @name.setter
    def name(self, name):
        self._name = name

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    student = Student.get()
    print(student)


def get_name():
    return input("name: ")


def get_house():
    return input("house: ")


if __name__ == "__main__":
    main()
