def calculate(op1, op2, f):
    if f =="add":
        return op1 + op2
    elif f == "subtract":
        return op1 - op2
    elif f == "multiply":
        return op1 * op2
    elif f == "divide":
        return op1 / op2
    else:
        print ('invalid')

print("Select operation.")
print("add")
print("subtract")
print("multiply")
print("divide")

choice = raw_input("Enter choice:")

op1 = int(raw_input("Enter first number: "))
op2 = int(raw_input("Enter second number: "))

results = calculate(op1, op2, choice)
print results
