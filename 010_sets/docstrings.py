
# docstrings
def meow(n: int) -> str:
    """
    Meow n times

    :param n: Number of times to meow
    :type n: int
    :raise TypeError:
    :return: A string of n mewos, one per line
    :rtype: str
    """
    return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")
