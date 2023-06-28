def main():
    name = input("What's your name? ")
    hello(name)
    hello()

def hello(name="world"):
    print("hello,", name)

main()
