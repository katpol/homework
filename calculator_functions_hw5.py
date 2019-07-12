x = int(input("Gib die erste Zahl ein: "))
y = int(input("Gib die zweite Zahl ein: "))

operation = input("Wähle eine Rechenart (+, -, *, /): ")

def add(x, y):
    print (x + y)

def subtract(x, y):
    print (x - y)

def multiplication(x, y):
    print (x * y)

def division(x, y):
    print (x / y)


if operation == "+":
    add(x, y)

elif operation == "-":
    subtract(x, y)

elif operation == "*":
    multiplication(x, y)

elif operation == "/":
    division(x, y)

else:
    print("Diese Eingabe ist ungültig.")

