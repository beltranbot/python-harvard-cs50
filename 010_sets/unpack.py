# unpack

# first, last = input("What's your name? ").split(" ")
# print(f"hello, {first}")

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

"""
coins = [100, 50, 25]
# * unpack list
print(total(*coins), "Knuts")
"""
coins = {
    "galleons": 100,
    "sickles": 50,
    "knuts": 25
}
print(total(**coins), "Knuts")
