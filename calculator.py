x = int(input("Gib die erste Zahl ein: "))
y = int(input("Gib die zweite Zahl ein: "))

operation = input("Wähle eine Rechenart (+, -, *, /): ")


if operation == "+":
    print (x + y)

elif operation == "-":
    print (x - y)

elif operation == "*":
    print (x * y)

elif operation == "/":
    print (x / y)

else:
    print("Diese Eingabe ist ungültig.")