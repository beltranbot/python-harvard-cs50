class Vault:

    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"Galleons: {self.galleons}, Sickles: {self.sickles}, Knuts: {self.sickles}"

    def __add__(self, other):
        # operation overload
        return Vault(
            self.galleons + other.galleons,
            self.sickles + other.sickles,
            self.sickles + other.sickles
        )


potter = Vault(100, 50, 25)
print(potter)
weasley = Vault(25, 50, 100)
print(weasley)

print(potter + weasley)
