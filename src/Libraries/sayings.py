def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

print(f"{__name__}")

if __name__ == "__main__":
    main()