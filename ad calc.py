
a = float(input("enter the first number :"))
b = input("enter the operator :")
c = float(input("enter the second number :"))

if b == "+":
    print("Result =: " + str(a + c))
elif b == "*":
    print("Result =: " + str(a * c))
elif b == "/":
    print("Result =: " + str(a / c))

elif b == "-":
    print("Result =: " + str(a - c))
else:
    print("Invalid Input")
