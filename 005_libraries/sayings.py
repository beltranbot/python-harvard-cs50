def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

# main()

# only run main if we specifically run this file
if __name__ == "__main__":
    main()
