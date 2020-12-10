def expo(base, power):
    result = 1
    for x in range(power):
        result = result * base
    return result


x = int(input("Enter the Base Digit : "))
y = int(input("Enter the Power :"))
c = expo(x, y)
print(x, " Raise to power ", y, " is equal to : ", c)
