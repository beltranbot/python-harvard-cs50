# map

def main():
    yell("this", "is", "cs50")


def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)
    # print(*map(str.upper, words))


if __name__ == "__main__":
    main()
