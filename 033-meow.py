def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        m = int(input("What's meows number? "))
        if m > 0:
            return m

def meow(n):
    print("meow\n" * n, end="")

main()