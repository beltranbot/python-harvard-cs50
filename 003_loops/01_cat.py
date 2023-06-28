def main():
    n = get_number()
    meow(n)

def get_number():
    n = 0
    while n <= 0:
        n = int(input("What's n? "))
    return n

def meow(n):
    for _ in range(n):
        print("meow")


# print("meow\n" * n, end="")

main()