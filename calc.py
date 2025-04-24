dig1 = float(input("Enter first digit: "))
op = input("Enter operator: ")
dig2 = float(input("Enter second digit: "))
if op == '+':
    print(dig1 + dig2)
elif op == '-':
    print(dig1 - dig2)
elif op == '*':
    print(dig1 * dig2)
elif op == '/':
    print(dig1 / dig2)
else:
    print("Invalid operator")                