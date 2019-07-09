print("Welcome to the FizzBuzz Game")
nr = int(input("Please enter a number: "))


def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"

    return input

for x in range(nr):
    print(fizz_buzz(x))

