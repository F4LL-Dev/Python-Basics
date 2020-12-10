i = int(input("Enter the starting number of the prime :"))
n = int(input("Enter the last digit : "))
print("--------------------prime Numbers from ", i, " to ", n, " are following ------------")
x = 1
Flag = False

while i <= n:
    Flag = False
    x = 1
    while x < i - 1:
        x += 1
        if i % x == 0:
            Flag = True

    if not Flag and i != 1:
        print(i)
    i += 1

print("\n Loop Terminated at i= ", i)

# or just to check the number if its prime or not
"""
print("To CHeck for Prime NUmbers")
i = int(input("enter the specific number to check if its prime :"))
Flag = False
if i == 1:
    print("1 is not a prime nor composite")
    Flag = True
elif i <= 0:
    print("Please Enter the Value a positive integer greater than 0")
else:
    x = 1
    while x < i - 1:
        x += 1
        if i % x == 0:
            Flag = True

    if not Flag:
        print(i," is the Prime Number")
    else:
        print(i, "is not a prime number")
"""
