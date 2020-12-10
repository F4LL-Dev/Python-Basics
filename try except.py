try:
    x = int(input("Input a number "))

except:
    print("INVALID INPUT")
#above will be printed on every error even if there is not the input error
#so to be specific check the following
print("\n To check specific error \n")
try:
    x=int(input("Input the number"))
    c=4/0
except ZeroDivisionError:
    print("Division By Zero is not possible ")
except ValueError:
    print("The value is incorrect")

print("\n to check original error")
try:
    c=3/0
except ZeroDivisionError as err:
    print(err)